# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         ScientificPitchNotation.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import re
from typing import Union

from pymuco.MusicData import ACCIDENTALS, NOTE_NAMES


class ScientificPitchNotation:
    """
    The ScientificPitchNotation class represents a musical note in Western
    music theory using the scientific pitch notation format.

    Parameters
    ----------
    pitch : str
    The pitch of the note.
    octave : int
    The octave of the note.

    Attributes
    ----------
    _pitch : str
    The pitch of the note.
    _octave : int
    The octave of the note.

    Methods
    ----------
    init(self, pitch: str, octave: int) -> None
    Initializes a new instance of the class with the specified pitch
    and octave values.
    Validates the input using _validate_params method.
    _validate_params(self) -> None
    Validates the pitch and octave values of a note.
    If invalid, raises a ValueError with a descriptive error message.
    _is_valid_pitch(self) -> None
    Checks whether the pitch of a note is valid.
    If invalid, raises a ValueError with a descriptive error message.
    _is_valid_octave(self) -> None
    Checks whether the octave of a note is valid.
    If invalid, raises a ValueError with a descriptive error message.
    pitch(self) -> str
    Returns the pitch of the note.
    octave(self) -> int
    Returns the octave of the note.
    octave(self, octave: int) -> None
    Setter method to set the octave of the note.
    If the input is not an integer, raises a TypeError with a descriptive
    error message.
    spn(self) -> str
    Returns the scientific pitch notation of the note.
    is_valid_pitch(pitch: str) -> bool
    Checks if a pitch string is valid.
    Returns True if the pitch is a valid note name followed by an
    optional accidental.
    is_valid_octave(octave: int, min_octave: int = 0,
    max_octave: int = 10) -> bool
    Checks if an octave value is valid.
    Returns True if the octave is between min_octave and max_octave, inclusive.
    str(self) -> str
    Returns a string representation of the object.
    eq(self, other: Union['ScientificPitchNotation', str]) -> bool
    Compares two objects of the class.
    Returns True if they represent the same note, False otherwise.

    Notes
    -----
    The is_valid_pitch and is_valid_octave methods use the NOTE_NAMES and
    ACCIDENTALS constants that are assumed to be defined elsewhere in the code.

    Returns
    -------
    None

    Raises
    ------
    ValueError
    If the input is not valid.
    TypeError
    If the input is not an integer.
    """

    def __init__(self, pitch: str, octave: int) -> None:
        self._pitch: str = pitch
        self._octave: int = octave
        self._validate_params()

    @property
    def pitch(self) -> str:
        """Return the pitch of the note"""
        return self._pitch

    @property
    def octave(self) -> int:
        """Return the octave of the note"""
        return self._octave

    @octave.setter
    def octave(self, octave: int) -> None:
        if not isinstance(octave, int):
            raise TypeError("Octave must be an integer.")
        self._octave = octave

    @property
    def spn(self) -> str:
        """
        Return the scientific pitch notation of the note.

        Returns:
        --------
        str
            The scientific pitch notation of the note.
        """
        return f"{self.pitch}{self.octave}"

    @staticmethod
    def is_valid_pitch(pitch: str) -> bool:
        """
        Check if a pitch string is a valid note name followed by an optional
        accidental.

        Args:
        -----
            pitch (str): The pitch string to check.

        Returns:
        --------
            bool: True if the pitch is a valid note name followed by an
            optional accidental.

        Raises:
        -------
            ValueError: If the pitch is not a string or if it does not match
            the expected format (i.e., a note name followed by an optional
            accidental).
        """
        pattern = re.compile(
            f"^[{''.join(NOTE_NAMES)}][{''.join(ACCIDENTALS)}]?$"
        )
        return pattern.match(pitch) is not None

    @staticmethod
    def is_valid_octave(
        octave: int, min_octave: int = 0, max_octave: int = 10
    ) -> bool:
        """
        Check if an octave value is valid.

        Parameters
        ----------
        octave : int
            The octave value to check.
        min_octave : int, optional
            The minimum valid octave (default is 0).
        max_octave : int, optional
            The maximum valid octave (default is 10).

        Returns
        -------
        bool
            True if the octave is between min_octave and max_octave, inclusive.

        """
        return octave >= min_octave and octave <= max_octave

    def _validate_params(self) -> None:
        """
        Validate the pitch and octave values of a note.

        This method checks that the pitch and octave of a note are valid
        according to the conventions of Western music theory.
        If the pitch or octave is invalid, a ValueError is raised with a
        descriptive error message.

        Raises:
        -------
            ValueError: If the pitch or octave is out of range or has an
                invalid format.

        """
        self._is_valid_pitch()
        self._is_valid_octave()

    def _is_valid_pitch(self) -> None:
        """
        Check whether the pitch of a note is valid.

        This method checks whether the pitch of a note is valid according to
        the conventions of Western music theory.
        If the pitch is invalid, a ValueError is raised with a descriptive
        error message.

        Raises:
        -------
            ValueError: If the pitch is out of range or has an invalid format.

        """
        if not self.is_valid_pitch(self._pitch):
            raise ValueError("Invalid pitch.")

    def _is_valid_octave(self) -> None:
        """
        Check whether the octave of a note is valid.

        This method checks whether the octave of a note is valid according to
        the conventions of Western music theory.
        If the octave is invalid, a ValueError is raised with a descriptive
        error message.

        Raises:
        -------
            ValueError: If the octave is out of range or has an invalid format.
        """
        if not self.is_valid_octave(self._octave):
            raise ValueError("Invalid octave.")

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
        str: The string representation of the object, which is the scientific
        pitch notation of the note.
        """
        return self.spn

    def __eq__(self, other: Union["ScientificPitchNotation", str]) -> bool:
        """Compare two ScientificPitchNotation objects for equality.

        Args:
            other (Union[ScientificPitchNotation, str]): The object to compare
                to. Can be another ScientificPitchNotation object or a string
                in scientific pitch notation format.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Raises:
            TypeError: If other is not a ScientificPitchNotation object or a
            string.
        """
        if isinstance(other, ScientificPitchNotation):
            return self.spn == other.spn
        return self.spn == other
