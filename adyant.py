import streamlit as st
import numpy as np
import pandas as pd
import random
import webbrowser
st.title("Adyant's Maths Software")
st.header("Click on the buttons for a Maths question.")
first = random.randint(99999, 999999)
second = random.randint(12000, 99998)
third = random.randint(399, 999)
fourth = random.randint(10, 30)

sub1 = ["Mala", "Sheetal", "Johnny", "Sachin", "Boiboi"]
sub2 = ["Akash", "Lenny", "Petro", "Danish", "Isaac"]
thing = ["Marbles", "Nu-Shakti Mix Me Sachets", "Books", "Grams of Rice", "Litres of water"]

asub = random.choice(sub1)
bsub = random.choice(sub2)
stf = random.choice(thing)


#if st.button('Addition'):
          #  st.error(f"{first} + {second}")
if st.button('Subtraction Word Problem'):
            st.error(f"{first} - {second}")
            st.error(f"str(asub) had {first} {stf}. They gave {second} to {bsub}. How many {stf} does {asub} have left?")
            
#if st.button('Multiplication'):
          #  st.error(f"{first} × {third}")
#if st.button('Division'):
   #         st.error(f"{fourth} ÷ {third}")
page_bg_img = '''
<style>
body {
background-image: url("https://img.freepik.com/free-photo/gold-fabric-cloth-background-texture_49683-3812.jpg?size=626&ext=jpg&ga=GA1.2.477405023.1609372800");
background-size: cover;
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

#Add = 'https://www.youtube.com/watch?v=i3WCL7AN5-g'
#
#if st.sidebar.button('How To Add'):
#    webbrowser.open_new_tab(Add)
#
#Sub = 'https://www.youtube.com/watch?v=61NUJRm-nyA'
#
#if st.sidebar.button('How To Subtract'):
#    webbrowser.open_new_tab(Sub)
#
#Mul = 'https://www.youtube.com/watch?v=UtAkNVbkXvU'
#
#if st.sidebar.button('How To Multiply'):
#    webbrowser.open_new_tab(Mul)
#
#Div = 'youtube.com/watch?v=3NvZo1rZKIo'
#
#if st.sidebar.button('How To Divide'):
#    webbrowser.open_new_tab(Div)
#sug = 'https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=minecode007@gmail.com'
#
#if st.sidebar.button('Leave Your Suggestions'):
#    webbrowser.open_new_tab(sug)
