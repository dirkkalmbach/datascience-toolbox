"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import sys
import pandas as pd
import numpy as np

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5],
  'second column': [10, 20, 30, 40, 44]
})

df
st.dataframe(df.style.highlight_max(axis=0))
sys.version_info
"Hi Dirk 😎"
st.write("Hi Dirk 😎")
x=np.arange(-5,5)
y=x**2
chart_data = pd.DataFrame(columns=["x","y"], 
    data={"x":np.arange(-5,5), "y":x**2})
st.line_chart(chart_data)

if st.checkbox('Show map'):
    map_data = pd.DataFrame(columns=["lat", "lon"],
    data={"lat":[31.22], "lon":[121.461]}
    )
    st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)