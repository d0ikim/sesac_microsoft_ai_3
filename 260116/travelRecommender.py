import asyncio
import os
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ChatAgent, MCPStdioTool

os.environ["AZURE_OPENAI_ENDPOINT"] = "https://sampleai123.cognitiveservices.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "<API_KEY>"
os.environ["AZURE_OPENAI_DEPLOYMENT"] = "o4-mini"

client = AzureOpenAIChatClient(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    deployment_name="gpt-4.1",
    api_version="2024-12-01-preview",
    temperature=0.7,
    max_tokens=2000
)

async def main():
    planner_agent = ChatAgent(
        chat_client=client,
        name="TravelPlanner",
        instructions="여행 계획자입니다. MCP 도구로 계산 후 계획 세우세요. 한국어 응답."
    )
    
    recommend_agent = ChatAgent(
        chat_client=client,
        name="Recommender",
        instructions="여행지 추천 에이전트입니다. 사용자의 취향을 기반으로 추천하고 MCP 도구 사용하세요. 한국어 응답."
    )
    
    mcp_tool = MCPStdioTool(
        name="CalculatorTool",
        command="uvx",
        args=["mcp-server-calculator"],
        description="여행 예산 계산 등 숫자 연산 도구"
    )
    
    planner_agent.tools = [mcp_tool]
    recommend_agent.tools = [mcp_tool]
    
    async with mcp_tool:
        while True:
            user_message = input("사용자 입력 (exit로 종료): ")
            if user_message.lower() == "exit":
                print("채팅 종료.")
                break
            if "추천" in user_message:
                result = await recommend_agent.run(user_message)
                print("추천: ", result.text)
            else:
                result = await planner_agent.run(user_message)
                print("여행 계획: ", result.text)
                
if __name__ == "__main__":
    asyncio.run(main())