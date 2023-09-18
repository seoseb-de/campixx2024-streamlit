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
    page_title='Campixx 2024 - Streamlit Examples',
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

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Seoseb SEO Tools')
st.markdown('Stuff going here')

with st.container():

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('Intro')
               
    with col_2:
        st.subheader('Examples')
        

    st.markdown('---')

with st.container():
    
    st.markdown('I also do other things. Maybe you want to head over to my website 🇩🇪')
    st.markdown('''
    - [Xpath für SEO](https://www.seoseb.de/artikel/texte/xpath-fur-seo-ein-einstieg)
    - [Sitemap Monitor mit GSheets & DataStudio](https://www.seoseb.de/artikel/texte/sitemap-monitor-mit-google-apps-script-data-studio)
    - [Page Speed Monitoring mit GSheets](https://www.seoseb.de/artikel/texte/pagespeed-monitoring-mit-der-psi-api)
    ''')

##########
# footer #
##########

st.markdown('---')
