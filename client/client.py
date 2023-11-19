from flask import Blueprint, render_template

# register a client blueprint
client_bp = Blueprint("client", __name__)

client_bp.static_folder = "static"
client_bp.template_folder = "templates"

@client_bp.route("/")
def index():
    """Return the index page."""
    return render_template("index.html")

@client_bp.route("/script.js")
def script():
    """Return the script.js file."""
    return client_bp.send_static_file("script.js")

@client_bp.route("/styles.css")
def style():
    """Return the style.css file."""
    return client_bp.send_static_file("styles.css")

@client_bp.route("/main.png")
def main():
    """Return the background.png file."""
    return client_bp.send_static_file("img/main.png")

@client_bp.route("/booklogo.png")
def booklogo():
    """Return the background.png file."""
    return client_bp.send_static_file("img/booklogo.png")

@client_bp.route("/adventure.jpeg")
def adventure():
    """Return the background.png file."""
    return client_bp.send_static_file("img/adventure.jpeg")

@client_bp.route("/fantasy.jpeg")
def fantasy():
    """Return the background.png file."""
    return client_bp.send_static_file("img/fantasy.jpeg")

@client_bp.route("/horror.jpeg")
def horror():
    """Return the background.png file."""
    return client_bp.send_static_file("img/horror.jpeg")

@client_bp.route("/mystery.jpeg")
def mystery():
    """Return the background.png file."""
    return client_bp.send_static_file("img/mystery.jpeg")

@client_bp.route("/romance.jpeg")
def romance():
    """Return the background.png file."""
    return client_bp.send_static_file("img/romance.jpeg")

@client_bp.route("/sci-fi.jpeg")
def scifi():
    """Return the background.png file."""
    return client_bp.send_static_file("img/sci-fi.jpeg")

@client_bp.route("/chat", methods=["POST", "GET"])
def char():
    """Return the chat page."""
    return render_template("chat.html")

@client_bp.route("/chat_script.js")
def chat_script():
    """Return the chat_script.js file."""
    return client_bp.send_static_file("chat_script.js")

@client_bp.route("/chat_styles.css")
def chat_style():
    """Return the chat_styles.css file."""
    return client_bp.send_static_file("chat_styles.css")