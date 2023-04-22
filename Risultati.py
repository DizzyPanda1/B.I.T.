import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title="HotBoard", page_icon="🔥")

st.sidebar.header('Results')

df = pd.read_csv('results.csv')
data = df['value'].tolist()
excitement = data[0]+data[1]
sincerity = data[2]+data[3]
ruggedness = data[4]+data[5]
competence = data[6]+data[7]
sophistication = data[8]+data[9]

cont = st.container()
col1, col2, col3, col4 ,col5 = cont.columns((1,1,1,1,1))
col1.metric('excitement',excitement)
col2.metric('sincerity',sincerity)
col3.metric('ruggedness',ruggedness)
col4.metric('competence', competence)
col5.metric('sophistication',sophistication)




df = pd.DataFrame(dict(
    value = [excitement, sincerity, ruggedness, competence, sophistication ],
    variable = ['excitement', 'sincerity', 'ruggedness', 'competence', 'sophistication' ]
))

fig = px.line_polar(df, r = 'value', theta = 'variable', line_close = True)
fig.update_traces(fill = 'toself')

st.plotly_chart(fig)







