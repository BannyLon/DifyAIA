import requests
import base64  # 添加这一行
import re
import urllib.parse
from flask import Flask, request, jsonify

app = Flask(__name__)

# 设置 GitHub API 的默认超时时间为 10 秒
requests.DEFAULT_REQUESTS_TIMEOUT = 10


# 定义路由和函数
@app.route('/get_readme', methods=['GET'])
def get_readme():
    # 获取并解码 URL 参数
    github_url = request.args.get('url')

    # 如果没有提供 GitHub URL，则返回错误信息
    if not github_url:
        return jsonify({"error": "No GitHub URL provided"}), 400

    # 解码 URL 参数
    github_url = urllib.parse.unquote(github_url)

    # 使用正则表达式提取有效的 GitHub URL
    match = re.search(r'https://github\.com/([^/]+)/([^/]+)', github_url)
    if not match:
        return jsonify({"error": "Invalid GitHub URL format"}), 400

    owner = match.group(1)
    repo = match.group(2)

    # GitHub API endpoint 用于获取 README
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    try:
        response = requests.get(api_url, timeout=requests.DEFAULT_REQUESTS_TIMEOUT)
        response.raise_for_status()  # 对于非2xx状态码抛出异常

        # 检查 GitHub API 的速率限制头
        rate_limit_remaining = int(response.headers.get("X-RateLimit-Remaining"))
        if rate_limit_remaining <= 0:
            return jsonify({"error": "Rate limit exceeded"}), 429

        data = response.json()

        # 检查 content 字段是否存在
        if 'content' in data and data['content']:
            readme_content = base64.b64decode(data['content']).decode('utf-8')
            return jsonify({"readme": readme_content})
        else:
            return jsonify({"error": "README file not found or empty"}), 404

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_structure', methods=['GET'])
def get_structure():
    # 获取并清理 URL 参数
    github_url = request.args.get('url')

    # 如果没有提供 GitHub URL，则返回错误信息
    if not github_url:
        return jsonify({"error": "No GitHub URL provided"}), 400

    # 清理 URL，去除可能的干扰字符
    github_url = github_url.replace(" ", "").replace("'", "")

    # 使用正则表达式提取有效的 GitHub URL
    match = re.search(r'https://github\.com/([^/]+)/([^/]+)', github_url)
    if not match:
        return jsonify({"error": "Invalid GitHub URL format"}), 400

    owner = match.group(1)
    repo = match.group(2)

    # GitHub API 端点用于获取仓库结构
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    try:
        # 发送请求并获取响应
        response = requests.get(api_url, timeout=requests.DEFAULT_REQUESTS_TIMEOUT)
        response.raise_for_status()  # 对于非2xx状态码抛出异常
        data = response.json()

        # 打印响应数据以供调试
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response data: {data}")

        # 返回仓库结构
        return jsonify({"structure": data})

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)