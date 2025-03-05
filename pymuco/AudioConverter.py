# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         AudioConverter.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import math
import os
import re
import secrets
import struct
import tempfile
import wave
from typing import List, Tuple, Union

from .MusicComputationNotation import MusicComputationNotation
from .NoteDuration import NoteDuration, NoteDurationMapping
from .NoteFrequencyConverter import NoteFrequencyConverter
from .ScientificPitchNotation import ScientificPitchNotation


class AudioConverter:
    """
    Class Name: AudioConverter

    Attributes:
    -----------

    _sample_rate (int): The sample rate to use for the audio file.
    _name (str): A randomly generated name to use for the output file.
    _file_path (str): The directory path to write the output file to.
    _note_duration_mapping (NoteDurationMapping): A NoteDurationMapping object
    used to convert duration strings to their corresponding values in seconds.
    _note_frequency_converter (NoteFrequencyConverter):
    A NoteFrequencyConverter object used to convert note names to their
    corresponding frequencies.
    _full_file_path (str): The full path of the output file, including the
    directory and file name.

    Methods:
    --------

    init(self, sample_rate=44100): Initializes a new instance of the
    AudioConverter class with the specified sample rate.
    convert_to_audio(self, mcn: MusicComputationNotation) -> str: Converts a
    MusicComputationNotation object to an audio file and returns the file path.
    _validate_file_path(self): Checks that the file path for writing audio
    samples is valid and can be accessed.
    _create_sample(self, mcn: List[Tuple[str, Union[str, float]]]): Creates an
    audio sample from a list of musical notes and their durations. The input is
    a list of tuples, with each tuple containing a note name and its duration
    in string or float format. The output is a concatenated sample list of the
    notes.
    """

    def __init__(self, sample_rate=44100):
        """
        Initializes a new instance of the AudioConverter class with the
        specified sample rate.

        Args:
            sample_rate (int, optional): The sample rate to use for the audio
            file. Defaults to 44100.

        """
        self._sample_rate = sample_rate
        self._sample_list = []
        self._name = secrets.token_hex(8)
        self._file_path = os.path.join(tempfile.gettempdir(), "")
        self._note_duration_mapping = NoteDurationMapping()
        self._note_frequency_converter = NoteFrequencyConverter()
        self._full_file_path = self._file_path + self._name

    def convert_to_audio(self, mcn: MusicComputationNotation):
        """
        Convert a MusicComputationNotation object to an audio file.

        The method takes a MusicComputationNotation object containing a
        sequence of notes and durations, generates audio samples for each note
        using a sine wave generator, and writes the samples to an audio file in
        WAV format. The file is written to the directory specified by the
        _file_path attribute of the object.

        Parameters
        ----------
        mcn : MusicComputationNotation
            A MusicComputationNotation object containing a sequence of notes
            and durations to be converted to audio.

        Returns
        -------
        str
            The file path of the created audio file.

        Raises
        ------
        TypeError
            If the argument is not a MusicComputationNotation object.
        ValueError
            If the file path specified in the object is invalid or cannot be
            accessed for reading and writing.

        Examples
        --------
        # Convert a valid MusicComputationNotation object to audio
        >>> instance = MyClass()
        >>> mcn = MusicComputationNotation("C4 1/4 D4 1/4 E4 1/4 F4 1/4 G4 1/4
        A4 1/4 B4 1/4")
        >>> instance.convert_to_audio(mcn)
        '/path/to/output/audio.wav'

        # Convert an invalid argument to audio
        >>> instance = MyClass()
        >>> instance.convert_to_audio("invalid argument")
        Traceback (most recent call last):
        ...
        TypeError: mcn must be an instance of MusicComputationNotation

        # Convert to audio with an invalid file path
        >>> instance = MyClass()
        >>> instance._file_path = "/nonexistent/path"
        >>> mcn = MusicComputationNotation("C4 1/4")
        >>> instance.convert_to_audio(mcn)
        Traceback (most recent call last):
        ...
        ValueError: Invalid file path: /nonexistent/path

        """
        if not isinstance(mcn, MusicComputationNotation):
            raise TypeError(
                "mcn must be an instance of MusicComputationNotation"
            )
        self._validate_file_path()
        return self._create_sample(mcn.notation)

    def _validate_file_path(self):
        """
        Check that the file path for writing audio samples is valid and can be
        accessed.

        This method checks that the directory specified by the file path exists
        and can be read from and written to by the current user. If the
        directory does not exist or cannot be accessed, a ValueError is raised.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the file path specified in the object is invalid or cannot be
            accessed for reading and writing.

        Examples
        --------
        # Validate a valid file path
        >>> instance = MyClass()
        >>> instance._file_path = "/path/to/output"
        >>> instance._validate_file_path()

        # Validate an invalid file path
        >>> instance = MyClass()
        >>> instance._file_path = "/nonexistent/path"
        >>> instance._validate_file_path()
        Traceback (most recent call last):
        ...
        ValueError: Invalid file path: /nonexistent/path
        """
        if (
            not os.path.exists(self._file_path)
            or not os.access(self._file_path, os.R_OK)
            or not os.access(self._file_path, os.W_OK)
        ):
            raise ValueError(f"Invalid file path: {self._file_path}")

    def _create_sample(self, mcn: List[Tuple[str, Union[str, float]]]):
        """
        Create an audio sample from a list of musical notes and their
        durations.

        The method iterates through each note and duration in the list, and
        generates a list of audio samples for each note using the corresponding
        frequency and duration. The resulting audio samples are concatenated
        into a single sample list for the audio object, and the sample list is
        written to a WAV file with the specified name and sample rate.

        Args:
        -----
            mcn (List[Tuple[str, Union[str, float]]]): A list of tuples
                representing musical notes and their durations. Each tuple
                should contain a string representing the note name (in
                scientific pitch notation) and either a string or float
                representing the duration of the note in seconds or as a note
                duration string (e.g. "4n" for quarter note).

        Returns:
        --------
            None.

        Raises:
        -------
            ValueError: If the input list is empty or contains invalid note or
                duration values.
            OSError: If there is an error writing to the output file, such as
                if the file path is invalid or the output file cannot be opened
                for writing.

        Examples:
        ---------
            # Create an audio sample from a list of notes and durations
            >>> instance = MyClass()
            >>> instance._name = "test.wav"
            >>> instance._file_path = "/path/to/output"
            >>> instance._sample_rate = 44100
            >>> notes = [("A4", 0.5), ("C#5", "4n"), ("D5", 1.0)]
            >>> instance._create_sample(notes)

            # Check that the output file was created and contains audio
            >>> os.path.isfile(os.path.join(instance._file_path,
            instance._name))
            True
            >>> with wave.open(os.path.join(instance._file_path,
            instance._name), 'r') as file:
            ...     file.getnframes() > 0
            True
        """
        for note, duration in mcn:
            note_freq = self._get_frequency_note(note)
            duration = self._validate_duration(duration)
            self._generate_samples(note_freq, duration)
        return self._write_to_file()

    def _generate_samples(self, frequency: float, duration: float):
        """
        Generate a list of audio samples for a sine wave with the specified
        frequency and duration.

        Args:
        -----
            frequency (float): The frequency of the sine wave in Hz.
            duration (float): The duration of the sine wave in seconds.

        Returns:
        --------
            None.

        Raises:
        -------
            None.

        Examples:
        ---------
            Generate a list of samples for a sine wave with a frequency of
            440 Hz and duration of 1s:

            >>> instance = MyClass()
            >>> instance._sample_rate = 44100
            >>> instance.generate_samples(440, 1.0)

            Check that the sample list was populated with the expected number
            of samples:

            >>> len(instance._sample_list)
            44100
        """
        sample_rate = self._sample_rate
        num_samples = int(sample_rate * duration)
        constant = 2 * math.pi * frequency / sample_rate
        samples = [32767 * math.sin(constant * i) for i in range(num_samples)]
        self._sample_list.extend(samples)

    def _write_to_file(self):
        """
        Write the list of samples to a WAV file with the specified name and
        sample rate.

        Args:
        -----
        None.

        Returns:
        --------
        None.

        Raises:
        -------
        OSError: If there is an error writing to the output file, such as if
        the file path is invalid or the output file cannot be opened for
        writing.

        Examples:
        ---------
        # Write a list of samples to a WAV file
        >>> instance = MyClass()
        >>> instance._sample_list = [0.5, 0.1, -0.3, -0.7, 0.2]
        >>> instance._sample_rate = 44100
        >>> instance._name = "test.wav"
        >>> instance._file_path = "/path/to/output"
        >>> instance._write_to_file()
        # Check that the output file was created
        >>> os.path.isfile(os.path.join(instance._file_path, instance._name))
        True

        """
        num_samples = len(self._sample_list)
        file_path = os.path.join(self._file_path, self._name)
        with wave.open(file_path, "w") as file:
            file.setparams(
                (
                    1,
                    2,
                    self._sample_rate,
                    num_samples,
                    "NONE",
                    "not compressed",
                )
            )
            for sample in self._sample_list:
                file.writeframes(struct.pack("<h", int(sample)))

    def _get_frequency_note(self, note):
        """
        Get the frequency of a given note name in hertz.

        Args:
        -----
            note (str): A string representation of the note name, which can
            include the pitch name (e.g. "C", "G#", "Fb"), an optional
            accidental (e.g. "#", "b"), and an optional octave number
            (e.g. "4", "5", "-1").

        Returns:
        --------
            float: The frequency of the note in hertz, calculated using the
            Scientific Pitch Notation of the note and the standard tuning
            frequency.

        Raises:
        -------
            ValueError: If the input string does not match the expected format
            for a note name, or if the input note cannot be converted to a
            ScientificPitchNotation object.

        Examples:
        ---------
            # Get the frequency of a valid note name
            >>> instance = MyClass()
            >>> instance._get_frequency_note("C4")
            261.6255653005986

            # Get the frequency of a note name with an accidental
            >>> instance._get_frequency_note("G#3")
            207.65234878997256

            # Get the frequency of a note name with a flat accidental and
            # negative octave
            >>> instance._get_frequency_note("Fb-1")
            6.875

            # Invalid note name format
            >>> instance._get_frequency_note("invalid")  # Raises ValueError
            Traceback (most recent call last):
                ...
            ValueError: Invalid note name format: 'invalid'

            # Unable to convert input note to SPN
            >>> instance._get_frequency_note(None)  # Raises ValueError
            Traceback (most recent call last):
                ...
            ValueError: Unable to convert input note to SPN: 'None'
        """
        spn = self._convert_to_spn(note)
        if isinstance(spn, ScientificPitchNotation):
            return self._note_frequency_converter.get_frequency_from_note_name(
                spn
            )

    def _convert_to_spn(self, note):
        """
        Convert a note name in string format to a Scientific Pitch Notation
        object.

        Args:
        -----
            note: A string representation of the note name, which can include
            the pitch name (e.g. "C",
                "G#", "Fb"), an optional accidental (e.g. "#", "b"), and an
                optional octave number (e.g.
                "4", "5", "-1").

        Returns:
        --------
            A ScientificPitchNotation object representing the note, with the
            pitch name, accidental,
            and octave parsed from the input string.

        Raises:
        -------
            ValueError: If the input string does not match the expected format
            for a note name.

        Examples:
        ---------
            # Convert a valid note name to SPN
            >>> instance = MyClass()
            >>> spn = instance._convert_to_spn("C#4")
            >>> spn
            <ScientificPitchNotation C#4>

            # Convert a note name with no accidental or octave
            >>> instance._convert_to_spn("A")
            <ScientificPitchNotation A0>

            # Convert a note name with a flat accidental and negative octave
            >>> instance._convert_to_spn("Fb-1")
            <ScientificPitchNotation Fb-1>

            # Invalid note name format
            >>> instance._convert_to_spn("invalid")  # Raises ValueError
            Traceback (most recent call last):
                ...
            ValueError: Invalid note name format: 'invalid'
        """
        pitch_pattern = re.compile(r"\s*\d+\s*")
        octave_pattern = re.compile(r"[^0-9]")

        pitch = pitch_pattern.sub("", note)
        octave = octave_pattern.sub("", note)

        spn = ScientificPitchNotation(pitch, int(octave))
        return spn

    def _validate_duration(self, duration):
        """
        Check if a given duration is valid and convert it to a float value.

        Args:
        -----
            duration: The duration to be validated, which can be a string
            representation of a
                note duration (e.g. "quarter", "half", "eighth"), or a
                numerical value representing
                the duration in beats (e.g. 1.0 for a quarter note, 0.5 for an
                eighth note).

        Returns:
        --------
            A float value representing the duration in beats, if it is a valid
            duration. If the duration is a string representation of a note
            duration, it will be converted to its corresponding numerical value
            using the `_note_duration_mapping` dictionary. If the duration is a
            numerical value, it will be returned as is.

        Raises:
        -------
            ValueError: If the duration is not a valid note duration or
            numerical value.

        Examples:
        ---------
            # Check a valid duration as a string
            >>> instance = MyClass()
            >>> instance._validate_duration("half")
            2.0

            # Check a valid duration as a float
            >>> instance._validate_duration(0.25)
            0.25

            # Check an invalid duration
            >>> instance._validate_duration("quarter")  # Raises ValueError
            Traceback (most recent call last):
                ...
            ValueError: Invalid duration: 'quarter'
        """
        for (
            note,
            note_duration,
        ) in self._note_duration_mapping.get_note_duration():
            if note == duration or note_duration == duration:
                if isinstance(duration, int):
                    return float(duration)
                else:
                    return NoteDuration(duration).duration_length
