#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_midi_utils.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import re
import unittest

from pymuco import MIDINoteConverter, ScientificPitchNotation


class TestMIDINoteConverter(unittest.TestCase):
    """
    TestMIDINoteConverter is a class that contains unit tests for the
    note_name_to_midi_note method of the MIDINoteConverter class.

    Attributes
    ----------
    _NOTES : dict
        A dictionary of MIDI notes and their corresponding scientific pitch
        notation.

    Methods
    -------
    test_note_name_to_midi_note():
        Tests the note_name_to_midi_note method by looping through the _NOTES
        dictionary and asserting that the calculated MIDI value of each note is
        equal to the expected MIDI value.

    Notes
    -----
    This class is likely part of a larger test suite that tests the
    functionality of the MIDINoteConverter class.
    """

    _NOTES = {
        127: "G9",
        126: "F#9/Gb9",
        125: "F9",
        124: "E9",
        123: "D#9/Eb9",
        122: "D9",
        121: "C#9/Db9",
        120: "C9",
        119: "B8",
        118: "A#8/Bb8",
        117: "A8",
        116: "G#8/Ab8",
        115: "G8",
        114: "F#8/Gb8",
        113: "F8",
        112: "E8",
        111: "D#8/Eb8",
        110: "D8",
        109: "C#8/Db8",
        108: "C8",
        107: "B7",
        106: "A#7/Bb7",
        105: "A7",
        104: "G#7/Ab7",
        103: "G7",
        102: "F#7/Gb7",
        101: "F7",
        100: "E7",
        99: "D#7/Eb7",
        98: "D7",
        97: "C#7/Db7",
        96: "C7",
        95: "B6",
        94: "A#6/Bb6",
        93: "A6",
        92: "G#6/Ab6",
        91: "G6",
        90: "F#6/Gb6",
        89: "F6",
        88: "E6",
        87: "D#6/Eb6",
        86: "D6",
        85: "C#6/Db6",
        84: "C6",
        83: "B5",
        82: "A#5/Bb5",
        81: "A5",
        80: "G#5/Ab5",
        79: "G5",
        78: "F#5/Gb5",
        77: "F5",
        76: "E5",
        75: "D#5/Eb5",
        74: "D5",
        73: "C#5/Db5",
        72: "C5",
        71: "B4",
        70: "A#4/Bb4",
        69: "A4",
        68: "G#4/Ab4",
        67: "G4",
        66: "F#4/Gb4",
        65: "F4",
        64: "E4",
        63: "D#4/Eb4",
        62: "D4",
        61: "C#4/Db4",
        60: "C4",
        59: "B3",
        58: "A#3/Bb3",
        57: "A3",
        56: "G#3/Ab3",
        55: "G3",
        54: "F#3/Gb3",
        53: "F3",
        52: "E3",
        51: "D#3/Eb3",
        51: "D#3/Eb3",
        50: "D3",
        49: "C#3/Db3",
        48: "C3",
        47: "B2",
        46: "A#2/Bb2",
        45: "A2",
        44: "G#2/Ab2",
        43: "G2",
        42: "F#2/Gb2",
        41: "F2",
        40: "E2",
        39: "D#2/Eb2",
        38: "D2",
        37: "C#2/Db2",
        36: "C2",
        35: "B1",
        34: "A#1/Bb1",
        33: "A1",
        32: "G#1/Ab1",
        31: "G1",
        30: "F#1/Gb1",
        29: "F1",
        28: "E1",
        27: "D#1/Eb1",
        26: "D1",
        25: "C#1/Db1",
        24: "C1",
        23: "B0",
        22: "A#0/Bb0",
        21: "A0",
    }

    def test_note_name_to_midi_note(self):
        """
        Test the method note_name_to_midi_note of the MIDINoteConverter class.

        This test loops through a dictionary of notes and their corresponding
        MIDI values, converts each note to its MIDI value using the
        note_name_to_midi_note method, and asserts that the calculated MIDI
        value is equal to the expected MIDI value. The test also asserts that
        the scientific pitch notation of the note is equal to the original note
        value.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Notes:
        ------
        - This test uses regular expressions to extract the octave and pitch
        information from the note value.
        - If the pitch is two characters or fewer, the octave and pitch are
        used to create a ScientificPitchNotation object, which is then passed
        to the note_name_to_midi_note method.
        - If the pitch is longer than two characters, the note value is split
        into two parts (before and after the slash) and each part is used to
        create a separate ScientificPitchNotation object, which is then passed
        to the note_name_to_midi_note method.

        Raises:
        -------
        AssertionError:
            If a calculated MIDI value is not equal to the expected MIDI value.

        Examples:
        ---------
        >>> test_note_name_to_midi_note()
        """
        number_pattern = r"\d+\.?\d*"
        pitch_pattern = r"[a-zA-Z]+"

        for key, value in self._NOTES.items():
            number_match = re.search(number_pattern, value)
            octave = int(number_match.group())

            pitch_match = re.findall(pitch_pattern, value)
            pitch = "".join(pitch_match)

            if len(pitch) <= 2:
                spn = ScientificPitchNotation(pitch, octave)
                midi = MIDINoteConverter().note_name_to_midi_note(spn)

                self.assertEqual(key, midi)
                self.assertEqual(value, spn)

            elif len(pitch) > 2:
                spn1 = re.search(r"([^0-9/]+)", value)
                note1 = ScientificPitchNotation(spn1.group(1), octave)
                midi1 = MIDINoteConverter().note_name_to_midi_note(note1)
                self.assertEqual(key, midi1)

                spn2 = re.search(r"(?<=/)[a-zA-Z]+", value)
                note2 = ScientificPitchNotation(spn2.group(), octave)
                midi2 = MIDINoteConverter().note_name_to_midi_note(note2)
                self.assertEqual(key, midi2)

    def test_midi_note_to_note_name(self):
        """
        Test the `midi_note_to_note_name` method of the MIDINoteConverter
        class.

        This unit test method loops through the dictionary of notes and their
        corresponding MIDI values, converts each MIDI value to its
        corresponding note name using the `midi_note_to_note_name` method, and
        asserts that the calculated note name is equal to the expected note
        name.

        Parameters:
        -----------
        self: TestMIDINoteConverter
            An instance of the TestMIDINoteConverter class.

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError
            If the calculated note name is not equal to the expected note name.

        Notes:
        ------
        This test uses regular expressions to extract the pitch information
        from the original note value. The extracted pitch is then compared to
        the calculated note name using the `assertEqual` method. This test
        ensures that the `midi_note_to_note_name` method correctly converts
        MIDI values to their corresponding note names.
        """
        for key, value in self._NOTES.items():
            midi = MIDINoteConverter().midi_note_to_note_name(key)
            spn_value = re.search(r"([^/]+)", value)
            self.assertEqual(spn_value.group(), midi)
