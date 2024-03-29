from connexion import NoContent

import app
import random
from app.create_challenge.create_challenge import create_challenge_on_item_add
from app.db.exceptions import DatabaseException
from app.db.models import Item


def get_all(from_user):
    items = app.db.get_user_items(from_user["id"])

    return [item.dump() for item in items]


def create(item):
    try:

        new_item = Item(**item)
        app.db.add_item(new_item)
        item = app.db.get_item(new_item.id)
        response = item.dump()

        if random.randint(0, 10) < 3:
            create_challenge_on_item_add(item)
            response.update({"new_challenge_created": True})

    except DatabaseException:
        return NoContent, 404

    return response
