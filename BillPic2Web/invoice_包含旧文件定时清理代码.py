from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import shutil
import time
from threading import Timer
import logging

app = Flask(__name__)

# 设置静态文件目录
STATIC_DIR = 'static'
os.makedirs(STATIC_DIR, exist_ok=True)

# 配置日志
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

# 清理旧文件的函数
def cleanup_old_files(max_age_seconds=3600):  # 默认保留一小时内的文件
    now = time.time()
    for filename in os.listdir(STATIC_DIR):
        path = os.path.join(STATIC_DIR, filename)
        if os.stat(path).st_mtime < now - max_age_seconds:
            try:
                os.remove(path)
            except Exception as e:
                app.logger.error(f"Error removing {path}: {e}")

@app.route('/invoice', methods=['POST'])
def receive_invoice():
    data = request.get_json(silent=True)  # 使用silent=True防止无效请求报错
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # 生成唯一的文件名
    file_name = f"{uuid.uuid4()}.html"
    file_path = os.path.join(STATIC_DIR, file_name)

    try:
        # 生成HTML内容
        app.logger.debug("Generating HTML content...")
        html_content = generate_html(data)

        # 确保generate_html返回了字符串
        if html_content is None or not isinstance(html_content, str):
            return jsonify({"error": "HTML content generation failed"}), 500

        # 写入文件
        app.logger.debug("Writing HTML content to file...")
        with open(file_path, 'w') as file:
            file.write(html_content)

        # 生成完整的预览链接
        base_url = request.host_url.rstrip('/')
        preview_url = f"{base_url}/static/{file_name}"
        app.logger.debug(f"Generated file: {file_name}")

        # 构建完整的响应消息
        response_message = f"文件已保存\n预览链接：{preview_url}"
        return jsonify({"message": response_message}), 200
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500  # 使用标准的500状态码

@app.route('/preview/<path:filename>')
def preview(filename):
    return send_from_directory(STATIC_DIR, filename)

def generate_html(data):
    # 生成HTML内容的逻辑
    title = data.get('title', 'Invoice')
    content = data.get('content', 'No content provided')

    # 添加CSS引用
    css_link = '<link rel="stylesheet" type="text/css" href="styles.css">'

    # 创建HTML模板
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    {css_link}  <!-- 将CSS引用插入到<head>标签内 -->
</head>
<body>
    <h1>{title}</h1>
    <p class="special-p">{content}</p>

    <!-- 动态添加其他内容 -->
    <div>
    """

    # 动态添加其他内容
    for key, value in data.items():
        if key not in ['title', 'content']:
            if isinstance(value, dict):
                # 处理嵌套字典
                html_content += f"<p><strong>{key}:</strong></p>"
                for k, v in value.items():
                    if v:  # 只显示非空值
                        html_content += f"<p>&nbsp;&nbsp;&nbsp;{k}: {v}</p>"
            elif isinstance(value, list):
                # 处理列表
                html_content += f"<p><strong>{key}:</strong></p>"
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        for k, v in item.items():
                            if v:  # 只显示非空值
                                html_content += f"<p>&nbsp;&nbsp;&nbsp;{k}: {v}</p>"
                    else:
                        html_content += f"<p>&nbsp;&nbsp;&nbsp;{index + 1}. {item}</p>"
            else:
                if value:  # 只显示非空值
                    html_content += f"<p><strong>{key}:</strong> {value}</p>"

    # 结束HTML模板
    html_content += """
    </div>
</body>
</html>
"""

    return html_content

# if __name__ == '__main__':
#     # 每隔一段时间清理一次旧文件
#     def periodic_cleanup():
#         cleanup_old_files()
#         Timer(3600, periodic_cleanup).start()  # 每小时执行一次清理
#
#     periodic_cleanup()

    # 启动Flask应用，绑定到所有网络接口
    app.run(host='0.0.0.0', port=5001, debug=False)  # 在生产环境关闭debug模式