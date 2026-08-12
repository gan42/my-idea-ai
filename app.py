import streamlit as st
from google import genai
import urllib.parse

st.set_page_config(page_title='아이디어 시각화 엔진',layout='wide')
st.title('아이디어 구체화 & 시각화 엔진')

api_key = st.sidebar.text_input('Gemini API Key를 입력하세요:',type='password')
user_input = st.text_area('머릿속에 떠오르는 생각을 자유롭게 적어보세요:',height=120)

if st.button('아이디어 구체화하기'):
    if not api_key:
        st.error('Gemini API Key를 입력해주세요!')
    elif user_input:
        col1,col2 = st.columns(2)
        with st.spinner('기획자 AI가 아이디어를 정밀하게 다듬는 중...'):
            client = genai.Client(api_key=api_key)
            system_prompt = """
            너는 창작 디렉터다. 사용자의 추상적인 아이디어를 바탕으로 다음 2가지를 출력하라.

            1. [기획서]: 사용자의 의도를 살려 공간/분위기/세부 요소를 한글로 풍부하게 확장한 기획글.
            2. [PROMPT]: 이미지 생성 AI(Flux/Midjourney)가 최상의 화질로 그려낼 수 있도록 빛,질감,구도,카메라 렌즈까지 포함한 상세한 영문 프롬프트 1문장.
               (단, 영문 프롬프트 시작 지점에 반드시 '[PROMPT]' 태그를 붙일 것)
            """

            response = client.models.generate_content(model='gemini-2.5-flash',contents=f'{system_prompt}\n\n사용자 아이디어: {user_input}')

            text_result = response.text

            prompt_tag = '[PROMPT]'
            if prompt_tag in text_result:
                plan_text,img_prompt = text_result.split(prompt_tag,1)
                img_prompt = img_prompt.strip()
            else:
                plan_text = text_result
                img_prompt = 'Modern high quality realistic architecture render'

        with col1:
            st.subheader('상세 기획안')
            st.write(plan_text)

        with col2:
            st.subheader('시각화 컨셉 아트')
            with st.spinner('화가 AI가 그림을 그리는 중...'):
                encoded_prompt = urllib.parse.quote(img_prompt)
                image_url = f'https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true'

                st.image(image_url,caption=f'생성된 프롬프트: {img_prompt}')

    else:
        st.warning('아이디어를 입력해 주세요!')