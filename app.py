import streamlit as st
import sklearn
import pickle
st.title("REVENUE PREDICTION")
t = st.number_input('Input Temperature')
filename = 'model.pickle'

# pickle.dump(model, open(filename, "wb"))
# model = pickle.load(open(filename, "rb"))
if st.button('Predict'):
  st.caption('Revenue predicttion')
  st.success(model)
