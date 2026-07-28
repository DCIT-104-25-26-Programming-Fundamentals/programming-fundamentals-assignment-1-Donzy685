# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
# (comments unchanged from scaffold)
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def add_student(students):
    """Prompt for name, ID, and scores, then add the student record."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)

    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimal places."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def display_all_students(students):
    """Print a formatted table of all students with their average scores."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(int(s)) if s == int(s) else str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average}")

    print("-" * 50)


def find_student_average(students):
    """Ask for a student ID, find them, and display their average score."""
    search_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == search_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: No student found with that ID.")


def print_menu():
    """Display the main menu."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")

        print()


if __name__ == "__main__":
    main()