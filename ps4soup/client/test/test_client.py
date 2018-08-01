import os
import sys
import unittest
import unittest.mock as mock

import responses

import ps4soup.client as client


class ClientTest(unittest.TestCase):
    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(here, 'test.html')
        with open(data_file) as fh:
            self.test_content = fh.read()

        self.expected_list = [
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

    def test_parse_html(self):
        res = client.parse_html(self.test_content)
        assert res == self.expected_list

    @responses.activate
    def test_fetch_list(self):
        responses.add(responses.GET, client.URL, body=self.test_content)

        res = client.fetch_list()
        assert len(responses.calls) == 1
        assert res == self.expected_list

    @responses.activate
    def test_fetch_list_forbidden(self):
        responses.add(responses.GET, client.URL, body='some content', status=403)

        res = client.fetch_list()
        assert len(responses.calls) == 1
        assert res == []

    @mock.patch('ps4soup.client.fetch_list')
    def test_cli(self, mock_list):
        mock_list.return_value = self.expected_list
        expected = '''89 Mega Man X Legacy Collection
87 Sonic Mania Plus
86 The Banner Saga 3
86 Dark Souls Remastered
85 Shantae: Half-Genie Hero - Ultimate Edition
83 Prey: Mooncrash
83 Yoku's Island Express
83 Street Fighter: 30th Anniversary Collection
82 Laser League
82 Defender's Quest: Valley of the Forgotten DX Edition
'''

        # simple mock for stdout
        class Out:
            def __init__(self):
                self.output = []

            def write(self, data):
                self.output.append(data)

            def __str__(self):
                return ''.join(self.output)

        stdout = sys.stdout
        out = Out()
        sys.stdout = out

        client.cli()

        assert str(out) == expected
        # reset in case we run more tests at some point
        sys.stdout = stdout
