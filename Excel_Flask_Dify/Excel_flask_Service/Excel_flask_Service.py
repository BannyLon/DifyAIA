import logging
from flask import Flask, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# 确保data目录存在
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


@app.route('/create_excel', methods=['POST'])
def create_excel():
    app.logger.debug('Received POST request to /create_excel')
    try:
        # 获取请求中的数据
        data = request.json
        fields = data.get('fields', [])
        values = data.get('values', {})

        # 输入验证
        if not fields or not isinstance(fields, list) or len(fields) == 0:
            return jsonify({"error": "'fields' must be a non-empty list."}), 400

        if not values or not isinstance(values, dict):
            return jsonify({"error": "'values' must be a dictionary."}), 400

        # 检查所有值列表是否长度一致
        expected_length = None
        for field in fields:
            if field not in values:
                return jsonify({"error": f"Missing values for field '{field}'."}), 400

            current_length = len(values[field])
            if expected_length is None:
                expected_length = current_length
            elif current_length != expected_length:
                return jsonify(
                    {"error": f"All value lists must have the same length. Field '{field}' does not match."}), 400

        app.logger.debug(f'Fields received: {fields}')
        app.logger.debug(f'Values received: {values}')

        # 创建带有数据的DataFrame
        df_data = {field: values.get(field, [None] * expected_length) for field in fields}
        df = pd.DataFrame(df_data)

        # 定义文件名和完整路径，确保文件名唯一
        base_filename = 'output_{}.xlsx'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]  # 使用毫秒级时间戳确保唯一性
        filename = base_filename.format(timestamp)
        file_path = os.path.join(DATA_DIR, filename)

        # 检查文件是否存在，如果存在则添加序号以保证文件名唯一
        counter = 1
        while os.path.exists(file_path):
            filename = base_filename.format(f"{timestamp}_{counter}")
            file_path = os.path.join(DATA_DIR, filename)
            counter += 1

        # 保存到Excel文件
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

        app.logger.debug(f'Excel file saved to: {file_path}')

        # 返回文件路径作为响应
        return jsonify({
            "message": "File created successfully.",
            "file_path": file_path
        }), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)