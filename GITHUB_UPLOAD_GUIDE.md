# 🚀 GitHub 上傳指南

## 📋 上傳前準備

### 1. 檢查專案結構
確保專案包含以下文件：
```
hahow-quality-engineer-project/
├── 📄 api_automation.py              # API 自動化測試
├── 📄 ui_automation.py               # UI 自動化測試
├── 📄 setup_environment.py           # 環境設定腳本
├── 📄 run_ui_tests.sh               # UI 測試執行腳本
├── 📄 run_all_tests.sh              # 完整測試執行腳本
├── 📄 requirements.txt              # API 測試依賴
├── 📄 ui_requirements.txt           # UI 測試依賴
├── 📄 pytest.ini                   # pytest 配置
├── 📄 .gitignore                    # Git 忽略文件
├── 📄 README.md                     # 專案說明
├── 📄 INTERVIEW_GUIDE.md            # 面試官分享指南
├── 📄 CONTRIBUTING.md               # 貢獻指南
├── 📄 LICENSE                       # 授權條款
├── 📄 GITHUB_UPLOAD_GUIDE.md        # 本文件
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 ci.yml                # CI/CD 配置
```

### 2. 測試專案功能
```bash
# 測試 API 功能
python3 api_automation.py

# 測試 UI 功能
python3 setup_environment.py
python3 ui_automation.py

# 測試完整套件
./run_ui_tests.sh
```

## 🔧 GitHub 上傳步驟

### 方法一：使用 GitHub CLI (推薦)

```bash
# 1. 安裝 GitHub CLI
# macOS: brew install gh
# Ubuntu: sudo apt install gh
# Windows: winget install GitHub.cli

# 2. 登入 GitHub
gh auth login

# 3. 初始化 Git 倉庫
git init
git add .
git commit -m "Initial commit: Hahow Quality Engineer 自動化測試專案"

# 4. 創建 GitHub 倉庫並推送
gh repo create hahow-quality-engineer-project --public --description "Hahow Quality Engineer 自動化測試專案 - 展示 API 和 UI 自動化測試能力"
git remote add origin https://github.com/your-username/hahow-quality-engineer-project.git
git branch -M main
git push -u origin main
```

### 方法二：使用 GitHub 網頁界面

1. **創建新倉庫**
   - 前往 [GitHub](https://github.com)
   - 點擊 "New repository"
   - 倉庫名稱：`hahow-quality-engineer-project`
   - 描述：`Hahow Quality Engineer 自動化測試專案 - 展示 API 和 UI 自動化測試能力`
   - 設為 Public
   - 不要初始化 README (我們已經有了)

2. **上傳文件**
   ```bash
   # 初始化 Git
   git init
   
   # 添加所有文件
   git add .
   
   # 提交變更
   git commit -m "Initial commit: Hahow Quality Engineer 自動化測試專案"
   
   # 添加遠端倉庫
   git remote add origin https://github.com/your-username/hahow-quality-engineer-project.git
   
   # 推送到 GitHub
   git branch -M main
   git push -u origin main
   ```

### 方法三：使用 Git 命令

```bash
# 1. 初始化 Git 倉庫
git init

# 2. 添加所有文件
git add .

# 3. 提交變更
git commit -m "Initial commit: Hahow Quality Engineer 自動化測試專案

- ✅ API 自動化測試 (Star Wars API)
- ✅ UI 自動化測試 (GitHub 專案)
- ✅ 完整的測試框架 (pytest + Selenium)
- ✅ 自動化環境設定
- ✅ 詳細的測試報告
- ✅ CI/CD 整合 (GitHub Actions)"

# 4. 添加遠端倉庫
git remote add origin https://github.com/your-username/hahow-quality-engineer-project.git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main
```

## 🎯 上傳後設定

### 1. 啟用 GitHub Pages
- 前往 Settings > Pages
- Source 選擇 "GitHub Actions"
- 這樣可以自動部署測試報告

### 2. 設定倉庫描述
- 在倉庫首頁點擊 ⚙️ 圖標
- 添加 Topics: `automation-testing`, `selenium`, `pytest`, `quality-engineering`, `api-testing`, `ui-testing`

### 3. 創建 Release
```bash
# 創建第一個版本
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# 在 GitHub 上創建 Release
# 前往 Releases > Create a new release
# Tag: v1.0.0
# Title: 🚀 Hahow Quality Engineer v1.0.0
# Description: 第一個正式版本，包含完整的 API 和 UI 自動化測試功能
```

## 📊 專案展示設定

### 1. 更新 README 中的連結
將 README.md 中的 `your-username` 替換為您的 GitHub 用戶名：

```bash
# 替換所有 your-username 為實際用戶名
sed -i 's/your-username/your-actual-username/g' README.md
```

### 2. 添加徽章
在 README.md 頂部添加：

```markdown
[![CI](https://github.com/your-username/hahow-quality-engineer-project/workflows/CI/badge.svg)](https://github.com/your-username/hahow-quality-engineer-project/actions)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.15-green.svg)](https://selenium.dev)
[![pytest](https://img.shields.io/badge/pytest-7.4-orange.svg)](https://pytest.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
```

### 3. 設定 GitHub Actions
- 前往 Actions 頁面
- 確認 CI/CD 工作流程正常運行
- 檢查測試報告是否正確生成

## 🎪 面試展示準備

### 1. 準備演示腳本
```bash
# 克隆到面試環境
git clone https://github.com/your-username/hahow-quality-engineer-project.git
cd hahow-quality-engineer-project

# 快速演示
python3 setup_environment.py
./run_ui_tests.sh
open reports/ui_report.html
```

### 2. 準備問題回答
- 技術選型理由
- 架構設計思路
- 測試策略規劃
- 擴展性考慮

### 3. 準備代碼講解
- 核心類別設計
- 異常處理機制
- 測試案例設計
- 工程實踐應用

## 🔍 檢查清單

上傳前請確認：

- [ ] 所有文件都已添加到 Git
- [ ] .gitignore 正確配置
- [ ] README.md 連結正確
- [ ] 測試功能正常
- [ ] 文檔完整
- [ ] 授權條款正確
- [ ] CI/CD 配置正確

## 📞 問題排除

### 常見問題

1. **推送被拒絕**
   ```bash
   # 強制推送 (謹慎使用)
   git push -f origin main
   ```

2. **文件過大**
   ```bash
   # 檢查大文件
   git ls-files | xargs ls -la | sort -k5 -rn | head
   ```

3. **權限問題**
   ```bash
   # 檢查遠端倉庫
   git remote -v
   # 重新設定
   git remote set-url origin https://github.com/your-username/hahow-quality-engineer-project.git
   ```

## 🎉 完成！

上傳完成後，您的專案將在以下位置可見：
- **倉庫地址**: `https://github.com/your-username/hahow-quality-engineer-project`
- **測試報告**: `https://your-username.github.io/hahow-quality-engineer-project/reports/`
- **Actions**: `https://github.com/your-username/hahow-quality-engineer-project/actions`

**祝您面試順利！** 🚀
