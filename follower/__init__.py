import feedparser


class Feed(object):

    _PARAMS = frozenset([
        'author', 'author_detail', 'authors', 'generator', 'generator_detail',
        'image', 'itunes_explicit', 'language', 'link', 'links', 'publisher',
        'publisher_detail', 'rawvoice_frequency', 'rawvoice_rating', 'rights',
        'rights_detail', 'subtitle', 'subtitle_detail', 'summary',
        'summary_detail', 'sy_updatefrequency', 'sy_updateperiod', 'tags',
        'title', 'title_detail', 'updated', 'updated_parsed'
    ])

    def __init__(self, url=None, **kwargs):
        self.url = url
        if url is not None:
            d = feedparser.parse(url)
            feed = d.feed
            self._entries = d.entries
            for key in self._PARAMS:
                setattr(self, key, feed_obj.feed.pop(key))
                setattr(self, key, kwargs.get(key))
            self._custom_keys = feed_obj.feed

    @property
    def entries(self):
        """
        Iterates through self._entries and yields an Entry object for each
        entry.

        :return: Generator of all the Entry objects in this Feed object.
        :rtype:  ``generator``
        """
        for entry in self._entries:
            yield Entry(**entry)


class Entry(object):

    _PARAMS = frozenset([
        'author', 'author_detail', 'authors', 'comments', 'content',
        'guidislink', 'id', 'itunes_duration', 'itunes_explicit', 'link',
        'links', 'published', 'published_parsed', 'slash_comments', 'subtitle',
        'subtitle_detail', 'summary', 'summary_detail', 'tags', 'title',
        'title_detail', 'wfw_commentrss'
    ])

    def __init__(self, **kwargs):
        for key in self._PARAMS:
            setattr(self, key, kwargs.get(key))
