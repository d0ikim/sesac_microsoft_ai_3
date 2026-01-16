# Azure OpenAI SDK를 사용한 간단한 챗봇 예제
import os
from openai import AzureOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = "ppt에 있는 키 복사해서 붙여넣기"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://sampleai123.openai.azure.com/"

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2024-12-01-preview"
)

response = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)