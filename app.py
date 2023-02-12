import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide',page_title="India's Census Data")

df=pd.read_csv('India1.csv')
state_list=list(df['State'].unique())
state_list.insert(0,'Overall India')
state_list.insert(0,'Select One')
parameter=sorted(list(df.columns[5:]))
parameter.insert(0,'Select One')


st.sidebar.title("INDIA KA CENSUS  DATA VISUALIZATION")
selected_state=st.sidebar.selectbox('Select States',state_list)

primary=st.sidebar.selectbox('Select Primary Parameter',parameter)
plot1=st.sidebar.button('Plot Graph for Primary Parameter')

secondary=st.sidebar.selectbox('Select Secondary Parameter',parameter)
plot2=st.sidebar.button('Plot Graph for Secondary Parameter')

st.sidebar.text('  ')
st.sidebar.text('  ')
st.sidebar.text('  ')

plot3=st.sidebar.button('Plot Graph for Both Parameter')


if plot1:
    st.title("INDIA'S CENSUS - 2011")
    st.markdown('### Size Represent Primary Parameter')
    st.markdown('### Color Represent Secondary Parameter')

    if selected_state=='Overall India':
       # ploting for india
        
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
        size = primary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=900,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    elif selected_state=='Select One':
        st.warning('Please Select Overall India or Any State')

    else:
        # ploting for states
        state_df=df[df['State']==selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
        size = primary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=800,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)

if plot2:
    st.title("INDIA'S CENSUS - 2011")
    st.markdown('### Size Represent Primary Parameter')
    st.markdown('### Color Represent Secondary Parameter')

    if selected_state=='Overall India':
       # ploting for india
        
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
        size=secondary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=900,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    elif selected_state=='Select One':
        st.warning('Please Select Overall India or Any State')

    else:
        # ploting for states
        state_df=df[df['State']==selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
        size=secondary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=800,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)

if plot3:
    st.title("INDIA'S CENSUS - 2011")
    st.markdown('### Size Represent Primary Parameter')
    st.markdown('### Color Represent Secondary Parameter')

    if selected_state=='Overall India':
       # ploting for india
        
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
        size = primary,color=secondary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=900,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    elif selected_state=='Select One':
        st.warning('Please Select Overall India or Any State') 

    else:
        # ploting for states
        state_df=df[df['State']==selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
        size = primary,color=secondary,
        zoom=4,size_max=35,
        mapbox_style='carto-positron', 
        width=1500, height=800,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)

