#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_enharmonic_mapping.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import EnharmonicMapping, ScientificPitchNotation


class TestEnharmonicMapping(unittest.TestCase):
    """
    Test case for EnharmonicMapping class.

    This class contains test methods to ensure that EnharmonicMapping class
    behaves as expected by checking that calling the `enharmonic_mapping()`
    method returns the expected dictionary.

    Attributes
    ----------
    _ENHARMONIC_MAPPING : dict
        A dictionary mapping notes to their enharmonic equivalents.
    enharmonic_mapping : EnharmonicMapping
        An instance of EnharmonicMapping to use in the test methods.

    Examples
    --------
    >>> class TestEnharmonicMapping(unittest.TestCase):
    ...     def setUp(self):
    ...         self.enharmonic_mapping = EnharmonicMapping()
    ...
    ...     def test_enharmonic_mapping(self):
    ...         for key, value in self._ENHARMONIC_MAPPING.items():
    ...             self.assertEqual(
    ...                 self.enharmonic_mapping.enharmonic_mapping(),
    ...                 self._ENHARMONIC_MAPPING,
    ...             )
    ...
    >>> test = TestEnharmonicMapping()
    >>> test.test_enharmonic_mapping()
    """

    _ENHARMONIC_MAPPING = {
        "Ax": "B",
        "A#": "Bb",
        "A": "A",
        "Ab": "G#",
        "A𝄫": "G",
        "Bx": "C#",
        "B#": "C",
        "B": "B",
        "Bb": "A#",
        "B𝄫": "A",
        "Cx": "D",
        "C#": "Db",
        "C": "C",
        "Cb": "B",
        "C𝄫": "Bb",
        "Dx": "E",
        "D#": "Eb",
        "D": "D",
        "Db": "C#",
        "D𝄫": "C",
        "Ex": "F#",
        "E#": "F",
        "E": "E",
        "Eb": "D#",
        "E𝄫": "D",
        "Fx": "G",
        "F#": "Gb",
        "F": "F",
        "Fb": "E",
        "F𝄫": "Eb",
        "Gx": "A",
        "G#": "Ab",
        "G": "G",
        "Gb": "F#",
        "G𝄫": "F",
    }

    def setUp(self):
        """
        Set up the test fixture for EnharmonicMapping class.

        This method initializes an instance of EnharmonicMapping class and
        assigns it to the instance variable `enharmonic_mapping`.

        Parameters
        ----------
        self: object
            The instance of the test class.

        Returns
        -------
        None

        Examples
        --------
        >>> class TestEnharmonicMapping(unittest.TestCase):
        ...     def setUp(self):
        ...         self.enharmonic_mapping = EnharmonicMapping()
        ...
        >>> test = TestEnharmonicMapping()
        >>> test.setUp()
        """
        self.enharmonic_mapping = EnharmonicMapping()

    def test_enharmonic_mapping(self):
        """
        Test that EnharmonicMapping class correctly maps enharmonic
        equivalents.

        This method iterates over each key-value pair in the
        _ENHARMONIC_MAPPING dictionary and asserts that calling the
        `enharmonic_mapping()` method of a new EnharmonicMapping instance
        returns the expected dictionary. This ensures that all the expected
        enharmonic mappings are present in the implementation.

        Parameters
        ----------
        self: object
            The instance of the test class.

        Returns
        -------
        None

        Examples
        --------
        >>> class TestEnharmonicMapping(unittest.TestCase):
        ...     def test_enharmonic_mapping(self):
        ...         for key, value in self._ENHARMONIC_MAPPING.items():
        ...             self.assertEqual(
        ...                 EnharmonicMapping().enharmonic_mapping(),
        ...                 self._ENHARMONIC_MAPPING,
        ...             )
        ...
        >>> test = TestEnharmonicMapping()
        >>> test.test_enharmonic_mapping()
        """
        for key, value in self._ENHARMONIC_MAPPING.items():
            self.assertEqual(
                EnharmonicMapping().enharmonic_mapping(),
                self._ENHARMONIC_MAPPING,
            )
