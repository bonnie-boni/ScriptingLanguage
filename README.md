# Python File Management and Data Processing Utility

This project is a Python-based utility designed to automate file management and data processing tasks. It includes features for creating, backing up, organizing, logging, and analyzing data files.

## Purpose

The main purpose of this utility is to demonstrate proficiency with Python's built-in modules for file handling (`os`, `shutil`), system interaction (`sys`), date and time management (`datetime`), and data serialization (`json`, `csv`). The project is divided into two main scripts:

1.  `file_manager.py`: A tool for managing student records files.
2.  `students_report.py`: A script for processing student data and generating a CSV report.

## Features

### file_manager.py

- **Project Initialization**: Automatically creates a `StudentFiles` directory if it doesn't exist.
- **File Creation**: Generates a text file with a name based on the current date (e.g., `records_2025-10-31.txt`) and populates it with user-provided student names.
- **File Information**: Displays file metadata, including contents, size, and last modified date.
- **Backup and Archive**: Creates a backup of the records file and moves it to an `Archive` subfolder.
- **Logging**: Records all major events (creation, archiving, deletion, errors) in `activity_log.txt` with timestamps.
- **File Deletion**: Allows the user to delete files from the `StudentFiles` directory.

### students_report.py

- **JSON Parsing**: Reads student data from a `students.json` file.
- **Data Processing**: Calculates the average score for each student.
- **CSV Generation**: Writes the processed data (ID, name, average score) to a `report.csv` file, sorted in descending order of the average score.
- **Error Handling**: Gracefully handles cases where the `students.json` file is missing.

## How to Run

### Prerequisites

- Python 3.x

### Running the Scripts

1.  **File Manager**:

    Open your terminal and run the following command:

    ```bash
    python3 file_manager.py
    ```

    The script will guide you through the process, prompting for student names and other inputs as needed.

2.  **Student Report Generator**:

    Make sure you have the `students.json` file in the same directory. Then, run the script:

    ```bash
    python3 students_report.py
    ```

    This will generate a `report.csv` file in the same directory.

## Included Files

- `file_manager.py`: The main file management script.
- `students_report.py`: The data processing and report generation script.
- `students.json`: Sample JSON data for `students_report.py`.
- `README.md`: This file.
