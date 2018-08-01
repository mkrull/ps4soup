from setuptools import setup

dependencies = [
    'beautifulsoup4>=4',
    'Flask>=1',
    'html5lib>=1',
    'requests>=2'
]

test_dependencies = [
    'pytest',
    'pytest-cov',
    'responses'
]

setup(
    name='ps4soup',
    version='0.0.1',
    author='Matthias Krull',
    author_email='m.krull@uninets.eu',
    description=(
        'List the top reviewed PS4 games'
    ),
    install_requires=dependencies,
    extras_require={'test': test_dependencies},
    packages=['ps4soup.client', 'ps4soup.api'],
    entry_points={
        'console_scripts':[
            'ps4soup-api = ps4soup.api:run',
            'ps4soup-cli = ps4soup.client:cli',
        ]
    },
    url='https://github.com/mkrull/ps4soup'
)
