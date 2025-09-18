#!/bin/bash

echo "=== Hahow API 自動化測試執行腳本 ==="
echo ""

# 建立報告目錄
mkdir -p reports

echo "正在執行 API 自動化測試..."
echo ""

# 執行主要分析程式
echo "1. 執行主要分析功能..."
python3 api_automation.py
echo ""

# 執行完整測試套件
echo "2. 執行 pytest 測試套件..."
python3 -m pytest api_automation.py -v --html=reports/report.html --self-contained-html --cov=. --cov-report=html:reports/coverage --cov-report=term-missing

echo ""
echo "=== 測試完成 ==="
echo "測試報告已生成："
echo "- HTML 報告: reports/report.html"
echo "- 覆蓋率報告: reports/coverage/index.html"
