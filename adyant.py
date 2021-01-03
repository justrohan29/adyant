import streamlit as st
import numpy as np
import pandas as pd
import random
st.title("Adyant's Maths Software")
st.header("Click on the buttons for a Maths question.")
first = random.randint(500, 999)
second = random.randint(100, 499)
third = random.randint(1, 10)
fourth = random.randint(1, 30)

if st.button('Addition'):
            st.error(f"{first} + {second}")
if st.button('Subtraction'):
            st.error(f"{first} - {second}")
if st.button('Multiplication'):
            st.error(f"{first} × {third}")
if st.button('Division'):
            st.error(f"{fourth} ÷ {third}")
page_bg_img = '''
<style>
body {
background-image: url("https://media.istockphoto.com/photos/yellow-nature-background-picture-id1024230944?k=6&m=1024230944&s=612x612&w=0&h=xY4FarmmXF0M1VZuJyTDGTDb2_N_tMkqXooZzzsXhgE=");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
