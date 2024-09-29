import aiohttp
import json
import os 
from dotenv import load_dotenv

load_dotenv()


GPT_API_TOKEN = os.getenv("GPT_API_TOKEN")


url = "https://gpt.serverspace.kz/v1/chat/completions"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Bearer {GPT_API_TOKEN}"
}

async def get_data(q: str):
    payload = {
            "model": "openchat-3.5-0106",
            "max_tokens": 1024,
            "top_p": 0.1,
            "temperature": 0.6,
            "messages": [
                {
                "role": "user",
                "content": f"{q}"
                }
            ]
    }
                
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=json.dumps(payload), headers=headers) as response:
            return await response.json()