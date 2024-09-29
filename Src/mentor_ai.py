import json
from database import UserProgress

class ProgrammingMentor:
    def __init__(self, content_file, progress_file):
        self.content = self.load_content(content_file)
        self.user_progress = UserProgress(progress_file)

    def load_content(self, content_file):
        with open(content_file, 'r') as file:
            return json.load(file)

    def explain_concept(self, concept):
        if concept in self.content['concepts']:
            return self.content['concepts'][concept]
        else:
            return "Concept not found."

    def get_exercise(self, exercise_id):
        for exercise in self.content['exercises']:
            if exercise['id'] == exercise_id:
                return exercise
        return None

    def suggest_improvement(self, code):
        return "Consider using better variable names for clarity."

    def track_progress(self, username, exercise_id):
        self.user_progress.update_progress(username, exercise_id)
