#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_chord.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import Chord, ChordType, ScientificPitchNotation


class TestChordType(unittest.TestCase):
    """
    A class to test the ChordType enum and its associated methods.

    Attributes
    ----------
    _CHORD_TYPE : dict
        A dictionary of chord types with keys as chord names and values as
        lists of intervals.

    Methods
    -------
    test_chord_name():
        Test that the chord names defined in the ChordType enum match their
        corresponding keys in the _CHORD_TYPE dictionary.

    test_chord_sequence():
        Test that the chord types defined in the ChordType enum match their
        corresponding sequences of intervals.
    """

    _CHORD_TYPE = {
        "MAJOR": [4, 7],
        "MINOR": [3, 7],
        "DIMINISHED": [3, 6],
        "AUGMENTED": [4, 8],
        "MAJOR_SEVENTH": [4, 7, 11],
        "MINOR_SEVENTH": [3, 7, 10],
        "DOMINANT_SEVENTH": [4, 7, 10],
        "HALF_DIMINISHED": [3, 6, 10],
        "SUSPENDED_SECOND": [2, 7],
        "SUSPENDED_FOURTH": [5, 7],
    }

    def test_chord_name(self):
        """
        Test that the chord names defined in the ChordType enum match their
        corresponding keys in the _CHORD_TYPE dictionary.

        This test loops over each key in the _CHORD_TYPE dictionary and
        verifies that the name associated with the same key in the ChordType
        enum is equal to the key itself using the assertEqual() method of the
        unittest module.

        Raises:
        -------
            AssertionError: If any of the comparisons fail.

        """
        for key in self._CHORD_TYPE.keys():
            self.assertEqual(ChordType[key].name, key)

    def test_chord_sequence(self):
        """
        Test that the chord types defined in the ChordType enum match their
        corresponding sequences of intervals.

        This test iterates through each key-value pair in the _CHORD_TYPE
        dictionary and checks that the value, which is a sequence of intervals
        representing the chord type, is equal to the tuple of intervals
        associated with the same key in the ChordType enum.

        Raises an AssertionError if any of the comparisons fail.

        Examples
        --------
        >>> chord = ChordType.MAJOR_TRIAD
        >>> chord.value
        (Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH)

        >>> tonality = Tonality(ScientificPitchNotation('C4'),
        TonalityType.MAJOR)
        >>> sequence = [chord, chord, chord, chord, ChordType.DOMINANT_SEVENTH,
        ChordType.MINOR_SEVENTH, chord]
        >>> chord_sequence = tonality.get_chord_sequence(sequence)
        >>> chord_sequence
        [(Pitch(C4), Pitch(E4), Pitch(G4)), (Pitch(C4), Pitch(E4), Pitch(G4)),
        (Pitch(C4), Pitch(E4), Pitch(G4)), (Pitch(C4), Pitch(E4), Pitch(G4)),
        (Pitch(C4), Pitch(E4), Pitch(G4), Pitch(Bf4)), (Pitch(C4), Pitch(Ef4),
        Pitch(G4), Pitch(Bf4)), (Pitch(C4), Pitch(E4), Pitch(G4))]
        """
        for key, value in self._CHORD_TYPE.items():
            self.assertEqual(ChordType[key].value, tuple(value))


class TestChord(unittest.TestCase):
    """
    A class for testing the `Chord` class.
    """

    _MAJOR_CHORD_NOTES = {
        "C_MAJOR": ["C", "E", "G"],
        "D_MAJOR": ["D", "F#", "A"],
        "E_MAJOR": ["E", "G#", "B"],
        "F_MAJOR": ["F", "A", "C"],
        "G_MAJOR": ["G", "B", "D"],
        "A_MAJOR": ["A", "C#", "E"],
        "B_MAJOR": ["B", "D#", "F#"],
        "C#_MAJOR": ["C#", "F", "G#"],
        "D#_MAJOR": ["D#", "G", "A#"],
        "F#_MAJOR": ["F#", "A#", "C#"],
        "G#_MAJOR": ["G#", "C", "D#"],
        "A#_MAJOR": ["A#", "D", "F"],
        "Db_MAJOR": ["Db", "F", "Ab"],
        "Eb_MAJOR": ["Eb", "G", "Bb"],
        "Gb_MAJOR": ["Gb", "Bb", "Db"],
        "Ab_MAJOR": ["Ab", "C", "Eb"],
        "Bb_MAJOR": ["Bb", "D", "F"],
    }

    _MINOR_CHORD_NOTES = {
        "C_MINOR": ["C", "Eb", "G"],
        "D_MINOR": ["D", "F", "A"],
        "E_MINOR": ["E", "G", "B"],
        "F_MINOR": ["F", "Ab", "C"],
        "G_MINOR": ["G", "Bb", "D"],
        "A_MINOR": ["A", "C", "E"],
        "B_MINOR": ["B", "D", "F#"],
        "C#_MINOR": ["C#", "E", "G#"],
        "D#_MINOR": ["D#", "F#", "A#"],
        "F#_MINOR": ["F#", "A", "C#"],
        "G#_MINOR": ["G#", "B", "D#"],
        "A#_MINOR": ["A#", "C#", "F"],
        "Cb_MINOR": ["Cb", "D", "Gb"],
        "Db_MINOR": ["Db", "E", "Ab"],
        "Eb_MINOR": ["Eb", "Gb", "Bb"],
        "Gb_MINOR": ["Gb", "A", "Db"],
        "Ab_MINOR": ["Ab", "B", "Eb"],
        "Bb_MINOR": ["Bb", "Db", "F"],
    }

    _DIMINISHED_CHORD_NOTES = {
        "C_DIMINISHED": ["C", "Eb", "F#"],
        "D_DIMINISHED": ["D", "F", "G#"],
        "E_DIMINISHED": ["E", "G", "A#"],
        "F_DIMINISHED": ["F", "Ab", "B"],
        "G_DIMINISHED": ["G", "Bb", "C#"],
        "A_DIMINISHED": ["A", "C", "D#"],
        "B_DIMINISHED": ["B", "D", "F"],
        "C#_DIMINISHED": ["C#", "E", "G"],
        "D#_DIMINISHED": ["D#", "F#", "A"],
        "F#_DIMINISHED": ["F#", "A", "C"],
        "G#_DIMINISHED": ["G#", "B", "D"],
        "A#_DIMINISHED": ["A#", "C#", "E"],
        "Cb_DIMINISHED": ["Cb", "D", "F"],
        "Db_DIMINISHED": ["Db", "E", "G"],
        "Eb_DIMINISHED": ["Eb", "Gb", "A"],
        "Gb_DIMINISHED": ["Gb", "A", "C"],
        "Ab_DIMINISHED": ["Ab", "B", "D"],
        "Bb_DIMINISHED": ["Bb", "Db", "E"],
    }

    _AUGMENTED_CHORD_NOTES = {
        "C_AUGMENTED": ["C", "E", "G#"],
        "D_AUGMENTED": ["D", "F#", "A#"],
        "E_AUGMENTED": ["E", "G#", "C"],
        "F_AUGMENTED": ["F", "A", "C#"],
        "G_AUGMENTED": ["G", "B", "D#"],
        "A_AUGMENTED": ["A", "C#", "F"],
        "B_AUGMENTED": ["B", "D#", "G"],
        "C#_AUGMENTED": ["C#", "F", "A"],
        "D#_AUGMENTED": ["D#", "G", "B"],
        "F#_AUGMENTED": ["F#", "A#", "D"],
        "G#_AUGMENTED": ["G#", "C", "E"],
        "A#_AUGMENTED": ["A#", "D", "F#"],
        "Cb_AUGMENTED": ["Cb", "Eb", "G"],
        "Db_AUGMENTED": ["Db", "F", "A"],
        "Eb_AUGMENTED": ["Eb", "G", "B"],
        "Gb_AUGMENTED": ["Gb", "Bb", "D"],
        "Ab_AUGMENTED": ["Ab", "C", "E"],
        "Bb_AUGMENTED": ["Bb", "D", "Gb"],
    }

    _MAJOR_SEVENTH_CHORD_NOTES = {
        "C_MAJOR_SEVENTH": ["C", "E", "G", "B"],
        "D_MAJOR_SEVENTH": ["D", "F#", "A", "C#"],
        "E_MAJOR_SEVENTH": ["E", "G#", "B", "D#"],
        "F_MAJOR_SEVENTH": ["F", "A", "C", "E"],
        "G_MAJOR_SEVENTH": ["G", "B", "D", "F#"],
        "A_MAJOR_SEVENTH": ["A", "C#", "E", "G#"],
        "B_MAJOR_SEVENTH": ["B", "D#", "F#", "A#"],
        "C#_MAJOR_SEVENTH": ["C#", "F", "G#", "C"],
        "D#_MAJOR_SEVENTH": ["D#", "G", "A#", "D"],
        "F#_MAJOR_SEVENTH": ["F#", "A#", "C#", "F"],
        "G#_MAJOR_SEVENTH": ["G#", "C", "D#", "G"],
        "A#_MAJOR_SEVENTH": ["A#", "D", "F", "A"],
        "Cb_MAJOR_SEVENTH": ["Cb", "Eb", "Gb", "Bb"],
        "Db_MAJOR_SEVENTH": ["Db", "F", "Ab", "C"],
        "Eb_MAJOR_SEVENTH": ["Eb", "G", "Bb", "D"],
        "Gb_MAJOR_SEVENTH": ["Gb", "Bb", "Db", "F"],
        "Ab_MAJOR_SEVENTH": ["Ab", "C", "Eb", "G"],
        "Bb_MAJOR_SEVENTH": ["Bb", "D", "F", "A"],
    }

    _MINOR_SEVENTH_CHORD_NOTES = {
        "C_MAJOR_SEVENTH": ["C", "Eb", "G", "Bb"],
        "D_MINOR_SEVENTH": ["D", "F", "A", "C"],
        "E_MINOR_SEVENTH": ["E", "G", "B", "D"],
        "F_MINOR_SEVENTH": ["F", "Ab", "C", "Eb"],
        "G_MINOR_SEVENTH": ["G", "Bb", "D", "F"],
        "A_MINOR_SEVENTH": ["A", "C", "E", "G"],
        "B_MINOR_SEVENTH": ["B", "D", "F#", "A"],
        "C#_MINOR_SEVENTH": ["C#", "E", "G#", "B"],
        "D#_MINOR_SEVENTH": ["D#", "F#", "A#", "C#"],
        "F#_MINOR_SEVENTH": ["F#", "A", "C#", "E"],
        "G#_MINOR_SEVENTH": ["G#", "B", "D#", "F#"],
        "A#_MINOR_SEVENTH": ["A#", "C#", "F", "G#"],
        "Cb_MINOR_SEVENTH": ["Cb", "D", "Gb", "A"],
        "Db_MINOR_SEVENTH": ["Db", "E", "Ab", "B"],
        "Eb_MINOR_SEVENTH": ["Eb", "Gb", "Bb", "Db"],
        "Gb_MINOR_SEVENTH": ["Gb", "A", "Db", "E"],
        "Ab_MINOR_SEVENTH": ["Ab", "B", "Eb", "Gb"],
        "Bb_MINOR_SEVENTH": ["Bb", "Db", "F", "Ab"],
    }

    _DOMINANT_SEVENTH_CHORD_NOTES = {
        "C_DOMINANT_SEVENTH": ["C", "E", "G", "A#"],
        "D_DOMINANT_SEVENTH": ["D", "F#", "A", "C"],
        "E_DOMINANT_SEVENTH": ["E", "G#", "B", "D"],
        "F_DOMINANT_SEVENTH": ["F", "A", "C", "D#"],
        "G_DOMINANT_SEVENTH": ["G", "B", "D", "F"],
        "A_DOMINANT_SEVENTH": ["A", "C#", "E", "G"],
        "B_DOMINANT_SEVENTH": ["B", "D#", "F#", "A"],
        "C#_DOMINANT_SEVENTH": ["C#", "F", "G#", "B"],
        "D#_DOMINANT_SEVENTH": ["D#", "G", "A#", "C#"],
        "F#_DOMINANT_SEVENTH": ["F#", "A#", "C#", "E"],
        "G#_DOMINANT_SEVENTH": ["G#", "C", "D#", "F#"],
        "A#_DOMINANT_SEVENTH": ["A#", "D", "F", "G#"],
        "Cb_DOMINANT_SEVENTH": ["Cb", "Eb", "Gb", "A"],
        "Db_DOMINANT_SEVENTH": ["Db", "F", "Ab", "B"],
        "Eb_DOMINANT_SEVENTH": ["Eb", "G", "Bb", "Db"],
        "Gb_DOMINANT_SEVENTH": ["Gb", "Bb", "Db", "E"],
        "Ab_DOMINANT_SEVENTH": ["Ab", "C", "Eb", "Gb"],
        "Bb_DOMINANT_SEVENTH": ["Bb", "D", "F", "Ab"],
    }

    _HALF_DIMINISHED_CHORD_NOTES = {
        "C_HALF_DIMINISHED": ["C", "Eb", "F#", "Bb"],
        "D_HALF_DIMINISHED": ["D", "F", "G#", "C"],
        "E_HALF_DIMINISHED": ["E", "G", "A#", "D"],
        "F_HALF_DIMINISHED": ["F", "Ab", "B", "Eb"],
        "G_HALF_DIMINISHED": ["G", "Bb", "C#", "F"],
        "A_HALF_DIMINISHED": ["A", "C", "D#", "G"],
        "B_HALF_DIMINISHED": ["B", "D", "F", "A"],
        "C#_HALF_DIMINISHED": ["C#", "E", "G", "B"],
        "D#_HALF_DIMINISHED": ["D#", "F#", "A", "C#"],
        "F#_HALF_DIMINISHED": ["F#", "A", "C", "E"],
        "G#_HALF_DIMINISHED": ["G#", "B", "D", "F#"],
        "A#_HALF_DIMINISHED": ["A#", "C#", "E", "G#"],
        "Cb_HALF_DIMINISHED": ["Cb", "D", "F", "A"],
        "Db_HALF_DIMINISHED": ["Db", "E", "G", "B"],
        "Eb_HALF_DIMINISHED": ["Eb", "Gb", "A", "Db"],
        "Gb_HALF_DIMINISHED": ["Gb", "A", "C", "E"],
        "Ab_HALF_DIMINISHED": ["Ab", "B", "D", "Gb"],
        "Bb_HALF_DIMINISHED": ["Bb", "Db", "E", "Ab"],
    }

    _SUSPENDED_SECOND_CHORD_NOTES = {
        "C_SUSPENDED_SECOND": ["C", "E", "G#"],
        "D_SUSPENDED_SECOND": ["D", "F#", "A#"],
        "E_SUSPENDED_SECOND": ["E", "G#", "C"],
        "F_SUSPENDED_SECOND": ["F", "A", "C#"],
        "G_SUSPENDED_SECOND": ["G", "B", "D#"],
        "A_SUSPENDED_SECOND": ["A", "C#", "F"],
        "B_SUSPENDED_SECOND": ["B", "D#", "G"],
        "C#_SUSPENDED_SECOND": ["C#", "F", "A"],
        "D#_SUSPENDED_SECOND": ["D#", "G", "B"],
        "F#_SUSPENDED_SECOND": ["F#", "A#", "D"],
        "G#_SUSPENDED_SECOND": ["G#", "C", "E"],
        "A#_SUSPENDED_SECOND": ["A#", "D", "F#"],
        "Cb_SUSPENDED_SECOND": ["Cb", "Eb", "G"],
        "Db_SUSPENDED_SECOND": ["Db", "F", "A"],
        "Eb_SUSPENDED_SECOND": ["Eb", "G", "B"],
        "Gb_SUSPENDED_SECOND": ["Gb", "Bb", "D"],
        "Ab_SUSPENDED_SECOND": ["Ab", "C", "E"],
        "Bb_SUSPENDED_SECOND": ["Bb", "C", "F"],
    }

    _SUSPENDED_FOURTH_CHORD_NOTES = {
        "C_SUSPENDED_FOURTH": ["C", "F", "G"],
        "D_SUSPENDED_FOURTH": ["D", "G", "A"],
        "E_SUSPENDED_FOURTH": ["E", "A", "B"],
        "F_SUSPENDED_FOURTH": ["F", "A#", "C"],
        "G_SUSPENDED_FOURTH": ["G", "C", "D"],
        "A_SUSPENDED_FOURTH": ["A", "D", "E"],
        "B_SUSPENDED_FOURTH": ["B", "E", "F#"],
        "C#_SUSPENDED_FOURTH": ["C#", "F#", "G#"],
        "D#_SUSPENDED_FOURTH": ["D#", "G#", "A#"],
        "F#_SUSPENDED_FOURTH": ["F#", "B", "C#"],
        "G#_SUSPENDED_FOURTH": ["G#", "C#", "D#"],
        "A#_SUSPENDED_FOURTH": ["A#", "D#", "F"],
        "Cb_SUSPENDED_FOURTH": ["Cb", "E", "Gb"],
        "Db_SUSPENDED_FOURTH": ["Db", "Gb", "Ab"],
        "Eb_SUSPENDED_FOURTH": ["Eb", "Ab", "Bb"],
        "Gb_SUSPENDED_FOURTH": ["Gb", "B", "Db"],
        "Ab_SUSPENDED_FOURTH": ["Ab", "Db", "Eb"],
        "Bb_SUSPENDED_FOURTH": ["Bb", "Eb", "F"],
    }

    def test_get_major_chord_notes(self):
        """
        Test that the `get_chord_notes()` method returns the correct notes for
        major chords.

        This test iterates through each key-value pair in the
        `_MAJOR_CHORD_NOTES` dictionary, where the keys are in the format
        "<root-note>_MAJOR" in scientific pitch notation, and the values are
        the expected notes in the chord. For each pair, a major chord is
        created with the root note specified by the key using the `Chord` class
        and the `MAJOR` chord type. The `get_chord_notes()` method is then
        called on this chord, and the resulting notes are compared with the
        expected value in the dictionary.

        Raises:
        -------
            AssertionError: If any of the comparisons fail.
        """
        for key, value in self._MAJOR_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4), ChordType.MAJOR
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_minor_chord_notes(self):
        """
        Test that the get_chord_notes() method returns the correct notes for
        minor chords.

        This test loops over each key-value pair in the _MINOR_CHORD_NOTES
        dictionary and creates a minor chord with the root note specified by
        the key (in Scientific Pitch Notation), and checks that the notes
        returned by the get_chord_notes() method match the value in the
        dictionary.

        Raises:
        -------
        AssertionError: If any of the comparisons fail.

        Examples
        --------
        >>> chord = Chord(ScientificPitchNotation('C4'), ChordType.MINOR_TRIAD)
        >>> chord.get_chord_notes()
        [Pitch(C4), Pitch(Ef4), Pitch(G4)]

        """
        for key, value in self._MINOR_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4), ChordType.MINOR
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_disminished_chord_notes(self):
        """
        Test that the `get_chord_notes()` method returns the correct notes for
        diminished chords.

        This test iterates over each key-value pair in the
        `_DIMINISHED_CHORD_NOTES` dictionary and creates a diminished chord
        with the root note specified by the key (in scientific pitch notation).
        It then checks that the notes returned by the `get_chord_notes()`
        method match the value in the dictionary using the `assertEqual()`
        method from the unittest module.

        Raises:
        -------
            AssertionError: If any of the comparisons fail.
        """
        for key, value in self._DIMINISHED_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.DIMINISHED,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_augmented_chord_notes(self):
        """
        Test that the get_chord_notes() method returns the correct notes for
        augmented chords.

        This method iterates over each key-value pair in the
        _AUGMENTED_CHORD_NOTES dictionary, creates an augmented chord with the
        root note specified by the key (in scientific pitch notation), and
        verifies that the notes returned by the get_chord_notes() method match
        the value in the dictionary.

        Raises:
        AssertionError: If any of the comparisons fail.

        """
        for key, value in self._AUGMENTED_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.AUGMENTED,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_major_seventh_chord_notes(self):
        """
        Test that the get_chord_notes() method returns the correct notes for
        major seventh chords.

        This method iterates over each key-value pair in the
        _MAJOR_SEVENTH_CHORD_NOTES dictionary, creates a major seventh chord
        with the root note specified by the key (in scientific pitch notation),
        and verifies that the notes returned by the get_chord_notes() method
        match the value in the dictionary.

        Raises:
        AssertionError: If any of the comparisons fail.

        """
        for key, value in self._MAJOR_SEVENTH_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.MAJOR_SEVENTH,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_minor_seventh_chord_notes(self):
        """
        Test that the get_chord_notes() method returns the correct notes for
        minor seventh chords.

        This method iterates over each key-value pair in the
        _MINOR_SEVENTH_CHORD_NOTES dictionary, creates a minor seventh chord
        with the root note specified by the key (in scientific pitch notation),
        and verifies that the notes returned by the get_chord_notes() method
        match the value in the dictionary.

        Raises:
        AssertionError: If any of the comparisons fail.

        """
        for key, value in self._MINOR_SEVENTH_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.MINOR_SEVENTH,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_dominant_seventh_chord_notes(self):
        """
        Test that the get_chord_notes() method returns the correct notes for
        dominant seventh chords.

        This method iterates over each key-value pair in the
        _DOMINANT_SEVENTH_CHORD_NOTES dictionary, creates a dominant seventh
        chord with the root note specified by the key (in scientific pitch
        notation), and verifies that the notes returned by the
        get_chord_notes() method match the value in the dictionary.

        Raises:
        AssertionError: If any of the comparisons fail.

        """
        for key, value in self._DOMINANT_SEVENTH_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.DOMINANT_SEVENTH,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_half_diminished_chord_notes(self):
        """
        Test the functionality of `get_chord_notes()` method for
        half-diminished chords.

        This test loops over each key-value pair in the
        `_HALF_DIMINISHED_CHORD_NOTES` dictionary, creates a half-diminished
        chord with the root note specified by the key (in scientific pitch
        notation) and asserts that the notes returned by the
        `get_chord_notes()` method match the expected value.

        Raises:
        -------
        AssertionError:
            If any of the comparisons fail.

        """
        for key, value in self._HALF_DIMINISHED_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.HALF_DIMINISHED,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_suspended_second_chord_notes(self):
        """
        Test the functionality of `get_chord_notes()` method for suspended
        second chords.

        This test loops over each key-value pair in the
        `_SUSPENDED_SECOND_CHORD_NOTES` dictionary, creates a suspended second
        chord with the root note specified by the key (in scientific pitch
        notation) and asserts that the notes returned by the
        `get_chord_notes()` method match the expected value.

        Raises:
        -------
        AssertionError:
            If any of the comparisons fail.

        """
        for key, value in self._SUSPENDED_SECOND_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.SUSPENDED_SECOND,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)

    def test_get_suspended_fourth_chord_notes(self):
        """
        Test the functionality of `get_chord_notes()` method for suspended
        fourth chords.

        This test loops over each key-value pair in the
        `_SUSPENDED_FOURTH_CHORD_NOTES` dictionary,
        creates a suspended fourth chord with the root note specified by the
        key (in scientific pitch notation) and asserts that the notes returned
        by the `get_chord_notes()` method match the expected value.

        Raises:
        -------
        AssertionError:
            If any of the comparisons fail.
        """
        for key, value in self._SUSPENDED_FOURTH_CHORD_NOTES.items():
            chord_notes = Chord(
                ScientificPitchNotation(key.split("_")[0], 4),
                ChordType.SUSPENDED_FOURTH,
            ).get_chord_notes()
        self.assertEqual(chord_notes, value)
