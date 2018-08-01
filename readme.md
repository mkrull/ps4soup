# ps4soup

ps4soup contains a command line tool and an api to fetch scores of the top reviewed PS4 titles from metacritic.

## Install

Clone this repository:

    $ git clone https://github.com/mkrull/ps4soup
    
Use pip to install it (ideally into a separate virtualenv):

    $ cd ps4soup
    $ pip install -r requirements.txt
    
> NOTE: Tested with Python 3.6 only
 
## Tests

To run the tests with detailed report use `pytest`:

    $ pytest --cov ps4soup.api --cov ps4soup.client --cov-report term-missing -vv
    
## Usage

The ps4soup package provides two commands, `ps4soup-cli` and `ps4soup-api`.

The cli will provide a pretty printed list of titles with their scores:

    $ ps4soup-cli
    89 Mega Man X Legacy Collection
    87 Sonic Mania Plus
    86 The Banner Saga 3
    86 Dark Souls Remastered
    85 Shantae: Half-Genie Hero - Ultimate Edition
    83 Prey: Mooncrash
    83 Yoku's Island Express
    83 Street Fighter: 30th Anniversary Collection
    82 Laser League
    82 Defender's Quest: Valley of the Forgotten DX Edition

The API has two endpoint that return JSON. Start it with:

    $ ps4soup-api
