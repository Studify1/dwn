from pyscript import Element, when

# Initial welcome message
Element("output").write("Welcome to Studifry01! Start your study journey here.")

# Add a button and handle its click event
@when("click", "#start-button")
def handle_click(event):
    Element("output").write("Let's begin! 🚀")