import streamlit as st
import pandas as pd
from pandas_datareader import data
from datetime import datetime, timedelta

st.title("Streamlit Stock prices App")

stock_name = st.text_input("Enter the stock name: \n")
option = st.slider("How many days of data would you like to see?", 1, 365, 1)

end = datetime.today().strftime('%Y-%m-%d')
start = (datetime.today() - timedelta(option)).strftime('%Y-%m-%d')

# Defining a function that collects the data based on these input
@st.cache
def load_data(stock, start_date, end_date):
    df = data.DataReader(name=stock, start=start_date, end=end_date, data_source='yahoo')
    return df

data_load_state = st.text("Loading data...")

df = load_data(stock=stock_name, start_date=start, end_date=end)
df.sort_index(axis=0, inplace=True, ascending=False)    # Create a pandas dataframe

# Displaying the dataframe and a line chart
st.subheader(f'{stock_name} stock prices for the past {option} days')
st.dataframe(df)

chart_data = df[['Close']]
st.subheader("Close Prices")
st.line_chart(chart_data)

data_load_state = st.text("Data loaded")
