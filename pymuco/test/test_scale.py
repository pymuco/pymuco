#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_scale.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import Scale, ScaleData, ScientificPitchNotation


class TestScaleData(unittest.TestCase):
    """
    This is a test case for the `ScaleData` class.

    Test methods:
    -------------
    test_major_scale_sequence:
        Tests the `major_scale_sequence` method of the `ScaleData` class.
    test_minor_scale_sequence:
        Tests the `minor_scale_sequence` method of the `ScaleData` class.

    See Also:
    ---------
    `ScaleData.major_scale_sequence`
    `ScaleData.minor_scale_sequence`
    """

    _SCALE_SEQUENCE = {
        "Major": [0, 2, 4, 5, 7, 9, 11, 12],
        "Minor": [0, 2, 3, 5, 7, 8, 10, 12],
    }

    def test_major_scale_sequence(self):
        """
        Unit test for the major_scale_sequence method of the ScaleData class.

        This test checks if the major_scale_sequence method of the ScaleData
        class returns the expected major scale sequence.

        Parameters
        ----------
        self : TestCase
            An instance of the unittest.TestCase class.

        Returns
        -------
        None

        Raises
        ------
        AssertionError
            If the returned value from the major_scale_sequence method does not
            match the expected major scale sequence.

        See Also
        --------
        ScaleData.major_scale_sequence : Method being tested.

        Notes
        -----
        This test compares the output of the major_scale_sequence method of the
        ScaleData class with the expected major scale sequence using the
        assertEqual method. This ensures that the major_scale_sequence method
        correctly returns the expected sequence.

        """
        self.assertEqual(
            ScaleData.SCALE_SEQUENCE.value["Major"],
            self._SCALE_SEQUENCE["Major"],
        )

    def test_minor_scale_sequence(self):
        """
        Test the `minor_scale_sequence` method of the `ScaleData` class.

        Tests if the `minor_scale_sequence` method of the `ScaleData` class
        returns the expected sequence of intervals for the Minor scale.

        Parameters:
        -----------
        self : object
            An instance of the `ScaleData` test class.

        Returns:
        --------
        None.

        Test method:
        test_minor_scale_sequence(self)

        Tested class:
        `ScaleData`

        Tested method:
        `minor_scale_sequence`

        Test procedure:
        ---------------
        1. Call the `minor_scale_sequence` method of the `ScaleData` class.
        2. Compare the returned value with the expected sequence of intervals
        for the Minor scale using the `assertEqual` method.

        Expected behavior:
        ------------------
        The `minor_scale_sequence` method of the `ScaleData` class should
        return the expected sequence of intervals for the Minor scale.

        See Also:
        ---------
        `ScaleData.SCALE_SEQUENCE`
        """
        self.assertEqual(
            ScaleData.SCALE_SEQUENCE.value["Minor"],
            self._SCALE_SEQUENCE["Minor"],
        )


class TestScale(unittest.TestCase):
    """
    The TestScale class is a subclass of unittest.TestCase, containing two test methods: test_get_major_scale and test_get_minor_scale.

    The class has two class-level dictionaries, _MAJOR_SCALE and _MINOR_SCALE, that define the notes of major and minor scales respectively.
    The test_get_major_scale method tests if the get_major_scale method of the Scale class returns the expected major scale for each note
    in the _MAJOR_SCALE dictionary. The test_get_minor_scale method tests if the get_scale method of the Scale class returns the expected scale
    for each note in the _MINOR_SCALE dictionary.
    """

    _MAJOR_SCALE = {
        "C": ["C", "D", "E", "F", "G", "A", "B", "C"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
        "F": ["F", "G", "A", "Bb", "C", "D", "E", "F"],
        "G": ["G", "A", "B", "C", "D", "E", "F#", "G"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"],
        "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"],
        "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"],
        "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"],
        "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "Gb": ["Gb", "Ab", "Bb", "B", "Db", "Eb", "F", "Gb"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],
    }

    _MINOR_SCALE = {
        "A": ["A", "B", "C", "D", "E", "F", "G", "A"],
        "E": ["E", "F#", "G", "A", "B", "C", "D", "E"],
        "D": ["D", "E", "F", "G", "A", "Bb", "C", "D"],
        "F#": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
        "C#": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
        "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"],
        "D#": ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"],
        "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "B", "Db", "Eb"],
        "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
        "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"],
        "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"],
        "G": ["G", "A", "Bb", "C", "D", "Eb", "F", "G"],
        "D": ["D", "E", "F", "G", "A", "Bb", "C", "D"],
    }

    def test_get_major_scale(self):
        """
        Unit test for the get_major_scale method of the Scale class.

        This test checks if the get_major_scale method of the Scale class returns the expected major scale for each note in the _MAJOR_SCALE dictionary. The method is called for each key-value pair in the _MAJOR_SCALE dictionary and the returned value is compared with the expected major scale using the assertListEqual method.

        Test method:
        test_get_major_scale(self)

        Tested class:
        Scale

        Tested method:
        get_major_scale

        Test procedure:

        Iterate through each key-value pair in the _MAJOR_SCALE dictionary.
        Create a ScientificPitchNotation object with the current note and octave 4.
        Call the get_major_scale method of the Scale class with the created ScientificPitchNotation object and the mode 'M'.
        Compare the returned scale with the expected major scale using the assertListEqual method.
        Expected behavior:
        The get_major_scale method of the Scale class should return the expected major scale for each note in the _MAJOR_SCALE dictionary.
        """
        for note, expected_scale in self._MAJOR_SCALE.items():
            with self.subTest(note=note, expected_scale=expected_scale):
                spn = ScientificPitchNotation(note, 4)
                scale = Scale(spn, "M").get_scale()
                self.assertListEqual(scale, expected_scale)

    def test_get_minor_scale(self):
        """
        Unit test for the get_scale method of the Scale class for minor scales.

        This test checks if the get_scale method of the Scale class returns the expected scale for each note in the _MINOR_SCALE dictionary. The method is called for each key-value pair in the _MINOR_SCALE dictionary and the returned value is compared with the expected scale using the assertListEqual method.

        Test method:
        test_get_minor_scale(self)

        Tested class:
        Scale

        Tested method:
        get_scale

        Test procedure:

        Iterate through each key-value pair in the _MINOR_SCALE dictionary.
        Create a ScientificPitchNotation object with the note and octave from the key.
        Call the get_scale method of the Scale class with the note and "m" as the scale type.
        Compare the returned value with the expected scale from the value of the key in the _MINOR_SCALE dictionary using the assertListEqual method.
        Expected behavior:
        The get_scale method of the Scale class should return the expected scale for each note in the _MINOR_SCALE dictionary.
        """
        for note, expected_scale in self._MINOR_SCALE.items():
            with self.subTest(note=note, expected_scale=expected_scale):
                spn = ScientificPitchNotation(note, 4)
                scale = Scale(spn, "m").get_scale()
                self.assertListEqual(scale, expected_scale)
