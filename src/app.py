from flask import Flask, render_template, request
from mentor_ai import ProgrammingMentor

app = Flask(__name__)
mentor = ProgrammingMentor('../data/content.json', '../data/user_progress.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    concept = request.form.get('concept')
    explanation = mentor.explain_concept(concept)
    return render_template('result.html', explanation=explanation, concept=concept)

@app.route('/exercise', methods=['POST'])
def exercise():
    exercise_id = int(request.form.get('exercise_id'))
    exercise = mentor.get_exercise(exercise_id)
    if exercise:
        username = request.form.get('username')
        mentor.track_progress(username, exercise_id)
        return render_template('result.html', explanation=exercise['description'], concept="Exercise")
    return "Exercise not found", 404

if __name__ == '__main__':
    app.run(debug=True)
