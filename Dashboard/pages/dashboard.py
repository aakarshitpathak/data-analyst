import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Explore Hidden Insights of Titanic Incident")

df = sns.load_dataset("titanic")
st.dataframe(df)