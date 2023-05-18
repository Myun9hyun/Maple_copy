import random
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
# import joblib
import seaborn as sns
from streamlit_option_menu import option_menu
import os
import openpyxl
from io import BytesIO
import base64
import datetime
import PyPDF2
import fitz
from bs4 import BeautifulSoup
FILE_PATH = 'data11.csv'

# 데이터를 파일에서 불러오기
def load_data():
    try:
        data = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Vote', 'Day'])
    return data

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH, index=False)

# 데이터 초기화 함수
def clear_data():
    data = pd.DataFrame(columns=['Name', 'Vote', 'Day'])
    # 파일 삭제
    os.remove(FILE_PATH)
    return data

# 데이터 삭제 함수
def delete_data(row_index):
    data = data.drop(index=row_index).reset_index(drop=True)
    return data

# 데이터 추가 함수
def add_data(name, vote, day):
    new_data = pd.DataFrame({'Name': [name], 'Vote': [vote], 'Day': [day]})
    data = pd.concat([data, new_data], ignore_index=True)
    return data

# 불러온 데이터를 전역 변수로 저장
data = load_data()

# Streamlit 애플리케이션 구현
def main():
    st.title("CSV 파일 관리")

    # 데이터 불러오기 버튼
    if st.button("데이터 불러오기"):
        data = load_data()
        st.write("데이터를 불러왔습니다.")
        st.write(data)

    # 데이터 저장하기 버튼
    if st.button("데이터 저장하기"):
        save_data(data)
        st.write("데이터를 저장했습니다.")

    # 데이터 초기화 버튼
    if st.button("데이터 초기화"):
        data = clear_data()
        st.write("데이터를 초기화했습니다.")
        st.write(data)

    # 데이터 추가 폼
    st.subheader("데이터 추가")
    name = st.text_input("이름")
    vote = st.number_input("투표 수", min_value=0)
    day = st.text_input("요일")
    if st.button("추가"):
        data = add_data(name, vote, day)
        st.write("데이터를 추가했습니다.")
        st.write(data)

    # 데이터 삭제 폼
    st.subheader("데이터 삭제")
    row_index = st.number_input("삭제할 행 인덱스", min_value=0, max_value=len(data) - 1, step=1)
    if st.button("삭제"):
        data = delete_data(row_index)
        st.write("데이터를 삭제했습니다.")
        st.write(data)

if __name__ == '__main__':
    main()
