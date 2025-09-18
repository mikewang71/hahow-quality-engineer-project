#!/usr/bin/env python3
"""
環境設定腳本 - 自動安裝並配置 ChromeDriver
"""

import os
import sys
import subprocess
import platform

def install_chromedriver():
    """安裝 ChromeDriver"""
    try:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
        print("✓ ChromeDriver 安裝成功")
        return True
    except ImportError:
        print("正在安裝 chromedriver-autoinstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "chromedriver-autoinstaller"])
            import chromedriver_autoinstaller
            chromedriver_autoinstaller.install()
            print("✓ ChromeDriver 安裝成功")
            return True
        except Exception as e:
            print(f"✗ ChromeDriver 安裝失敗: {e}")
            return False

def check_chrome_installed():
    """檢查 Chrome 是否已安裝"""
    system = platform.system()
    
    if system == "Windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
    elif system == "Darwin":  # macOS
        chrome_paths = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    else:  # Linux
        chrome_paths = ["/usr/bin/google-chrome", "/usr/bin/chromium-browser"]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✓ 找到 Chrome: {path}")
            return True
    
    print("⚠ 未找到 Chrome 瀏覽器")
    print("請安裝 Google Chrome: https://www.google.com/chrome/")
    return False

def install_dependencies():
    """安裝 Python 依賴套件"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Python 依賴套件安裝成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 依賴套件安裝失敗: {e}")
        return False
    except FileNotFoundError:
        print("✗ 找不到 requirements.txt 檔案")
        return False

def create_directories():
    """建立必要的目錄"""
    directories = ["reports", "logs", "screenshots"]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ 建立目錄: {directory}")

def main():
    """主要設定流程"""
    print("=== Hahow UI 自動化測試環境設定 ===\n")
    
    success = True
    
    # 1. 檢查 Chrome
    print("1. 檢查 Chrome 瀏覽器...")
    if not check_chrome_installed():
        success = False
    
    # 2. 安裝 Python 依賴
    print("\n2. 安裝 Python 依賴套件...")
    if not install_dependencies():
        success = False
    
    # 3. 安裝 ChromeDriver
    print("\n3. 設定 ChromeDriver...")
    if not install_chromedriver():
        success = False
    
    # 4. 建立目錄
    print("\n4. 建立必要目錄...")
    create_directories()
    
    print("\n" + "="*50)
    
    if success:
        print("✓ 環境設定完成！")
        print("\n您現在可以執行以下命令:")
        print("  python ui_automation.py        # 直接執行分析")
        print("  pytest ui_automation.py -v     # 執行測試套件")
    else:
        print("✗ 環境設定過程中遇到問題，請檢查上述錯誤訊息")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
