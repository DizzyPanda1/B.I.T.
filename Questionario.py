import streamlit as st
import pandas as pd
import time

questions = pd.read_csv('questions.csv')
st.set_page_config(page_title="Questionario", page_icon="🔥")

## make a max 5 choices and fill with empty strings
    

def genslider(q):
    el = q[4].strip('][').split(', ')
    st.write()
    v = st.slider(q[2], int(el[0]), int(el[1]), value = 0)
    return v
def genmultiple(q):
    el = q[4].strip('][').split(', ')

    v = st.radio(q[2], el)
    return v
def genbox(q):
    el = q[4].strip('][').split(', ')

    v = st.selectbox(q[2], el)
    return v

def GenerateCards(quest):
            print(quest)
            if quest[3] == 'slider':
                res = genslider(quest)
            elif quest[3] == 'multiple':
                res = genmultiple(quest)
            elif quest[3] =='selectbox':
                  res = genbox(quest)
            return res
        
            

d={}

###Question 1
q = questions.loc[0].tolist()
val1 = GenerateCards(q)

###Question 2
q = questions.loc[1].tolist()
val2 = GenerateCards(q)
el = q[4].strip('][').split(', ')
v2 = el.index(val2)
###Question 3
q = questions.loc[2].tolist()
val3 = GenerateCards(q)

###Question 4
q = questions.loc[3].tolist()
val4 = GenerateCards(q)
el = q[4].strip('][').split(', ')
v4 = el.index(val4)

###Question 4
q = questions.loc[4].tolist()
val5 = GenerateCards(q)

###Question 4
q = questions.loc[5].tolist()
val6 = GenerateCards(q)
el = q[4].strip('][').split(', ')
v6 = el.index(val6)
###Question 4
q = questions.loc[6].tolist()
val7 = GenerateCards(q)
###Question 4
q = questions.loc[7].tolist()
val8 = GenerateCards(q)
el = q[4].strip('][').split(', ')
v8 = el.index(val8)

###Question 4
q = questions.loc[8].tolist()
val9 = GenerateCards(q)

q = questions.loc[9].tolist()
val10 = GenerateCards(q)



col1, col2 = st.columns((4,1))
butt = col2.button('vai ai risultati')

if butt:  
    resflag = True
    l = [val1, v2, val3, v4, val5, v6, val7, v8, val9, val10]
 
   

    l = pd.DataFrame(l, columns=['value'])
    l.to_csv('results.csv')

  
