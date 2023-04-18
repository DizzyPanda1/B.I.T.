import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pickle
c1, c2 = st.columns((1,3))


excitement, sincerity, ruggedness, competence, sophistication = 0,0,0,0,0

cont  = st.container()
st.text_input('tiktok @')
contemporary = c1.slider("contemporary", 1,5)
unique = c1.slider("unique", 1,5)
up_to_class= c1.slider("up_to_class", 1,5)
independent = c1.slider("independent", 1,5)
imaginative= c1.slider("imaginative", 1,5)

dth = c1.slider("downt_to_earth", 1,5)
honest = c1.slider("honest", 1,5)
sincere = c1.slider("sincere", 1,5)
realistic = c1.slider("realistic", 1,5)
original = c1.slider("original", 1,5)

outdoorsy = c1.slider("outdoorsy", 1,5)
masculine = c1.slider("masculine", 1,5)
tough= c1.slider("tough", 1,5)
western = c1.slider("western", 1,5)
rugged = c1.slider("rugged", 1,5)


secure = c1.slider("secure", 1,5)
intelligent = c1.slider("intelligent", 1,5)
corporate = c1.slider("corporate", 1,5)
leader = c1.slider("leader", 1,5)
confident= c1.slider("confident", 1,5)

upper_class= c1.slider("upper class", 1,5)
feminine= c1.slider("feminine", 1,5)
smooth = c1.slider("smooth", 1,5)
good_looking = c1.slider("good looking", 1,5)
glamorous = c1.slider("glamorous", 1,5)


excitement = np.mean([contemporary, unique, up_to_class,independent, imaginative])
sincerity = np.mean([dth, honest, sincere, realistic, original])
ruggedness = np.mean([outdoorsy, masculine, tough, western, rugged])
competence = np.mean([secure, intelligent, corporate, leader, confident])
sophistication = np.mean([upper_class, feminine, smooth, good_looking, glamorous])

df = pd.DataFrame(dict(
    value = [excitement, sincerity, ruggedness, competence, sophistication ],
    variable = ['excitement', 'sincerity', 'ruggedness', 'competence', 'sophistication' ]
))

fig = px.line_polar(df, r = 'value', theta = 'variable', line_close = True)
fig.update_traces(fill = 'toself')

c2.plotly_chart(fig)




