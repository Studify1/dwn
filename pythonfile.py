from pyscript import display, Element, when

# Update a specific HTML element
Element("output").write("Python is running!")

# React to button clicks
@when("click", "#my-button")
def handle_click(event):
    display("Button clicked!", target="output")