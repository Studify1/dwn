from pyscript import Element, when

@when("click", ".hamburger")
def toggle_menu(event):
    nav_links = Element("nav-links")
    nav_links.element.classList.toggle("active")

@when("click", "body")
def close_menu(event):
    nav_links = Element("nav-links")
    hamburger = Element("hamburger")
    if not nav_links.element.contains(event.target) and not hamburger.element.contains(event.target):
        nav_links.element.classList.remove("active")