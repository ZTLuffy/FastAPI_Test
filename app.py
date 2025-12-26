from flask import Flask, request
import csv
import os

app = Flask(__name__)

CSV_FILE = "data.csv"

# 首页
@app.route('/')
def home():
    return "Hello, Render! Submit your numbers to /submit"

# 提交数据接口
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    numbers = data.get("numbers")
    if not numbers:
        return {"status": "error", "message": "No numbers provided"}, 400

    # 写入 CSV
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(numbers)
    
    return {"status": "success"}

# 查看提交数据
@app.route('/view', methods=['GET'])
def view():
    if not os.path.exists(CSV_FILE):
        return "No data yet"
    
    with open(CSV_FILE, 'r') as f:
        lines = f.readlines()
    return "<br>".join([line.strip() for line in lines])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
