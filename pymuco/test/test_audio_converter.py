#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         test_audio_converter.py
# Purpose:      Pymuco Unit Tests
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import os
import unittest
import wave
from unittest.mock import MagicMock

from pymuco import AudioConverter, ScientificPitchNotation


class TestAudioConverter(unittest.TestCase):
    """
    Test case for the AudioConverter class.

    This test case contains four test methods that test the
    `_validate_file_path()` method of the AudioConverter class. Each test
    method simulates a different scenario in which the file path is either
    valid or invalid and asserts that the `_validate_file_path()` method
    behaves correctly in each case.

    Methods:
    ----------
    setUp(self):
        Method called to prepare the test fixture. This method creates an
        instance of the AudioConverter class.

    test_validate_file_path_with_valid_path(self):
        Test that the `validate_file_path()` method of the AudioConverter class
        correctly validates a file path that exists and has the necessary
        permissions. This test mocks the `os.path.exists()` and `os.access()`
        methods to return True, indicating that the file path is valid.

    test_validate_file_path_with_nonexistent_path(self):
        Test that the `_validate_file_path()` method returns False if the
        specified file path does not exist. The test mocks the
        `os.path.exists()` method to always return False for the duration of
        the test and calls the `_validate_file_path()` method with a mock file
        path. The test uses the `assertRaises()` method of the unittest module
        to check that a `ValueError` is raised.

    test_validate_file_path_with_unreadable_path(self):
        Test that the `_validate_file_path()` method of the AudioConverter
        class raises a `ValueError` if the file path is not readable. The test
        mocks the `os.path.exists()` and `os.access()` methods to simulate a
        readable directory with an unreadable file. It then calls the
        `_validate_file_path()` method of an instance of AudioConverter. Since
        the file is unreadable, the method should raise a `ValueError`. The
        `assertRaises()` method of the unittest module is used to check that
        the `ValueError` is raised.

    test_validate_file_path_with_unwritable_path(self):
        Test that the `_validate_file_path()` method of the AudioConverter
        class raises a `ValueError` when the specified file path is not
        writable. The method sets up a mock object for `os.path.exists()`
        which returns True and for `os.access()` which returns True and False.
        This simulates a file path that exists but is not writable. The test
        asserts that a `ValueError` is raised when the `_validate_file_path()`
        method is called in this situation.

    The test case inherits from `unittest.TestCase`.
    """

    def setUp(self):
        """
        Set up the unit test fixture by creating an instance of the
        AudioConverter class.
        """
        self.instance = AudioConverter()

    def test_validate_file_path_with_valid_path(self):
        """
        Test that the validate_file_path() method of the AudioConverter class
        correctly validates a file path that exists and has the necessary
        permissions.

        This test mocks the os.path.exists() and os.access() methods to return
        True, indicating that the file path is valid.

        The test sets the file path of the AudioConverter instance to a valid
        path and calls the validate_file_path() method. It verifies that the
        method returns None, indicating that the file path is valid, using the
        assertIsNone() method of the unittest module.

        Raises:
        -------
        AssertionError: If the validate_file_path() method returns a non-None
        value or raises an unexpected exception.
        """
        os.path.exists = MagicMock(return_value=True)
        os.access = MagicMock(return_value=True)
        self.instance._file_path = "/path/to/output"
        self.assertIsNone(self.instance._validate_file_path())

    def test_validate_file_path_with_nonexistent_path(self):
        """
        Test whether the `validate_file_path()` method of the `AudioConverter`
        class returns `False` when the specified file path does not exist.

        The test creates a mock file path and mocks the `os.path.exists()`
        method to always return `False`. It then calls the
        `validate_file_path()` method with the mock file path and asserts that
        the method returns `False` using the `assertFalse()` method of the
        `unittest` module.

        Raises:
        -------
        ValueError:
            If the file path exists when it should not.

        """
        os.path.exists = MagicMock(return_value=False)
        with self.assertRaises(ValueError):
            self.instance._validate_file_path()

    def test_validate_file_path_with_unreadable_path(self):
        """
        Test that the `_validate_file_path()` method of the `AudioConverter`
        class raises a `ValueError` if the specified file path is not readable.

        This test mocks the `os.path.exists()` and `os.access()` methods to
        simulate a readable directory with an unreadable file. It then calls
        the `_validate_file_path()` method of an instance of `AudioConverter`.
        Since the file is unreadable, the method should raise a `ValueError`.
        The `assertRaises()` method of the `unittest` module is used to check
        that the `ValueError` is raised.

        Raises:
        -------
            ValueError: If the file path is not readable.
        """
        os.path.exists = MagicMock(return_value=True)
        os.access = MagicMock(side_effect=[False, True])
        with self.assertRaises(ValueError):
            self.instance._validate_file_path()

    def test_validate_file_path_with_unwritable_path(self):
        """
        Test that the _validate_file_path() method of the AudioConverter class
        raises a ValueError when the specified file path is not writable.

        The test sets up a mock object for os.path.exists() which returns True
        and for os.access() which returns True and False in sequence. This
        simulates a file path that exists but is not writable.
        The _validate_file_path() method of an instance of AudioConverter is
        then called. Since the file is not writable, the method should raise a
        ValueError. The assertRaises() method of the unittest module is used to
        check that the ValueError is raised.

        Raises:
        -------
            ValueError: If the specified file path is not writable.
        """
        os.path.exists = MagicMock(return_value=True)
        os.access = MagicMock(side_effect=[True, False])
        with self.assertRaises(ValueError):
            self.instance._validate_file_path()


class TestGenerateSamples(unittest.TestCase):
    """
    This class contains unit tests for the _generate_samples() method of the
    AudioConverter class using the unittest.TestCase framework.

    Methods:
    -------

    setUp():
    Method called to prepare the test fixture. This creates an instance of the
    `AudioConverter` class used in the individual test methods to test its
    functionality.

    test_sample_list_length():
        Verify that the `_generate_samples()` method generates a list of
        samples of the expected length. This test calls the
        `_generate_samples()` method with a frequency of 440 Hz and a duration
        of 1 second. The expected length of the resulting list of samples is
        44100, which corresponds to the number of samples in 1 second of audio
        with a sample rate of 44100 Hz. This test uses the `assertEqual()`
        method of the `unittest` module to verify that the length of the actual
        list of samples is equal to the expected length.

    test_sample_list_type():
        Verify that the `_generate_samples()` method of the `AudioConverter`
        class returns a list object for the `_sample_list` attribute after
        being called with valid parameters. This test ensures that the data
        type of the returned object is correct to ensure proper functionality
        in future use of this attribute.

    test_sample_list_values():
        Verify the values of the sample list generated by the
        `_generate_samples()` method. This unit test generates a sample list
        with a specified frequency and duration, then checks that the maximum
        and minimum values of the list are within the range of [-32768, 32767].
        This is to ensure that the generated audio samples are within the range
        of a 16-bit PCM audio format, which is commonly used for digital audio.

    Raises:
    -------

    AssertionError: If the maximum or minimum value of the sample list is
    outside the expected range.

    Note:
    -------

    The `_generate_samples()` method is responsible for generating a list of
    audio samples based on the given frequency and duration.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.

        This method creates an instance of the AudioConverter class that is
        used in the individual test methods to test its functionality.
        """
        self.instance = AudioConverter()

    def test_sample_list_length(self):
        """
        Test case for the "_generate_samples()" method of the AudioConverter
        class.

        This unit test verifies that the method generates a list of samples of
        the expected length. The "_generate_samples()" method is called with a
        frequency of 440 Hz and a duration of 1 second. The expected length of
        the resulting list of samples is 44100, which corresponds to the number
        of samples in 1 second of audio with a sample rate of 44100 Hz.

        The test uses the assertEqual() method of the unittest module to verify
        that the length of the actual list of samples is equal to the expected
        length.
        """
        self.instance._generate_samples(440, 1.0)
        self.assertEqual(len(self.instance._sample_list), 44100)

    def test_sample_list_type(self):
        """
        Test that the "_generate_samples" method of the "AudioConverter" class
        returns a list object for the "_sample_list" attribute after being
        called with valid parameters. This test verifies that the data type of
        the returned object is correct to ensure proper functionality in future
        use of this attribute.
        """
        self.instance._generate_samples(440, 1.0)
        self.assertIsInstance(self.instance._sample_list, list)

    def test_sample_list_values(self):
        """
        Verify values of the sample list generated by `_generate_samples()`
        method.

        This unit test generates a sample list with a specified frequency and
        duration, then checks that the maximum and minimum values of the list
        are within the range of [-32768, 32767]. This is to ensure that the
        generated audio samples are within the range of a 16-bit PCM audio
        format, which is commonly used for digital audio.

        Raises:
        -------
            AssertionError: If the maximum or minimum value of the sample list
            is outside the expected range.
        """
        self.instance._generate_samples(440, 1.0)
        max_value = max(self.instance._sample_list)
        min_value = min(self.instance._sample_list)
        self.assertLessEqual(max_value, 32767)
        self.assertGreaterEqual(min_value, -32768)


class TestWriteToFile(unittest.TestCase):
    """
    This class contains unit tests for the "_write_to_file()" method of the
    AudioConverter class.

    Attributes:
    -----------
    Inherits from:
        unittest.TestCase : A unit testing framework.

    Methods:
    --------
    setUp(self):
        This method initializes an instance of the AudioConverter class with a
        sample list. It is called before each test method.

    test_file_created(self):
        Test that the _write_to_file() method of the AudioConverter class
        creates a file with the specified name in the specified directory.
        The test creates an instance of AudioConverter, calls the
        _write_to_file() method, and checks if the file exists
        by joining the file name and directory using os.path.join() and
        checking if the resulting path is a file using os.path.isfile().
        The test uses the assertTrue() method of the unittest module to assert
        that the file exists.

    test_file_params(self):
        Test that the file created by the _write_to_file() method of the
        AudioConverter instance has the correct parameters.
        The method creates a .wav file with a sample rate of 44100 Hz, a bit
        depth of 16 bits, and a single channel.
        The test checks the file parameters using the wave module. It verifies
        that the file has only one channel, a sample width of 2 bytes
        (16 bits), and a sample rate of 44100 Hz. The assertEqual() method is
        used to compare the actual values of the file parameters to the
        expected values.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.

        This method creates an instance of the `AudioConverter` class that is
        used in the individual test methods to test its functionality. It also
        sets the `_sample_list` attribute of the instance to a predefined list
        of float values [0.5, 0.1, -0.3, -0.7, 0.2]. This list of samples
        is used in some of the unit tests to verify the functionality of other
        methods of the `AudioConverter` class.

        Returns:
        --------
        None
        """
        self.instance = AudioConverter()
        self.instance._sample_list = [0.5, 0.1, -0.3, -0.7, 0.2]

    def test_file_created(self):
        """
        Verify that the `_write_to_file()` method of the `AudioConverter`
        class creates a file with the specified name in the specified
        directory.

        The test creates an instance of `AudioConverter` and calls the
        `_write_to_file()` method. It then checks if the file exists by joining
        the file name and directory using `os.path.join()` and checking if the
        resulting path is a file using `os.path.isfile()`. The test uses the
        `assertTrue()` method of the `unittest` module to assert that the file
        exists.

        Raises:
        -------
        AssertionError: If the file does not exist in the specified directory
        or if any of the underlying methods called during `_write_to_file()`
        execution raises an exception.
        """
        self.instance._write_to_file()
        file_path = os.path.join(self.instance._file_path, self.instance._name)
        self.assertTrue(os.path.isfile(file_path))

    def test_file_params(self):
        """
        This unit test ensures that the file created by the "_write_to_file()"
        method of the AudioConverter instance has the correct parameters.

        The method creates a .wav file with a sample rate of 44100 Hz, a bit
        depth of 16 bits, and a single channel.

        The test checks the file parameters using the wave module. It verifies
        that the file has only one channel, a sample width of 2 bytes
        (16 bits), and a sample rate of 44100 Hz.

        Raises:
        -------
        AssertionError: If any of the file parameters (number of channels,
        sample width, and sample rate) do not match the expected values.
        """
        self.instance._write_to_file()
        file_path = os.path.join(self.instance._file_path, self.instance._name)
        with wave.open(file_path, "r") as file:
            self.assertEqual(file.getnchannels(), 1)
            self.assertEqual(file.getsampwidth(), 2)
            self.assertEqual(file.getframerate(), 44100)
