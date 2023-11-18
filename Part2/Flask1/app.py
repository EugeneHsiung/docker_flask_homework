from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# template from: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK8/code/docker_example_2/app.py