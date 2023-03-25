#!/usr/bin/env python3
"""tests for utils module
"""
from typing import Mapping, Sequence
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
import requests

from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """class for utils.access_nested_map
     function modules test
    """

    @parameterized.expand([({'a': 1}, ('a',), 1),
                           ({"a": {"b": 2}}, ('a',), {'b': 2}),
                           ({"a": {"b": 2}}, ('a', 'b'), 2)])
    def test_access_nested_map(self, map: Mapping, path: Sequence,
                               expected: Mapping):
        """
        tests the access_nested_map
        funtion
        """
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([({}, ('a')), ({'a': 1}, ('a', 'b'))])
    def test_access_nested_map_exception(self, map, path):
        """
        tests that access_nested_map
        raises KeyError correctly
        """
        with self.assertRaises(KeyError) as ke:
            access_nested_map(map, path)

        self.assertIn(path[-1], str(ke.exception))


class TestGetJson(TestCase):
    """tests for utils.get_json
    function
    """

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get',)
    def test_get_json(self, url, payload, mock_get):
        """tests get_json
        """
        mock_get.return_value = Mock(requests.Response, json=lambda: payload)

        res = get_json(url)

        mock_get.assert_called_once()
        mock_get.assert_called_once_with(url)
        self.assertEqual(res, payload)
