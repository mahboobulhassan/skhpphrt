import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

    
def app():
    #st.set_page_config(page_title="SKHPP-DAM")
    st.sidebar.header(' :red[Suki Kinary Hydropower Project]')
    st.sidebar.subheader(' :blue[Monitoring of Geological Equipment]')


    st.subheader(' :red[DAM PIEZOMETER MONITORING]')
    file=st.file_uploader('Choose Excel File')
    sheets=['ULN-P-01','ULN-P-02','ULN-P-03','ULN-P-04','ULN-P-05','ULN-P-06','ULN-P-07','ULN-P-08','ULN-P-09',
            'ULN-P-10','ULN-P-11','ULN-P-12','ULN-P-13','ULN-P-14','ULN-P-15','ULN-P-16','ULN-P-17','ULN-P-18',
            'ULN-P-19','ULN-P-20','ULN-P-21','ULN-P-22','ULN-P-23','ULN-P-24','ULN-P-25','ULN-P-26','ULN-P-27',
            'ULN-P-28','ULN-P-29','ULN-P-30','ULN-P-31','ULN-P-32','ULN-P-33']
    sheet=st.selectbox('Select Equipment ', sheets)
    if file:
        df1=pd.read_excel(file,sheet)
        
        df=df1.iloc[:,0:8]
        st.dataframe(df)

        x_col='Date'
        y_col=['Pressure (kPa)']
        fig=px.line(df,x=x_col,y=y_col)
        fig.update_xaxes(ticks='outside',
                        ticklabelmode='period',
                        ticklen=6,
                        minor=dict(ticklen=2,
                                    griddash='dot'))
        fig.update_layout(plot_bgcolor="rgb(242,242,242)")
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        st.plotly_chart(fig)
        y_cols=['Water Ievel (m）','Reservoir Water Level']
        fig=px.line(df,x=x_col,y=y_cols)
        fig.update_layout(plot_bgcolor="rgb(242,242,242)")
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        st.plotly_chart(fig)


              


