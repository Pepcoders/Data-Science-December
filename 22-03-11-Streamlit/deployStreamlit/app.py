import streamlit as st
import pandas as pd
import numpy as np

url = 'https://www.github.com'
st.write("check out this [github](https://www.github.com)")

number = st.selectbox("Select your lucky nunmber", [1, 2, 3, 4, 5, 6])
st.write(number)

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# checkbox
checked = st.checkbox('checkbox')
if checked:
  st.table(df)
  


# multiselect
fist = st.multiselect('selcts your options', [x for x in range(10, 20)])
# st.write(fist)

# st.balloons()


# sidebar
st.sidebar.selectbox('How would like to connect ', ['Home', 'Email', 'Mobile Number'])

df1 = pd.DataFrame({
    "Number": [x for x in range(1, 10)],
    "Square" :[x*x for x in range(1, 10)],
    "cube":[x*x*x for x in range(1, 10)],
    "add10":[x+10 for x in range(1, 10)]
})
# df1

import matplotlib.pyplot as plt
# st.balloons()
plt.style.use('ggplot')
col = st.sidebar.selectbox("choose your columns", df1.columns)
plt.plot(df1['Number'], df1[col])
st.pyplot()



# import streamlit as st
option = st.radio('Select three known variables:', ['initial velocity (u)', 'final velocity (v)', 'acceleration (a)', 'time (t)'])

st.slider('Pick a Value', 5, 20, 7)
st.slider('Pick a Range', 5, 20, (7, 10))

import time

status = st.empty()
bar =  st.progress(0)
for i in range(100):
    status.text('Current Iteration {}'.format(i+1))
    bar.progress(i+1)
    time.sleep(0.2)

st.error('Error')
st.success('Success')
st.info('Info')
st.exception(RuntimeError('This is custom error'))
st.warning('Warning')