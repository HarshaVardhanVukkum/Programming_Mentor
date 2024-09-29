import json

class UserProgress:
    def __init__(self, progress_file):
        self.progress_file = progress_file
        self.progress = self.load_progress()

    def load_progress(self):
        try:
            with open(self.progress_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"users": {}}

    def get_progress(self, username):
        return self.progress['users'].get(username, {"completed_exercises": []})

    def update_progress(self, username, exercise_id):
        if username not in self.progress['users']:
            self.progress['users'][username] = {"completed_exercises": []}
        if exercise_id not in self.progress['users'][username]["completed_exercises"]:
            self.progress['users'][username]["completed_exercises"].append(exercise_id)
        self.save_progress()

    def save_progress(self):
        with open(self.progress_file, 'w') as file:
            json.dump(self.progress, file, indent=4)
