import streamlit as st


if 'total' not in st.session_state:
    st.session_state.total = 0.0


st.title('total amount calculator')
add_button_clicked = st.button('Add', type='primary')
clear_clicked = st.button('Clear', type='secondary')

amount = st.number_input('Enter amount')


if clear_clicked:
    st.session_state.total = 0
    st.rerun()
elif add_button_clicked:
    st.session_state.total = st.session_state.total + amount
    st.write(f'Total amount = {st.session_state.total}')
        
