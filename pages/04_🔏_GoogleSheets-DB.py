
import streamlit as st
from streamlit_gsheets import GSheetsConnection


###########################################
# page config - must be first st command! #
###########################################

st.set_page_config(
    page_title='Campixx 2024 - GoogleSheets_Demo',
    page_icon='https://www.seoseb.de/artikel/media/files/favicon-16.png',
    layout='centered',
    initial_sidebar_state='expanded'
)

connection = st.connection('gsheets', type = GSheetsConnection)
sheet_quelle = connection.read(worksheet = 'crawl_data', usecols = ['Adresse', 'Status-Code', 'CO₂ (mg)', 'Größe (Bytes)', 'Übertragen (Bytes)', 'Total Transferred (bytes)'], ttl="2m",)

with st.sidebar:
    
    st.title('Was siehst Du hier?')
    st.markdown('''
                Diese App demonstriert die Verbindung zu
                einem privaten Google-Sheets-Tabellendokument als Datenquelle.
                Das Praktische bei dieser Verbindung ist, dass die Datenquelle
                mit SQL angesprochen werden kann.
                Die Verbindungsinformationen liegen in den App-Secrets.
                Der Zugriff wird über einen Googel-Cloud-Service-Account geregelt,
                mit dem das Sheet geteilt wurde.''')
    st.markdown('_fiddled by [seoseb](https://www.seoseb.de) | [@seoseb](https://seocommunity.social/@seoseb)_')

##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024 - App auf Google-Sheets aufsetzen')
st.markdown('Diese App verwendet ein privates Google Sheets Dokument als Datenquelle')

st.subheader('Hier ist unser Sheet')

with st.expander('schau ins Sheet', expanded = False):
    st.dataframe(sheet_quelle)


sql = '''
SELECT 
    "Adresse",
    "CO₂ (mg)",
FROM
    crawl_data
WHERE
    "Status-Code" == 200
ORDER BY 
    "CO₂ (mg)" Desc;

'''

df_co2 = connection.query(sql = sql)

max_co2 = df_co2['CO₂ (mg)'].max()
min_co2 = 0

with st.expander('Tabelle erstellt mit:', expanded = False):
    st.code(sql, 'sql', line_numbers = True)
        
st.dataframe(df_co2, hide_index = True, column_config={
                        "CO₂ (mg)": st.column_config.ProgressColumn("CO₂ Footprint",  
                                                                 help="CO₂ Footprint der URL - errechnet vom Screaming Frog",
                                                                 format="%d mg",
                                                                 min_value=min_co2,
                                                                 max_value=max_co2),
                                        },
                                        use_container_width = True
) 

#############
# functions #
#############


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
