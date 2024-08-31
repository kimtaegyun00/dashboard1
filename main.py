import streamlit as st
import pandas as pd

from data_loader import load_data

def main(): 
    st.title("This is a dashboard1")

    df = load_data()

st.subheader("Select Date Range")
df['Date'] = pd.to_datetime(df['Date'])
start_date = st.date_input("Start date", df['Date'].min())
end_date = st.date_input("End date", df['Date'].max())

ranged_df = df[(df['Date'] >= pd.to_datetime(start_date))
               & (df['Date'] <= pd.to_datetime(end_date))]
ranged_df = ranged_df.reset_index(drop=True)
st.table(ranged_df)

if __name__ == '__main__' :
    main()
