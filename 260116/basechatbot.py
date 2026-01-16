# 나중에 최종프로젝트든 azure ai foundry 기반으로 할 때 참고용으로 쓸 코드
import asyncio
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentClient(
            azure_endpoint="https://ExampleAIFoundry.services.ai.azure.com/api/projects/AIFoundryProject",
            model_deployment_name="gpt-4.1",
            async_credential=credential,
            agent_name="HelperAgent"
        ).create_agent(
            instructions="You are a helpful assistant."
        ) as agent,
    ):
        while True:
            user_message = input("채팅 (exit로 종료): ")
            if user_message.lower() == "exit":
                print("채팅 종료.")
                break
            result = await agent.run(user_message)
            print("에이전트 응답: ", result.text)
            
if __name__ == "__main__":
    asyncio.run(main())