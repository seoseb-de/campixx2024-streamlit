#####
#
# Work in Progress
#
####

import streamlit as st
import pandas as pd
import altair as alt

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

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Campixx 2024 - Visualisierungen')
st.markdown('Stuff going here')

st.subheader('Crawls visualisieren')

crawl_csv =  st.file_uploader(label=':frog: Crawl-Export hochladen', type='csv', help='Hier kannst du deine Crawl-Export-CSV hochladen.')

if crawl_csv is not None:
    # read csv to pandas dataframe
    crawl_df = pd.read_csv(crawl_csv)

    status_code_list = crawl_df['Status-Code'].unique().tolist()
    status_code_selection = [200, 301, 302, 304, 403, 404, 410, 500, 503]

    status_chart = alt.Chart(crawl_df, title = 'Verteilung der Status-Codes').mark_bar().encode(
        x = 'Status-Code:O',
        y = 'count(Adresse):Q',
        color = 'Status-Code'
    ).properties(
        height = 400
    )

    title_length_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Title-Längen').mark_bar().encode(
        x = alt.X('Adresse:N',).sort('y'),
        y = 'Länge von Titel 1:Q',
        tooltip = ['Adresse','Länge von Titel 1', 'Titel 1']
    ).properties(
        height = 400
    )

    description_length_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Description-Längen').mark_bar().encode(
        x = alt.X('Adresse:N', ).sort('y'),
        y = 'Länge von Meta Description 1:Q',
        tooltip = ['Adresse','Länge von Meta Description 1', 'Meta Description 1']
    ).properties(
        height = 400
    )

    psi_score_verteilung = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verteilung der Pagespeed Scores').mark_bar().encode(
        x = 'Performance Score:O',
        y = 'count(Adresse):Q',
    ).properties(
        height = 400
    )

    performance_scatter = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'Verhältnis: Klicks, Impressions, Position').mark_point(size=100, color='red').encode(
        x = alt.Y('Klicks:O').sort('x'),
        y = alt.Y('Impressionen:O').sort('-y'),
        color = 'Position:O',
        tooltip = ['Adresse', 'Titel 1', 'Klicks', 'Position', 'Impressionen']
    ).interactive().properties(
        height = 400
    )

    inlink_verteilung_chart = alt.Chart(crawl_df[crawl_df['Status-Code'] == 200], title = 'unique Inlinks').mark_circle().encode(
        x = 'Inlinks',
        y = 'Outlinks',
        size = 'Link Score',
        tooltip=['Inlinks', 'Outlinks', 'Link Score', 'Adresse', 'Titel 1']
    ).properties(
        height = 400
    )

    with st.expander('Crawldaten ansehen', expanded=False):

        selectet_status = st.multiselect('Grenze Status Codes ein:', status_code_selection, status_code_selection)
        status_code_mask = crawl_df['Status-Code'].isin(selectet_status)

        st.dataframe(crawl_df.sort_values('Adresse',key=lambda x:x.str.len())[status_code_mask])

    meta_tab, url_tab, performance_tab =  st.tabs(['Metadaten', 'URL Infos', 'Performance'])

    with meta_tab:
        with st.container():
            col_1, col_2 = st.columns(2, gap='small')

            with col_1:

                st.subheader('Title Länge')
                st.altair_chart(title_length_chart, use_container_width=True)

            with col_2:

                st.subheader('Description Länge')
                st.altair_chart(description_length_chart, use_container_width=True)

    with url_tab:
        with st.container():
            col_1, col_2 = st.columns(2, gap='small')

            with col_1:
                st.subheader('Linkpower-Verteilung')
                st.altair_chart(inlink_verteilung_chart, use_container_width=True)

            with col_2:
                st.subheader('Status Code Verteilung')
                st.altair_chart(status_chart, theme=None, use_container_width=True)

    with performance_tab:


        with st.container():
            col_1, col_2 = st.columns(2, gap='small')

            with col_1:
                st.subheader('PSI Score Verteilung')
                st.altair_chart(psi_score_verteilung, use_container_width=True)

            with col_2:
                st.subheader('Perf_Scatter')
                st.altair_chart(performance_scatter, use_container_width=True)


