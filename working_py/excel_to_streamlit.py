import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pivottablejs import pivot_ui

st.title("안전실태조사 결과 분석(test)")

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.dropna(how='all', inplace = True)
    
    st.dataframe(df)

    option = st.sidebar.selectbox(
    'Which data do you want?', list(df.columns.values)
    )
    'You selected:', option

    # (1) 선택한 option(컬럼) 내 데이터를 추출하여 반환
    grouped = df.groupby(option)
    st.text(df[option].value_counts())

    # (2) 선택한 option(컬럼) 내 데이터를 list로 추출하여 반환
    g_list = list(grouped.groups.keys())
    st.text(g_list)
    for i in range(len(g_list)):
        st.text("{}:".format(g_list[i]))

    # piviottavle 생성(html파일 별도 생성)
    # t = pivot_ui(df)

    # with open(t.src, encoding='utf-8') as t:
    #     components.html(t.read(), width=1000, height=1000, scrolling=True)