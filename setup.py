#!/usr/bin/env python
from setuptools import setup

setup(
    name='mdx_emoticons',
    version='1.0',
    author='Fabien Batteix',
    author_email='skywodd+pipy@gmail.com',
    description='Python-Markdown extension to support Wordpress-style emoticons.',
    license='GNU General Public License v3 (GPLv3)',
    keywords='markdown extension smiley emoticons',
    url='https://github.com/skywodd/python-markdown-emoticons',
    py_modules=['mdx_emoticons'],
    install_requires=['Markdown>=2.0', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    include_package_data=True,
    zip_safe=False
)