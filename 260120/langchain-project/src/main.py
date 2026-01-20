import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# 0. 환경변수 로드 (.env 파일이 있을 경우)
load_dotenv()

# 1. 모델 객체 초기화 (gpt-4o-mini 권장)
# llm = ChatOpenAI(model="gpt-4o-mini")
# Azure OpenAI 설정
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

# 2. 모델 호출 (Invoke)
response = llm.invoke("안녕! 한 줄로 자기소개 해줘")

# 3. 결과 출력 (AIMesssage.content)
print(response.content)