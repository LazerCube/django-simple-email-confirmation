import re
import sys
from os import path
from setuptools import setup, find_packages

# read() and find_version() taken from jezdez's python apps, ex:
# https://github.com/jezdez/django_compressor/blob/develop/setup.py

def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-simple-email-confirmation',
    version=find_version('simple_email_confirmation', '__init__.py'),
    author='Mike Fogel',
    author_email='mike@fogel.ca',
    description="Simple email confirmation for django.",
    long_description=read('README.rst'),
    url='https://github.com/mfogel/django-simple-email-confirmation',
    license='BSD',
    packages = find_packages(),
    install_requires=[
        'django>=1.7.0' if sys.version_info[0] > 2 else 'Django<2.0',
        'six'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Topic :: Utilities',
        "Framework :: Django",
    ]
)
