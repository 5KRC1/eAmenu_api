from flask import Blueprint
from waiter.waiter import Waiter

# blueprint
views = Blueprint("views", __name__)

# === views ===
@views.post("/run_service")
def run_service():
    '''
    changes meals if disliked
    '''
    # Get from headers
    username = request.headers["username"]
    password = request.headers["password"]
    disliked_foods = request.headers["disliked_foods"]
    preferred_menu = request.headers["selected_menu"]
    favourite_foods = requests.headers["favourite_foods"]
    default_menu = requests.headers["default_menu"]

    # Run waiter
    waiter = Waiter()
    waiter.username = username
    waiter.password = password
    waiter.login()

    waiter.favourite_foods = favourite_foods
    waiter.disliked_foods = disliked_foods
    waiter.preferred_menu = preferred_menu
    waiter.default_menu = default_menu

    return waiter.service()
