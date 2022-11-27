import streamlit as st

st.write("""
# Multiplication of two Numbers
""")

#Get Input
st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("Number 1",step=1)
    num2 = st.number_input("Number 2",step=1)

    return f'Multiplication of {num1} and {num2} is {num1*num2}'

result = user_input_features()

st.subheader('Result')
st.write(result)
