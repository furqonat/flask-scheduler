from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-Scheduler',
    version='0.0.1',
    description='Flask scheduler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/forqonat/flask-scheduler',
    author='Furqon Romdhani',
    author_email='danixml31@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Web Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='flask scheduler',
    platforms='any',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'test_*']),
    python_requires='>=3.7',
    install_requires=[
        'flask',
        'apscheduler',
    ],
)
