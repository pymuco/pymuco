#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_interval.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import (
    Interval,
    IntervalCalculator,
    IntervalName,
    DEFAULT_OCTAVE,
    C,
    G,
    ScientificPitchNotation
)


class TestIntervalName(unittest.TestCase):
    """
    A subclass of unittest.TestCase that tests the correctness of the
    IntervalName class.

    Attributes
    ----------
    _INTERVAL_NAME: dict
        A dictionary that maps interval names to their values.

    Methods
    -------
    test_interval_name(self):
        Test the correctness of the IntervalName class by comparing its name
        attribute to the keys in the _INTERVAL_NAME dictionary. The function
        iterates through each key-value pair in the _INTERVAL_NAME dictionary
        and asserts that the name attribute of a new IntervalName object
        created with the corresponding value is equal to the key.

        Returns
        -------
        None
    """

    _INTERVAL_NAME = {
        "UNISON": 0,
        "MINOR_SECOND": 1,
        "MAJOR_SECOND": 2,
        "MINOR_THIRD": 3,
        "MAJOR_THIRD": 4,
        "PERFECT_FOURTH": 5,
        "TRITONE": 6,
        "PERFECT_FIFTH": 7,
        "MINOR_SIXTH": 8,
        "MAJOR_SIXTH": 9,
        "MINOR_SEVENTH": 10,
        "MAJOR_SEVENTH": 11,
        "OCTAVE": 12,
        "MINOR_NINTH": 13,
        "MAJOR_NINTH": 14,
        "MINOR_TENTH": 15,
        "MAJOR_TENTH": 16,
        "PERFECT_ELEVENTH": 17,
        "DIMINISHED_TWELFTH": 18,
        "AUGMENTED_ELEVENTH": 19,
        "PERFECT_TWELFTH": 20,
        "MINOR_THIRTEENTH": 21,
        "MAJOR_THIRTEENTH": 22,
        "MINOR_FOURTEENTH": 23,
        "MAJOR_FOURTEENTH": 24,
        "DOUBLE_OCTAVE": 25,
    }

    def test_interval_name(self):
        """
        Test the correctness of the IntervalName class.

        The function iterates through each key-value pair in the
        _INTERVAL_NAME dictionary and asserts that the name attribute of a new
        IntervalName object created with the corresponding value is equal to
        the key.

        Returns
        -------
        None
        """
        for key, value in self._INTERVAL_NAME.items():
            self.assertEqual(IntervalName(value).name, key)


class TestInterval(unittest.TestCase):
    """
    Test case for the Interval class.

    Tests the correctness of its methods get_interval_name(),
    get_interval_direction(), and get_interval_inversion().

    Methods
    -------
    test_get_interval_name()
        Tests the correctness of the get_interval_name() method of the Interval
        class.
    test_get_ascending_interval_direction()
        Tests the correctness of the get_interval_direction() method of the
        Interval class
        on an ascending interval.
    test_get_descending_interval_direction()
        Tests the correctness of the get_interval_direction() method of the
        Interval class
        on a descending interval.
    test_get_interval_inversion()
        Tests the correctness of the get_interval_inversion() method of the
        Interval class.
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

    def test_get_interval_name(self):
        """
        Test the correctness of the get_interval_name() method of the Interval
        class.

        The function creates two nested for-loops that iterate over all the
        notes in the _NOTE_MAPPING dictionary, creating a pitch object for each
        note at the default octave, and then using these pitch objects to
        create an interval object. The function then calls the
        get_interval_name() method of the Interval class on this interval
        object, which returns an IntervalName object. The function then
        compares the name attribute of this IntervalName object to the interval
        name determined from the _semitones attribute of the interval object
        using the IntervalName class.

        Returns
        -------
        None
        """
        for note1 in self._NOTE_MAPPING:
            for note2 in self._NOTE_MAPPING:
                pitch1 = ScientificPitchNotation(note1, DEFAULT_OCTAVE)
                pitch2 = ScientificPitchNotation(note2, DEFAULT_OCTAVE)
                interval = Interval(pitch1, pitch2)
                self.assertEqual(
                    Interval(pitch1, pitch2).get_interval_name(),
                    IntervalName(interval._semitones).name,
                )

    def test_get_ascending_interval_direction(self):
        """
        Test the correctness of the get_interval_direction() method of the
        Interval class.

        The function creates an interval object with a start pitch of C and an
        end pitch of G, both at the default octave. The function then calls the
        get_interval_direction() method of the Interval class on this interval
        object and compares the output to True, which asserts that the interval
        direction is ascending.

        Returns
        -------
        None
        """
        self.assertTrue(
            Interval(
                ScientificPitchNotation(C, DEFAULT_OCTAVE),
                ScientificPitchNotation(G, DEFAULT_OCTAVE),
            ).get_interval_direction(),
            True,
        )

    def test_get_descending_interval_direction(self):
        """
        Test the correctness of the get_interval_direction() method of the
        Interval class.

        The function creates an interval object with a start pitch of G and an
        end pitch of C, both at the default octave. The function then calls the
        get_interval_direction() method of the Interval class on this interval
        object and compares the output to False, which asserts that the
        interval direction is descending.

        Returns
        -------
        None
        """
        self.assertFalse(
            Interval(
                ScientificPitchNotation(G, DEFAULT_OCTAVE),
                ScientificPitchNotation(C, DEFAULT_OCTAVE),
            ).get_interval_direction(),
            False,
        )

    def test_get_interval_inversion(self):
        """
        This unit test function tests the correctness of the
        get_interval_inversion() method of the Interval class.

        It does this by creating two nested for-loops that iterate over all
        the notes in the _NOTE_MAPPING dictionary, creating a pitch object for
        each note at the default octave, and then using these pitch objects to
        create an interval object.

        The function then calls the get_interval_inversion() method of the
        Interval class on this interval object, which returns an Interval
        object representing the inversion of the original interval.

        The function then compares the name attribute of this new Interval
        object to the interval name determined from the _semitones attribute of
        the original interval object using the IntervalName class.

        Returns:
        None
        """
        for note1 in self._NOTE_MAPPING:
            for note2 in self._NOTE_MAPPING:
                pitch1 = ScientificPitchNotation(note1, DEFAULT_OCTAVE)
                pitch2 = ScientificPitchNotation(note2, DEFAULT_OCTAVE)
                interval = Interval(pitch1, pitch2)
                self.assertEqual(
                    interval.get_interval_inversion(),
                    IntervalName(interval._get_semitones()).name.replace(
                        "_", " "
                    ),
                )


class TestIntervalCalculator(unittest.TestCase):
    """
    Test case for the IntervalCalculator class.

    Methods:
    -------
    test_calculate_ascending_interval():
        A unit test that checks if the calculate_ascending_interval method in
        the IntervalCalculator class is correctly calculating the ascending
        interval between two scientific pitch notations (SPN).
    test_calculate_descending_interval():
        A unit test that checks if the calculate_descending_interval method in
        the IntervalCalculator class is correctly calculating the descending
        interval between two scientific pitch notations (SPN).

    The tests check all possible intervals within an octave for each note in a
    note mapping. The expected outcome is that the calculated intervals have
    the correct number of semitones.
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

    def test_calculate_ascending_interval(self):
        """
        Test the `calculate_ascending_interval()` method of the
        `IntervalCalculator` class to ensure that it accurately calculates the
        ascending interval between two `ScientificPitchNotation` instances for
        all possible intervals within an octave.

        The method creates an instance of the `ScientificPitchNotation` class
        and an instance of the `IntervalCalculator` class. It then calls the
        `calculate_ascending_interval()` method with an `IntervalName` and the
        `ScientificPitchNotation` instance as arguments to get the calculated
        interval note.

        It creates a new `ScientificPitchNotation` instance for the interval
        note, calculates the direction of the interval using the `Interval`
        class, and adjusts the octave if the interval is descending. It then
        creates an instance of the `Interval` class with the original
        `ScientificPitchNotation` instance and the interval
        `ScientificPitchNotation` instance, calculates the semitones between
        them, and checks if the calculated semitones equal the expected
        semitones using the `assertEqual()` method of the `unittest.TestCase`
        class.

        Parameters:
        -----------
        self: TestInterval
            An instance of the `TestInterval` class.

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError
            If the calculated semitones do not equal the expected semitones for
            any interval.
        """

        for note in self._NOTE_MAPPING:
            spn = ScientificPitchNotation(note, DEFAULT_OCTAVE)
            ic = IntervalCalculator()
            for i in range(0, 12):
                interval_note = ic.calculate_ascending_interval(
                    IntervalName(i), spn
                )
                interval_note_spn = ScientificPitchNotation(
                    interval_note, DEFAULT_OCTAVE
                )
                interval_direction = Interval(
                    spn, interval_note_spn
                ).get_interval_direction()
                if interval_direction is False:
                    interval_note_spn.octave += 1
                interval = Interval(spn, interval_note_spn)
                interval._get_semitones()
                self.assertEqual(interval._get_semitones(), i)

    def test_calculate_descending_interval(self):
        """
        A unit test that checks if the `calculate_descending_interval` method
        in the `IntervalCalculator` class is correctly calculating the
        descending interval between two scientific pitch notations (SPN). The
        test covers all possible intervals within an octave (12 semitones) for
        each note in a note mapping.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This test creates an instance of the `ScientificPitchNotation` class
        and an instance of the `IntervalCalculator` class. It then calls the
        `calculate_descending_interval` method with an `IntervalName` and the
        `ScientificPitchNotation` instance as arguments to get the calculated
        interval note.

        It creates a new `ScientificPitchNotation` instance for the interval
        note and creates an instance of the `Interval` class with the original
        SPN and the interval SPN. It calculates the semitones between them and
        checks if the calculated semitones equal the expected semitones using
        the `assertEqual` method of the `unittest.TestCase` class.

        If the calculated semitones do not equal the expected semitones, the
        test assumes that the interval is ascending rather than descending and
        adjusts the octave of the interval SPN accordingly.

        The purpose of this test is to ensure that the `IntervalCalculator`
        class is accurately calculating descending intervals between SPNs, and
        that the calculated intervals have the correct number of semitones.
        """
        for note in self._NOTE_MAPPING:
            spn = ScientificPitchNotation(note, DEFAULT_OCTAVE)
            ic = IntervalCalculator()
            for i in range(0, 12):
                interval_note = ic.calculate_descending_interval(
                    IntervalName(i), spn
                )
                interval_note_spn = ScientificPitchNotation(
                    interval_note, DEFAULT_OCTAVE
                )
                interval = Interval(spn, interval_note_spn)
                interval._get_semitones()
                if interval._get_semitones() != i:
                    interval_note_spn.octave -= 1
                self.assertEqual(interval._get_semitones(), i)
