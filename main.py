# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()  # 변수 이름 오타 수정

st.title('인공지능 시인')

content = st.text_input('시의 주제를 입력해 주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")  # 변수 이름 오타 수정
        st.write(result)

# st.write('입력', content)







# from langchain.llms import openai
# llms = openai.OpenAI()
# result = llms.predict("내가 좋아하는 동물은?")
# print(result)