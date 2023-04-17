from inertia import share
from django.conf import settings
from django.contrib.messages import get_messages
import json


def inertia_share(get_response):
    def middleware(request):
        message = None
        for message in get_messages(request):
            message = {
                "message": message.message,
                "level": message.level,
                "tags": message.tags,
                "extra_tags": message.extra_tags,
                "level_tag": message.level_tag,
            }
        share(
            request,
            flash=message,
            user=lambda: request.user,  # evaluated lazily at render time
        )

        return get_response(request)

    return middleware
