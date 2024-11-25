# personaldiary.github.io

Description:
The Personal Diary Application is a simple and intuitive tool for keeping track of personal diary entries. It allows users to:

Add new diary entries: Users can input a title and content for their diary entries.
View diary entries: Users can view the full content of any selected diary entry.
Delete diary entries: Users can remove unwanted or outdated entries from the diary.
This application uses the Tkinter library for a graphical user interface (GUI) and SQLite for storing the diary entries in a local database. The application features a modern and clean UI with buttons for adding, viewing, and deleting entries, and a listbox to display the diary titles. The database ensures that diary entries are stored persistently.

Instructions:
Install Python:

Make sure that Python 3.x is installed on your computer. You can download it from the official Python website.
Download the Code:

Copy the provided Python code into a text editor or IDE, such as VS Code, PyCharm, or IDLE, and save it as personal_diary.py.
Running the Application:

Open a terminal (Command Prompt on Windows or Terminal on macOS/Linux).
Navigate to the directory where you saved personal_diary.py using the cd command.
Type the following command and press Enter to run the application:
python personal_diary.py
Using the Application:

Add Entry: To create a new diary entry, click the "Add Entry" button. You will be prompted to enter a title and content for your entry.
View Entry: To view a diary entry, select an entry from the list on the left and click the "View Entry" button. This will open a popup displaying the full content of the entry.
Delete Entry: To delete a diary entry, select it from the list and click the "Delete Entry" button. This will remove the entry from both the list and the database.
Exiting the Application:

Close the window by clicking the "X" button in the top-right corner, and the application will shut down. All changes to the diary (added/deleted entries) will be saved in the SQLite database automatically.


Requirements List:
Python Version:

Python 3.x (Python 3.6 or higher recommended).
Required Libraries:

Tkinter: This is the standard Python library used for creating the GUI. It comes bundled with Python, so you don’t need to install it separately.
SQLite3: SQLite3 is also included in Python by default, and it's used for database management to store diary entries persistently.
System Requirements:

Windows, macOS, or Linux: The application is cross-platform and works on all major operating systems.
Software:

A text editor or IDE to edit the Python code, such as:
VS Code, PyCharm, Sublime Text, or IDLE (the default editor that comes with Python).
Optional (for advanced features):

If you plan to add advanced features like rich text formatting, icons on buttons, or exporting to PDF, you may need additional libraries such as:
Pillow for handling images/icons.
ReportLab for generating PDFs.
