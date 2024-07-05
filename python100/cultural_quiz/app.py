from flask import Flask, render_template, request
from questions import questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    user_answers = request.form
    score = 0
    for i, question in enumerate(questions):
        if question['answer'] == user_answers.get(f'question-{i}'):
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
