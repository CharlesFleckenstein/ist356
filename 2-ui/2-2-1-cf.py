import streamlit as st

if 'lenght' not in st.session_state:
    st.session_state.length = 0
if 'width' not in st.session_state:
    st.session_state.width = 0

st.title('Perimiter Area Calculator')
calculate_clicked = st.button('Calculate Perimiter')
clear_clicked = st.button('Clear')

width = st.number_input('Enter width of rectangle', value = st.session_state.width)
length = st.number_input('Enter length of rectangle', value = st.session_state.length)

if calculate_clicked:
    if width and length:
        perimiter = 2 * (width + length)
        st.success(f'Perimiter = {perimiter}')
    else:
        st.error('You didnt type anything')
        
if clear_clicked:
    st.session_state.width = None
    st.session_state.lenght = None
    st.rerun()
    