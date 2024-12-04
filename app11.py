

import streamlit as st
import pandas as pd 
import plotly.express as px 
st.set_page_config(layout='wide')

df = px.data.tips()


def page1():
    
    tab1 , tab2 , tab3 = st.tabs(['histogram' , 'box-plot' , 'scatter'])
    
    # start put charts in each tab 
    
    with tab1:
    
        col1 , col2 , col3 = st.columns(3)
    
        
        # col1 .....
        
        with col1 :
        
            st.plotly_chart(px.histogram(data_frame=df , x = 'total_bill'))
            st.plotly_chart(px.box(data_frame=df , x = 'total_bill'))
        
        with col2 :
        
            st.plotly_chart(px.pie(data_frame=df , names = 'sex'))
            st.plotly_chart(px.pie(data_frame=df , names = 'time'))
        
        with col3 :
        
            st.plotly_chart(px.scatter(data_frame=df , x = 'total_bill' , y = 'tip'))
            st.plotly_chart(px.violin(data_frame=df , x = 'total_bill'))
            
    with tab2:
    
        
        st.plotly_chart(px.scatter(data_frame=df , x = 'total_bill' , y = 'tip' , color = 'sex'))
    
    
    with tab3:
    
        st.plotly_chart(px.scatter(data_frame=df , x = 'total_bill' , y = 'tip' , color = 'time'))
    
    


    


def page2():

    st.plotly_chart(px.violin(data_frame=df , x = 'total_bill'))



def page3():

    st.plotly_chart(px.box(data_frame=df , x = 'total_bill'))

pages = {
    'histogram' : page1,
    'violin' : page2,
    'box' : page3
}

pg = st.sidebar.radio('Navigate between pages' , pages.keys())

pages[pg]()
