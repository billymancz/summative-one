import random


def equation_generator():
    """
    Generates an equation in the form of a*x = b.

    Returns:
        - str: equation as a string.
        - int: correct solution for x.
    """
    # Choose random integers for a and x
    a = random.randint(1, 10)
    x = random.randint(1, 10) 
    b = a * x 

    # Create equation string with x as unknown
    equation_str = f"{a}*x = {b}"
    return equation_str, x


def question_asker(equation, correct_answer):
    """
    Display the equation, prompt user for an answer, and
    return whether the answer is correct.

    Args:
        equation (str): Equation to display.
        correct_answer (int): Correct answer for the equation.

    Returns:
        bool: True if equation answered correctly, False otherwise.
    """
    
    print(equation)

    # Prompt user for answer
    try:
        user_input = input("What is the value of x? ")
        user_answer = int(user_input)
    except ValueError:
        # In case user doesn't enter integer
        print("Invalid input. Please enter an integer.\n")
        return False

    # Check if answer is correct
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")
        return False


def main():
    """
    Main function to run equation quiz.
    """
    score = 0
    num_questions = 3

    # Loop through equations
    for number in range(num_questions):
        equation, solution = equation_generator()
        if question_asker(equation, solution):
            score += 1

    print(f"Total score: {score}/{num_questions}")


if __name__ == "__main__":
    main()