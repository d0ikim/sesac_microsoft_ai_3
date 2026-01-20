import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0.7,
)


# ---------------------------
# 1) 단계별 체인 정의
# ---------------------------

# (1) Title: 입력 dict에서 topic 사용 -> "title" 문자열 1개만 반환(5개가 아니라 1개로 단순화)
title_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 한국어 블로그 제목을 잘 짓는 편집자다. 제목 1개만 출력해라."),
    ("user", "주제: {topic}\n클릭을 유도하지만 과장 없는 블로그 제목 1개만 추천해줘.")
])
title_chain = title_prompt | llm | StrOutputParser()  # 결과: str

# (2) Outline: topic + title 받아서 목차 생성(마크다운 목록 형태로)
outline_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 한국어 블로그 구조 설계자다. 목차만 출력해라(마크다운 불릿)."),
    ("user",
     "주제: {topic}\n"
     "제목: {title}\n"
     "서론-본론-결론 구조로 목차를 만들어줘. (H2/H3와 불릿 혼합 가능)")
])
outline_chain = outline_prompt | llm | StrOutputParser()  # 결과: str

# (3) Body: topic + title + outline 받아 최종 본문 마크다운
body_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "너는 한국어 블로그 전문가 이다.\n"
     "출력은 마크다운 문서만.\n"
     "서론-본론-결론 구조를 따르고, 소제목을 사용해라."),
    ("user",
     "주제: {topic}\n"
     "제목: {title}\n"
     "목차:\n{outline}\n\n"
     "요구사항:\n"
     "- 1200~1800자 내외\n"
     "- 독자가 따라할 수 있게 예시 포함\n"
     "- 과장/허위 금지\n")
])
body_chain = body_prompt | llm  # 결과: AIMessage (response.content로 출력)

# ---------------------------
# 2) 파이프라인 구성 (assign로 누적)
# ---------------------------
blog_chain = (
    # 입력을 dict로 표준화:
    # - invoke({"topic": ...})도 되고
    # - invoke("...")도 되게 하려면 아래처럼 key mapping 사용
    {"topic": RunnablePassthrough()}
    | RunnablePassthrough.assign(title=title_chain)
    | RunnablePassthrough.assign(outline=outline_chain)
    | body_chain
)

# ---------------------------
# 3) 실행
# ---------------------------
response = blog_chain.invoke("LCEL 완벽 가이드")
print(response.content)
