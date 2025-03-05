#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_note_mapping.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import NoteMapping, ScientificPitchNotation


class TestNoteMapping(unittest.TestCase):
    """
    A test case class for testing the functionality of the NoteMapping class.

    The class has a single test method called test_get_note_mapping, which
    checks if the get_note_mapping method of the NoteMapping class returns the
    expected note mapping dictionary. The _NOTE_MAPPING dictionary is used as a
    reference to compare the returned dictionary with the expected one.

    Attributes:
    -----------
        _NOTE_MAPPING (dict): A dictionary that maps note names to their
        corresponding MIDI numbers.

    Methods:
    --------
        setUp(self): Sets up a NoteMapping instance for testing.
        test_get_note_mapping(self): Tests the get_note_mapping method of the
        NoteMapping class for returning the expected note mapping dictionary.

    Example:
    --------
        >>> test = TestNoteMapping()
        >>> test.setUp()
        >>> test.test_get_note_mapping()
    """

    _NOTE_MAPPING = {
        "C": 0,
        "B#": 0,
        "D𝄫": 0,
        "C#": 1,
        "Bx": 1,
        "Db": 1,
        "D": 2,
        "Cx": 2,
        "E𝄫": 2,
        "D#": 3,
        "Eb": 3,
        "E": 4,
        "Dx": 4,
        "Fb": 4,
        "F": 5,
        "E#": 5,
        "G𝄫": 5,
        "F#": 6,
        "Ex": 6,
        "Gb": 6,
        "G": 7,
        "A𝄫": 7,
        "Fx": 7,
        "G#": 8,
        "Ab": 8,
        "A": 9,
        "B𝄫": 9,
        "Gx": 9,
        "A#": 10,
        "Bb": 10,
        "B": 11,
        "Ax": 11,
        "Cb": 11,
    }

    def setUp(self):
        """
        Method called to prepare the test fixture. It creates an instance of
        the NoteMapping class and assigns it to the
        self.note_mapping attribute.

        Test method:
        ------------
        setUp(self)

        Tested class:
        -------------
        N/A

        Tested method:
        ---------------
        N/A

        Test procedure:
        ---------------
        Create an instance of the NoteMapping class.
        Assign the created instance to the self.note_mapping attribute.

        Expected behavior:
        ------------------
        The self.note_mapping attribute should be an instance of the
        NoteMapping class after calling the setUp method.
        """
        self.note_mapping = NoteMapping()

    def test_get_note_mapping(self):
        """
        Test the `get_note_mapping` method of the `note_mapping` class.

        This method checks if the `get_note_mapping` method of the
        `note_mapping` class returns the expected note mapping dictionary. The
        method is called for each key-value pair in the `_NOTE_MAPPING`
        dictionary, and the returned value is compared with the expected
        `_NOTE_MAPPING` dictionary using the `assertEqual` method.

        Parameters
        ----------
        self: unittest.TestCase
            The instance of the `unittest.TestCase` class.

        Returns
        -------
        None
            This method asserts the correctness of the `get_note_mapping`
            method.

        Raises
        ------
        AssertionError
            If the returned value of the `get_note_mapping` method does not
            match the expected `_NOTE_MAPPING` dictionary.

        See Also
        --------
        note_mapping.get_note_mapping : Returns the note mapping dictionary.

        Example
        -------
        >>> test = TestNoteMapping()
        >>> test.test_get_note_mapping()
        """
        for key, value in self._NOTE_MAPPING.items():
            self.assertEqual(
                self.note_mapping.get_note_mapping(), self._NOTE_MAPPING
            )
