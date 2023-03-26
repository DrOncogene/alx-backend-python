#!/usr/bin/env python3
"""tests for GithubOrgClient
"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """tests for GithubOrgClient
    methods
    """

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        tests the org method
        """
        client = GithubOrgClient(org_name)
        res = client.org()

        url = client.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(url)
