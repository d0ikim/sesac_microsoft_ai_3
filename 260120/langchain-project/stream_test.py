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

print('----- Streaming Start -----')

for chunk in llm.stream("짧은 시를 써줘, 200자 내외로."):
    print(chunk.content, end='', flush=True)

print('\n----- Streaming End -----')