import json
import unittest
import unittest.mock as mock

import pytest

import ps4soup.api as api

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    return api.app.test_client()


class APITest(unittest.TestCase):
    def setUp(self):
        self.games = [
            {'score': 89, 'title': 'Mega Man X Legacy Collection'},
            {'score': 87, 'title': 'Sonic Mania Plus'},
            {'score': 86, 'title': 'The Banner Saga 3'},
            {'score': 86, 'title': 'Dark Souls Remastered'},
            {'score': 85, 'title': 'Shantae: Half-Genie Hero - Ultimate Edition'},
            {'score': 83, 'title': 'Prey: Mooncrash'},
            {'score': 83, 'title': "Yoku's Island Express"},
            {'score': 83, 'title': 'Street Fighter: 30th Anniversary Collection'},
            {'score': 82, 'title': 'Laser League'},
            {'score': 82, 'title': "Defender's Quest: Valley of the Forgotten DX Edition"}]
        self.expected_games = b'''[{"title": "Mega Man X Legacy Collection", "score": 89}, {"title": "Sonic Mania Plus", "score": 87}, {"title": "The Banner Saga 3", "score": 86}, {"title": "Dark Souls Remastered", "score": 86}, {"title": "Shantae: Half-Genie Hero - Ultimate Edition", "score": 85}, {"title": "Prey: Mooncrash", "score": 83}, {"title": "Yoku's Island Express", "score": 83}, {"title": "Street Fighter: 30th Anniversary Collection", "score": 83}, {"title": "Laser League", "score": 82}, {"title": "Defender's Quest: Valley of the Forgotten DX Edition", "score": 82}]'''

    @mock.patch('ps4soup.api.fetch_list')
    def test_games_endpoint(self, mock_fetch):
        mock_fetch.return_value = self.games

        res = client().get('/games')
        assert res.status_code == 200
        # Load back to dict to avoid problems with key order
        assert json.loads(res.data) == self.games

    @mock.patch('ps4soup.api.fetch_list')
    def test_show_game_endpoint(self, mock_fetch):
        mock_fetch.return_value = self.games

        res = client().get('/games/Mega%20Man%20X%20Legacy%20Collection')
        assert res.status_code == 200
        # Load back to dict to avoid problems with key order
        assert json.loads(res.data) == self.games[0]

    @mock.patch('ps4soup.api.fetch_list')
    def test_show_game_endpoint_not_found(self, mock_fetch):
        mock_fetch.return_value = self.games

        res = client().get('/games/not-in-the-list')
        assert res.status_code == 404
        # Load back to dict to avoid problems with key order
        assert res.data == b'{}'
