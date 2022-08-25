from setuptools import setup

setup(
    name='shell2udp',
    version='1.0',
    description='Executing shell commands via UDP server',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GitHub30/shell2udp',
    project_urls={ 'Bug Tracker': 'https://github.com/GitHub30/shell2udp/issues' },
    author='Tomofumi Inoue',
    author_email='funaox@gmail.com',
    platforms="any",
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="shell2http shell2udp subprocess python",
    entry_points={
        'console_scripts': [
            'shell2udp = shell2udp:serve'
        ]
    }
)

# Publish commands
# https://packaging.python.org/tutorials/packaging-projects/
#pip install --upgrade pip build twine
#python3 -m build
#python3 -m twine upload dist/*
