import streamlit as st
import pickle

st.title('Penguin Classifier')
st.write('This app uses 6 inputs to predict the species of penguin using a model built in the Palmer\'s Penguin dataset.  Use the form below to get started!')


rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)

st.write(rfc)
st.write(unique_penguin_mapping)

island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass = st.number_input('Body Mass (g)', min_value=0)

st.write('the user inputs are {}'.format([island, sex, bill_length, bill_depth, flipper_length, body_mass]))