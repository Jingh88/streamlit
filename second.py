import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

_, col, _ = st.columns([2,6,2])
col.header('Iris 시각화')
iris_df = sns.load_dataset('iris')

with st.sidebar:
    selectX = st.selectbox('X 변수를 선택하세요:', ['sepal_length','sepal_width','petal_length','petal_width'])
    selectY = st.selectbox('Y 변수를 선택하세요:', ['sepal_length','sepal_width','petal_length','petal_width'])
    selectSpecies = st.multiselect('붓꽃 유형을 선택하세요:', ['setosa','versicolor','virginica'])
    selectAlpha = st.slider('alpha 설정:', 0.1, 1.0, 0.5)

    colors = {'setosa':'red', 'versicolor':'orange','virginica':'green'}

if selectSpecies:
    
    fig = plt.figure(figsize=(7,5))

    for aSpecies in selectSpecies:
        df = iris_df[iris_df.species==aSpecies]
        plt.scatter(df[selectX], df[selectY], color=colors[aSpecies], alpha=selectAlpha, label=aSpecies)

    plt.xlabel(selectX)
    plt.ylabel(selectY)
    plt.title('iris scatter plot')
    st.pyplot(fig)

else:
    st.warning('붓꽃의 유형을 선택해주세요')    