#Tip calculator
import streamlit as st
st.title("Tip calculator")
bill=st.number_input("Enter Food items bill ",min_value=0,step=1)
tip=0
if bill <=1000:
    tip=(bill*2)/100
elif bill<=5000:
    tip=(bill*5)/100
else:
    tip=(bill*7)/100
st.write("Tip",tip)


    

