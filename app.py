#####
#
# Work in Progress
#
####

import streamlit as st

###########################################
# page config - must be first st command! #
###########################################

st.set_page_config(
    page_title='Campixx 2024',
    page_icon='https://www.seoseb.de/artikel/media/files/favicon-16.png',
    layout='centered',
    initial_sidebar_state='expanded'
)

with st.sidebar:
    
    st.title('Sidebar Stuff')
    st.caption('Work in progress…')
    st.markdown('_fiddled by [seoseb](https://www.seoseb.de) | [@seoseb](https://seocommunity.social/@seoseb)_')

#############
# variables #
#############



##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024')
st.markdown('Stuff going here')

with st.container():

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('Intro')
        st.markdown('![@campixx](https://www.campixx.de/wp-content/uploads/2021/10/campixx-logo-2023-3.png')
               
    with col_2:
        st.subheader('Examples')
        

    st.markdown('---')

with st.container():
    
    st.markdown('Campixx 2021 🇩🇪')
    st.markdown('''
    - [Speaker-Profil](https://www.campixx.de/speaker/sebastian-adler/)
    - [Xpath für SEO](https://www.seoseb.de/artikel/texte/xpath-fur-seo-ein-einstieg)
    ''')

##########
# footer #
##########

st.markdown('---')
