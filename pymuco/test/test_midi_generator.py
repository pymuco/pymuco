#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_midi_generator.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest
from unittest.mock import patch, mock_open
from typing import List, Tuple

from pymuco import (
    MidiGenerator,
    NoteDuration,
    ScientificPitchNotation
)


class TestMidiGenerator(unittest.TestCase):
    """
    A class that contains unit tests for the MidiGenerator class.

    Attributes:
    -----------
    midi_generator : MidiGenerator
        An instance of the MidiGenerator class for testing purposes.

    Methods:
    --------
    test_write_note_on():
        Tests the '_write_note_on' method by verifying the correct data is
        added to the track data when a 'Note On' event is written.

    test_write_note_off():
        Tests the '_write_note_off' method by verifying the correct data is
        added to the track data when a 'Note Off' event is written.

    test_create_midi_file():
        Tests the 'create_midi_file' method by simulating a file write and
        verifying that the correct data is written to the file.
    """

    def setUp(self) -> None:
        """
        Sets up the testing environment before each test. This method is called
        before each test and initializes an instance of MidiGenerator for
        testing purposes.

        Returns:
        --------
        None
        """
        self.midi_generator = MidiGenerator()

    def test_write_note_on(self):
        """
        Test the `_write_note_on` method of the MidiGenerator class.

        This test verifies that the correct MIDI data is added to the track
        when a 'Note On' event is written. It checks the structure and content
        of the data in the track to ensure it matches the expected format.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError: If the generated MIDI data does not match the expected
        values.
        """
        track_data = []
        delta_time = 0
        note_name = ScientificPitchNotation("C", 4)  # Use ScientificPitchNotation
        velocity = 64

        self.midi_generator._write_note_on(track_data, delta_time, note_name, velocity)

        expected_data = [0x00, 0x90, 60, 64]  # Expected MIDI 'Note On' event for C4
        self.assertEqual(track_data, expected_data)

    def test_write_note_off(self):
        """
        Test the `_write_note_off` method of the MidiGenerator class.

        This test verifies that the correct MIDI data is added to the track
        when a 'Note Off' event is written. It checks the structure and content
        of the data in the track to ensure it matches the expected format.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError: If the generated MIDI data does not match the expected
        values.
        """
        track_data = []
        delta_time = 0
        note_name = ScientificPitchNotation("C", 4)
        velocity = 64

        self.midi_generator._write_note_off(track_data, delta_time, note_name, velocity)

        expected_data = [0x00, 0x80, 60, 64]  # Expected MIDI 'Note Off' event for C4
        self.assertEqual(track_data, expected_data)

    def test_create_track_data(self):
        """
        Test the `_create_track_data` method of the MidiGenerator class.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError:
        """
        spn1 = ScientificPitchNotation("C", 4)
        spn2 = ScientificPitchNotation("D", 4)
        duration1 = NoteDuration(1.0)
        duration2 = NoteDuration(0.5)

        music_computation_notation = [(spn1, duration1), (spn2, duration2)]
        track_data = self.midi_generator._create_track_data(music_computation_notation)
        duration1_ticks = int(duration1.duration_length * 96)
        duration2_ticks = int(duration2.duration_length * 96)

        expected_data = [
            0x4D,
            0x54,
            0x72,
            0x6B,  # Chunk type "MTrk"
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x90,
            60,
            64,
            duration1_ticks,
            0x80,
            60,
            64,
            0x00,
            0x90,
            62,
            64,
            duration2_ticks,
            0x80,
            62,
            64,
            0x00,
            0xFF,
            0x2F,
            0x00,  # Meta event: End of track
        ]

        self.assertEqual(track_data[: len(expected_data)], expected_data)

    def test_write_variable_length(self):
        """
        Test the `_write_variable_length` method of the MidiGenerator class.

        This test verifies that the conversion of a duration value into a
        MIDI variable-length format is correct.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError: If the conversion does not produce the expected result.
        """
        result = self.midi_generator._write_variable_length(240)  # 240 ticks
        expected = [0x81, 0x70]  # Variable length format for 240

        self.assertEqual(result, expected)

    def test_insert_track_length(self):
        """
        Test the `_insert_track_length` method of the MidiGenerator class.

        This test verifies that the correct track length is calculated and
        inserted into the MIDI track data.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError: If the inserted track length does not match the
        expected values.
        """
        track_data = [0x4D, 0x54, 0x72, 0x6B, 0x00, 0x00, 0x00, 0x00, 0x90, 60, 64]
        self.midi_generator._insert_track_length(track_data)
        # The length of the track data minus the first 8 bytes (header) is 3
        expected_length = [0x00, 0x00, 0x00, 0x03]
        self.assertEqual(track_data[4:8], expected_length)

    @patch("builtins.open", new_callable=mock_open)
    def test_create_midi_file(self, mock_file):
        """
        Test the `create_midi_file` method of the MidiGenerator class.

        Parameters:
        -----------
        mock_file : mock_open

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError:
        """
        spn = ScientificPitchNotation("C", 4)
        duration = NoteDuration(1.0)
        music_computation_notation: List[
            Tuple[ScientificPitchNotation, NoteDuration]
        ] = [(spn, duration)]
        self.midi_generator.create_midi_file(music_computation_notation, "output.mid")
        mock_file.assert_any_call("output.mid", "wb")
        handle = mock_file()
        handle.write.assert_called()
