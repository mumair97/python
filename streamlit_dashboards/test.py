import streamlit as st
import seaborn as sns 

st.header("This app is brought to you by Umair")
st.text("are you having fun?")

st.header("Stay tuned")

df = sns.load_dataset("iris")
st.write(df.head(10))
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])
