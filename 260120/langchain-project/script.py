import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser as strOutputParser

# 환경변수 로드
load_dotenv()

# Azure OpenAI 설정//모델 객체 초기화
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)


# 메시지 목록으로 템플릿 정의 (System/User)
pt = ChatPromptTemplate.from_messages([
    ("system", "역할: 한국어 문법 교정기"),
    ("user", "{text}")
])

# 체인 연결 (파이프 연산자 | 사용)
chain = pt | llm | strOutputParser()
result = chain.invoke({"text": "안뇽? 방가방가!"})

print(result)