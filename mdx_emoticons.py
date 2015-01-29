"""
Emoticons Extension for Python-Markdown
======================================

Converts Wordpress-style emoticon symbols to images, with the symbols
as their ``alt`` text.

Basic usage:

    >>> import markdown
    >>> text = 'Hello world :)'
    >>> markdown.markdown(text, ['emoticons'])
    '<p>Hello world <img alt=":)" class="smiley" src="/icon_smile.gif" /></p>'

License: [GNU General Public License v3 (GPLv3)](http://www.gnu.org/licenses/gpl-3.0.txt)
Dependencies: [Markdown 2.0+](https://pypi.python.org/pypi/Markdown)

See [Using_Smilies](http://codex.wordpress.org/Using_Smilies) from [Wordpress codex](http://codex.wordpress.org/)
for more details about the available emoticons.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import re

from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


class EmoticonsExtension(Extension):

    def __init__(self, *args, **kwargs):
        self.config = {
            'emoticons': [{
                ':)': 'icon_smile',
                ':-)': 'icon_smile',
                ':smile:': 'icon_smile',

                ':D': 'icon_grin',
                ':-D': 'icon_grin',
                ':grin:': 'icon_grin',

                ':(': 'icon_sad',
                ':-(': 'icon_sad',
                ':sad:': 'icon_sad',

                ':o': 'icon_eek',
                ':O': 'icon_eek',
                ':-o': 'icon_eek',
                ':-O': 'icon_eek',
                ':eek:': 'icon_eek',

                '8o': 'icon_shock',
                '8O': 'icon_shock',
                '8-o': 'icon_shock',
                '8-O': 'icon_shock',
                ':shock:': 'icon_shock',

                ':?': 'icon_confused',
                ':-?': 'icon_confused',
                ':???:': 'icon_confused',
                ':confused:': 'icon_confused',

                '8)': 'icon_cool',
                '8-)': 'icon_cool',
                ':cool:': 'icon_cool',

                ':x': 'icon_mad',
                ':X': 'icon_mad',
                ':-x': 'icon_mad',
                ':-X': 'icon_mad',
                ':mad:': 'icon_mad',

                ':p': 'icon_tongue',
                ':P': 'icon_tongue',
                ':-p': 'icon_tongue',
                ':-P': 'icon_tongue',
                ':razz:': 'icon_tongue',

                ':|': 'icon_neutral',
                ':-|': 'icon_neutral',
                ':neutral:': 'icon_neutral',

                ';)': 'icon_wink',
                ';-)': 'icon_wink',
                ':wink:': 'icon_wink',

                ':lol:': 'icon_lol',
                ':oops:': 'icon_oops',
                ':cry:': 'icon_cry',
                ':evil:': 'icon_evil',
                ':twisted:': 'icon_twisted',
                ':roll:': 'icon_roll',
                ':!:': 'icon_exclaim',
                ':?:': 'icon_question',
                ':idea:': 'icon_idea',
                ':arrow:': 'icon_arrow',
                ':mrgreen:': 'icon_mrgreen',
                }, 'Mapping of smiley\'s string and associated image filename.'],
            'base_url': ['/', 'String to append to the beginning of the smiley URL.'],
            'file_extension': ['gif', 'File extension to append to the end of the smiley URL.'],
            'html_class': ['smiley', 'CSS hook. Leave blank for none.'],
        }

        super(EmoticonsExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        self.md = md

        # Append to the end of inline patterns
        EMOTICONS_RE = '(?P<emoticon>%s)' % '|'.join(
            [re.escape(emoticon) for emoticon in self.getConfig('emoticons').keys()])
        emoticonsPattern = EmoticonsPattern(EMOTICONS_RE, self.getConfigs())
        emoticonsPattern.md = md
        md.inlinePatterns.add('emoticons', emoticonsPattern, '<not_strong')


class EmoticonsPattern(Pattern):
    
    def __init__(self, pattern, config):
        super(EmoticonsPattern, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        emoticon = m.group('emoticon').strip()
        if emoticon:
            emoticons, base_url, file_extension, html_class = self._getMeta()
            img = etree.Element('img')
            img.set('src', '%s%s.%s' % (base_url, emoticons[emoticon], file_extension))
            img.set('alt', emoticon)
            if html_class:
                img.set('class', html_class)
            return img
        return ''

    def _getMeta(self):
        """ Return meta data or config data. """
        emoticons = self.config['emoticons']
        base_url = self.config['base_url']
        file_extension = self.config['file_extension']
        html_class = self.config['html_class']
        if hasattr(self.md, 'Meta'):
            if 'emoticons_base_url' in self.md.Meta:
                base_url = self.md.Meta['emoticons_base_url'][0]
            if 'emoticons_file_extension' in self.md.Meta:
                file_extension = self.md.Meta['emoticons_file_extension'][0]
            if 'emoticons_html_class' in self.md.Meta:
                file_extension = self.md.Meta['emoticons_html_class'][0]
        return emoticons, base_url, file_extension, html_class


def makeExtension(*args, **kwargs):
    return EmoticonsExtension(*args, **kwargs)