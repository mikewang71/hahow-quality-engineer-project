#!/bin/bash
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
