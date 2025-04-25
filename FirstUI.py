# MOVIE TICKETS CALCULATIONS
import streamlit as st

st.title("TEKWORK MOVIES 🎬")
st.success("Welcome to TekMovies!")

# Movie selection
if st.button("Select your movie"):
    movie = st.selectbox("Choose a movie:", ["KALKI2", "BAHUBALI3", "SPRIT", "RAJASAAB"])
else:
    movie = None
    
person = st.number_input("Enter the number of persons", min_value=0, step=1)
price_str = st.selectbox("Select your ticket price", ["250", "300"])
price = int(price_str)  

if st.button("TOTAL"):
    total_amount = person * price
    st.success(f"Total Amount : ₹{total_amount}")
    st.write("Enjoy your movie ")

    
