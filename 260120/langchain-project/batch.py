import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# 환경변수 로드
load_dotenv()

# Azure OpenAI 설정//모델 객체 초기화
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

response = llm.batch(["자기소개","격언 한개","시 써줘"])

print([res.content for res in response])

