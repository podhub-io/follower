from . import mc
import feedparser
import hashlib
import re


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
            self.parse_feed()

    @property
    def lookup(self):
        """
        :return: Dictionary lookup containing `{id: entry}`.
        :rtype: ``dict``
        """
        return {entry.entry_id: entry for entry in self.entries}

    def parse_feed(self):
        url_hash = hashlib.md5(self.url).hexdigest()

        d = mc.get(url_hash)
        if not d:
            d = feedparser.parse(self.url)
            mc.set(url_hash, d)

        feed_obj = d.feed
        for key in self._PARAMS:
            setattr(self, key, feed_obj.feed.pop(key))
        self._custom_keys = feed_obj.feed

        self.entries = frozenset(Entry(**entry) for entry in d.entries)


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

    @property
    def entry_id(self, link_regex=r'\d+$'):
        m = re.search(link_regex, self.id)
        return int(m.group())

    @property
    def audio(self):
        """
        :return href: URL of audio file for podcast.
        :rtype  href: ``str``
        """
        return filter(
            lambda x: x.get('rel') == 'enclosure', self.links).next().get(
                'href')
