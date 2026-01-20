import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 환경변수 로드
load_dotenv()

# Azure OpenAI 설정//모델 객체 초기화
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_template("{theme} 주제로 감성적인 4행시를 지어줘.")

# 2. LCEL 체인 연결 (파이프 연산자 | 사용)
chain = prompt | llm | StrOutputParser()

# 3. 체인 실행 (Dictionary 형태로 변수 주입)
result = chain.invoke({"theme": "눈오는 날"})
print(result)