from ..utils import get_db
from django import template
from bson.objectid import ObjectId

register = template.Library()


def tags(author_id):
    db = get_db()
    tags = db.tags.find({"_id": ObjectId(author_id)})
    return [tag['name'] for tag in tags]


register.filter('tags', tags)
