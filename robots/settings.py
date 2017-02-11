import sys

from django.conf import settings


class Settings(object):
    defaults = {
        #: A list of one or more sitemaps to inform robots about:
        'SITEMAP_URLS': ('ROBOTS_SITEMAP_URLS', []),
        'USE_SITEMAP': ('ROBOTS_USE_SITEMAP', True),
        'USE_HOST': ('ROBOTS_USE_HOST', True),
        'CACHE_TIMEOUT': ('ROBOTS_CACHE_TIMEOUT', None),
        'SITE_BY_REQUEST': ('ROBOTS_SITE_BY_REQUEST', False),
    }

    def __getattr__(self, attribute):
        if attribute in self.defaults:
            return getattr(settings, *self.defaults[attribute])


sys.modules[__name__] = Settings()
