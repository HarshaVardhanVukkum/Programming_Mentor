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
    
    while True:
        print("\n1. Explain a coding concept")
        print("2. Get a programming exercise")
        print("3. Suggest code improvement")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            concept = input("Enter the concept: ")
            explanation = mentor.explain_concept(concept)
            print(explanation)
            
        elif choice == '2':
            exercise_id = int(input("Enter exercise ID: "))
            exercise = mentor.get_exercise(exercise_id)
            if exercise:
                print(f"Exercise: {exercise['title']}\nDescription: {exercise['description']}\nSolution: {exercise['solution']}")
            else:
                print("Exercise not found.")
                
        elif choice == '3':
            code = input("Enter your code: ")
            suggestion = mentor.suggest_improvement(code)
            print(suggestion)
            
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
