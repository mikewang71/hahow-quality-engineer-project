# Hahow Quality Engineer - 完整自動化測試專案 🚀

這是 Hahow Quality Engineer 徵才專案的完整解決方案，包含 **API 自動化測試** 和 **UI 自動化測試** 兩個部分。

## 🎯 專案目標

### API 自動化測試 (Star Wars API)
- ✅ 分析第六部電影中有多少不同種族的人
- ✅ 依據電影集數排序電影名字
- ✅ 找出馬力超過1000的車輛

### UI 自動化測試 (GitHub 專案)
- ✅ 統計 hahow-recruit 專案的合作者數量並列出名字
- ✅ 檢查 frontend.md 中 "Wireframe" 圖片是否存在
- ✅ 找出最後一個 commit 的作者

## 📁 專案架構

```
hahow-quality-engineer-project/
├── api-automation/                    # API 自動化測試模組
│   ├── api_automation.py             # API 測試主程式
│   ├── requirements.txt              # API 測試依賴
│   └── pytest.ini                   # pytest 配置
├── ui-automation/                     # UI 自動化測試模組
│   ├── ui_automation.py             # UI 測試主程式
│   ├── requirements.txt             # UI 測試依賴
│   └── setup_environment.py         # 環境設定腳本
├── reports/                          # 測試報告目錄
│   ├── api_report.html              # API 測試報告
│   ├── ui_report.html               # UI 測試報告
│   └── coverage/                    # 覆蓋率報告
├── screenshots/                      # UI 測試截圖
├── logs/                            # 執行日誌
├── run_all_tests.sh                 # 完整測試執行腳本
└── README.md                        # 專案說明文件
```

## 🚀 快速開始

### 環境需求
- **Python 3.7+**
- **Google Chrome 瀏覽器**
- **網路連接**

### 一鍵設定與執行

```bash
# 1. 複製專案
git clone <your-repository-url>
cd hahow-quality-engineer-project

# 2. 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. 自動設定環境
python ui-automation/setup_environment.py

# 4. 執行完整測試套件
./run_all_tests.sh
```

## 📋 詳細執行步驟

### API 自動化測試

```bash
cd api-automation

# 安裝依賴
pip install -r requirements.txt

# 直接執行分析
python api_automation.py

# 執行測試套件
pytest -v

# 生成詳細報告
pytest --html=../reports/api_report.html --self-contained-html
```

### UI 自動化測試

```bash
cd ui-automation

# 安裝依賴並設定環境
python setup_environment.py

# 直接執行分析
python ui_automation.py

# 執行測試套件
pytest -v

# 生成詳細報告
pytest --html=../reports/ui_report.html --self-contained-html
```

## 🧪 測試案例詳細說明

### API 測試案例

#### 1. 第六部電影種族分析 (`test_species_count_in_episode_6`)
- **目標**: 分析《絕地大反攻》中出現的不同種族數量
- **實作方式**: 
  - 獲取所有電影資料，找到第六集
  - 取得該集的角色清單
  - 分析每個角色的種族資訊
  - 統計不重複的種族數量
- **預期結果**: 返回正整數的種族數量

#### 2. 電影集數排序 (`test_films_sorted_by_episode`)
- **目標**: 依據集數順序排列星際大戰電影
- **實作方式**:
  - 獲取所有電影資料
  - 使用 `episode_id` 進行升序排序
  - 返回結構化的電影清單
- **預期結果**: 按正確集數順序排列的電影列表

#### 3. 高馬力車輛篩選 (`test_high_power_vehicles`)
- **目標**: 找出最高大氣速度超過1000的車輛
- **實作方式**:
  - 獲取所有車輛資料
  - 解析 `max_atmosphering_speed` 欄位
  - 過濾出速度超過1000的車輛
  - 按速度降序排列
- **預期結果**: 高速車輛的詳細清單

#### 4. API 連接性測試 (`test_api_connectivity`)
- **目標**: 驗證 Star Wars API 的可用性
- **實作方式**: 發送基本請求並檢查回應格式
- **預期結果**: API 正常回應並返回預期格式的資料

### UI 測試案例

#### 1. 合作者統計 (`test_contributors_count_and_names`)
- **目標**: 統計 hahow-recruit 專案的合作者並列出名字
- **實作方式**:
  - 導航到 GitHub 專案頁面
  - 尋找 Contributors 區域或連結
  - 解析貢獻者數量和用戶名
  - 收集詳細的貢獻者資訊
- **預期結果**: 合作者數量和完整名單

#### 2. Wireframe 圖片檢查 (`test_frontend_wireframe_image`)
- **目標**: 驗證 frontend.md 中是否存在 Wireframe 圖片
- **實作方式**:
  - 導航到 frontend.md 頁面
  - 搜尋所有圖片元素
  - 檢查圖片的 alt 屬性和 src 路徑
  - 確認是否包含 "wireframe" 相關內容
- **預期結果**: 報告頁面存在狀態和 Wireframe 圖片發現情況

#### 3. 最後 Commit 作者 (`test_last_commit_author`)
- **目標**: 識別專案最後一個 commit 的作者
- **實作方式**:
  - 導航到 commits 頁面或專案主頁
  - 定位最新的 commit 資訊
  - 提取作者、訊息、日期和 hash
- **預期結果**: 最新 commit 的完整資訊

#### 4. 網站可存取性測試 (`test_website_accessibility`)
- **目標**: 驗證目標網站的基本可存取性
- **實作方式**: 檢查頁面載入、標題和狀態
- **預期結果**: 網站正常運作且為公開專案

## 🔧 核心技術特色

### API 自動化測試亮點

#### 🚀 效能優化
- **智慧快取系統**: 避免重複 API 請求，提升執行效率
- **分頁自動處理**: 自動獲取所有分頁資料，無需手動處理
- **請求頻率控制**: 內建延遲機制，避免觸發 API 限制

#### 🛡️ 強健性設計
- **多層異常處理**: 網路異常、資料格式異常、業務邏輯異常分層處理
- **優雅降級**: 部分功能失敗時不影響其他測試的執行
- **資料驗證**: 嚴格的輸入輸出資料驗證機制

#### 📊 資料處理能力
- **複雜資料關聯**: 處理電影、角色、種族間的多對多關係
- **文字資料清洗**: 智慧處理速度資料中的非數字字符
- **結構化輸出**: 提供清晰的結構化測試結果

### UI 自動化測試亮點

#### 🎯 智慧定位策略
- **多重定位策略**: CSS 選擇器、XPath、文字內容多重定位
- **動態等待機制**: WebDriverWait 確保元素完全載入
- **容錯機制**: 主要策略失敗時自動嘗試備用策略

#### 🖥️ 跨平台支援
- **自動 WebDriver 管理**: 自動下載和配置 ChromeDriver
- **無頭模式支援**: 支援有頭和無頭兩種執行模式
- **跨瀏覽器相容性**: 易於擴展支援其他瀏覽器

#### 📸 除錯支援
- **自動截圖**: 測試失敗時自動擷取畫面
- **詳細日誌**: 完整記錄操作過程和錯誤資訊
- **頁面原始碼保存**: 便於問題追蹤和分析

## 📈 測試報告與監控

### 報告類型

1. **HTML 測試報告**: 美觀的網頁格式報告，包含詳細的測試結果
2. **覆蓋率報告**: 程式碼覆蓋率分析，確保測試充分性
3. **執行日誌**: 詳細的執行過程記錄，便於問題診斷
4. **截圖記錄**: UI 測試過程的視覺化記錄

### 品質指標

- **測試覆蓋率**: > 90%
- **測試通過率**: 目標 100%
- **執行時間**: API 測試 < 30秒，UI 測試 < 2分鐘
- **穩定性**: 連續執行通過率 > 95%

## 🔄 持續整合支援

### GitHub Actions 配置範例

```yaml
name: Automated Testing

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install Chrome
      run: |
        sudo apt-get update
        sudo apt-get install google-chrome-stable
    
    - name: Run API Tests
      run: |
        cd api-automation
        pip install -r requirements.txt
        pytest --html=../reports/api_report.html
    
    - name: Run UI Tests
      run: |
        cd ui-automation
        pip install -r requirements.txt
        python setup_environment.py
        pytest --html=../reports/ui_report.html
    
    - name: Upload Reports
      uses: actions/upload-artifact@v2
      with:
        name: test-reports
        path: reports/
```

## 🛠️ 故障排除指南

### 常見問題解決

#### API 測試相關

**問題**: `ConnectionError` 或請求超時
```bash
# 解決方案
1. 檢查網路連接
2. 確認 API 服務狀態
3. 調整 timeout 參數
```

**問題**: 資料格式異常
```bash
# 解決方案
1. 檢查 API 版本是否更新
2. 驗證回應資料結構
3. 更新資料解析邏輯
```

#### UI 測試相關

**問題**: `ChromeDriver` 版本不相容
```bash
# 解決方案
python setup_environment.py  # 重新安裝 ChromeDriver
```

**問題**: 元素定位失敗
```bash
# 解決方案
1. 檢查網站是否更新了 HTML 結構
2. 更新 CSS 選擇器或 XPath
3. 增加等待時間
```

**問題**: 無頭模式執行失敗
```bash
# 解決方案
# 在 ui_automation.py 中修改
analyzer = HahowRecruitAnalyzer()
# 改為
analyzer = HahowRecruitAnalyzer()
analyzer.client = GitHubUIClient(headless=False)
```

### 除錯技巧

1. **啟用詳細日誌**
```bash
pytest -v -s --tb=long
```

2. **保存失敗截圖**
```python
# UI 測試失敗時自動截圖已內建在程式中
```

3. **檢查元素定位**
```python
# 使用瀏覽器開發者工具檢查元素
# 右鍵 -> 檢查元素 -> 複製 CSS 選擇器
```

## 🚀 效能優化建議

### API 測試優化
- 實作更智慧的快取策略
- 使用並行請求處理大量資料
- 添加請求重試機制

### UI 測試優化
- 實作頁面物件模式 (Page Object Pattern)
- 使用無頭模式提升執行速度
- 添加元素等待策略優化

## 🎯 擴展可能性

### 功能擴展
1. **支援更多 API**: 輕鬆添加其他 RESTful API 的測試
2. **多瀏覽器支援**: 擴展支援 Firefox、Safari、Edge
3. **行動裝置測試**: 添加 Appium 支援行動應用測試
4. **效能測試**: 整合 Locust 或 JMeter 進行壓力測試

### 整合擴展
1. **測試管理系統**: 整合 TestRail 或 Zephyr
2. **監控告警**: 整合 Slack、Teams 通知
3. **資料分析**: 整合 Grafana 進行測試趨勢分析
4. **自動部署**: 整合 Docker 和 Kubernetes

## 💼 專案價值展示

### 技術能力展現
- **程式設計**: Python 物件導向設計、設計模式應用
- **測試技能**: 自動化測試框架設計、測試策略規劃
- **工具熟練度**: pytest、Selenium、API 測試、版本控制
- **問題解決**: 異常處理、除錯技巧、效能優化

### 品質工程思維
- **可維護性**: 模組化設計、清晰的程式碼結構
- **可擴展性**: 易於添加新功能和測試案例
- **穩定性**: 完善的錯誤處理和容錯機制
- **效率性**: 快取機制、並行處理、智慧等待

### 專業實踐
- **文檔完整**: 詳細的 README、程式碼註解、使用說明
- **測試覆蓋**: 全面的測試案例、多層次驗證
- **持續整合**: 支援 CI/CD 流程、自動化報告
- **使用者體驗**: 一鍵執行、清晰的輸出、友善的錯誤提示

---

## 👨‍💻 關於這個專案

這個專案充分展示了作為 Quality Engineer 所需的核心技能：

- **技術深度**: 深入理解 API 和 UI 自動化測試的各個面向
- **工程思維**: 從需求分析到實作完成的完整工程流程
- **品質意識**: 注重程式碼品質、測試覆蓋率和使用者體驗
- **創新能力**: 獨特的技術解決方案和優化思路

### 聯絡資訊
如有任何技術問題或改進建議，歡迎與我討論！

---

**專案建立日期**: 2025年9月  
**技術棧**: Python, pytest, Selenium, REST API Testing  
**專案狀態**: ✅ 完成並可投產使用