import os
import sys
import shutil
from datetime import datetime

def initialize_project():
    """
    Task 1: Project Initialization
    - Checks for the 'StudentFiles' directory.
    - Creates it if it doesn't exist.
    - Displays its absolute path.
    - Handles exceptions and exits gracefully.
    """
    folder_name = "StudentFiles"
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists.")
        
        absolute_path = os.path.abspath(folder_name)
        print(f"Absolute path of '{folder_name}': {absolute_path}")
        return absolute_path
    except Exception as e:
        print(f"Error: Failed to create folder '{folder_name}'. {e}")
        sys.exit(1)

def create_and_write_file(base_path):
    """
    Task 2: File Creation and Writing
    - Generates a filename with the current date.
    - Prompts the user for five student names.
    - Writes the names to the file.
    - Saves the file in the 'StudentFiles' folder.
    - Displays a success message.
    """
    try:
        today_str = datetime.now().strftime("%Y-%m-%d")
        file_name = f"records_{today_str}.txt"
        file_path = os.path.join(base_path, file_name)

        print("\nEnter five student names:")
        with open(file_path, "w") as f:
            for i in range(5):
                name = input(f"Enter name {i+1}: ")
                f.write(name + "\n")

        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nSuccess: File '{file_name}' created at {creation_time}.")
        return file_path
    except Exception as e:
        log_activity(base_path, f"Error creating file: {e}")
        print(f"Error: Could not create or write to the file. {e}")
        return None

def read_and_display_file_info(file_path, base_path):
    """
    Task 3: Reading and File Information
    - Reads and displays the file's contents.
    - Displays the file's size and last modified date.
    """
    if not file_path:
        return
    try:
        print(f"\n--- Contents of {os.path.basename(file_path)} ---")
        with open(file_path, "r") as f:
            print(f.read())
        
        file_size = os.path.getsize(file_path)
        last_modified_timestamp = os.path.getmtime(file_path)
        last_modified_date = datetime.fromtimestamp(last_modified_timestamp)

        print(f"File size: {file_size} bytes")
        print(f"Last modified: {last_modified_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        log_activity(base_path, f"Error reading file info: {e}")
        print(f"Error: Could not read file information. {e}")

def backup_and_archive(file_path, base_path):
    """
    Task 4: Backup and Archiving
    - Creates a backup of the file.
    - Creates an 'Archive' subfolder.
    - Moves the backup file to the 'Archive' folder.
    - Lists files in the 'Archive' folder.
    """
    if not file_path:
        return
    try:
        file_name = os.path.basename(file_path)
        backup_file_name = f"backup_{file_name}"
        backup_file_path = os.path.join(base_path, backup_file_name)
        shutil.copy(file_path, backup_file_path)
        print(f"\nBackup '{backup_file_name}' created.")

        archive_folder = os.path.join(base_path, "Archive")
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)
        
        shutil.move(backup_file_path, archive_folder)
        print(f"Backup moved to '{archive_folder}'.")

        archived_files = os.listdir(archive_folder)
        print(f"Files in Archive folder: {archived_files}")
        log_activity(base_path, f"{file_name} created and archived successfully.")
    except Exception as e:
        log_activity(base_path, f"Error during backup and archive: {e}")
        print(f"Error: Backup and archiving failed. {e}")

def log_activity(base_path, message):
    """
    Task 5: Logging System
    - Creates or appends to 'activity_log.txt'.
    - Logs events with a timestamp.
    """
    log_file_path = os.path.join(base_path, "activity_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Critical Error: Could not write to log file. {e}")

def manage_files(base_path):
    """
    Task 6: Advanced File Operations
    - Asks the user if they want to delete a file.
    - Deletes the specified file.
    - Logs the deletion.
    - Displays remaining files.
    """
    try:
        delete_choice = input("\nDo you want to delete a file from the StudentFiles folder? (Yes/No): ").strip().lower()
        if delete_choice == "yes":
            file_to_delete = input("Enter the name of the file to delete: ").strip()
            file_path_to_delete = os.path.join(base_path, file_to_delete)

            if os.path.exists(file_path_to_delete):
                os.remove(file_path_to_delete)
                print(f"File '{file_to_delete}' deleted successfully.")
                log_activity(base_path, f"File '{file_to_delete}' was deleted by the user.")
            else:
                print("Error: File not found.")
                log_activity(base_path, f"User attempted to delete non-existent file '{file_to_delete}'.")

        remaining_files = os.listdir(base_path)
        print(f"\nRemaining files in StudentFiles: {remaining_files}")
    except Exception as e:
        log_activity(base_path, f"Error during file deletion: {e}")
        print(f"Error: File management operation failed. {e}")

if __name__ == "__main__":
    student_files_path = initialize_project()
    created_file_path = create_and_write_file(student_files_path)
    read_and_display_file_info(created_file_path, student_files_path)
    backup_and_archive(created_file_path, student_files_path)
    manage_files(student_files_path)
    print("\nProgram finished.")
