import streamlit as st
view = [100, 150, 230]
view
st.write("# 유튜브 보기")
st.write("## bar chart")
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview