
import json
import csv
import sys

def process_student_data():
    """
    Task 7: JSON and CSV Data Processing
    - Reads student data from a JSON file.
    - Computes each student's average score.
    - Writes the results to a CSV file, sorted by average score.
    - Handles file not found errors gracefully.
    """
    json_file = 'students.json'
    csv_file = 'report.csv'

    try:
        with open(json_file, 'r') as f:
            students_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{json_file}'.")
        sys.exit(1)

    report_data = []
    for student in students_data:
        try:
            avg_score = round(sum(student['scores']) / len(student['scores']), 2)
            report_data.append({
                'id': student['id'],
                'name': student['name'],
                'average': avg_score
            })
        except (ZeroDivisionError, TypeError) as e:
            print(f"Warning: Could not compute average for student {student.get('id', '(unknown)')}. Skipping. Error: {e}")

    # Sort the data by average score in descending order
    report_data.sort(key=lambda x: x['average'], reverse=True)

    try:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'average'])
            writer.writeheader()
            writer.writerows(report_data)
        print(f"Successfully created '{csv_file}' with student average scores.")
    except Exception as e:
        print(f"Error: Could not write to the CSV file '{csv_file}'. {e}")

if __name__ == "__main__":
    process_student_data()
