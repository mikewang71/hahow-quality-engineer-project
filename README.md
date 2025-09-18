# Hahow Quality Engineer 徵才小專案

這是一個小型的徵才專案，實作 API 自動化驗證（已完成）與 UI 自動化驗證（可延伸）。

## 作業說明與需求

- 使用 git / GitHub 版本控管（見下方「如何發布到 GitHub」）
- 提供 README 文件（本檔）說明如何執行與專案架構

### API 任務
- 目標 API: `https://swapi.info/`
- 已完成驗證：
  - 第六部電影中有多少「不同種族」的人
  - 依據電影集數排序電影名字
  - 挑出所有車輛中，最高大氣速度（視為馬力指標）> 1000 的車輛

對應實作在 `api_automation.py` 內的：
- `SWAPIClient`: 呼叫 SWAPI，對於回傳為 list 的情況做相容處理
- `StarWarsAnalyzer`: 提供上述三個分析方法
- `TestStarWarsAPI`: 使用 pytest 的 4 個測試案例（含 API 連線性）

### UI 任務（延伸方向）
- 目標頁面: `https://github.com/hahow/hahow-recruit`
- 建議驗證：
  - 取得此 repo 的合作者人數與清單
  - 進入 `frontend.md` 並檢查 "Wireframe" 圖片是否存在
  - 取得最後一次 commit 的作者
- 可使用 Playwright 或 Selenium 撰寫；若需我補上自動化腳本，可在此專案新增 `ui/` 目錄與測試指令。

---

## 環境需求
- Python 3.8+（macOS 請使用 `python3` 指令）
- 可連線網際網路

## 安裝步驟
1) 建立與啟用虛擬環境（建議）
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows: venv\Scripts\activate
```
2) 安裝依賴
```bash
pip install -r requirements.txt
```

## 執行方式
- 直接執行分析程式：
```bash
python3 api_automation.py
```
- 執行測試（含 HTML 報告與覆蓋率）：
```bash
python3 -m pytest api_automation.py -v \
  --html=reports/report.html --self-contained-html \
  --cov=. --cov-report=html:reports/coverage --cov-report=term-missing
```
- 使用腳本一鍵執行（分析 + 測試 + 報告）：
```bash
chmod +x run_tests_sh.sh
./run_tests_sh.sh
```

## 產出報告位置
- 測試報告（HTML）：`reports/report.html`
- 覆蓋率報告（HTML）：`reports/coverage/index.html`

## 專案結構
```
├── api_automation.py      # API 客戶端、分析器、pytest 測試
├── run_tests_sh.sh        # 一鍵執行腳本（python3 + pytest）
├── requirements.txt       # 依賴套件
├── pytest.ini             # pytest 設定
├── README.md              # 本說明文件
└── reports/               # 測試與覆蓋率報告（執行後生成）
```

## 注意事項
- 若系統中 `python` 指令不存在，請改用 `python3`。
- 若出現 SSL/OpenSSL 警告，為環境相容性提示，不影響測試執行。
- 已對 SWAPI 直接回傳陣列的情況做相容處理。

---

## 如何發布到 GitHub（步驟）
1) 初始化 git 並提交：
```bash
git init -b main
git add .
git commit -m "feat: initial commit (API automation, tests, docs)"
```
2) 建立遠端 repo 並推送（二擇一）：
- 使用 GitHub CLI：
```bash
gh repo create hahow-quality-engineer-project --private --source . --remote origin --push
```
- 或手動建立 repo 後設定遠端：
```bash
git remote add origin <your_repo_url>
git push -u origin main
```