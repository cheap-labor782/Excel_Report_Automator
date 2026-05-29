import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Excel 自動化報表生成器", layout="wide", page_icon="📊")

st.title("📊 Excel 自動化報表生成器")
st.caption("**作者：趴元** | 幫助你快速產出專業報表")

# 側邊欄
with st.sidebar:
    st.header("⚙️ 操作設定")
    report_type = st.selectbox("選擇報表類型", 
                              ["銷售總結報表", "月度績效分析", "資料清洗工具", "庫存分析"])
    
    st.divider()
    st.info("支援 .xlsx / .xls / .csv 檔案")

# 上傳檔案
uploaded_file = st.file_uploader("上傳 Excel 或 CSV 檔案", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ 成功讀取檔案！共 {len(df):,} 筆資料，{len(df.columns)} 個欄位")
        
        # 資料預覽
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("原始資料預覽")
            st.dataframe(df.head(10), use_container_width=True)
        
        with col2:
            st.subheader("資料資訊")
            st.write(f"**行數：** {len(df)}")
            st.write(f"**欄位：** {list(df.columns)}")
        
        # 自動清洗
        if st.button("🧹 執行資料清洗"):
            # 簡單清洗
            df_clean = df.copy()
            df_clean.columns = df_clean.columns.str.strip()
            df_clean = df_clean.drop_duplicates()
            numeric_cols = df_clean.select_dtypes(include='number').columns
            df_clean[numeric_cols] = df_clean[numeric_cols].fillna(0)
            
            st.success("資料清洗完成！")
            st.dataframe(df_clean.head(8), use_container_width=True)
            
            # 生成報表
            st.subheader("📈 自動生成報表")
            
            if report_type == "銷售總結報表" and len(numeric_cols) > 0:
                total = df_clean[numeric_cols[0]].sum() if len(numeric_cols) > 0 else 0
                st.metric("總金額", f"{total:,.0f}")
                
                fig = px.bar(df_clean.head(20), x=df_clean.columns[0], y=numeric_cols[0], title="前20筆銷售分布")
                st.plotly_chart(fig, use_container_width=True)
            
            # 下載按鈕
            output = pd.ExcelWriter('report_output.xlsx', engine='openpyxl')
            df_clean.to_excel(output, sheet_name='清洗後資料', index=False)
            
            # 建立摘要頁
            summary = pd.DataFrame({
                '項目': ['總筆數', '總金額', '生成時間'],
                '數值': [len(df_clean), total if 'total' in locals() else 0, datetime.now().strftime("%Y-%m-%d %H:%M")]
            })
            summary.to_excel(output, sheet_name='報表摘要', index=False)
            output.close()
            
            with open('report_output.xlsx', 'rb') as f:
                st.download_button(
                    label="📥 下載完整報表 (Excel)",
                    data=f,
                    file_name=f"報表_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                
    except Exception as e:
        st.error(f"讀取檔案失敗：{e}")
else:
    st.info("👆 請上傳 Excel 或 CSV 檔案開始使用")

st.caption("此專案僅供學習與作品展示使用")