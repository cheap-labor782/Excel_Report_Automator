# 📊 Excel 自動化報表生成器

一個方便實用的 **Excel 自動化處理工具**，使用 Streamlit 開發。

專為需要快速產生專業報表、資料清洗、統計分析的使用者設計，非常適合接案展示。

## ✨ 主要功能

- 支援上傳 Excel (.xlsx, .xls) 和 CSV 檔案
- 自動資料清洗（去除重複、空白、修正欄位名稱）
- 自動產生視覺化圖表（柱狀圖）
- 自動計算總計與關鍵指標
- 一鍵下載「清洗後 + 完整報表」Excel 檔案（含摘要頁）

## 🚀 線上體驗

（部署完成後請把網址貼在這裡）

## 🛠️ 本地執行

```bash
git clone https://github.com/cheap-labor782/Excel_Report_Automator.git
cd Excel_Report_Automator
pip install -r requirements.txt
streamlit run app.py
