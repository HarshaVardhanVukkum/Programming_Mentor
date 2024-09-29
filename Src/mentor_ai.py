import json

class ProgrammingMentor:
    def __init__(self, content_file):
        self.content = self.load_content(content_file)

    def load_content(self, content_file):
        with open(content_file, 'r') as file:
            return json.load(file)

    def explain_concept(self, concept):
        """Provide an explanation for a coding concept."""
        if concept in self.content['concepts']:
            return self.content['concepts'][concept]
        else:
            return "Concept not found."

    def get_exercise(self, exercise_id):
        """Retrieve a programming exercise by ID."""
        for exercise in self.content['exercises']:
            if exercise['id'] == exercise_id:
                return exercise
        return None

    def suggest_improvement(self, code):
        """Suggest improvements for a given piece of code."""
        return "Consider using better variable names for clarity."

# Example usage
if __name__ == "__main__":
    mentor = ProgrammingMentor('data/content.json')
    print(mentor.explain_concept('print'))
    exercise = mentor.get_exercise(1)
    print(f"Exercise: {exercise['title']}\nDescription: {exercise['description']}")
    print(f"Solution: {exercise['solution']}")
    print(mentor.suggest_improvement("a = 5\nb = 10\nprint(a+b)"))
