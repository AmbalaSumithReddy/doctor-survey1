#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from io import BytesIO

file_path = "doctor_survey.xls"  
with open(file_path, "rb") as file:
    csv_data = file.read()

# Streamlit UI
st.title("Doctor Survey File Download")
input_time = st.text_input("Enter Time (HH:MM format)", "06:00")

if input_time == "06:00":
    st.download_button(
        label="Download Doctor List",
        data=csv_data,
        file_name="doctor_survey.xls",
        mime="text/csv"
    )


# In[ ]:




