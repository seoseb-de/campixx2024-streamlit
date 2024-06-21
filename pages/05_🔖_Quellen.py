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
    
    st.title('Was siehst Du hier?')
    st.markdown('''
                Hier sind die Quellen gesammelt, 
                die ich für meine Session und die Beispiel-Anwendungen 
                genutzt habe, sowie Anleitungen und 
                Hilfestellungen,d ie Dir die Einarbeitung 
                ins Thema erleichtern''')
    st.markdown('_fiddled by [seoseb](https://www.seoseb.de) | [@seoseb](https://seocommunity.social/@seoseb)_')

#############
# variables #
#############



##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Quellen')
st.markdown('Stuff going here')

with st.container():

    st.subheader('Pakete & Umgebungen')

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('Anaconda :snake:')
        #st.image('https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png', use_column_width=True)
        st.page_link('https://www.anaconda.com/', label = 'Anaconda', icon= '🐍')
               
    with col_2:
        st.subheader('Streamlit :balloon:')
        #st.image('https://streamlit.io/images/brand/streamlit-mark-color.png', use_column_width=True)
        st.page_link('http://www.streamlit.io', label = "Streamlit", icon = '🎈')

st.divider()

with st.expander(label = 'Hilfestellungen'):

    st.subheader('Streamlit Helferlein')

    st.markdown('''
        * [Streamlit Dokumentation](https://docs.streamlit.io/)
        * [Streamlit Cheatsheet](https://cheat-sheet.streamlit.app/)
        ''')

st.divider()

with st.expander(label = 'SEO related'):

    st.subheader('Streamlit & SEO')

    st.markdown('''
                ### Streamlit Apps
                * [Charly Wargniers App Collection](https://www.charlywargnier.com/my-public-web-apps)
                * [Search Console Connector](https://search-console-connector.streamlit.app/)
                * [SEO Data Blender](https://dethfire-python-seo-streamlit-data-blend-l4ywic.streamlit.app/)
                
                #### Artikel
                * [Using Python + Streamlit To Find Striking Distance Keyword Opportunities](https://www.searchenginejournal.com/python-seo-striking-distance/423009/)
                * [Streamlit Tutorial For SEOs: How To Create A UI For Your Python App](https://www.searchenginejournal.com/streamlit-tutorial-with-user-authentication-and-dockerfile/469205/)
        ''')


with st.expander(label = 'YouTube Videos'):

    st.markdown('''
                * [Streamlit & Googel-Sheets: The Easiest "Database"](https://www.youtube.com/watch?v=HwxrXnYVIlU)            
                * [EPIC Google Sheets to Interactive Dashboard in Python ft. Streamlit / CSS](https://www.youtube.com/watch?v=Mrwgkra33Ko)
                * [How to use Streamlit session states and callback functions](https://www.youtube.com/watch?v=5l9COMQ3acc)
                ''')

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
