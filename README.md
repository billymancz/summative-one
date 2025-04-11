# Equation Quiz: task_1.py

This project is a quiz that generates equations of the form **a*x = b**. Users are prompted to solve for **x**, and the program checks their answers while tracking a score over multiple questions. 
---

## Table of Contents

- [Overview](#overview)
- [User Guide](#user-guide)
  - [Installation](#installation)
  - [Running the Program](#running-the-program)
  - [Interacting with the Quiz](#interacting-with-the-quiz)
  - [Troubleshooting](#troubleshooting)
- [Technical Documentation](#technical-documentation)
  - [Code Structure](#code-structure)
  - [Function Details](#function-details)
- [Future Enhancements](#future-enhancements)

---

## Overview

The Equation Quiz in **task_1.py** is designed to test your algebra skills by generating equations where the variable **x** is unknown. Each time the program runs, it creates a new equation using randomly generated numbers, ensuring a unique experience with every session. After answering a set of questions, the quiz displays your total score, helping you assess your understanding of the material.

---

## User Guide

### Installation

Follow these steps if you are new to Python or programming:

1. **Install Python:**
   - Download the latest version of Python from the [official website](https://www.python.org/downloads/).
   - Follow the platform-specific installation instructions.

2. **Save the Program:**
   - Copy the code into a file named `task_1.py`.
   - Use a text editor (such as VSCode) and ensure the file is saved with a `.py` extension.

### Running the Program

1. **Open Your Command Line Interface:**
   - Windows users: Open Command Prompt or PowerShell.
   - macOS/Linux users: Open Terminal.

2. **Navigate to the Program Directory:**
   - Use the `cd` command to change to the directory where `task_1.py` is stored.
   - For example:
     ```
     cd user/documents/project/task_1.py
     ```

3. **Execute the Program:**
   - Run the program by typing:
     ```
     python task_1.py
     ```
   - If your system uses `python3` for Python 3.x, use:
     ```
     python3 task_1.py
     ```

### Interacting with the Quiz

- **Answering Equations:**
  - When the program starts, it displays an equation (e.g., `4*x = 20`).
  - You will see a prompt: `What is the value of x?`
  - Type your answer and press Enter.

- **Feedback:**
  - The program checks your answer and immediately informs you if it is correct.
  - If the answer is wrong, the program displays the correct answer.

- **Scoring:**
  - The quiz contains three questions by default.
  - Your score is updated with each correct answer.
  - After the final question, the total score is displayed in the format: `Total score: X/3`.

### Troubleshooting

If you run into issues while using the quiz, consider these tips:

- **Python Not Found:**
  - Ensure that Python is installed correctly and added to your system's PATH.
  - Verify by running `python --version` or `python3 --version` in your terminal.

- **File Location Issues:**
  - Confirm that `task_1.py` is saved in the correct directory.
  - List the directory contents using `dir` (Windows) or `ls` (macOS/Linux).

- **Invalid Input Errors:**
  - The program expects an integer input. Non-integer values will trigger an error message and count as an incorrect answer.
  - Make sure to enter a whole number when prompted.

- **General Advice:**
  - If the program behaves unexpectedly, review the code for any typing errors.
  - Restart your terminal session and try running the program again.

---

## Technical Documentation

### Code Structure

The **task_1.py** program is organized into several functions to separate the quiz logic:

- **`equation_generator()`**
  - **Purpose:** Randomly creates an equation in the format **a*x = b**.
  - **Process:** Generates random values for the coefficient **a** and the solution **x**, calculates **b**, and returns both the equation string and the correct value of **x**.

- **`question_asker(equation, correct_answer)`**
  - **Purpose:** Displays the equation, gathers user input, and verifies the answer.
  - **Process:** Prompts the user, validates that the input is an integer, compares it to the correct answer, and prints appropriate feedback.

- **`main()`**
  - **Purpose:** Controls the overall flow of the quiz.
  - **Process:** Iterates through a fixed number of questions (three by default), calls `equation_generator()` for each question, uses `question_asker()` to process user responses, and finally prints the user’s score.

### Function Details

- **Random Number Generation:**
  - The program uses Python’s `random` module to ensure each equation is different, enhancing the quiz's replay value.

- **User Input and Validation:**
  - The `input()` function is used to collect user responses. The program converts this input into an integer and handles errors if the input is not valid.

- **Score Management:**
  - A score counter keeps track of correct answers. After all questions are answered, the final score is output, making it easy to assess performance.

- **Modular Design:**
  - The separation of functionalities into distinct functions allows for easy maintenance and scalability. For instance, more complex equations or additional quiz features could be integrated with minimal changes to the existing structure.

---

## Future Enhancements

The current design of **task_1.py** is simple, but it leaves room for future improvements:

- **Logic Handling:**
  - Add logic to ensure that the same equation is not displayed to the user multiple times in the same round. 
  
- **Difficulty Levels:**
  - Adding adjustable difficulty settings by varying the range of numbers or the complexity of equations.
  
- **Graphical User Interface (GUI):**
  - Implementing a GUI would make the quiz more visually appealing and accessible.
  
- **Customization Options:**
  - Allow users to choose the number of questions, set specific difficulty levels, or select the types of equations they prefer to solve.

- **Enhanced Learning Feedback:**
  - Future updates could offer detailed explanations for incorrect answers, providing insights into the mathematical principles involved.