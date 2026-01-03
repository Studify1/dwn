from pyscript import Element, when

# Initial welcome message
Element("output").write("Welcome to Studifry01! Start your study journey here.")

# Add a button and handle its click event
@when("click", "#start-button")
def handle_click(event):
    Element("output").write("Let's begin! 🚀")



    from pyscript import Element, when

# Quiz questions (same as before)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Jane Austen"],
        "answer": 1
    }
]

current_question = 0
score = 0

def display_question():
    global current_question
    Element("output").clear()  # Clear previous content
    q = questions[current_question]
    Element("output").write(f"<h3>{q['question']}</h3>")
    
    # Create buttons for each option
    for i, option in enumerate(q["options"]):
        Element("output").write(f"<button class='quiz-btn' id='option-{i}'>{option}</button><br>")
    
    # Attach click events to buttons
    for i in range(len(q["options"])):
        btn = Element(f"option-{i}")
        btn.add_event_listener("click", check_answer)

def check_answer(event):
    global current_question, score
    button_id = event.target.id
    selected_index = int(button_id.split("-")[1])
    
    # Check if answer is correct
    if questions[current_question]["answer"] == selected_index:
        score += 1
    
    current_question += 1
    
    if current_question < len(questions):
        display_question()
    else:
        Element("output").write(f"<h2>Quiz Complete! Your score: {score}/{len(questions)}</h2>")

# Handle "Start Now" button click
@when("click", "#start-button")
def start_quiz(event):
    Element("start-button").element.style.display = "none"  # Hide the button
    display_question()