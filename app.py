import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Excel 自動化報表生成器", layout="wide", page_icon="📊")

st.title("📊 Excel 自動化報表生成器")
st.caption("**作者：趴元** | 快速產出專業 Excel 報表")

with st.sidebar:
    st.header("⚙️ 設定")
    report_type = st.selectbox("報表類型", 
                              ["銷售總結報表", "月度績效分析", "資料清洗工具", "自訂分析"])
    st.info("支援 .xlsx、.xls、.csv 檔案")

uploaded_file = st.file_uploader("上傳你的 Excel / CSV 檔案", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ 成功讀取！共 {len(df):,} 筆資料，{len(df.columns)} 個欄位")
        
        st.subheader("📋 原始資料預覽")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 執行自動化處理 & 生成報表"):
            df_clean = df.copy()
            df_clean.columns = df_clean.columns.str.strip()
            df_clean = df_clean.drop_duplicates()
            
            numeric_cols = df_clean.select_dtypes(include='number').columns
            df_clean[numeric_cols] = df_clean[numeric_cols].fillna(0)
            
            st.success("🧹 資料清洗完成！")
            
            if len(numeric_cols) > 0:
                col_to_sum = numeric_cols[0]
                total = df_clean[col_to_sum].sum()
                st.metric(label="總計", value=f"{total:,.0f}")
                
                fig = px.bar(df_clean.head(20), x=df_clean.columns[0], y=col_to_sum, 
                           title=f"前20筆 {col_to_sum} 分布")
                st.plotly_chart(fig, use_container_width=True)
            
            output_file = f"自動化報表_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df_clean.to_excel(writer, sheet_name='清洗後資料', index=False)
                summary = pd.DataFrame({
                    '統計項目': ['總筆數', '數值總和', '處理時間'],
                    '結果': [len(df_clean), total if 'total' in locals() else 0, datetime.now().strftime("%Y-%m-%d %H:%M")]
                })
                summary.to_excel(writer, sheet_name='報表摘要', index=False)
            
            with open(output_file, 'rb') as f:
                st.download_button(
                    label="📥 下載完整報表",
                    data=f,
                    file_name=output_file,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
    except Exception as e:
        st.error(f"❌ 發生錯誤: {str(e)}")
else:
    st.info("👆 請上傳檔案開始使用")

st.caption("此專案用於學習與作品展示")
                
    except Exception as e:
        st.error(f"讀取檔案失敗：{e}")
else:
    st.info("👆 請上傳 Excel 或 CSV 檔案開始使用")

st.caption("此專案僅供學習與作品展示使用")
