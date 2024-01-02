import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

bank_data=pd.DataFrame({
    '은행':['국민은행','국민은행','국민은행','국민은행','국민은행','국민은행',
            '신한은행','신한은행','신한은행','신한은행','신한은행','신한은행',
            '하나은행','하나은행','하나은행','하나은행','하나은행','하나은행',
            '우리은행','우리은행','우리은행','우리은행','우리은행','우리은행'],
    '적금':['온국민 건강적금-골든라이프','청년도약계좌','특한적금','국민행복적금','미소드림적금','장병내일준비적금',
          '패밀리상생적금','신한SK LPG쏠쏠한 행복적금','청년도약계좌','군인행복적금','연금저축왕적금','쓸수록모이는 소비적금',
        '아이키움적금','청년도약계좌','급여하나 월복리 적금','트래블로그 여행 적금','도전365적금','주거래하나적금',
        '데일리워킹적금','N일적금','우리퍼스트 정기적금','Super주거래 정기적금','우리 으쓱 적금','첫급여 우리적금'],
    '기간(개월수)':[6,12,12,12,24,24,
               12,12,12,24,24,12,
               12,6,12,24,6,12,
               12,24,24,24,24,12],
    '최고금리(%)':[11,6,3,2.6,8,13,
            11,12,7,8.7,6.2,3,
            2,2.5,9,10,3.4,2.5,
            2.2,2.4,5,6,6.7,8],
    '기본금리(%)':[4,2,3,2.5,2.1,3,
               2,2.3,2.1,3,3,2,
               2,2.4,3.1,3,2.6,2,
               2.1,2.1,2.3,4,3.1,2.2]                       
})

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "어떤 정보를 얻고 싶은가요?",
        ("원하는 적금 찾기", "은행별 금리 분포도", "코드 보기")
    )    

#1    
if add_radio=='원하는 적금 찾기':

    st.header('원하는 조건의 적금을 찾아보세요!')

    selected_banks = st.multiselect('은행을 선택하시오:', bank_data['은행'].unique())
    selected_duration = st.multiselect('기간(개월수)를 선택하시오:', bank_data['기간(개월수)'].unique())
    selected_interest = st.multiselect('최고금리(%)를 선택하시오:', bank_data['최고금리(%)'].unique())

    selected_data = bank_data.copy() #초기에 전체 데이터를 담고 있음.

    if selected_banks: #각 조건문에 따라 데이터가 필터링 되어 담김
        selected_data = selected_data[selected_data['은행'].isin(selected_banks)]

    if selected_duration:
        selected_data = selected_data[selected_data['기간(개월수)'].isin(selected_duration)]

    if selected_interest:
        selected_data = selected_data[selected_data['최고금리(%)'].isin(selected_interest)]

    st.write(selected_data)  #만약 은행, 기간, 최고금리 모두 선택시 세개의 if 문 모두 실행됨. 

#2
if add_radio=='은행별 금리 분포도':
    st.scatter_chart(bank_data, x='은행', y='최고금리(%)', color='#ffaa00',use_container_width=True) 
    
#3 
code='''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

bank_data=pd.DataFrame({
    '은행':['국민은행','국민은행','국민은행','국민은행','국민은행','국민은행',
            '신한은행','신한은행','신한은행','신한은행','신한은행','신한은행',
            '하나은행','하나은행','하나은행','하나은행','하나은행','하나은행',
            '우리은행','우리은행','우리은행','우리은행','우리은행','우리은행'],
    '적금':['온국민 건강적금-골든라이프','청년도약계좌','특한적금','국민행복적금','미소드림적금','장병내일준비적금',
          '패밀리상생적금','신한SK LPG쏠쏠한 행복적금','청년도약계좌','군인행복적금','연금저축왕적금','쓸수록모이는 소비적금',
        '아이키움적금','청년도약계좌','급여하나 월복리 적금','트래블로그 여행 적금','도전365적금','주거래하나적금',
        '데일리워킹적금','N일적금','우리퍼스트 정기적금','Super주거래 정기적금','우리 으쓱 적금','첫급여 우리적금'],
    '기간(개월수)':[6,12,12,12,24,24,
               12,12,12,24,24,12,
               12,6,12,24,6,12,
               12,24,24,24,24,12],
    '최고금리(%)':[11,6,3,2.6,8,13,
            11,12,7,8.7,6.2,3,
            2,2.5,9,10,3.4,2.5,
            2.2,2.4,5,6,6.7,8],
    '기본금리(%)':[4,2,3,2.5,2.1,3,
               2,2.3,2.1,3,3,2,
               2,2.4,3.1,3,2.6,2,
               2.1,2.1,2.3,4,3.1,2.2]                       
})

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "어떤 정보를 얻고 싶은가요?",
        ("원하는 적금 찾기", "은행별 금리 분포도", "코드 보기")
    )    

#1    
if add_radio=='원하는 적금 찾기':

    st.header('원하는 조건의 적금을 찾아보세요!')

    selected_banks = st.multiselect('은행을 선택하시오:', bank_data['은행'].unique())
    selected_duration = st.multiselect('기간(개월수)를 선택하시오:', bank_data['기간(개월수)'].unique())
    selected_interest = st.multiselect('최고금리(%)를 선택하시오:', bank_data['최고금리(%)'].unique())

    selected_data = bank_data.copy() #초기에 전체 데이터를 담고 있음.

    if selected_banks: #각 조건문에 따라 데이터가 필터링 되어 담김
        selected_data = selected_data[selected_data['은행'].isin(selected_banks)]

    if selected_duration:
        selected_data = selected_data[selected_data['기간(개월수)'].isin(selected_duration)]

    if selected_interest:
        selected_data = selected_data[selected_data['최고금리(%)'].isin(selected_interest)]

    st.write(selected_data)  #만약 은행, 기간, 최고금리 모두 선택시 세개의 if 문 모두 실행됨. 

#2
if add_radio=='은행별 금리 분포도':
    st.scatter_chart(bank_data, x='은행', y='최고금리(%)', color='#ffaa00',use_container_width=True) 
    
#3 

if add_radio=='코드 보기':
    st.code(code,language='python')
'''
if add_radio=='코드 보기':
    st.code(code,language='python')