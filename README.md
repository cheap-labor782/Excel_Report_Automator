# 📊 Excel 自動化報表生成器

一個實用型的 **Excel 自動處理工具**，幫助使用者快速清洗資料並產生專業報表。

🔗 **線上體驗**：  
[https://excelreportautomator-2bvepxviwseyjhvr7etkdk.streamlit.app/](https://excelreportautomator-2bvepxviwseyjhvr7etkdk.streamlit.app/)

## ✨ 功能特色

- 支援 Excel (.xlsx/.xls) 與 CSV 檔案上傳
- 自動資料清洗（去除重複、空白、修正欄位）
- 自動計算總計與關鍵指標
- 產生視覺化柱狀圖
- 一鍵下載處理後的完整 Excel 報表（含摘要頁）

## 🛠️ 技術棧

- Streamlit（前端介面）
- Pandas（資料處理）
- Plotly（圖表）
- Openpyxl（Excel 操作）

## 🚀 本地執行

```bash
git clone https://github.com/cheap-labor782/Excel_Report_Automator.git
cd Excel_Report_Automator
pip install -r requirements.txt
streamlit run app.py
