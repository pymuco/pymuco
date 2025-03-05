#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_note_frequency_converter.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import re
import unittest

from pymuco import NoteFrequencyConverter, ScientificPitchNotation


class TestNoteFrequencyConverter(unittest.TestCase):
    """
    A test case class used for testing the functionality of a note frequency
    converter.

    Attributes:
    _MIDI_NOTES (dict): A dictionary that stores the MIDI notes and their
    corresponding frequencies.

    Methods:
    setUp(self): Initializes a NoteFrequencyConverter object.
    test_get_frequency_from_midi_number(self): Test the
    get_frequency_from_midi_number method of the Converter class with valid
    input.
    test_get_frequency_from_note_name(self): Test the
    get_frequency_from_note_name method of a Converter object.
    """

    _MIDI_NOTES = {
        127: 12543.85,
        126: 11839.82,
        125: 11175.30,
        124: 10548.08,
        123: 9956.06,
        122: 9397.27,
        121: 8869.84,
        120: 8372.02,
        119: 7902.13,
        118: 7458.62,
        117: 7040.00,
        116: 6644.88,
        115: 6271.93,
        114: 5919.91,
        113: 5587.65,
        112: 5274.04,
        111: 4978.03,
        110: 4698.64,
        109: 4434.92,
        108: 4186.01,
        107: 3951.07,
        106: 3729.31,
        105: 3520.00,
        104: 3322.44,
        103: 3135.96,
        102: 2959.96,
        101: 2793.83,
        100: 2637.02,
        99: 2489.02,
        98: 2349.32,
        97: 2217.46,
        96: 2093.00,
        95: 1975.53,
        94: 1864.66,
        93: 1760.00,
        92: 1661.22,
        91: 1567.98,
        90: 1479.98,
        89: 1396.91,
        88: 1318.51,
        87: 1244.51,
        86: 1174.66,
        85: 1108.73,
        84: 1046.50,
        83: 987.77,
        82: 932.33,
        81: 880.00,
        80: 830.61,
        79: 783.99,
        78: 739.99,
        77: 698.46,
        76: 659.26,
        75: 622.25,
        74: 587.33,
        73: 554.37,
        72: 523.25,
        71: 493.88,
        70: 466.16,
        69: 440.00,
        68: 415.30,
        67: 392.00,
        66: 369.99,
        65: 349.23,
        64: 329.63,
        63: 311.13,
        62: 293.66,
        61: 277.18,
        60: 261.63,
        59: 246.94,
        58: 233.08,
        57: 220.00,
        56: 207.65,
        55: 196.00,
        54: 185.00,
        53: 174.61,
        52: 164.81,
        51: 155.56,
        50: 146.83,
        49: 138.59,
        48: 130.81,
        47: 123.47,
        46: 116.54,
        45: 110.00,
        44: 103.83,
        43: 98.00,
        42: 92.50,
        41: 87.31,
        40: 82.41,
        39: 77.78,
        38: 73.42,
        37: 69.30,
        36: 65.41,
        35: 61.74,
        34: 58.27,
        33: 55.00,
        32: 51.91,
        31: 49.00,
        30: 46.25,
        29: 43.65,
        28: 41.20,
        27: 38.89,
        26: 36.71,
        25: 34.65,
        24: 32.70,
        23: 30.87,
        22: 29.14,
        21: 27.50,
        20: 25.96,
        19: 24.50,
        18: 23.12,
        17: 21.83,
        16: 20.60,
        15: 19.45,
        14: 18.35,
        13: 17.32,
        12: 16.35,
        11: 15.43,
        10: 14.57,
        9: 13.75,
        8: 12.98,
        7: 12.25,
        6: 11.56,
        5: 10.91,
        4: 10.30,
        3: 9.72,
        2: 9.18,
        1: 8.66,
        0: 8.18,
    }

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

    def setUp(self):
        """
        Initializes a NoteFrequencyConverter object.

        Returns:
        None.
        """
        self.converter = NoteFrequencyConverter()

    def test_get_frequency_from_midi_number(self):
        """
        Test the get_frequency_from_midi_number method of the Converter class
        with valid input.

        This method iterates through a dictionary `_MIDI_NOTES` which maps MIDI
        note numbers to their corresponding frequency values. For each key in
        the dictionary, the method calls the `get_frequency_from_midi_number`
        method of the `Converter` class and compares the returned value to the
        expected frequency value.

        Raises:
            AssertionError: if the returned frequency value does not match the
            expected frequency value for any MIDI note number.

        Returns:
            None. This method asserts the correctness of the
            `get_frequency_from_midi_number` method.

        Example:
            >>> converter = Converter()
            >>> converter.test_get_frequency_from_midi_number()
            None
        """
        for key, value in self._MIDI_NOTES.items():
            self.assertEqual(
                value, self.converter.get_frequency_from_midi_number(key)
            )

    def test_get_frequency_from_note_name(self):
        """
        Test the get_frequency_from_note_name method of a Converter object.

        This method loops through a dictionary of note names and their
        corresponding MIDI numbers. For each note name, the method parses the
        note name to extract the pitch and octave. The method then creates a
        `ScientificPitchNotation` object from the parsed pitch and octave, and
        calls the `get_frequency_from_note_name` method of the `Converter`
        object with this object. The method asserts that the returned frequency
        value matches the expected MIDI number.

        Raises:
            AssertionError: if the returned frequency value does not match the
            expected MIDI number for any note name.

        Returns:
            None. This method asserts the correctness of the
            `get_frequency_from_note_name` method.

        Example:
            >>> converter = Converter()
            >>> converter.test_get_frequency_from_note_name()
            None
        """
        number_pattern = r"\d+\.?\d*"
        pitch_pattern = r"[a-zA-Z]+"

        for key1, key2 in zip(self._NOTES, self._MIDI_NOTES):
            number_match = re.search(number_pattern, self._NOTES[key1])
            octave = int(number_match.group())

            pitch_match = re.findall(pitch_pattern, self._NOTES[key1])
            pitch = "".join(pitch_match)

            if len(self._NOTES[key1]) > 2:
                continue

            self.assertEqual(
                self.converter.get_frequency_from_note_name(
                    ScientificPitchNotation(pitch, octave)
                ),
                self._MIDI_NOTES[key2],
            )
