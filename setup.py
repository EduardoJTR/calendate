from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A packege to work with dates'
LONG_DESCRIPTION = 'Calendate is a simple python package to work with calendars and dates'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License'
]

setup(
    name="calendate",
    version=VERSION,
    author="Eduardo José Teixeira Rosa",
    author_email="edjo.terra@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords=['python', 'calendar', 'date', 'time', 'year', 'day'],
    packages=find_packages(),
    classifiers=classifiers,
    url='https://github.com/EduardoJTR/calendate'
)
