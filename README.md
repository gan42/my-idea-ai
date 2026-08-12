\# 💡 Idea to Visualizer (아이디어 시각화 엔진)



> \*\*두서없이 던진 머릿속 생각을 기획서와 컨셉 아트로 구체화해 주는 1인 개발 AI 웹 서비스\*\*



!\[Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)

!\[Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square\&logo=streamlit\&logoColor=white)

!\[Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat-square\&logo=googlegemini\&logoColor=white)



\---



\## 📌 프로젝트 소개 (Overview)



머릿속에 떠오르는 아이디어나 단편적인 잔상들을 글이나 그림으로 구체화하는 데 어려움을 느끼는 사람들을 위한 미니 웹 앱입니다.



사용자가 대충 적은 문장을 \*\*\[기획자 AI]\*\*가 맥락을 파악해 정교한 상세 기획안과 영문 프롬프트로 다듬고, 이를 \*\*\[화가 AI]\*\*에게 전달하여 한 화면에서 \*\*글과 고화질 이미지\*\*로 동시에 시각화해 줍니다.



\---



\## ✨ 핵심 기능 (Features)



\* \*\*두서없는 입력 수용:\*\* 단어 몇 개나 거친 문장도 문맥을 살려 기획안으로 확장

\* \*\*Dual AI 파이프라인:\*\* 

&#x20; \* 📝 \*\*기획자 AI (Gemini):\*\* 아이디어 구체화, 분위기/공간 묘사, 이미지 생성용 영문 프롬프트 추출

&#x20; \* 🎨 \*\*화가 AI (Pollinations / DALL-E / Flux):\*\* 추출된 프롬프트를 바탕으로 시각화 이미지 생성

\* \*\*100% 무료 \& 초간단 실행:\*\* Streamlit 기반으로 가볍고 빠르게 동작



\---



\## 🛠️ 기술 스택 (Tech Stack)



\* \*\*Frontend / Web:\*\* Streamlit

\* \*\*LLM (Text):\*\* Google Gemini 2.5 Flash API

\* \*\*Image Gen:\*\* Pollinations.ai (Free Test API) / DALL-E 3 / Flux

\* \*\*Language:\*\* Python 3.x



\---



\## 🚀 시작하기 (Quick Start)



\### 1. Repository Clone \& 패키지 설치

```bash

git clone \[https://github.com/gan42/my-idea-ai.git](https://github.com/gan42/my-idea-ai.git)

cd my-idea-ai

pip install -r requirements.txt
```
\### 2. 로컬 실행

```bash
streamlit run app.py
```
📝 사용 방법 (Usage)
웹 화면이 열리면 사이드바에 Gemini API Key를 입력합니다.

입력창에 머릿속에 떠오르는 생각(예: "새벽 안개 낀 고즈넉한 현대식 한옥, 지하 주차장" 등)을 편하게 작성합니다.

[아이디어 구체화하기] 버튼을 누르면 기획글과 시각화 이미지가 생성됩니다.

Created with 💡 by a independent developer.
