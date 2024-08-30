import streamlit as st

from data_loader import load_data

def main(): 
    st.title("This is a dashboard1")

    df = load_data()

if __name__ == '__main__' :
    main()
