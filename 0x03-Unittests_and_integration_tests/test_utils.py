#!/usr/bin/env python3
"""tests for utils module
"""
from typing import Mapping, Sequence
from unittest import TestCase
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """class for utils modules test"""

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
