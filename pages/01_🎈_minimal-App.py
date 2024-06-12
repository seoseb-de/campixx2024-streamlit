import streamlit as st 

with st.echo(code_location = 'below', line_numbers = True):

    st.title('Hallo Campixx! 👋')

    if st.button('🎈 Ballons!'):
        st.balloons()

