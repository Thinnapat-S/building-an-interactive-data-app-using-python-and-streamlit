import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
st.write(df)