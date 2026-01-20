import os
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import AzureChatOpenAI

# 환경변수 로드
load_dotenv()

# 1) 추출할 데이터의 구조(Schema) 정의
class Place(BaseModel):
    name: str = Field(description="맛집 상호명")
    address: str = Field(description="주소 (도로명)")
    rating: float = Field(description="평점 (0.0~5.0)")

# 2) 파서 초기화
parser = PydanticOutputParser(pydantic_object=Place)

# 3) 포맷 지시사항 생성 (LLM에게 '이 형식으로만 출력'시키는 핵심)
format_instructions = parser.get_format_instructions()

# Azure OpenAI 모델 객체 초기화
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0,
)

# 4) 프롬프트 구성
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "너는 사용자 입력에서 '맛집 정보'를 추출하는 정보추출기야.\n"
     "반드시 아래 출력 포맷 지시사항을 따르고, 다른 말은 절대 하지 마.\n"
     "평점은 0.0~5.0 사이 실수로만.\n\n"
     "{format_instructions}"
    ),
    ("user", "{text}")
])

# 5) 체인 구성 (prompt -> llm -> parser)
chain = prompt | llm | parser

# 6) 테스트 입력
text = "제주에 있는 '오는정김밥' 알아? 주소는 제주특별자치도 서귀포시 동문로 2이고 평점은 4.7 정도로 유명해."

# 7) 실행
result = chain.invoke({
    "text": text,
    "format_instructions": format_instructions
})

print(result)
print(type(result))
print(result.model_dump())
