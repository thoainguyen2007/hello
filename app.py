import streamlit as st
import sklearn
import pickles
st.title("REVENUE PREDICTION")
a = st.number_input('Input Temperature')
if st.button('Predict'):
  st.caption('Revenue predicttion')
  st.success('n')
