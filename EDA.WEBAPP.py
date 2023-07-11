import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


## Title of Webapp
st.markdown(''' 
            # **Exploratory Data Analysis Web Application(EDA)**
            This app is develop by Muhammad Saad''')

## Uploading dataset

with st.sidebar.header("Upload your Dataset(.csv)"):
    uploaded_file=st.sidebar.file_uploader("Upload Your File",type=['csv'])
    df=sns.load_dataset("titanic")
    df.head(4)
    st.sidebar.markdown ("[Example Csv file](df)")    
    

## profiling report for pandas

if uploaded_file is not None:
    
    
    def  load_csv():
         csv=pd.read_csv(uploaded_file)
         return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info("Awating For CSV File")
    if st.button ('press to use example data'):
    
    ## example data
    
       def load_Data():
           a=pd.DataFrame(np.random.rand(100,5),
                          columns=['Apple','Boy','Cam','Dog','ETA'])
           return a
       df=load_Data()
       pr=ProfileReport(df,explorative=True)
       st.header('**Input DF**')
       st.write(df)
       st.write('---')
       st.header('**Profiling report with pandas**')
       st_profile_report(pr)