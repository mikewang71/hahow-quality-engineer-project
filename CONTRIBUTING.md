# 🤝 貢獻指南

感謝您對 Hahow Quality Engineer 專案的關注！我們歡迎各種形式的貢獻。

## 📋 如何貢獻

### 🐛 回報問題
如果您發現了 bug 或有功能建議，請：

1. 檢查 [Issues](https://github.com/your-username/hahow-quality-engineer-project/issues) 確認問題尚未被回報
2. 創建新的 Issue，包含：
   - 清楚的問題描述
   - 重現步驟
   - 預期行為 vs 實際行為
   - 環境資訊 (OS, Python 版本等)

### 🔧 提交代碼
1. Fork 本專案
2. 創建功能分支：`git checkout -b feature/AmazingFeature`
3. 提交變更：`git commit -m 'Add some AmazingFeature'`
4. 推送分支：`git push origin feature/AmazingFeature`
5. 開啟 Pull Request

## 📝 代碼規範

### Python 代碼風格
- 使用 **Black** 進行代碼格式化
- 使用 **isort** 進行 import 排序
- 使用 **Flake8** 進行代碼檢查
- 遵循 **PEP 8** 規範

### 測試要求
- 新功能必須包含測試案例
- 測試覆蓋率不低於 90%
- 所有測試必須通過

### 文檔要求
- 新功能必須更新 README.md
- 複雜邏輯必須添加註解
- 遵循現有的文檔格式

## 🧪 本地開發

### 環境設定
```bash
# 1. 複製專案
git clone https://github.com/your-username/hahow-quality-engineer-project.git
cd hahow-quality-engineer-project

# 2. 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. 安裝依賴
pip install -r requirements.txt
pip install -r ui_requirements.txt

# 4. 安裝開發依賴
pip install black isort flake8 mypy pytest-cov
```

### 執行測試
```bash
# API 測試
python api_automation.py
pytest api_automation.py -v

# UI 測試
python setup_environment.py
python ui_automation.py
pytest ui_automation.py -v

# 完整測試
./run_ui_tests.sh
```

### 代碼品質檢查
```bash
# 格式化代碼
black .
isort .

# 檢查代碼風格
flake8 .
mypy .

# 檢查測試覆蓋率
pytest --cov=. --cov-report=html
```

## 📋 Pull Request 流程

### 提交前檢查清單
- [ ] 代碼通過所有測試
- [ ] 代碼符合風格規範
- [ ] 添加了必要的測試案例
- [ ] 更新了相關文檔
- [ ] 提交訊息清楚明確

### PR 描述模板
```markdown
## 📝 變更描述
簡潔描述此 PR 的變更內容

## 🔗 相關 Issue
Closes #(issue number)

## 🧪 測試
- [ ] 新增的測試案例
- [ ] 現有測試仍然通過
- [ ] 手動測試結果

## 📸 截圖 (如適用)
添加相關截圖

## 📋 檢查清單
- [ ] 代碼通過所有測試
- [ ] 代碼符合風格規範
- [ ] 更新了相關文檔
```

## 🏷️ 標籤說明

### Issue 標籤
- `bug` - 錯誤回報
- `enhancement` - 功能增強
- `documentation` - 文檔相關
- `question` - 問題詢問
- `good first issue` - 適合新手的問題

### PR 標籤
- `ready for review` - 準備審查
- `work in progress` - 進行中
- `needs testing` - 需要測試
- `breaking change` - 破壞性變更

## 🎯 開發重點

### 優先級功能
1. **多瀏覽器支援** - Firefox, Safari, Edge
2. **行動裝置測試** - Appium 整合
3. **效能測試** - Locust, JMeter 整合
4. **Docker 支援** - 容器化部署

### 代碼品質目標
- 測試覆蓋率 > 90%
- 代碼複雜度 < 10
- 文檔覆蓋率 100%
- 零 linting 錯誤

## 📞 聯絡方式

- **GitHub Issues**: [專案 Issues](https://github.com/your-username/hahow-quality-engineer-project/issues)
- **Email**: encoreh48080@gmail.com
- **LinkedIn**: [MikeWang](https://linkedin.com/in/mikewang0701)

## 🙏 致謝

感謝所有貢獻者的努力！您的貢獻讓這個專案變得更好。

---

**記住：好的貢獻不只是代碼，還包括文檔、測試、和社群建設！** 🚀
