import os
from flask import Flask, request
import requests

app = Flask(__name__)

# 目标地址
target_url = 'https://api.openai.com'

is_docker = os.getenv('IS_DOCKER', 'No') == 'Yes'
host_ip = os.getenv('HOST_IP', 'localhost')

print(f'host_ip: {host_ip}')

# 代理配置
proxy = {
    'http': f'http://{host_ip}:8888',
    'https': f'http://{host_ip}:8888'
}

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(path):
    # 构建目标 URL
    url = f'{target_url}/{path}'

    # 获取请求方法和请求体
    method = request.method

    headers = {
        'Content-Type': request.headers.get('Content-Type'),
        # 'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
        'Authorization': request.headers.get('Authorization')
    }

    try:
        # 使用 Clash 代理进行转发
        proxy_response = requests.request(method, url, headers=headers, json=request.get_json(), proxies=proxy) # type: ignore
        # proxy_response = requests.request(method, url, headers=headers, data=body, proxies=proxy, stream=True)

        return proxy_response.json()

    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
