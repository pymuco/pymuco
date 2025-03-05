#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_tonality.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import Tonality, ScientificPitchNotation


class TestTonality(unittest.TestCase):
    """
    A class containing unit tests for the Tonality class.

    Attributes
    ----------
    None

    Methods
    -------
    test_tonality_creation()
        Test method for the Tonality class constructor.

    Examples
    --------
    Create a TestTonality object and run its test methods:

    >>> test = TestTonality()
    >>> test.test_tonality_creation()
    """

    def test_tonality_creation(self):
        """
        Test method for the Tonality class constructor.

        Parameters
        ----------
        self : TestTonality instance
            The current test instance.

        Returns
        -------
        None

        Notes
        -----
        This test method creates a Tonality object with a root note and
        tonality type, and checks that the object is an instance of the
        Tonality class and that its attributes match the expected values.

        Example
        -------
        >>> test = TestTonality()
        >>> test.test_tonality_creation()
        """
        root_note = ScientificPitchNotation("C", 4)
        tonality_type = "major"
        tonality = Tonality(root_note, tonality_type)
        self.assertIsInstance(tonality, Tonality)
        self.assertEqual(tonality._root_note, root_note)
        self.assertEqual(tonality._tonality_type, tonality_type)
