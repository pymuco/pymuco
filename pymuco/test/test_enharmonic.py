#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_enharmonic.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import (
    Enharmonic,
    DEFAULT_OCTAVE,
    ScientificPitchNotation
)


class TestEnharmonic(unittest.TestCase):
    """
    Unittest class for the Enharmonic class.

    This class tests the functionality of the Enharmonic class, which provides
    methods for obtaining the enharmonic equivalent of a given note in Western
    music notation.

    The class contains the following unit tests:

    test_get_enharmonic:
    Tests if the get_enharmonic method returns the correct enharmonic note
    value for each note in the _ENHARMONIC_MAPPING dictionary.

    test_is_enharmonic:
    Tests if the is_enharmonic method returns True for each note in the
    _ENHARMONIC_MAPPING dictionary.

    test_get_all_enharmonics:
    Tests if the get_all_enharmonics method returns the expected list of
    enharmonic notes for a given note.

    The _ENHARMONIC_MAPPING dictionary maps each note name to its enharmonic
    equivalent, accounting for double sharps and flats.

    This class inherits from unittest.TestCase, which provides the testing
    functionality for each test case. The setUp method is not required since
    the tests do not require any specific setup.
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

    def test_get_enharmonic(self):
        """
        Test the get_enharmonic method of the Enharmonic class.

        This method tests whether the get_enharmonic method of the Enharmonic
        class correctly returns the enharmonic note value for each note in the
        _ENHARMONIC_MAPPING dictionary. For each note in the dictionary, a
        ScientificPitchNotation object is created with the note and the default
        octave, and passed to the Enharmonic constructor. The get_enharmonic
        method is then called on the Enharmonic object, and the pitch of the
        returned note is compared to the expected enharmonic value in the
        dictionary using self.assertEqual.

        Parameters
        ----------
        self : unittest.TestCase
            An instance of the unittest.TestCase class.

        Returns
        -------
        None
            This method does not return anything. It raises an exception if the
            test fails.

        Raises
        ------
        AssertionError
            If the pitch of the returned note is not equal to the expected
            enharmonic value.
        """
        for note, enharmonic_value in self._ENHARMONIC_MAPPING.items():
            spn = ScientificPitchNotation(note, DEFAULT_OCTAVE)
            enharmonic_note = Enharmonic(spn).get_enharmonic()
            self.assertEqual(enharmonic_note.pitch, enharmonic_value)

    def test_is_enharmonic(self):
        """
        Test for the `is_enharmonic` method of the Enharmonic class.

        Tests if the method returns True for each note in the
        `_ENHARMONIC_MAPPING` dictionary. For each note in the dictionary, a
        `ScientificPitchNotation` object is created with the note and the
        default octave, and passed to the `Enharmonic` constructor. The
        `is_enharmonic` method is then called on the `Enharmonic` object, and
        the result is compared to True using `self.assertTrue`.

        Returns
        -------
        None

        """
        for pitch in self._ENHARMONIC_MAPPING.keys():
            spn = ScientificPitchNotation(pitch, DEFAULT_OCTAVE)
            self.assertTrue(Enharmonic(spn).is_enharmonic(), True)

    def test_get_all_enharmonics(self):
        """
        Test the `get_all_enharmonics()` method of the `Enharmonic` class.

        This method checks if the `get_all_enharmonics()` method returns the
        expected list of enharmonic notes for a given note.

        Raises:
            AssertionError: If the returned list of enharmonic notes is not
            equal to the expected list ['A𝄫', 'Fx', 'G'].
        """
        self.assertEqual(
            Enharmonic(
                ScientificPitchNotation("G", DEFAULT_OCTAVE)
            ).get_all_enharmonics(),
            ["A𝄫", "Fx", "G"],
        )
