import streamlit as st
from streamlit_option_menu import option_menu

import pizele, pizpt,dampiz


st.set_page_config(page_title='Instrument Monitoring')

class Multiapp:
    #def __init__(self):
        #self.apps=[]
    #def add_app(self,title,function):
        #self.app.append({'title':title,'function':function})
    def run():
        with st.sidebar:
            app=option_menu(
                'Main Manu',
                options=['Piezometers(Elec)','Pezometers(Tube)','Dam Pizometers'],
                icons=['house-fill','person-circle','smile'],
                menu_icon="🏛️",
                styles={'container':{'background-color':'lightgray'}}
            )
        if app=='Piezometers(Elec)':
            pizele.app()
        if app=='Pezometers(Tube)':
            pizpt.app()
        if app=='Dam Pizometers':
            dampiz.app()
    
    run()        
    