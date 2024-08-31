import streamlit as st
import pandas as pd

from data_loader import load_data

def main(): 
    st.title("주식 데이터 시각화")

    df = load_data()

    st.subheader("Select Date Range")
    df['Date'] = pd.to_datetime(df['Date'])
    start_date = st.date_input("시작일", df['Date'].min())
    end_date = st.date_input("종료일", df['Date'].max())

    ranged_df = df[(df['Date'] >= pd.to_datetime(start_date))
               & (df['Date'] <= pd.to_datetime(end_date))]
    ranged_df = ranged_df.reset_index(drop=True)
    st.table(ranged_df)

if __name__ == '__main__' :
    main()
