from django.core.urlresolvers import get_resolver

def get_views(urlconf=None):
    return [
        "%s.%s" % (view.__module__, view.__name__)
        for view in get_resolver(urlconf).reverse_dict.keys() if callable(view)
    ]

def get_urls(urlconf=None):
    return [
        (
            pattern[1],
            "%s.%s" % (view.__module__, view.__name__)
        )
        for view, pattern in get_resolver(urlconf).reverse_dict.items()
        if callable(view)
    ]
