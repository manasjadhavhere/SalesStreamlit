#importing necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

#Setting Page Configuration and Title
st.set_page_config(page_title=' Business Quant Assignment- Sales Report ')
st.header('Business Quant Assignment- Sales Report')
st.subheader('by Manas Jadhav')

#Reading and Organizing Data
df=pd.read_csv('data')
df=df.drop(columns=['Unnamed: 0'],axis=1)
df_values=df['Item'].unique().tolist()

#Creating the Table to display for the WebPage
selector=st.multiselect('Select Items:',df_values)
container = st.container()
all = st.checkbox("Select all",value=True)
if all:
  st.dataframe(df)
elif not all:
    df_selection=df.query("Item == @selector")
    all=False
    st.dataframe(df_selection)