#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_key_signature.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import KeySignature, ScientificPitchNotation


class TestKeySignature(unittest.TestCase):
    """
    Class for testing the KeySignature class in Python.

    Methods
    -------
    test_get_key_signature():
        Test the get_key_signature() method of the KeySignature class.
        Sets up expected results for each input note and compares the actual
        result to the expected result for each note.
        Uses the self.assertEqual() method to perform the comparison.

    test_get_key_signature_notes():
        Test the get_key_signature_notes() method of the KeySignature class.
        Creates a KeySignature object with each input note and mode "M" and
        compares the actual list of notes in the key signature to the expected
        list of notes for each note.
        Uses the self.assertEqual() method to perform the comparison.
    """

    def test_get_key_signature(self):
        """
        Test the functionality of the get_key_signature() method in the
        KeySignature class.

        The KeySignature class takes a ScientificPitchNotation object and a
        mode ("M" for major or "m" for minor) as arguments, and returns the
        corresponding key signature in the format of the number of sharps or
        flats.

        This test sets up expected results for each input note and uses a for
        loop to iterate over each input note. For each note, a
        ScientificPitchNotation object with that note and octave 4 is created,
        a KeySignature object is created with that ScientificPitchNotation
        object and mode "M", and the get_key_signature() method is called to
        get the actual key signature. The self.assertEqual() method is used to
        compare the actual result to the expected result for that note.

        The test ensures that the expected results match the actual results for
        each input note in the KeySignature class's get_key_signature() method.

        Parameters
        ----------
        self : unittest.TestCase
            An instance of the unittest.TestCase class.

        Returns
        -------
        None
            This test only checks if the get_key_signature() method of the
            KeySignature class returns the expected values.
        """
        expected_results = [
            "0",
            "1#",
            "2#",
            "3#",
            "4#",
            "5#",
            "6#",
            None,
            "6b",
            "5b",
            "4b",
            "3b",
            "2b",
            "1b",
        ]
        inputs = [
            "C",
            "G",
            "D",
            "A",
            "E",
            "B",
            "F#",
            "C#",
            "Gb",
            "Db",
            "Ab",
            "Eb",
            "Bb",
            "F",
        ]

        for i, note in enumerate(inputs):
            with self.subTest(note=note):
                pitch = ScientificPitchNotation(note, 4)
                ks = KeySignature(pitch, "M")
                result = ks.get_key_signature()
                expected = expected_results[i]
                self.assertEqual(result, expected)

    def test_get_key_signature_notes(self):
        """
        Test the `get_key_signature_notes` method of the KeySignature class.

        The `get_key_signature_notes` method returns a list of the notes in the
        key signature of the given pitch.

        Parameters
        ----------
        self : TestCase
            A unittest TestCase object.

        Returns
        -------
        None

        Notes
        -----
        This method creates a list of input note names and expected results.
        For each input note, the method creates a `ScientificPitchNotation`
        object and a `KeySignature` object with the given note and a mode of
        "M" (major). The method then calls the `get_key_signature_notes` method
        of the `KeySignature` object and compares the resulting list of notes
        to the expected list of notes for that input note using the
        `assertEqual` method. The `with self.subTest(note=note):` statement is
        used to create a subtest for each input note.

        This unit test ensures that the `get_key_signature_notes` method of the
        `KeySignature` class returns the expected list of notes for a given
        pitch and mode.

        Examples
        --------
        >>> ks = KeySignature(ScientificPitchNotation("C", 4), "M")
        >>> ks.get_key_signature_notes()
        []

        >>> ks = KeySignature(ScientificPitchNotation("G", 4), "M")
        >>> ks.get_key_signature_notes()
        ["F#"]
        """
        inputs = [
            "C",
            "G",
            "D",
            "A",
            "E",
            "B",
            "F#",
            "C#",
            "Gb",
            "Db",
            "Ab",
            "Eb",
            "Bb",
            "F",
        ]
        expected_notes = [
            [],
            ["F#"],
            ["F#", "C#"],
            ["F#", "C#", "G#"],
            ["F#", "C#", "G#", "D#"],
            ["F#", "C#", "G#", "D#", "A#"],
            ["F#", "C#", "G#", "D#", "A#", "E#"],
            None,
            ["Bb", "Eb", "Ab", "Db", "Gb", "B"],
            ["Bb", "Eb", "Ab", "Db", "Gb"],
            ["Bb", "Eb", "Ab", "Db"],
            ["Bb", "Eb", "Ab"],
            ["Bb", "Eb"],
            ["Bb"],
        ]

        for i, note in enumerate(inputs):
            with self.subTest(note=note):
                pitch = ScientificPitchNotation(note, 4)
                ks = KeySignature(pitch, "M")
                result = ks.get_key_signature_notes()
                expected = expected_notes[i]
                self.assertEqual(result, expected)
