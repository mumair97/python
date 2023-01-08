import streamlit as st
import seaborn as sns
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kashti ki App")
    st.text("In this project we will work on kashti data")
    
with data_sets:
    st.header("kashti doob gayi")
    st.text("coming soon")
    
    # import data set
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head(10))
    
    st.subheader("gender value counts for male and female")
    st.bar_chart(df['sex'].value_counts())
    
    #other plots
    st.subheader("header difference")
    st.bar_chart(df['class'].value_counts())
    
    st.bar_chart(df['age'].sample(10)) # taking 10 samples
    
    
with features:
    st.header("these are our app features")
    st.text("coming soon")
    st.markdown('1. **Feature 1:** This will tell you about feature 1')
    st.markdown('2. **Feature 1:** This will tell you about feature 2')

    
with model_training:
    st.header("this is our model training")
    st.text("coming soon")
    st.markdown('1. **Model 1:** This will tell you about model 1')
    
    # making columns
    input, display = st.columns(2)
    
    # in first col. selection rows are there
    max_depth = input.slider("How many people do you know", min_value=10, max_value=100, value=20, step=5)
    
    # n_estimaters
    n_estimators = input.selectbox("how many tree should be there in a RF?", options=[50, 100, 200, 300, 'No limit'])
    
    # adding list of features
    input.write(df.columns)
    
    # input features from users
    input_features = input.text_input('which feature we should use?')
    
    # machine learning model
    model = RandomForestRegressor(max_depth = max_depth , n_estimators=n_estimators)
    
    # condition for "No limit"
    if n_estimators == 'No limit':
        model = RandomForestRegressor(max_depth=max_depth)
    else:
        model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
    
    # define X and Y
    X = df[[input_features]]
    Y = df[['fare']]
    
    # # fit the model
    model.fit(X,Y)
    pred = model.predict(Y)
    
    # # display metrices
    display.subheader("Mean absolute error of the model is: ")
    display.write(mean_absolute_error(Y, pred))
    display.subheader("Mean squared error of the model is: ")
    display.write(mean_squared_error(Y, pred))
    display.subheader("R squared error of the model is: ")
    display.write(r2_score(Y, pred))

    
    
    
    
    

    
    