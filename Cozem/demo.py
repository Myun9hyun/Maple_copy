import streamlit as st
import pandas as pd
import os
import requests

# 파일 다운로드 함수
def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# 빈 CSV 파일 다운로드
CSV_URL = 'https://raw.githubusercontent.com/Myun9hyun/Maple_copy/main/Cozem/data11.csv'
FILE_PATH = 'data11.csv'

# if not os.path.exists(FILE_PATH):
#     st.write('빈 CSV 파일 다운로드 중...')
#     download_file(CSV_URL, FILE_PATH)
#     st.write('빈 CSV 파일 다운로드 완료')

options = ["닉네임 남기기➕", "닉네임 조회🔎", "닉네임 삭제✂", "초기화💣", "추첨하기🎊"]
option = st.selectbox("기능 선택", options, key='select3')

# 파일에서 데이터 불러오기
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
    global data
    data = pd.DataFrame(columns=['Name', 'Vote', 'Day'])
    # 파일 삭제
    os.remove(FILE_PATH)

# 데이터 삭제 함수
def delete_data(row_index):
    global data
    data = data.drop(index=row_index).reset_index(drop=True)

# 불러온 데이터를 전역 변수로 저장
data = load_data()

def add_data(name, vote, day):
    global data
    new_data = pd.DataFrame({'Name': [name], 'Vote': [vote], 'Day': [day]})
    data = pd.concat([data, new_data], ignore_index=True)

if option == "닉네임 남기기➕":
    name = st.text_input("닉네임")
    vote = st.number_input("투표수", value=0)
    day = st.number_input("날짜", value=0)
    if st.button("저장"):
        add_data(name, vote, day)
        save_data(data)
        st.success("데이터가 저장되었습니다.")

elif option == "닉네임 조회🔎":
    st.table(data)

elif option == "닉네임 삭제✂":
    row_index = st.number_input("삭제할 행 번호", min_value=0, max_value=len(data)-1, value=0)
    if st.button("삭제"):
        delete_data(row_index)
        save_data(data)
        st.success("데이터가 삭제되었습니다.")

elif option == "초기화💣":
    if st.button("초기화"):
        clear_data()
        st.success("데이터가 초기화되었습니다.")

elif option == "추첨하기🎊":
    # 추첨 로직 구현
    pass
