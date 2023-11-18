"""Main file for API handling."""

import os
from dotenv import load_dotenv
from openai import OpenAI
import api.summary
from flask import Blueprint, request

client = None

prompt = """
Continue the story based on context and current user input. 
Do not deviate from the story. After each interaction, 
add event that advances said story by guiding the user. Max length 150"""

def init():
    """Initialize the API."""
    # load .env file
    load_dotenv()
    # set openai key
    global client
    client = OpenAI(
        api_key=os.getenv("OPENAI_KEY"),
    )
    api.summary.init()

# ===============================================================================
context = []
def get_context():
    # lets the ai remember the last few interactions
    global context
    if len(context) > 5:
        context = context[-5:]
    return context

def add_context(text):
    global context
    context.append(text)
    # remove summary if it gets too long
    if len(context) > 5:
        context = context[-5:]
# ===============================================================================
# make api calls
def get_response(prompt, story, context, text):
    """Get a response from the API."""
    # create a context

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt + "\n\n" + story + "\n\n" + "\n\n".join(context) + "\n\n" + "User: " + text
            },
        ],
        model="gpt-3.5-turbo-1106",
        max_tokens=150
    )
    # get content from response
    content = response.choices[0].message.content
    print(content)
    # add to summary
    context.append(api.summary.summarize(content, 1))
    
# ===============================================================================

api_bp = Blueprint("api", __name__)

@api_bp.route("/api", methods=["POST"])
def api():
    """Handle API requests."""
    data = request.json

    return "Hello world"