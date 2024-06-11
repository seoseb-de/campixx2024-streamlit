import streamlit as st
import pandas as pd
import altair as alt

###########################################
# page config - must be first st command! #
###########################################

st.set_page_config(
    page_title='Campixx 2024 - Visualizations_Demo',
    page_icon='https://www.seoseb.de/artikel/media/files/favicon-16.png',
    layout='wide',
    initial_sidebar_state='expanded'
)


##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024 - Visualisierungen')
st.markdown('Einfache Beispiele für Visualisierungen aus Screaming-Frog-Exporten')

st.header('Crawls visualisieren')


with st.expander('Anleitung', expanded=False):

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('Export erzeugen')
        st.markdown('''
                    1. Crawl abschließen
                    1. Crrawlanalyse durchführen
                    1. Pagespeed-API Daten abholen
                    1. GSC-API Daten abholen

                    _dann:_

                    Im Tab "Intern" HTML-Dokumente wählen und den "Export" Button drücken.''')
    
    with col_2:
        st.subheader('Screens')
        st.image('./assets/frog_screen.png', caption = 'hier findest Ddu die Exportfunktion 🔍')

crawl_csv =  st.file_uploader(label=':frog: Crawl-Export hochladen', type='csv', help='Hier kannst du deine Crawl-Export-CSV hochladen.')

if crawl_csv is not None:
    # read csv to pandas dataframe
    crawl_df = pd.read_csv(crawl_csv)

    status_code_list = crawl_df['Status-Code'].unique().tolist()
    status_code_selection =  status_code_list   # [200, 301, 302, 304, 403, 404, 410, 500, 503]

    domain = [200, 301, 302, 304, 307, 403, 404, 410, 500, 503]
    range_ = ['green', 'orange', 'darkorange', 'yellow', 'lightgreen', 'red', 'red', 'darkred', 'blue', 'blue' ]

    status_chart = alt.Chart(crawl_df, title = 'Verteilung der Status-Codes').mark_bar().encode(
        x = 'Status-Code:O',
        y = 'count(Adresse):Q',
        color = alt.Color('Status-Code:O').scale(domain=domain, range=range_)
    ).interactive().properties(
        height = 520
    )

    title_length_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Title-Längen in Zeichen').mark_bar().encode(
        x = 'Länge von Titel 1:Q',
        y = 'count(Adresse):Q',
        tooltip = ['count(Adresse)','Länge von Titel 1']
    ).interactive().properties(
        height = 520
    )

    description_length_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Description-Längen').mark_bar().encode(
        #x = alt.X('Adresse:N', ).sort('y'),
        x = 'Länge von Meta Description 1:Q',
        y = 'count(Adresse):Q',
        tooltip = ['Länge von Meta Description 1', 'count(Adresse)']
    ).interactive().properties(
        height = 520
    )

    psi_score_verteilung = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Pagespeed Scores').mark_bar().encode(
        x = 'Performance Score:O',
        y = 'count(Adresse):Q',
    ).properties(
        height = 520
    )

    performance_scatter = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verhältnis: Klicks, Impressions, Position').mark_circle(size=100, color='red').encode(
        x = alt.Y('Klicks').sort('x'),
        y = alt.Y('Impressionen').sort('-y'),
        color = alt.Color('Position').scale(scheme="goldred"),
        tooltip = ['Adresse', 'Titel 1', 'Klicks', 'Position', 'Impressionen']
    ).interactive().properties(
        height = 520
    )

    inlink_verteilung_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'unique Inlinks').mark_circle().encode(
        x = 'Inlinks',
        y = 'Outlinks',
        size = 'Link Score',
        color = alt.Color('Link Score').scale(scheme="pinkyellowgreen"),
        tooltip=['Inlinks', 'Outlinks', 'Link Score', 'Adresse', 'Titel 1']
    ).interactive().properties(
        height = 520
    )

    with st.expander('Crawldaten ansehen', expanded=False):

        st.subheader('Rohdaten')

        raw_data_tab, df_info_tab =  st.tabs(['Crawldatentabelle', 'Datenverteilung'])

        with raw_data_tab:

            selectet_status = st.multiselect('Grenze Status Codes ein:', status_code_selection, status_code_selection)
            status_code_mask = crawl_df['Status-Code'].isin(selectet_status)

            st.dataframe(crawl_df.sort_values('Adresse',key=lambda x:x.str.len())[status_code_mask], 
                        column_config={
                        "Performance Score": st.column_config.ProgressColumn("Performance Score",  
                                                                 help="Pagespeed Insights Performance Score auf der Skala von 0-100",
                                                                 format="%d %%",
                                                                 min_value=0,
                                                                 max_value=100),
                                        }
                            )

        with df_info_tab:
            
            st.write(crawl_df.describe())

    meta_tab, url_tab, performance_tab =  st.tabs(['Metadaten', 'URL Infos', 'Performance'])

    with meta_tab:
        with st.container():
            col_1, col_2 = st.columns(2, gap='medium')

            with col_1:

                st.subheader('Title Länge')
                st.altair_chart(title_length_chart, use_container_width=True)

                st.markdown('#### URLs mit zu breiten Titles')

                max_title_px = crawl_df[crawl_df['Status-Code'] == 200]['Pixelbreite von Titel 1'].max()
                
                title_limit = st.slider('Ab wann sind Titles zu breit?', 0, max_title_px, value = 512, format = '%d px', help = 'das Empfohlene Maximum liegt bei 512 px.')

                title_data = crawl_df[(crawl_df['Status-Code'] == 200) & (crawl_df['Pixelbreite von Titel 1'] > title_limit )][['Pixelbreite von Titel 1', 'Titel 1', 'Adresse']].sort_values(by=['Pixelbreite von Titel 1'], ascending = False)
                
                st.write(f'{len(title_data.index)} URLs mit zu breiten Titeln')

                st.dataframe(title_data, hide_index = True, column_config={
                        "Pixelbreite von Titel 1": st.column_config.ProgressColumn("Pixelbreite von Titel 1",  
                                                                 help="Pixelbreite des Titles",
                                                                 format="%d px",
                                                                 min_value=0,
                                                                 max_value=int(max_title_px),
                                                                 width = "medium"),
                                        } )
                
            with col_2:

                st.subheader('Description Länge')
                st.altair_chart(description_length_chart, use_container_width=True)

                st.markdown('#### URLs mit zu breiten Descriptions')

                max_description_px = crawl_df[crawl_df['Status-Code'] == 200]['Pixelbreite von Meta Description 1'].max()
                
                description_limit = st.slider('Ab wann sind Descriptions zu breit?', 0, max_description_px, value = 920, format = '%d px', help = 'das Empfohlene Maximum liegt bei 920 px.')

                description_data = crawl_df[(crawl_df['Status-Code'] == 200) & (crawl_df['Pixelbreite von Meta Description 1'] > description_limit )][['Pixelbreite von Meta Description 1', 'Meta Description 1', 'Adresse']].sort_values(by=['Pixelbreite von Meta Description 1'], ascending = False)

                st.write(f'{len(description_data.index)} URLs mit zu breiten Descriptions')                

                st.dataframe(description_data, hide_index = True, column_config={
                        "Pixelbreite von Meta Description 1" : st.column_config.ProgressColumn("Pixelbreite von Meta Description 1",  
                                                                 help="Pixelbreite des Titles",
                                                                 format="%d px",
                                                                 min_value=0,
                                                                 max_value=int(max_description_px),
                                                                 width = "medium"),
                        "Meta Description 1" : st.column_config.TextColumn(
                                                help = "Meta Description",
                                                width = "large"
                                            )
                                        } )
                
    with url_tab:
        with st.container():

            col_1, col_2 = st.columns(2, gap='medium')

            with col_1:

                st.subheader('Linkpower-Verteilung')

                link_chart_switch = st.toggle('custom Chart', help = 'Schalte zwischen dem internen Scatter-Chart und dem expliziten Altair Scatter-Chart um')

                if link_chart_switch:    
                    st.altair_chart(inlink_verteilung_chart, use_container_width=True)

                else:
                    altair_data = crawl_df[crawl_df['Status-Code'] == 200][['Inlinks', 'Outlinks', 'Link Score']]
                    st.scatter_chart(altair_data, x = 'Inlinks', y = 'Outlinks', size = 'Link Score', color = 'Link Score', height = 520)

                st.divider()

                stat1, stat2, stat3 = st.columns(3)
                            
                max_inlinks = crawl_df[crawl_df['Inlinks'] == crawl_df['Inlinks'].max()]['Inlinks'].iloc[0]
                avg_inlinks = round(crawl_df['Inlinks'].mean(), 2)
                min_inlinks = crawl_df[crawl_df['Inlinks'] == crawl_df['Inlinks'].min()]['Inlinks'].iloc[0]

                stat1.metric(label = 'min Inlinks', value = min_inlinks)
                stat2.metric(label = 'avg Inlinks', value = avg_inlinks)
                stat3.metric(label = 'max Inlinks', value = max_inlinks)

                max_outlinks = crawl_df[crawl_df['Outlinks'] == crawl_df['Outlinks'].max()]['Outlinks'].iloc[0]
                avg_outlinks = round(crawl_df['Outlinks'].mean(), 2)
                min_outlinks = crawl_df[crawl_df['Outlinks'] == crawl_df['Outlinks'].min()]['Outlinks'].iloc[0]

                stat1.metric(label = 'min Outlinks', value = min_outlinks)
                stat2.metric(label = 'avg Outlinks', value = avg_outlinks)
                stat3.metric(label = 'max Outlinks', value = max_outlinks)
                
              
            with col_2:
                st.subheader('Status Code Verteilung')
          
                st.altair_chart(status_chart, theme=None, use_container_width=True)

                status_code_zusammenfassung = crawl_df.groupby('Status-Code')['Adresse'].count().reset_index()

                st.dataframe(status_code_zusammenfassung, hide_index = True, 
                        column_config={
                        "Adresse": st.column_config.ProgressColumn("URLs",  
                                                                 help="Häufigkeit des Status-Codes",
                                                                 format="%d",
                                                                 width = "medium",
                                                                 min_value = 0,
                                                                 max_value = int(status_code_zusammenfassung['Adresse'].max()))
                                        })

                st.divider()

                redirects_data = crawl_df[(crawl_df['Status-Code'] >= 300) & (crawl_df['Status-Code'] <= 400)][['Adresse', 'Status-Code', 'Umleitungs-URL']]

                st.dataframe(redirects_data, hide_index = True, column_config={
                        "Adresse" : st.column_config.LinkColumn(
                                                help = "URL mit Weiterleitung",
                                                width = "medium",
                                                display_text="https?://[a-z0-9]*\.?campixx.de(.*?)$"
                                            )
                                        })

    with performance_tab:


        with st.container():
            col_1, col_2 = st.columns(2, gap='medium')

            with col_1:
                st.subheader('PSI Score Verteilung')
                st.altair_chart(psi_score_verteilung, use_container_width=True)
              
            with col_2:
                st.subheader('GSC Performance')
                st.altair_chart(performance_scatter, use_container_width=True)
                
                with st.expander('⚠️ Hinweis'):
                    st.info('Die GSC-Daten wurden zur Veranschaulichung zufällig generiert.')

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
