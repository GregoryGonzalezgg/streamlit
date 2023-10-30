import streamlit as st
import time as tm
from datetime import datetime,time
import numpy as np
import pandas as pd

st.title('st.cache')
a0 = tm.time()
st.subheader('Using st.cache')

@st.cache_data()
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = tm.time()
st.info(a1-a0)
