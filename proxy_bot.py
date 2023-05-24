from flask import Flask, request
import requests

app = Flask(__name__)

# 目标地址
target_url = 'https://api.openai.com'

# 代理配置
proxy = {
    'http': 'http://localhost:8888',
    'https': 'http://localhost:8888'
}

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(path):
    # 构建目标 URL
    url = f'{target_url}/{path}'

    # 获取请求方法和请求体
    method = request.method
    body = request.get_data()

    # 获取请求头
    headers = request.headers
    headers['Host'] = target_url.split('//')[1]

    try:
        # 使用 Clash 代理进行转发
        response = requests.request(method, url, headers=headers, data=body, proxies=proxy)

        # 返回代理响应
        return response.content, response.status_code, response.headers.items()

    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
