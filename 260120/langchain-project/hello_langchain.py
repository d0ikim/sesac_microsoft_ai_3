import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# 환경변수 로드
load_dotenv()

# Azure OpenAI 설정
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

# 모델 호출
response = llm.invoke("안녕하세요, 자기소개 해주세요")

# 결과 출력
print(response)