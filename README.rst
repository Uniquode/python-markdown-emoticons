Python Markdown Emoticons Extension
===================================

Summary
-------

The Python-Markdown Emoticons extension converts Wordpress-style emoticon symbols to images, with the symbols
as their ``alt`` attribute.

Syntax
------

See [Using Smilies](http://codex.wordpress.org/Using_Smilies) from [Wordpress codex](http://codex.wordpress.org/)
for more details about the available emoticons.

Note that emoticons are automatically assigned `class="emoticons"` making it
easy to style emoticons differently from other img tags on a page if one so
desires. See below for ways to alter the class.

Usage
-----

See [Extensions](https://pythonhosted.org/Markdown/extensions/index.html) for general
extension usage, specify `emoticons` as the name of the extension.

See the [Library Reference](https://pythonhosted.org/Markdown/reference.html#extensions) for information about
configuring extensions.

The default behavior is to point each img:src link to the document root of the current
domain and use a .gif extension. Additionally, each img tag is assigned to
the html class `emoticons`.
All default smiley images can be found [here](https://github.com/WordPress/WordPress/tree/master/wp-includes/images/smilies)

The following options are provided to change the default behavior:

* **`emoticons`**: Mapping of smiley\'s string and associated image filename.

    Default: See [Using Smilies](http://codex.wordpress.org/Using_Smilies).

* **`base_url`**: String to append to the beginning of the smiley URL.

    Default: `'/'`

* **`file_extension`**: File extension to append to the end of the smiley URL.

    Default: `'gif'`

* **`html_class`**: CSS class. Leave blank for none.

    Default: `'emoticons'`

Examples
--------

For an example, let us suppose that smiley images are in the subdirectory
`/images/` and end with `.png`

    >>> from mdx_emoticons import EmoticonsExtension
    >>> html = markdown.markdown(text,
    ...     extensions=[EmoticonsExtension(base_url='/images/', file_extension='png')]
    ... )

The above would result in the following html for `Smiley are cool :)`.

    <p>Smiley are cool <img alt=":)" class="smiley" src="/images/icon_smile.png" /></p>

Using with Meta-Data extension
------------------------------

The Emoticons extension also supports the [Meta-Data](https://pythonhosted.org/Markdown/extensions/meta_data.html) extension.
Please see the documentation for that extension for specifics. The supported
meta-data keywords are:

* `emoticons_base_url`
* `emoticons_file_extension`
* `emoticons_html_class`

When used, the meta-data will override the settings provided through the
`extension_configs` interface.

This document:

    emoticons_base_url: http://example.com/
	
    emoticons_file_extension:  .png
	
    emoticons_html_class:

    Hello world :)

would result in the following output (notice the blank `emoticons_html_class`):

    <p>Hello world <img alt=":)" src="/images/icon_smile.png" /></p>