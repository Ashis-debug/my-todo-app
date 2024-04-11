# Minimalistic TODO Application

This is a minimalistic TODO application built using Python and Streamlit.

## Introduction

This application allows users to manage their tasks by adding, removing, and marking them as completed. It provides a simple user interface and stores tasks in a text file.

## Features

- Add new tasks
- Mark tasks as completed
- Remove tasks
- Minimalistic user interface
- Stores tasks in a text file

## Getting Started

To get started with the TODO application, follow these steps:

1. Clone the repository to your local machine:

https://github.com/Ashis-debug/my-todo-app.git

2. Install the required dependencies using pip:

pip install -r requirements.txt

3. Run the Streamlit web application:

streamlit run web_app.py


4. Access the application in your web browser by navigating to [http://localhost:8501](http://localhost:8501).

## Usage

- To add a new task, type the task in the text input field and press Enter.
- To mark a task as completed, check the checkbox next to it.
- To remove a task, uncheck the checkbox next to it.
- The application automatically saves changes to the task list.

## File Structure

- `functions.py`: Contains functions for reading and updating the task list.
- `web_app.py`: Contains the Streamlit web application.
- `todos.txt`: Text file for storing the task list.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `requirements.txt`: Lists the required Python packages for the application.
