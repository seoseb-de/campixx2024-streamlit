#####
#
# Work in Progress
# Thanks to Elias Dabbas for providing https://colab.research.google.com/drive/1kqiA9A6-B3d7R6Ix7LEe2iwQQNYQnWuj#scrollTo=eS1TfgSz-9ez
#
####

import streamlit as st
import ipaddress
import requests
import pandas as pd


###########################################
# page config - must be first st command! #
###########################################

st.set_page_config(
    page_title='Campixx 2024 - Visualizations_Demo',
    page_icon='https://www.seoseb.de/artikel/media/files/favicon-16.png',
    layout='centered',
    initial_sidebar_state='expanded'
)


##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024 - aktuelle Bot-IP-Listen')
st.markdown('Diese App basiert auf dem [Jupyter-Notebook "google_bing_bot_ip_addresses.ipynb"](https://colab.research.google.com/drive/1kqiA9A6-B3d7R6Ix7LEe2iwQQNYQnWuj) von Elias Dabbas')

st.subheader('Aktuelle IP-Listen erstellen')


#############
# functions #
#############

bots_urls = {
    'google': 'https://developers.google.com/search/apis/ipranges/googlebot.json',
    'bing': 'https://www.bing.com/toolbox/bingbot.json'
}

@st.cache_data
def bot_ip_addresses():
    ip_addresses = []
    for bot, url in bots_urls.items():
        bot_resp = requests.get(url)
        for iprange in bot_resp.json()['prefixes']:
            network = iprange.get('ipv4Prefix')
            if network:
                ip_list = [(bot, str(ip)) for ip in ipaddress.IPv4Network(network)]
                ip_addresses.extend(ip_list)
    adresses_df = pd.DataFrame(ip_addresses, columns=['Bot-Name', 'IP-Adresse'])

    laenge_der_liste = len(adresses_df.index)

    st.success(f'''{laenge_der_liste} IP-Adressen erfolgreich geladen''', icon="✅")

    return adresses_df

@st.cache_data
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode("utf-8")

def reset():
    st.session_state.geladen = False

IP_liste_holen = st.button('IP-Liste holen', type = 'primary')

# Session State initialisieren
if 'geladen' not in st.session_state:
    st.session_state.geladen = False

if IP_liste_holen or st.session_state.geladen:

    st.session_state.geladen = True

    # Bot-Namen finden & Filtern

    IP_df = bot_ip_addresses()
    bot_list = IP_df['Bot-Name'].unique().tolist()

    bot_select = st.multiselect('Welcher Bot interessiert dich?', bot_list, bot_list)
    bot_mask = IP_df['Bot-Name'].isin(bot_select)

    # Dataframe mit ausgewählten Bot-Namen anzeigen

    st.dataframe(IP_df[bot_mask], use_container_width=True, hide_index=True)
    
    csv = convert_df_to_csv(IP_df[bot_mask])

    if st.download_button(
        label = 'CSV herunterladen',
        data = csv,
        file_name = 'bot-ip-adressen.csv',
        mime = 'text/csv'
    ):

        st.balloons()

    st.button('Reset', on_click = reset)
    
    st.echo('above')

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