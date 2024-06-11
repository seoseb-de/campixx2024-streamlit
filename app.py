#####
#
# Hallo Seolinis!
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

download_landingpage = 'https://www.reachx.de/'

##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024')
st.markdown('Hier sind die Beispiele aus der Campixx Session vom 14.06.2024 gesammelt.')

with st.container():

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('Slides')
        st.markdown('''
                    Die Slides erhältst Du hier:
                    ''')
        st.link_button(label = 'Slides herunterladen', url = download_landingpage)
               
    with col_2:
        st.subheader('Beispiele')

        st.page_link('pages/01_🎈_minimal-App.py', label = 'Minimalbeispiel', icon = '🎈' )
        st.page_link('pages/02_🤖_Bot-IP_Beispiel.py', label = 'Bot-IPs laden', icon = '🤖' )
        st.page_link('pages/03_📈_Visualisations.py', label = 'Crawl-Analysen', icon = '📈' )
        st.page_link('pages/05_🔖_Quellen.py', label = 'Quellen & Doku', icon = '🔖' )

    st.markdown('---')

##########
# footer #
##########

st.markdown('---')

with st.container():
    st.markdown('Campixx 2024 🇩🇪')
    st.markdown('''
    - [Speaker-Profil](https://www.campixx.de/speaker/sebastian-adler/)
    - [Xpath für SEO](https://www.seoseb.de/artikel/texte/xpath-fur-seo-ein-einstieg)
    ''')
