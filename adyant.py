import streamlit as st
import numpy as np
import pandas as pd
import random
st.title("Adyant's Maths Software")
st.header("Click on the buttons for a Maths question.")
first = random.randint(100, 250)
second = random.randint(100, 499)
third = random.randint(2, 9)
fourth = random.randint(10, 30)

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
background-image: url("https://img.freepik.com/free-photo/gold-fabric-cloth-background-texture_49683-3812.jpg?size=626&ext=jpg&ga=GA1.2.477405023.1609372800");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
