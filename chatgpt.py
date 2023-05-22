import os
import requests
import json

ROLE_SYSTEM = 'system'
ROLE_USER = 'user'
ROLE_ASSISTANT = 'assistant'

messages = []

def add_message(role: str, content: str):
    messages.append({
        'role': role,
        'content': content,
    })

def chat_with_gpt(prompt):
    api_key = os.environ.get('OPENAI_API_KEY')
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    add_message(ROLE_USER, prompt)

    data = {
        'model': "gpt-3.5-turbo-0301",
        'messages': messages,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = json.loads(response.text)

    # chat_reply = response_data['choices'][0]['message']['content']
    chat_reply = response_data['choices'][0]['message']
    return chat_reply


while True:
    # 提示用户输入对话的开头
    user_prompt = input('请输入: ')
    if user_prompt.strip() == '':
        continue

    # 调用 chat_with_gpt 函数与 ChatGPT 进行对话
    gpt_reply = chat_with_gpt(user_prompt)

    # 打印 ChatGPT 的回复
    print("ChatGPT 的回复:", gpt_reply['content'])
    add_message(gpt_reply['role'], gpt_reply['content'])

