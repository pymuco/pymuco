#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_note_duration.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import NoteDuration, NoteDurationMapping


class TestNoteDurationMapping(unittest.TestCase):
    """
    A unittest test case to test the NoteDurationMapping class.

    Attributes
    ----------
    expected_note_lengths : list of tuples
        A list of tuples representing the expected note lengths for each note
        type. Each tuple contains a string representing the note type and a
        float representing its duration in terms of whole notes.

    Methods
    -------
    setUp()
        Set up the test fixture by creating an instance of NoteDurationMapping
        and assigning it to the instance variable self.note_duration_mapping.
    test_note_duration_mapping()
        Test the NoteDurationMapping.get_note_duration method by comparing its
        output with the expected_note_lengths list.
    """

    expected_note_lengths = [
        ("WHOLE_NOTE", 1.0),
        ("HALF_NOTE", 0.5),
        ("QUARTER_NOTE", 0.25),
        ("EIGHTH_NOTE", 0.125),
        ("SIXTEENTH_NOTE", 0.0625),
        ("THIRTY_SECOND_NOTE", 0.03125),
    ]

    def setUp(self):
        """
        Set up the test fixture.

        This method creates an instance of NoteDurationMapping and assigns it
        to the instance variable self.note_duration_mapping.

        Returns
        -------
        None
            This method only sets up the test fixture and doesn't return
            anything.
        """
        self.note_duration_mapping = NoteDurationMapping()

    def test_note_duration_mapping(self):
        """
        Test NoteDurationMapping.get_note_duration method.

        Returns
        -------
        None
            This function only tests that the output of get_note_duration method
            matches the expected_note_lengths list and raises an AssertionError
            otherwise.

        Raises
        ------
        AssertionError
            If the output of get_note_duration method doesn't match the
            expected_note_lengths list.
        """
        self.assertListEqual(
            self.note_duration_mapping.get_note_duration(),
            self.expected_note_lengths,
        )


class TestNoteDuration(unittest.TestCase):
    """
    A class for testing the NoteDuration class.

    Methods
    -------
    test_duration_type()
        Test that duration_type() method returns the expected value for each
        input.
    test_duration_length()
        Test that duration_length() method returns the expected value for each
        input.

    Raises
    ------
    ValueError
        If an invalid note type or length is provided.
    """

    def test_duration_type(self):
        """
        Test that duration_type() method returns the expected value for each
        input.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If an invalid note type is provided.
        """
        self.assertEqual(
            NoteDuration("WHOLE_NOTE").duration_type, "WHOLE_NOTE"
        )
        self.assertEqual(NoteDuration("HALF_NOTE").duration_type, "HALF_NOTE")
        self.assertEqual(
            NoteDuration("QUARTER_NOTE").duration_type, "QUARTER_NOTE"
        )
        self.assertEqual(
            NoteDuration("EIGHTH_NOTE").duration_type, "EIGHTH_NOTE"
        )
        self.assertEqual(
            NoteDuration("SIXTEENTH_NOTE").duration_type, "SIXTEENTH_NOTE"
        )
        self.assertEqual(
            NoteDuration("THIRTY_SECOND_NOTE").duration_type,
            "THIRTY_SECOND_NOTE",
        )
        with self.assertRaises(ValueError):
            NoteDuration("INVALID_NOTE_TYPE")

    def test_duration_length(self):
        """
        Test that duration_length() method returns the expected value for each
        input.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If an invalid note length is provided.
        """
        self.assertAlmostEqual(NoteDuration(1.0).duration_length, 1.0)
        self.assertAlmostEqual(NoteDuration(0.5).duration_length, 0.5)
        self.assertAlmostEqual(NoteDuration(0.25).duration_length, 0.25)
        self.assertAlmostEqual(NoteDuration(0.125).duration_length, 0.125)
        self.assertAlmostEqual(NoteDuration(0.0625).duration_length, 0.0625)
        self.assertAlmostEqual(NoteDuration(0.03125).duration_length, 0.03125)
        with self.assertRaises(ValueError):
            NoteDuration(2.0).duration_length
