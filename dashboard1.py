import streamlit as st
import pandas as pd 
import plotly.express as px


 # ui configuration
sr.set_page_config(
    page_title="Pokemon app",
    page_icon="🐲",
    layout="wide",
)

  # load data 
@st.catch_data
def load_data():
    df = pd.read_csv("Pokemon.csv", index_col='#')
    df = df.set_index('Name')
    return df


  # ui integration
with st.spinner("Loading dataset..."):
    df = load_data()


st.title("Pokemon Dta Analytica")
st.subheader("🦚")


