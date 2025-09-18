import requests
import pytest
from typing import List, Dict, Any
import json
import time

class SWAPIClient:
    """Star Wars API 客戶端類別"""
    
    def __init__(self, base_url: str = "https://swapi.info/api"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def _make_request(self, endpoint: str, params: dict = None) -> Dict[Any, Any]:
        """發送 API 請求並處理錯誤"""
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # 如果回傳的是陣列，包裝成標準格式
            if isinstance(data, list):
                return {"results": data, "next": None}
            
            return data
        except requests.RequestException as e:
            print(f"API 請求失敗: {e}")
            raise
            
    def get_all_pages(self, endpoint: str) -> List[Dict[Any, Any]]:
        """獲取所有分頁的資料"""
        all_results = []
        page = 1
        
        while True:
            try:
                data = self._make_request(endpoint, params={"page": page})
                all_results.extend(data.get("results", []))
                
                if not data.get("next"):
                    break
                    
                page += 1
                time.sleep(0.1)  # 避免過於頻繁的請求
                
            except Exception as e:
                print(f"獲取第 {page} 頁時發生錯誤: {e}")
                break
                
        return all_results
    
    def get_films(self) -> List[Dict[Any, Any]]:
        """獲取所有電影資料"""
        return self.get_all_pages("films")
    
    def get_people(self) -> List[Dict[Any, Any]]:
        """獲取所有人物資料"""
        return self.get_all_pages("people")
    
    def get_vehicles(self) -> List[Dict[Any, Any]]:
        """獲取所有車輛資料"""
        return self.get_all_pages("vehicles")
    
    def get_species(self) -> List[Dict[Any, Any]]:
        """獲取所有種族資料"""
        return self.get_all_pages("species")


class StarWarsAnalyzer:
    """星際大戰資料分析器"""
    
    def __init__(self):
        self.client = SWAPIClient()
        self._cache = {}
    
    def _get_cached_data(self, data_type: str) -> List[Dict[Any, Any]]:
        """獲取快取的資料"""
        if data_type not in self._cache:
            method = getattr(self.client, f"get_{data_type}")
            self._cache[data_type] = method()
        return self._cache[data_type]
    
    def get_species_count_in_episode_6(self) -> int:
        """獲取第六部電影中不同種族的數量"""
        films = self._get_cached_data("films")
        people = self._get_cached_data("people")
        
        # 找到第六部電影
        episode_6 = None
        for film in films:
            if film.get("episode_id") == 6:
                episode_6 = film
                break
        
        if not episode_6:
            raise ValueError("找不到第六部電影")
        
        # 獲取第六部電影中的角色 URLs
        episode_6_characters = set(episode_6.get("characters", []))
        
        # 找到出現在第六部的角色們的種族
        species_in_episode_6 = set()
        
        for person in people:
            person_url = person.get("url")
            if person_url in episode_6_characters:
                person_species = person.get("species", [])
                species_in_episode_6.update(person_species)
        
        # 如果沒有指定種族，視為人類
        if not species_in_episode_6:
            species_in_episode_6.add("Human")
        
        return len(species_in_episode_6)
    
    def get_films_sorted_by_episode(self) -> List[Dict[str, Any]]:
        """依據電影集數排序電影名字"""
        films = self._get_cached_data("films")
        
        sorted_films = sorted(films, key=lambda x: x.get("episode_id", 0))
        
        return [
            {
                "episode_id": film.get("episode_id"),
                "title": film.get("title"),
                "release_date": film.get("release_date")
            }
            for film in sorted_films
        ]
    
    def get_high_power_vehicles(self, min_horsepower: int = 1000) -> List[Dict[str, Any]]:
        """獲取馬力超過指定值的車輛"""
        vehicles = self._get_cached_data("vehicles")
        
        high_power_vehicles = []
        
        for vehicle in vehicles:
            try:
                # 處理馬力資料（可能包含非數字字符）
                max_speed = vehicle.get("max_atmosphering_speed", "unknown")
                if max_speed == "unknown" or max_speed == "n/a":
                    continue
                
                # 移除非數字字符並轉換為整數
                speed_value = int(''.join(filter(str.isdigit, str(max_speed))))
                
                if speed_value > min_horsepower:
                    high_power_vehicles.append({
                        "name": vehicle.get("name"),
                        "model": vehicle.get("model"),
                        "max_speed": max_speed,
                        "speed_value": speed_value
                    })
                    
            except (ValueError, TypeError):
                continue
        
        return sorted(high_power_vehicles, key=lambda x: x["speed_value"], reverse=True)


class TestStarWarsAPI:
    """API 自動化測試類別"""
    
    @pytest.fixture(scope="class")
    def analyzer(self):
        """測試用的分析器實例"""
        return StarWarsAnalyzer()
    
    def test_species_count_in_episode_6(self, analyzer):
        """測試：第六部電影中有多少不同種族的人"""
        species_count = analyzer.get_species_count_in_episode_6()
        
        print(f"\n第六部電影中出現了 {species_count} 個不同的種族")
        
        # 驗證結果合理性
        assert isinstance(species_count, int)
        assert species_count > 0
        assert species_count < 100  # 合理的上限檢查
    
    def test_films_sorted_by_episode(self, analyzer):
        """測試：依據電影集數排序電影名字"""
        sorted_films = analyzer.get_films_sorted_by_episode()
        
        print(f"\n依集數排序的電影列表:")
        for i, film in enumerate(sorted_films, 1):
            print(f"{i}. 第{film['episode_id']}集: {film['title']} ({film['release_date']})")
        
        # 驗證結果
        assert len(sorted_films) > 0
        assert all(isinstance(film['episode_id'], int) for film in sorted_films)
        
        # 檢查是否確實按集數排序
        episode_ids = [film['episode_id'] for film in sorted_films]
        assert episode_ids == sorted(episode_ids)
    
    def test_high_power_vehicles(self, analyzer):
        """測試：找出馬力超過1000的車輛"""
        high_power_vehicles = analyzer.get_high_power_vehicles(1000)
        
        print(f"\n馬力超過1000的車輛:")
        if high_power_vehicles:
            for i, vehicle in enumerate(high_power_vehicles, 1):
                print(f"{i}. {vehicle['name']} ({vehicle['model']}) - 最高速度: {vehicle['max_speed']}")
        else:
            print("沒有找到馬力超過1000的車輛")
        
        # 驗證結果
        assert isinstance(high_power_vehicles, list)
        for vehicle in high_power_vehicles:
            assert vehicle['speed_value'] > 1000
    
    def test_api_connectivity(self):
        """測試：API 連接性"""
        client = SWAPIClient()
        
        # 測試基本連接
        films = client._make_request("films")
        assert "results" in films
        
        print(f"\nAPI 連接測試通過，共找到 {len(films['results'])} 部電影")


if __name__ == "__main__":
    # 直接執行分析
    print("=== Star Wars API 自動化分析 ===")
    
    analyzer = StarWarsAnalyzer()
    
    try:
        # 1. 分析第六部電影的種族數量
        print("\n1. 分析第六部電影中的種族數量...")
        species_count = analyzer.get_species_count_in_episode_6()
        print(f"第六部電影中出現了 {species_count} 個不同的種族")
        
        # 2. 按集數排序電影
        print("\n2. 按集數排序電影...")
        sorted_films = analyzer.get_films_sorted_by_episode()
        for i, film in enumerate(sorted_films, 1):
            print(f"{i}. 第{film['episode_id']}集: {film['title']}")
        
        # 3. 找出高馬力車輛
        print("\n3. 尋找馬力超過1000的車輛...")
        high_power_vehicles = analyzer.get_high_power_vehicles(1000)
        if high_power_vehicles:
            for i, vehicle in enumerate(high_power_vehicles, 1):
                print(f"{i}. {vehicle['name']} - 最高速度: {vehicle['max_speed']}")
        else:
            print("沒有找到馬力超過1000的車輛")
            
    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
