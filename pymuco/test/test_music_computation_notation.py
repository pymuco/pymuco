#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_music_computation_notation.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import (
    MusicComputationNotation,
    NoteDuration,
    ScientificPitchNotation
)


class TestMusicComputationNotation(unittest.TestCase):
    """
    Test class for MusicComputationNotation.

    Methods
    -------
    test_add_block_one_block:
        Test adding a single block of notes to the notation.
    test_add_single_blocks:
        Test adding multiple single blocks of notes to the notation.
    test_add_multiple_blocks:
        Test adding multiple blocks of notes to the notation.
    test_add_invalid_block:
        Test adding invalid blocks to the notation.
    """

    def setUp(self):
        """
        Sets up the MusicComputationNotation object and pitch and duration
        objects needed for testing.

        Creates the following objects:

        Parameters
        ----------
        self : TestMusicComputationNotation
            Instance of TestMusicComputationNotation class.

        Returns
        -------
        None

        Attributes
        ----------
        music_notation : MusicComputationNotation
            A MusicComputationNotation object for testing.
        C4 : ScientificPitchNotation
            A ScientificPitchNotation object representing the pitch C4.
        E4 : ScientificPitchNotation
            A ScientificPitchNotation object representing the pitch E4.
        G4 : ScientificPitchNotation
            A ScientificPitchNotation object representing the pitch G4.
        half_note : NoteDuration
            A NoteDuration object representing a half note (duration of 0.5
            quarter notes).
        whole_note : NoteDuration
            A NoteDuration object representing a whole note (duration of 4
            quarter notes).
        """
        self.music_notation = MusicComputationNotation()
        self.C4 = ScientificPitchNotation("C", 4)
        self.E4 = ScientificPitchNotation("E", 4)
        self.G4 = ScientificPitchNotation("G", 4)
        self.half_note = NoteDuration(0.5)
        self.whole_note = NoteDuration("WHOLE_NOTE")

    def test_add_block_one_block(self):
        """
        Tests the `add_block` method of the MusicComputationNotation class.

        Parameters:
        -----------
        None

        Setup:
        ------
        music_notation : MusicComputationNotation object
            An instance of MusicComputationNotation.

        C4 : ScientificPitchNotation object
            A ScientificPitchNotation object representing C4.

        whole_note : NoteDuration object
            A NoteDuration object representing a whole note (duration of 4
            quarter notes).

        Actions:
        --------
        Adds a single block consisting of `C4` pitch and `whole_note` duration
        to the `music_notation` object.

        Returns:
        --------
        None

        Assertions:
        -----------
        - Compares the resulting notation to an expected notation.
        - The expected notation is a list containing a single tuple with the
        pitch and duration of the block added.
        - The test checks that the notation stored in the `music_notation`
        object after the addition matches the expected notation.
        """
        self.music_notation.add_block(self.C4, self.whole_note)
        expected_notation = [(self.C4.spn, self.whole_note.duration_length)]
        self.assertEqual(self.music_notation.notation, expected_notation)

    def test_add_single_blocks(self):
        """
        Test that the notation correctly stores single blocks added one at a
        time.

        Parameters:
        -----------
        None

        Setup:
        ------
        Creates a MusicComputationNotation object and adds three blocks of
        notes to it.

        - `music_notation`: a MusicComputationNotation object for testing.
        - `E4`: a ScientificPitchNotation object representing the pitch E4.
        - `G4`: a ScientificPitchNotation object representing the pitch G4.
        - `C4`: a ScientificPitchNotation object representing the pitch C4.
        - `half_note`: a NoteDuration object representing a half note
        (duration of 0.5 quarter notes).
        - `whole_note`: a NoteDuration object representing a whole note
        (duration of 4 quarter notes).

        Expected Result:
        ----------------
        The notation should contain the three blocks in the correct order.

        Test Strategy:
        --------------
        Test the add_block method and the notation property.

        Returns:
        --------
        None
        """
        self.music_notation.add_block(self.E4, self.half_note)
        self.music_notation.add_block(self.G4, self.whole_note)
        self.music_notation.add_block(self.C4, self.half_note)
        expected_notation = [
            (self.E4.spn, self.half_note.duration_length),
            (self.G4.spn, self.whole_note.duration_length),
            (self.C4.spn, self.half_note.duration_length),
        ]
        self.assertEqual(self.music_notation.notation, expected_notation)

    def test_add_multiple_blocks(self):
        """
        Test the functionality of adding multiple blocks to a
        MusicComputationNotation object.

        Parameters:
        -----------
        None

        Setup:
        ------
        music_notation : MusicComputationNotation object
            An instance of MusicComputationNotation to which three blocks of
            notes will be added.

        E4 : Pitch object
            A Pitch object representing the note E4.
        G4 : Pitch object
            A Pitch object representing the note G4.
        C4 : Pitch object
            A Pitch object representing the note C4.

        half_note : Duration object
            A Duration object representing a half note.
        whole_note : Duration object
            A Duration object representing a whole note.

        Returns:
        --------
        None

        Expected Result:
        ----------------
        The notation property of the MusicComputationNotation object should
        contain the three blocks of notes
        in the correct order.

        Test Strategy:
        --------------
        This test case tests the add_block method and the notation property of
        the MusicComputationNotation class.

        """
        self.music_notation.add_block(
            self.E4,
            self.half_note,
            self.G4,
            self.whole_note,
            self.C4,
            self.half_note,
        )
        expected_notation = [
            (self.E4.spn, self.half_note.duration_length),
            (self.G4.spn, self.whole_note.duration_length),
            (self.C4.spn, self.half_note.duration_length),
        ]
        self.assertEqual(self.music_notation.notation, expected_notation)

    def test_add_invalid_block(self):
        """
        Test case for the add_block method of the MusicComputationNotation
        class, when adding invalid blocks.

        Parameters:
        -----------
        None

        Setup:
        ------
        music_notation : MusicComputationNotation object
            An instance of MusicComputationNotation to which blocks with
            invalid arguments will be added.

        C4 : ScientificPitchNotation object
            A ScientificPitchNotation object representing C4.

        whole_note : NoteDuration object
            A NoteDuration object representing a whole note.

        Returns:
        --------
        None

        Expected Result:
        ----------------
        A TypeError should be raised in all three scenarios.

        Test Strategy:
        --------------
        - Call add_block with a string as the pitch argument, and verify that a
        TypeError is raised.
        - Call add_block with a float as the duration argument, and verify that
        a TypeError is raised.
        - Call add_block with an invalid string as the duration argument, and
        verify that a TypeError is raised.
        """
        with self.assertRaises(TypeError):
            self.music_notation.add_block("C4", self.whole_note)
        with self.assertRaises(TypeError):
            self.music_notation.add_block(self.C4, 1.5)
        with self.assertRaises(TypeError):
            self.music_notation.add_block(self.C4, "invalid_duration")
