# coding: utf-8
from setuptools import setup


setup(
    name='Pirate',
    version='0.01',
    url='https://github.com/neo1218/pirate/',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='a mvc restful api framework',
    long_description=__doc__,
    packages=['src.cli', 'src.jsonify', 'src.orm',
              'src.pirate', 'src.route'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Werkzeug',
        'gevent',
    ],
    classifiers=[
        'Development Status :: 0 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
