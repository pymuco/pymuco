#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_circle_of_fifths.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import CircleOfFifths, ScientificPitchNotation


class TestCircleOfFifths(unittest.TestCase):
    """
    The TestCircleOfFifths class is a unit test that verifies the functionality
    of the CircleOfFifths class.

    The CircleOfFifths class is expected to have two methods, circle_of_fifths
    and relative_minors, which return pre-defined lists of musical keys. The
    test_circle_of_fifths method ensures that the circle_of_fifths method
    returns the expected list of keys, and the test_relative_minors method
    ensures that the relative_minors method returns the expected list of
    relative minor keys. If either method returns a list that is not equal to
    the pre-defined list, the corresponding test will fail.

    Methods
    -------
    test_circle_of_fifths(self):
        Unit test to verify the functionality of the 'circle_of_fifths' method.

    test_relative_minors(self):
        Unit test to verify the functionality of the 'relative_minors' method.
    """

    _CIRCLE_OF_FIFTHS = [
        "C",
        "G",
        "D",
        "A",
        "E",
        "B",
        ["F#", "Gb"],
        "Db",
        "Ab",
        "Eb",
        "Bb",
        "F",
    ]
    _RELATIVE_MINORS = [
        "A",
        "E",
        "B",
        "F#",
        "C#",
        "G#",
        ["D#", "Eb"],
        "Bb",
        "F",
        "C",
        "G",
        "D",
    ]

    def setUp(self):
        """
        Sets up the CircleOfFifths object for use in the test suite.

        This method initializes a CircleOfFifths object and assigns it to the
        instance variable '_circle_of_fifths'. This object can be used in the
        test cases to verify the correctness of the implementation.

        Parameters
        ----------
        self : TestCase
            The test case instance.

        Returns
        -------
        None
        """
        self._circle_of_fifths = CircleOfFifths()

    def test_circle_of_fifths(self):
        """
        Unit test to verify the functionality of the 'circle_of_fifths' method.

        This test ensures that the 'circle_of_fifths' method returns the
        expected circle of fifths object. The test compares the object returned
        by the method with a pre-defined circle of fifths object. If the method
        returns an object that is not equal to the pre-defined object, the test
        will fail.

        Parameters
        ----------
        self : TestCase
            The test case instance.

        Returns
        -------
        None
        """
        self.assertEqual(
            self._circle_of_fifths.circle_of_fifths, self._CIRCLE_OF_FIFTHS
        )

    def test_relative_minors(self):
        """
        Unit test to verify the functionality of the 'circle_of_fifths' method.

        This test ensures that the 'circle_of_fifths' method returns the
        expected circle of fifths object. The test compares the object returned
        by the method with a pre-defined circle of fifths object. If the method
        returns an object that is not equal to the pre-defined object, the test
        will fail.

        Parameters
        ----------
        self : TestCase
            The test case instance.

        Returns
        -------
        None
        """
        self.assertEqual(
            self._circle_of_fifths.relative_minors, self._RELATIVE_MINORS
        )
