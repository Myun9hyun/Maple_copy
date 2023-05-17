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


st.set_page_config(page_title="BanShamDoongDolYoung", page_icon=":rabbit:", layout="wide")
password = "970808"
password_test = "1234"

image = Image.open("Cozem/image/cover_guild.jpg")
width, height = image.size
# 이미지에 텍스트 추가
draw = ImageDraw.Draw(image)
text_kor = "아기자기"
text_eng = "Welcome to"
text_ver = "updated_05.16"
text_madeby = "@둥둥향"
font_kor = ImageFont.truetype("Cozem/font/NanumSquareNeo-eHv.ttf", 50)
font_eng = ImageFont.truetype("Cozem/font/ARIAL.TTF", 50)
text_width, text_height = draw.textsize(text_kor, font=font_kor)
font_ver = ImageFont.truetype("Cozem/font/NanumSquareNeo-eHv.ttf", 15)
font_madeby = ImageFont.truetype("Cozem/font/NanumSquareNeo-eHv.ttf", 15)
stroke_width = 2
stroke_fill = (0, 0, 0)

x = text_width - 100
y = height - text_height - 200
z = height - text_height - 255
x_ver = width - text_width + 70
y_ver = height - text_height + 30
x_made = width - text_width + 70
y_made = height - text_height + 10
# 테두리가 있는 텍스트 그리기

# 아기자기 글씨 구현
draw.text((x - stroke_width, y), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x + stroke_width, y), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y - stroke_width), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y + stroke_width), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y), text_kor, font=font_kor, fill=(255, 255, 255))

# Welcome to 구현
draw.text((x - stroke_width, z), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x + stroke_width, z), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, z - stroke_width), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, z + stroke_width), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, z), text_eng, font=font_eng, fill=(255, 255, 255))

# 버전 구현
draw.text((x_ver - stroke_width, y_ver), text_ver, font=font_ver, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_ver + stroke_width, y_ver), text_ver, font=font_ver, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_ver, y_ver - stroke_width), text_ver, font=font_ver, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_ver, y_ver + stroke_width), text_ver, font=font_ver, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_ver, y_ver), text_ver, font=font_ver, fill=(255, 255, 255))

# madeby구현
draw.text((x_made - stroke_width, y_made), text_madeby, font=font_madeby, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_made + stroke_width, y_made), text_madeby, font=font_madeby, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_made, y_made - stroke_width), text_madeby, font=font_madeby, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_made, y_made + stroke_width), text_madeby, font=font_madeby, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x_made, y_made), text_madeby, font=font_madeby, fill=(255, 255, 255))
def set_BGM(bgm):
    if bgm:
        audio_path = f"Cozem/bgm/{bgm}.mp3"
        audio_file = open(audio_path, 'rb').read()

        return st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                            {base64.b64encode(audio_file).decode()}"></audio>',\
                            unsafe_allow_html=True)
    else:
        st.write("잘못된 입력입니다.")
        pass

# # streamlit에 이미지 표시
st.image(image, use_column_width=True)

with st.sidebar:
    choice = option_menu("Menu", ["메인페이지", "길드페이지", "퀴즈풀기", "아카이브", "의견남기기"],
                         icons=['house', 'bi bi-emoji-smile', 'bi bi-lightbulb', 'bi bi-palette','bi bi-archive', 'bi bi-card-text'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    df = pd.DataFrame()

    # st.sidebar.dataframe(df)
    st.write(df.to_markdown(index=False))
    # choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)
    bgms = ["나린","도원경", "차원의균열", "첫번째동행", "에오스탑외부", "오시리아대륙항해", "아쿠아리움필드",
                "오디움_신의창", "강림_괴력난신" , "아델의맹세", "아쉴롬_일리움", "악몽의시계탑", "시간의신전"]
    bgm = st.selectbox("🔈원하시는 배경음악을 골라주세용", bgms)
    st.write("음악은 다른 기능을 사용하면 정지됩니다.")
    # set_BGM(bgm)
    col3, col4 = st.columns(2)
    with col3:
        st.write("Play")
        if st.button("▶"):
            st.success("음악 재생")
            set_BGM(bgm)
    with col4:
        st.write("Stop")
        if st.button("⬛"):
            st.warning("음악 정지")
            pass

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "메인페이지":
    st.header("💜아기자기 길드 페이지💚")
    st.write("### 아기자기 길드 페이지에 오신것을 환영합니다😊")
      
    st.write()
    '''
    ##### 우리 아기자기는요~
    * 2019년 6월 창설
    * 2022년 5월 14일 30레벨 달성
    * 47포 길드
    * Lv220 이상 가입 가능
    * 연합길드 '초초' 보유
    '''

elif choice == "길드페이지":
    tab1, tab2, tab3= st.tabs(["😎Manager", "📋Rules", "Character Data"])
    with tab1:
        st.header("😎Manager")
        st.write()
        # col1, col2 = st.columns(2)
        # with col1:
        '''
        ---
        ### 길드 간부진 💪
        | 직책 | 이름  | 직업 | 간부진 1:1오픈채팅 | 메지지 프로필 |
        | :---: | :---: | :---: | :---: | :---:|
        | 길마👑 | 뱌닢 | 나이트로드 | [![Colab](https://img.shields.io/badge/kakaotalk-뱌닢-yellow)](https://open.kakao.com/o/spPPOAhc) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/뱌닢) |
        | 부마 | 릎샴  | 아크 | [![Colab](https://img.shields.io/badge/kakaotalk-릎샴-yellow)](https://open.kakao.com/o/s0FeFIee) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/릎샴) |
        | 부마 | 둥둥향 | 캐논슈터 | [![Colab](https://img.shields.io/badge/kakaotalk-둥둥향-yellow)](https://open.kakao.com/o/sl6WBJUc) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/둥둥향) |
        | 부마 | 돌체라페  | 메르세데스 | [![Colab](https://img.shields.io/badge/kakaotalk-돌체라페-yellow)](https://open.kakao.com/o/sEmQw9Ye) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/돌체라페) |
        | 부마 | 영래곰  | 듀얼블레이드 | [![Colab](https://img.shields.io/badge/kakaotalk-영래곰-yellow)](https://open.kakao.com/o/sBK5y3md) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/영래곰) |
        '''
# pdf_path = "Cozem/rule/아기자기_길드_규정_2023.pdf"
        # with col2:
        #     st.image("Cozem/image/elinel.jpg", use_column_width=True)
    with tab2:
        st.header("📋길드 규정집📋")
        # st.image("Cozem/read_me_image/guide_new_1.jpg", use_column_width=True)
        # st.image("Cozem/read_me_image/guide_new_2.jpg", use_column_width=True)
        st.image("Cozem/read_me_image/rule_new.jpg", use_column_width=True)
        # # PDF 파일의 URL을 입력받습니다.
        # st.write("pdf파일!")
        # pdf_url = "Cozem/rule/아기자기_길드_규정_2023.pdf"

        # # PDF 파일을 이미지로 변환합니다.
        # if pdf_url:
        #     with fitz.open(pdf_url) as doc:
        #         for i, page in enumerate(doc):
        #             pixmap = page.get_pixmap(dpi=300)  # dpi 값을 300으로 설정
        #             image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        #             st.image(image, caption=f"Page {i+1}", use_column_width=True)
    with tab3:
        st.header("메이플지지 검색")

        # 검색할 캐릭터 이름
        character_name = st.text_input("닉네임을 입력해주세요 : ")

        # 검색 결과 페이지의 URL
        url = f'https://maple.gg/u/{character_name}'

        if character_name:
            # requests 모듈을 이용해 HTTP GET 요청을 보내고 HTML 코드를 가져옴
            response = requests.get(url)
            html = response.content

            # BeautifulSoup 모듈을 이용해 HTML 코드를 파싱
            soup = BeautifulSoup(html, 'html.parser')

            # 직업 정보 가져오기
            job_element = soup.select_one('.user-summary-item:nth-child(2)')
            job = job_element.text.strip() if job_element else 'Not found'

            # 월드 정보 가져오기
            world_element = soup.select_one('.user-detail h3 img')
            world = world_element['alt'] if world_element else 'Not found'

            # 길드 정보 가져오기
            guild_element = soup.select_one('.user-additional b')
            guild = guild_element.find_next_sibling().text.strip() if guild_element else 'Not found'

            # 무릉 최고기록 정보 가져오기
            mulung_element = soup.select_one('.col-lg-3:nth-child(1) .user-summary-box .user-summary-box-content')
            if mulung_element:
                mulung_floor = mulung_element.select_one('.user-summary-floor').text.strip().split()[0]
                mulung_duration = mulung_element.select_one('.user-summary-duration').text.strip()
                mulung_info = f'{mulung_floor} ({mulung_duration})'
            else:
                mulung_info = 'Not found'

            level_element = soup.select_one('.user-summary-item:nth-child(1)')
            if level_element:
                level_info = level_element.text.strip().split('(')
                level = level_info[0]
                exp_percentage = level_info[1].replace(')', '')
            else:
                level = 'Not found'
                exp_percentage = 'Not found'

        def get_maple_info(character_name):
            url = f"https://maple.gg/u/{character_name}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            coord_items = soup.select(".character-coord__item")
            coord_list = []
            for item in coord_items:
                item_type = item.select_one(".character-coord__item-type").text.strip()
                item_name = item.select_one(".character-coord__item-name").text.strip()
                coord_list.append(f"{item_type}: {item_name}")

            img_url = soup.select_one(".character-image")["src"]
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))

            return coord_list, img

        if st.button("코디 분석"):
            if not character_name:
                st.warning("닉네임을 입력해주세요!")
            else:
                coord_list, img = get_maple_info(character_name)
                st.write("코디 분석 결과:")
                st.image(img, width=200)
                for item in coord_list:
                    st.write(item) 

        if st.button("랭킹 조회"):
            st.write(f'직업: {job}')
            st.write(f'서버: {world}')
            st.write(f'길드: {guild}')
            st.write(f'무릉: {mulung_info}')
            st.write(f'레벨: {level}')
            st.write(f'경험치: {exp_percentage}')
            
elif choice == "퀴즈풀기":
    tab1, tab2, tab3= st.tabs(["Readme", "Quiz", "Special_Quiz"])
    with tab1:
        st.header("길드 창설이벤트 퀴즈 풀기!")
        st.write()
        '''
        ## 아래의 글을 먼저 잘 읽고 참여하길 바래!
        #### 우리 아기자기가 창설 4주년을 맞아 퀴즈 이벤트를 준비해봤어!
        #### 우리 아기자기와 항상 함께해준 아깅이들 정말 고마워!
        #### 이번 창설 이벤트는 참여 조건이 기여도 15만 이상의 아깅이들만 참석할 수 있어!
        #### 창설이벤트에 참석하지 못하더라도, 왼쪽 메뉴에서 '의견남기기'탭에 들어가 의견을 남겨줘!
        #### 의견을 남겨준 길드원 전원에게 코어젬스톤 5개씩 지급할게!
        #### Quiz탭에 들어가서 문제를 순서대로 풀면 돼!
        #### 첫번째 문제의 비밀번호는 공지방에 시간에 맞춰 공개될거야!
        '''
    with tab2:
        st.header( "길드 창설이벤트 퀴즈 풀기!")
        st.write("#### 창설이벤트에 참가해준 아깅이들 모두 반가워!")
        password = "970808"
        password1 = "창설이벤트"
        answer1 = "아기자기"
        password2 = "초초"
        answer2 = "뱌닢"
        password3 = "반디"
        answer3 = "릎샴"
        password4 = "금손"
        answer4 = "둥둥향"
        password5 = "둥둥"
        answer5 = "1"
        password6 = "커피"
        answer6 = "4"
        password7 = ""
        answer7 = "아깅이"
        password8 = ""
        answer8 = "3"
        password9 = ""
        answer9 = "2"
        password10 = ""
        answer10 = "뱐뎅"


        st.write("1번 문제의 비밀번호는 공지방에서 알려주는 비밀번호를 확인해줘")

        # ----------------------------------------------------------------------------------------------------------
        # 1번
        quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
        if quiz1_password == password1:
            quiz1 = st.text_input("우리 길드의 이름은 뭘까?(⊙_⊙)？")
            if st.button("정답 확인", key="check_answer_button1"):
                if quiz1 == answer1:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("우리 길드와 함께해줘서 고마워 ╰(*°▽°*)╯")
                    st.write("2번 문제 오픈을 위한 비밀번호는 '초초' 야!")
                    st.write("'초초'는 우리 아기자기 연합 길드로, 길드원들의 부캐릭터를 가입 시킬 수 있어!")
                else:
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key="check_hint_button1"):
                    st.write("이건 힌트를 줄 수가 없어! 잘 생각해 봐")
        elif quiz1_password != "" and quiz1_password != password1:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 2번
        quiz2_password = st.text_input("2번 문제 오픈을 위한 비밀번호를 입력해주세요!")
        if quiz2_password == password2:
            quiz2 = st.text_input("아기자기 길드의 길드마스터로, 디코에 자주 출몰하는 간부의 이름은?")
            if st.button("정답 확인"):
                if quiz2 == answer2:
                    st.balloons()
                    st.success("정답입니다!")
                    # st.image("메지지 이미지 넣기")
                    st.write("[뱌닢]은 우리 길드의 길드마스터야!")
                    st.write("[뱌닢]은 길드를 위해 누구보다 열심히 일해😊")
                    st.write("[뱌닢]은 매번 위클리 이벤트로 분배된 코젬을 나누는 역할을 하고있어!")
                    st.write("[뱌닢]은 길드 노블 공지, 길드 이벤트 공지등의 역할도 하고 있어!")
                    st.write("3번 문제 오픈을 위한 비밀번호는 '반디' 야!")
                else :
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기"):
                st.write("이 사람의 예전 직업은 '제로'였어!")
                st.write("이 사람의 예전 본캐의 닉네임은 '반디풀잎' 이야!")
        elif quiz2_password != "" and quiz2_password != password2:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 3번
        quiz3_password = st.text_input("3번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz3_password3")
        if quiz3_password == password3:
            quiz3 = st.text_input("이번 메이플 팬페스트 금손 부스에 참석한 간부는 누구일까?")
            if st.button("정답 확인", key= "check_answer_button3"):
                if quiz3 == answer3:
                    st.balloons()
                    st.success("정답입니다!")
                    # st.image("메지지 이미지 넣기")
                    st.write("[릎샴]은 이번 팬페스트에 '볼빵빵하우스'라는 부스 담당자로 참석했어!")
                    st.write("[릎샴]은 길드에서 포스터, 각종 양식틀, 길드규정문 등을 만드는 디자이너 역할을 하고 있어!")
                    st.write("[릎샴]은 이번 창설이벤트 경품으로 제공되는 물품도 만들었어!")
                    st.write("[릎샴]은 길드 이벤트, 공지글 작성 후 최종 검토해주는 역할도 하고 있어!")


                    st.write("4번 문제 오픈을 위한 비밀번호는 '금손' 이야!")
                else : 
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button3"):
                st.write("캡틴 김수호와 직업이 같은 사람을 생각해봐!")
                st.write("이 사람은 '이달의 아깅이' 이벤트에서 키링 이미지 제작도 해주고 있어!")
        elif quiz3_password != "" and quiz3_password != password3:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 4번
        quiz4_password = st.text_input("4번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz4_password")
        if quiz4_password == password4:
            quiz4 = st.text_input("이 페이지 누가 만들었을까?")
            if st.button("정답 확인", key="check_answer_button4"):
                if quiz4 == answer4:
                    st.balloons()
                    st.success("정답입니다!")
                    # st.image("메지지 프로필 넣기")
                    st.write("[둥둥향]은 하찮은 컴퓨터 실력으로 페이지와 코젬계산기 만드는 역할을 맡고 있어!")
                    st.write("[둥둥향]은 공지방에서 이벤트 정리글을 공유하는 역할을 하고 있어!")
                    st.write("[둥둥향]은 공지글의 멘트를 작성하는 역할을 하고 있어!")
                    st.write("[둥둥향]은 페이스북 '스카니아모임'에 길드 홍보 멘트를 작성했어!")
                    st.write("5번 문제 오픈을 위한 비밀번호는 '둥둥'이야!")
                else :
                    st.error("다시 한번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button4"):
                st.write("이 사람의 직업은 캐논마스터야!")
                st.write("이 사람은 공지방에서 이벤트 알림이 역할을 하고 있어!")
                st.write("상단에 배너 우측 하단을 보면 만든 사람이 적혀있어!")
        elif quiz4_password != "" and quiz4_password != password4:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 5번
        quiz5_password = st.text_input("5번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz5_password")
        if quiz5_password == password5:
            quiz5 = st.text_input("문제를 읽고, 아래의 보기에서 정답을 '숫자'로 입력해줘!", key="quiz5")
            st.write("나는 공지방에서 썬데이 메이플 공지를 하고 있습니다!")
            st.write("나의 직업은 '영웅' 직업군입니다")
            st.write("나는 누구 일까요?")
            st.write("---")
            st.write("1. 돌체라페")
            st.write("2. 카페라떼")
            st.write("3. 콤퓨타")
            st.write("4. 턴테이블")
            st.write("5. 퀸메아")
            if st.button("정답 확인", key = "check_answer_button5"):
                if quiz5 == answer5:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("[돌체라페]는 간부진 막내로서 다른 간부들을 위해 열심히 도와주고 있어!")
                    st.write("[돌체라페]는 매주 금요일 10시 썬데이메이플 내용을 공지방에 공유해주고 있어")
                    st.write("[돌체라페]는 매주 일요일 길드 컨텐츠 이행여부를 확인하고, 직위 상승/하락을 확인하고 있어")
                    st.write("[돌체라페]는 간부진들 중 막내야!")
                    st.write("6번 문제 오픈을 위한 비밀번호는 '커피'야!")
                else  :
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button5"):
                st.write("나는 연유가 들어간 커피야!")
        elif quiz5_password != "" and quiz5_password != password5:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 6번
        quiz6_password = st.text_input("6번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz6_password")
        if quiz6_password == password6:
            quiz6 = st.text_input("문제를 읽고, 아래의 보기에서 정답을 '숫자'로 입력해줘!", key = "quiz6")
            st.write("나는 이름에 동물이 들어가있어")
            st.write("나의 직업은 '모험가 도적군'이야")
            st.write("나는 레벨이 280을 넘었어!")
            st.write("나는 누구일까요?")
            st.write("1. 영래닭")
            st.write("2. 영래소")
            st.write("3. 영래모기")
            st.write("4. 영래곰")
            if st.button("정답 확인", key = "check_answer_button6"):
                if quiz6 == answer6:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("[영래곰]은 길드에서 길드원 명단을 엑셀로 관리를 하고 있어.")
                    st.write("[영래곰]은 간부진들 중에서 레벨이 제일 높아")
                    st.write("[영래곰]은 플래그 모든맵에서 1000점을 획득할 수 있는 플래그 고수야")
                    st.write("[영래곰]은 주기적으로 고확으로 길드원 모집을 하고 있어!")
                    st.write("[영래곰]은 여러캐릭으로 부족한 주간미션과 플래그 점수를 채워주고 있어!")
                    st.write("7번 문제 오픈을 위한 비밀번호는 ") 
                else : 
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button6"):
                st.write("문을 거꾸로 뒤집으면 뭘까요?")
        elif quiz6_password != "" and quiz6_password != password6:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 7번
        quiz7_password = st.text_input("7번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz7_password")
        if quiz7_password == password7:
            quiz7 = st.text_input("길드원분들을 부르는 애칭은 뭘까?╰(°▽°)╯")
            if st.button("정답 확인", key = "check_answer_button7"):
                if quiz7 == answer7:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("우리가 정한 애칭은 [아깅이]야! ")
                    st.write("애칭은 아깅이 여러분들의 투표로 정해졌어(●'◡'●)")
                    st.write("아깅이들이 함께 해줘서 아기자기가 여기까지 성장할 수 있었어!")
                    st.write("앞으로도 잘 부탁해(´▽`ʃ♡ƪ)")
                else :
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button7"):
                st.write("간부진들이 공지글을 올릴때 종종 이 단어를 쓰곤 해")
        elif quiz7_password != "" and quiz7_password != password7:
            st.error("비밀번호가 틀렸어!")
        
        # ----------------------------------------------------------------------------------------------------------
        # 8번
        quiz8_password = st.text_input("8번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz8_password")
        if quiz8_password == password8:
            quiz8 = st.text_input("문제를 읽고, 아래의 보기에서 정답을 '숫자'로 입력해줘!",key = "quiz8")
            st.write("길드 필참 컨텐츠 중 주간미션을 이 점수 만큼 필수로 채워야 하는데 몇점 일까?")
            st.write("보기")
            st.write("1. 5점")
            st.write("2. 4점")
            st.write("3. 3점")
            st.write("4. 2점")
            st.write("5. 1점")
            if st.button("정답 확인", key = "check_answer_button8"):
                if quiz8 == answer8:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("노블레스 스킬 사용을 위해서는 주간미션을 3점이상 채워줘야해!")
                    st.write("그 외에는 지하수로를 점수 제한 없이 참여만 하면 되니까 잠깐씩만 시간 내서 참여해줘")
                else :
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기", key = "check_hint_button8"):
                st.write("레벨 범위 몬스터 15000마리를 퇴치하면 채울 수 있어!")
                st.write("레벨 범위 몬스터 5000마리 당 주간미션은 1점 채워져😉")
        elif quiz8_password != ""  and quiz_password8 != password8:
            st.error("비밀번호가 틀렸어!")
        
        # ----------------------------------------------------------------------------------------------------------
        # 9번
        quiz9_password = st.text_input("9번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz9_password") 
        if quiz9_password == password9:
            quiz9 = st.text_input("문제를 읽고, 아래의 보기에서 정답을 '숫자'로 입력해줘!", key = "quiz9")
            st.write("아기자기 길드의 길드집은 어디일까?")
            st.write("보기")
            st.write("1. Ch.18 셀라스")       
            st.write("2. Ch.18 리나의 집")       
            st.write("3. Ch.18 헤네시스 공원")       
            st.write("4. Ch.18 세르니움 광장")       
            st.write("5. Ch.18 이름없는 마을")       
            if st.button("정답 확인"):
                if quiz9 == password9:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("아기자기의 길드집은 18채널 리나의 집이야!")
                    st.write("우리는 여기서 길드 사진을 찍기도 하고, 대화를 나누기도 해!")
                    st.write("헤도, 와헌등의 버프가 필요하면 길집에서 받을 수 있어(✿◡‿◡)")
                    st.write("아깅이들도 길집에 자주 모여서 친해지고, 대화도 자주 했으면 좋겠어(☆▽☆)")
                else : 
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기"):
                st.write("인게임 길드 소개글을 확인해봐!")
        elif quiz9_password != "" and quiz_password9 != password9:
            st.error("비밀번호가 틀렸어!")

        # ----------------------------------------------------------------------------------------------------------
        # 10번    
        quiz10_password = st.text_input("10번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz10_password")
        if quiz10_password == password10:
            quiz10 = st.text_input("우리 아기자기에서 길드원들 중 기여도가 제일 높은 사람의 닉네임을 적어줘!")
            if st.button("정답 확인"):
                if quiz10 == password10:
                    st.balloons()
                    st.success("정답입니다!")
                    st.write("[뱐뎅]님은 우리 아기자기에서 길드원들 중에서 기여도가 제일 높아!")
                    st.write("[뱐뎅]님의 기여도는 무려 ()나 돼!┗|｀O′|┛")
                    st.write("스페셜 문제 오픈을 위한 비밀번호는 '아깅이들고마워'야!")
                    st.write("스페셜 문제는 Special_Quiz탭에서 진행해줘!")
                else:
                    st.warning("다시 한 번 생각해봐!")
            if st.button("힌트 보기"):
                st.write("[뱍뎅]과 이름이 매우 유사해!")
                st.write("ㄱ과 ㄷ 사이에 들어갈 자음은 뭘까요?")
        elif quiz10_password != "" and quiz10_password != password10:
            st.error("비밀번호가 틀렸어!")
        
    # ----------------------------------------------------------------------------------------------------------
    # 11번    
    
    with tab3:
        password11 ="아깅이들고마워"
        quiz11_password = st.text_input("11번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz11_password")
        if quiz11_password == password11:
            st.write("와~! 여기까지 문제 푸느라 정말 고생 많았어!")
            st.write("우리 아기자기가 이렇게 유지되고 있는것은 아깅이들 덕분이야!")
            st.write("정말 고맙다는 마음 다시 한번 전하고 싶어!（づ￣3￣）づ╭❤️～")
            st.write("아래의 입력 창에 문제를 끝까지 풀어준 ")

elif choice == "아카이브":
    st.header("길드 아카이브")
    options = st.selectbox(
    '원하는 종류를 골라주세요',
    ('포스터', '길드사진'))
    if options=='포스터':
        st.write("길드포스터 아카이브🎨")
        st.write("길드홍보 포스터 저장소입니다")
        option = st.selectbox(
        '원하는 포스터를 골라주세요',
        ('초기포스터', '주황', '빨강', '파랑', '오디움', '회색', '봄'))
        if option == '초기포스터':
            st.write("초기 포스터입니다")
            st.image("Cozem/poster/초기.jpg", use_column_width=True)
        elif option == '주황':
            st.write("주황색 컨셉 포스터입니다")
            st.image("Cozem/poster/주황.jpg", width=500)
        elif option == '빨강':
            st.write("빨간색 컨셉 포스터입니다")
            st.image("Cozem/poster/빨강.jpg", width=500)
        elif option == '파랑':
            st.write("파란색 컨셉 포스터입니다")
            st.image("Cozem/poster/파랑.jpg", width=500)    
        elif option == '오디움':
            st.write("오디움 컨셉 포스터입니다")
            st.image("Cozem/poster/오디움.jpg", width=500)
        elif option == '회색':
            st.write("회색 컨셉 포스터입니다")
            st.image("Cozem/poster/회색.jpg", width=500)
        elif option == '봄':
            st.write("봄 컨셉 포스터입니다")
            st.image("Cozem/poster/봄.jpg", width=500)    
    elif options=='길드사진':
        st.write("길드 사진 아카이브입니다.")
        col1, col2=st.columns(2)
        with col1:
            st.write("**리나와 한컷**")
            st.image("Cozem/image/guild1.jpg", use_column_width=True)
        with col2:
            st.write("**왕의 쉼터**")
            st.image("Cozem/image/guild2.jpg", use_column_width=True)
        col3, col4 = st.columns(2)
        with col3:
            st.write("**옷맞춤**")
            st.image("Cozem/image/guild3.jpg", use_column_width=True)
        with col4:
            st.write("**엘리넬**")
            st.image("Cozem/image/elinel.jpg", use_column_width=True)

elif choice == "의견남기기":
    st.write("간부진들에게 하고싶은 말을 남겨주세요")
    st.write("남겨주신 의견은 간부진들만 확인하며, 남겨주신 내용을 바탕으로 더 나은 길드 만들겠습니다!")
    FILE_PATH10 = 'data10.csv'
    options = ["의견 남기기➕", "내용 조회🔎", "내용 삭제✂", "초기화💣" ]
    option = st.selectbox("기능 선택", options, key='select3')
    # 파일에서 데이터 불러오기
    def load_data10():
        try: 
            data10 = pd.read_csv(FILE_PATH10)
        except FileNotFoundError:
            data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
        return data10

    # 데이터를 파일에 저장하기
    def save_data10(data10):
        data10.to_csv(FILE_PATH10, index=False)

    # 데이터 초기화 함수
    def clear_data10():
        global data10
        data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
        # 파일 삭제
        os.remove(FILE_PATH10)

    # 데이터 삭제 함수
    def delete_data10(row_index):
        global data10
        data10 = data10.drop(index=row_index).reset_index(drop=True)

    # 불러온 데이터를 전역 변수로 저장
    data10 = load_data10()
    def add_data10(name, comment, day):
        global data10
        new_data10 = pd.DataFrame({'Name': [name], 'Comment': [comment], 'Day': [day]})
        data10 = pd.concat([data10, new_data10], ignore_index=True)
    def main():
        if option == "내용 삭제✂":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.text_input('비밀번호를 입력해주세요 : ', key='pass1')
            if password_input == password:
                st.success('접근을 허용합니다')
                st.write(data10[['Name','Comment', 'Day']])
                row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data10.shape[0]-1)
                st.write("Enter를 입력하면 삭제됩니다.")
                if st.button('데이터 삭제'):
                    # 해당 행이 존재할 경우, 행을 삭제
                    if row_index >= 0 and row_index < data10.shape[0]:
                        delete_data10(row_index)
                        save_data10(data10)  # 데이터를 파일에 저장
                        st.success('입력하신 행이 삭제되었습니다.')
            elif password_input != "" and password_input != password:
                st.warning('비밀번호가 틀렸습니다.')
        elif option == "의견 남기기➕":
            name = st.text_input("의견 남기시는 분의 이름을 입력해주세요")
            comment = st.text_input("내용을 적어주세요")
            day = st.date_input(
                "의견 남기는 날짜를 설정해주세요",
                datetime.date.today())
            if st.button('의견 남기기'):
                add_data10(name, comment, day)
                save_data10(data10)
                st.success("감사합니다!!ヾ(•ω•`)o")

        elif option == "내용 조회🔎":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.text_input('비밀번호를 입력해주세요 : ',key='pass2')
            if password_input == password:
                st.success('접근을 허용합니다')
                if st.button('내용 확인'):
                    st.write("내용입니다.")
                    st.write(data10)
            elif password_input != "" and password_input != password:
                st.warning('비밀번호가 틀렸습니다.')

        elif option == "초기화💣":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.text_input('비밀번호를 입력해주세요 : ',key='pass3')
            if password_input == password:
                st.success('접근을 허용합니다')
                # 데이터 전부 삭제
                st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
                st.write("⚠️신중하게 누르세요!!⚠️")
                if st.button('초기화'):
                    clear_data10()
                    st.warning('초기화 되었습니다')
            elif password_input != "" and password_input != password:
                st.warning('비밀번호가 틀렸습니다.')
    if __name__ == "__main__":
        main()