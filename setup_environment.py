#!/usr/bin/env python3
"""
Hahow Quality Engineer UI 自動化測試環境設定腳本
自動安裝所需依賴並設定 ChromeDriver
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def print_step(step, message):
    """打印步驟訊息"""
    print(f"\n{'='*50}")
    print(f"步驟 {step}: {message}")
    print('='*50)

def run_command(command, description=""):
    """執行命令並處理錯誤"""
    print(f"執行: {command}")
    if description:
        print(f"說明: {description}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ 成功: {description}")
        if result.stdout:
            print(f"輸出: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 失敗: {description}")
        print(f"錯誤: {e.stderr}")
        return False

def check_python_version():
    """檢查 Python 版本"""
    print_step(1, "檢查 Python 版本")
    
    version = sys.version_info
    print(f"當前 Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ 錯誤: 需要 Python 3.7 或更高版本")
        return False
    
    print("✓ Python 版本符合要求")
    return True

def check_chrome_installed():
    """檢查 Chrome 瀏覽器是否已安裝"""
    print_step(2, "檢查 Chrome 瀏覽器")
    
    system = platform.system().lower()
    chrome_paths = {
        'darwin': ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'],
        'linux': ['/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium-browser'],
        'windows': [
            r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        ]
    }
    
    for path in chrome_paths.get(system, []):
        if os.path.exists(path):
            print(f"✓ 找到 Chrome 瀏覽器: {path}")
            return True
    
    # 嘗試使用命令檢查
    if system == 'darwin':
        if run_command("which google-chrome", "檢查 Chrome 命令"):
            return True
    elif system == 'linux':
        if run_command("which google-chrome", "檢查 Chrome 命令"):
            return True
    elif system == 'windows':
        if run_command("where chrome", "檢查 Chrome 命令"):
            return True
    
    print("❌ 警告: 未找到 Chrome 瀏覽器")
    print("請先安裝 Google Chrome 瀏覽器:")
    print("https://www.google.com/chrome/")
    return False

def install_python_dependencies():
    """安裝 Python 依賴套件"""
    print_step(3, "安裝 Python 依賴套件")
    
    # 檢查 requirements.txt 是否存在
    requirements_file = "ui_requirements.txt"
    if not os.path.exists(requirements_file):
        print(f"❌ 錯誤: 找不到 {requirements_file}")
        return False
    
    # 升級 pip
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "升級 pip"):
        print("⚠ 警告: pip 升級失敗，繼續安裝依賴...")
    
    # 安裝依賴
    if not run_command(f"{sys.executable} -m pip install -r {requirements_file}", 
                      f"安裝 {requirements_file} 中的依賴套件"):
        return False
    
    print("✓ Python 依賴套件安裝完成")
    return True

def setup_chromedriver():
    """設定 ChromeDriver"""
    print_step(4, "設定 ChromeDriver")
    
    try:
        # 嘗試使用 chromedriver-autoinstaller
        import chromedriver_autoinstaller
        print("使用 chromedriver-autoinstaller 自動安裝 ChromeDriver...")
        chromedriver_autoinstaller.install()
        print("✓ ChromeDriver 自動安裝完成")
        return True
    except ImportError:
        print("chromedriver-autoinstaller 未安裝，嘗試手動安裝...")
        
        # 手動安裝 chromedriver-autoinstaller
        if run_command(f"{sys.executable} -m pip install chromedriver-autoinstaller", 
                      "安裝 chromedriver-autoinstaller"):
            try:
                import chromedriver_autoinstaller
                chromedriver_autoinstaller.install()
                print("✓ ChromeDriver 手動安裝完成")
                return True
            except Exception as e:
                print(f"❌ ChromeDriver 安裝失敗: {e}")
                return False
        else:
            print("❌ 無法安裝 chromedriver-autoinstaller")
            return False
    except Exception as e:
        print(f"❌ ChromeDriver 設定失敗: {e}")
        return False

def create_directories():
    """創建必要的目錄"""
    print_step(5, "創建必要的目錄")
    
    directories = [
        "screenshots",
        "logs", 
        "reports"
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ 創建目錄: {directory}")
        except Exception as e:
            print(f"❌ 創建目錄失敗 {directory}: {e}")
            return False
    
    return True

def test_selenium_setup():
    """測試 Selenium 設定"""
    print_step(6, "測試 Selenium 設定")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        print("測試 Chrome WebDriver...")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        print(f"✓ Selenium 測試成功，頁面標題: {title}")
        return True
        
    except Exception as e:
        print(f"❌ Selenium 測試失敗: {e}")
        return False

def create_test_script():
    """創建測試腳本"""
    print_step(7, "創建測試腳本")
    
    # 創建 run_ui_tests.sh
    script_content = """#!/bin/bash
# Hahow Quality Engineer UI 自動化測試執行腳本

echo "=== Hahow Quality Engineer UI 自動化測試 ==="
echo "開始時間: $(date)"
echo ""

# 檢查 Python 環境
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 未找到 python3 命令"
    exit 1
fi

# 檢查依賴
echo "檢查依賴套件..."
python3 -c "import selenium, pytest, chromedriver_autoinstaller" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ 錯誤: 依賴套件未正確安裝"
    echo "請執行: python3 setup_environment.py"
    exit 1
fi

# 執行測試
echo "開始執行 UI 自動化測試..."
echo ""

# 直接執行分析
echo "1. 執行直接分析..."
python3 ui_automation.py

echo ""
echo "2. 執行 pytest 測試套件..."
pytest ui_automation.py -v --tb=short

echo ""
echo "3. 生成 HTML 測試報告..."
pytest ui_automation.py --html=reports/ui_report.html --self-contained-html

echo ""
echo "=== 測試完成 ==="
echo "結束時間: $(date)"
echo ""
echo "測試報告位置: reports/ui_report.html"
echo "截圖位置: screenshots/"
echo "日誌位置: logs/"
"""
    
    try:
        with open("run_ui_tests.sh", "w", encoding="utf-8") as f:
            f.write(script_content)
        
        # 設定執行權限
        os.chmod("run_ui_tests.sh", 0o755)
        print("✓ 創建測試腳本: run_ui_tests.sh")
        return True
    except Exception as e:
        print(f"❌ 創建測試腳本失敗: {e}")
        return False

def main():
    """主要執行函數"""
    print("🚀 Hahow Quality Engineer UI 自動化測試環境設定")
    print("=" * 60)
    
    steps = [
        check_python_version,
        check_chrome_installed,
        install_python_dependencies,
        setup_chromedriver,
        create_directories,
        test_selenium_setup,
        create_test_script
    ]
    
    success_count = 0
    total_steps = len(steps)
    
    for step_func in steps:
        try:
            if step_func():
                success_count += 1
            else:
                print(f"⚠ 步驟失敗，但繼續執行...")
        except Exception as e:
            print(f"❌ 步驟執行異常: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 環境設定完成報告")
    print("=" * 60)
    print(f"成功步驟: {success_count}/{total_steps}")
    
    if success_count == total_steps:
        print("🎉 所有步驟都成功完成！")
        print("\n📋 後續步驟:")
        print("1. 執行測試: ./run_ui_tests.sh")
        print("2. 或直接執行: python3 ui_automation.py")
        print("3. 查看報告: reports/ui_report.html")
    else:
        print("⚠ 部分步驟失敗，請檢查上述錯誤訊息")
        print("\n🔧 故障排除:")
        print("1. 確保已安裝 Google Chrome 瀏覽器")
        print("2. 確保 Python 版本 >= 3.7")
        print("3. 檢查網路連接")
        print("4. 重新執行此腳本")
    
    print("\n📞 如需協助，請檢查錯誤訊息或重新執行設定腳本")

if __name__ == "__main__":
    main()
