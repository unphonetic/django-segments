from django.conf import settings


# Highly recommended you set this to a readonly DB connection
SEGMENTS_CONNECTION_NAME = getattr(settings, 'SEGMENTS_CONNECTION_NAME', 'default')
SEGMENTS_REFRESH_ON_SAVE = getattr(settings, 'SEGMENTS_REFRESH_ON_SAVE', True)