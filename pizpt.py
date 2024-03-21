import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def app():
    st.header('Sukikinari Hydeopower Project')
    st.subheader(' :blue[Dam Geotech Instrument Monitoring]')
    st.subheader(' :red[Piezometers(Tube Type)]')
    
    
        
    sheets=['ULN-PT-01','ULN-PT-02','ULN-PT-03','ULN-PT-04','ULN-PT-05','ULN-PT-06']
    sheet=st.selectbox('Select Equipment',sheets)
    if st.checkbox("load eqipment data file"):
        data=pd.read_excel('Dam Piezometric tube PT.xlsx',sheet)
        df=data.iloc[:,0:11]
        if st.checkbox('Show Equipment Data',sheet):
            st.dataframe(df)
        
        if st.checkbox('Show equipment detail'):
            df1=data.iloc[0:4,11:13]
            st.dataframe(df1)
        
        chart=st.checkbox('Show Chart')
        if chart:
            fig=make_subplots(specs=[[{'secondary_y':True}]])
            fig.add_trace(go.Scatter(x=df['Date'],y=df['Change In Level（m)'],name='Change in Level(m)'),secondary_y=False)
            fig.add_trace(go.Scatter(x=df['Date'],y=df['Osmotic pressure coefficient（αi)'],name='Osmotic pressure coefficient'),secondary_y=True)
            fig.update_layout(legend=dict(orientation='h',yanchor='top',xanchor='center',y=1.1,x=0.5))
            fig.update_yaxes(title='Change in level(m)',secondary_y=False)
            fig.update_yaxes(title='Osmatic Pressure Coefficient',secondary_y=True)
            st.plotly_chart(fig)
            
            
    