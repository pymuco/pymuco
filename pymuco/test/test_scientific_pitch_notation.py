#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_scientific_pitch_notation.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import unittest

from pymuco import (
    ACCIDENTALS,
    DEFAULT_OCTAVE,
    NOTE_NAMES,
    C,
    ScientificPitchNotation
)


class TestValidPitch(unittest.TestCase):
    """
    Unit test for the is_valid_pitch and invalid_pitch methods of the
    ScientificPitchNotation class.

    The ScientificPitchNotation class is a class for representing musical
    pitches in scientific pitch notation. This test suite checks if the
    is_valid_pitch and invalid_pitch methods of the ScientificPitchNotation
    class behave as expected.

    Tested class
    ------------
    ScientificPitchNotation

    Test methods
    ------------
    1. test_valid_pitch: checks if all valid pitches are recognized as valid by
    the is_valid_pitch method.
    2. test_invalid_pitch: checks if the invalid_pitch method raises a
    ValueError when an invalid pitch is given as input.

    Test procedure
    ---------------
    1. Create an instance of ScientificPitchNotation.
    2. Call the method being tested with the input.
    3. Verify that the output is correct.

    Returns
    -------
    None
        This function does not return anything.

    See Also
    --------
    is_valid_pitch: Method of ScientificPitchNotation class that checks if a
    pitch is valid. invalid_pitch: Method of ScientificPitchNotation class that
    raises a ValueError if a pitch is invalid.

    Notes
    -----
    In scientific pitch notation, the pitch of a note is represented by a
    letter from A to G, optionally followed by a number indicating the octave
    (e.g., C4 is middle C).

    Examples
    --------
    To run the tests in this class, create an instance of TestValidPitch and
    call the `run` method.

    >>> test_valid_pitch = TestValidPitch()
    >>> test_valid_pitch.run()
    """

    def test_valid_pitch(self):
        """
        Test the `is_valid_pitch` method of the `ScientificPitchNotation`
        class.

        Tests if all valid pitches are recognized as valid by the
        `is_valid_pitch` method of the `ScientificPitchNotation` class. Each
        pitch is created using a combination of note name and accidental from
        the `NOTE_NAMES` and `ACCIDENTALS` constants, and the `DEFAULT_OCTAVE`.
        The `is_valid_pitch` method is called with the pitch, and the result is
        compared with the expected result (True) using the `assertEqual`
        method.

        Parameters:
        -----------
        self : object
            An instance of the `ScientificPitchNotation` test class.

        Returns:
        --------
        None.

        Test method:
        test_valid_pitch(self)

        Tested class:
        `ScientificPitchNotation`

        Tested method:
        `is_valid_pitch`

        Test procedure:
        ---------------
        For each note name and accidental combination in `NOTE_NAMES` and
        `ACCIDENTALS` constants, create a pitch using
        `ScientificPitchNotation`. Call the `is_valid_pitch` method with the
        created pitch and compare the result with the expected result (True)
        using the `assertEqual` method.

        Expected behavior:
        ------------------
        The `is_valid_pitch` method of the `ScientificPitchNotation` class
        should recognize all valid pitches as valid.

        See Also:
        ---------
        `ScientificPitchNotation`
        """
        for note in NOTE_NAMES:
            for accidental in ACCIDENTALS:
                spn = ScientificPitchNotation(
                    note + accidental, DEFAULT_OCTAVE
                )
                result = spn.is_valid_pitch(spn.pitch)
                self.assertEqual(
                    result, True, f"{spn.pitch} should be a valid pitch"
                )

    def test_invalid_pitch(self):
        """
        Test the invalid_pitch method of the ScientificPitchNotation class.

        This test verifies that the invalid_pitch method of the
        ScientificPitchNotation class raises a ValueError when an invalid pitch
        is given as input.

        Parameters
        ----------
        self : unittest.TestCase
            An instance of the unit test case.

        Raises
        ------
        ValueError
            If an invalid pitch is given as input.

        Returns
        -------
        None
            This function does not return anything.

        Test Method
        -----------
        test_invalid_pitch(self)

        Tested Class
        ------------
        ScientificPitchNotation

        Tested Method
        --------------
        invalid_pitch

        Test Procedure
        ---------------
        1. Call the invalid_pitch method of the ScientificPitchNotation class
        with invalid pitches.
        2. Verify that a ValueError is raised.
        3. Compare the raised exception with the expected exception using the
        assertRaises method.

        Expected Behavior
        ------------------
        The invalid_pitch method of the ScientificPitchNotation class should
        raise a ValueError when an invalid pitch is given as input.
        """
        for note in range(ord("H"), ord("Z") + 1):
            with self.assertRaises(ValueError) as context:
                ScientificPitchNotation(str(chr(note)), 4)
            self.assertEqual(str(context.exception), "Invalid pitch.")


class TestValidOctave(unittest.TestCase):
    """
    A unittest class for the ScientificPitchNotation class is_valid_octave
    method.

    Tests:
    - test_valid_octave: checks if all valid octave values ranging from 0 to 10
    are recognized as valid by the is_valid_octave method of the
    ScientificPitchNotation class.
    - test_invalid_negative_octave: checks if the invalid_negative_octave
    method of the ScientificPitchNotation class raises a ValueError when a
    negative octave value is given as input.
    - test_invalid_octave: checks if the invalid_octave method of the
    ScientificPitchNotation class raises a ValueError when an octave value
    outside the range [0, 10] is given as input.

    Methods:
    1. test_valid_octave(self)
    2. test_invalid_negative_octave(self)
    3. test_invalid_octave(self)

    Tested class:
    ScientificPitchNotation

    """

    def test_valid_octave(self):
        """
        Unit test for the is_valid_octave method of the ScientificPitchNotation
        class.

        This test checks if all valid octaves are recognized as valid by the
        is_valid_octave method of the ScientificPitchNotation class. Octaves
        are created by calling the ScientificPitchNotation class with a note
        name (C) and the octave value ranging from 0 to 10. The is_valid_octave
        method is called with the octave value, and the result is compared with
        the expected result (True) using the assertTrue method.

        Test method
        -----------
        test_valid_octave(self)

        Tested class
        ------------
        ScientificPitchNotation

        Tested method
        -------------
        is_valid_octave: Method of ScientificPitchNotation class that checks if
        an octave value is valid.

        Test procedure
        ---------------
        1. Create an instance of ScientificPitchNotation with note name 'C' and
        octave value ranging from 0 to 10.
        2. Call the is_valid_octave method with the octave value.
        3. Verify that the output is True using the assertTrue method.

        Returns
        -------
        None
            This function does not return anything.

        See Also
        --------
        is_valid_octave: Method of ScientificPitchNotation class that checks if
        an octave value is valid.

        Notes
        -----
        In scientific pitch notation, the pitch of a note is represented by a
        letter from A to G, optionally followed by a number indicating the
        octave (e.g., C4 is middle C).

        Examples
        --------
        To run the tests in this method, create an instance of the
        TestValidOctave class and call the `run` method.

        >>> test_valid_octave = TestValidOctave()
        >>> test_valid_octave.run()
        """
        for octave in range(0, 11):
            spn = ScientificPitchNotation(C, octave)
            self.assertTrue(spn.is_valid_octave(spn.octave) == True)

    def test_invalid_negative_octave(self):
        """
        Test the invalid_negative_octave method of the ScientificPitchNotation
        class.

        This method checks if the invalid_negative_octave method of the
        ScientificPitchNotation class raises a ValueError when a negative
        octave value is given as input. The method is called with a negative
        octave, and the raised exception is compared with the expected
        exception using the assertRaises method.

        Parameters
        ----------
        self : unittest.TestCase
            The unittest class.

        Returns
        -------
        None

        Test method:
        test_invalid_negative_octave(self)

        Tested class:
        ScientificPitchNotation

        Tested method:
        invalid_negative_octave

        Test procedure:
        Call the invalid_negative_octave method of the ScientificPitchNotation
        class with a negative octave. Check if a ValueError is raised, and
        compare the raised exception with the expected exception using the
        assertRaises method.

        Expected behavior:
        The invalid_negative_octave method of the ScientificPitchNotation class
        should raise a ValueError when a negative octave value is given as
        input.
        """
        with self.assertRaises(ValueError) as context:
            ScientificPitchNotation(C, -1)
        self.assertEqual(str(context.exception), "Invalid octave.")

    def test_invalid_octave(self):
        """
        Unit test for the invalid_octave method of the ScientificPitchNotation
        class.

        This test checks if the invalid_octave method of the
        ScientificPitchNotation class raises a ValueError when an invalid
        octave is given as input. The method is called with an octave that is
        outside the range [0, 10], and the raised exception is compared with
        the expected exception using the assertRaises method.

        Parameters:
        -----------
        self : unittest.TestCase
            The test case instance

        Returns:
        -------
        None

        Test method:
        test_invalid_octave

        Tested class:
        ScientificPitchNotation

        Tested method:
        invalid_octave

        Test procedure:
        Call the invalid_octave method of the ScientificPitchNotation class
        with an octave value that is outside the range [0, 10]. Check if a
        ValueError is raised, and compare the raised exception with the
        expected exception using the assertRaises method.

        Expected behavior:
        The invalid_octave method of the ScientificPitchNotation class should
        raise a ValueError when an invalid octave is given as input.
        """
        with self.assertRaises(ValueError) as context:
            ScientificPitchNotation(C, 11)
        self.assertEqual(str(context.exception), "Invalid octave.")


# python -m unittest discover .
# python -m unittest discover <directory>

#  ~/code/pymuco/pymuco  python3 -m unittest discover test
