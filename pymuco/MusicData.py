# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         MusicData.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from typing import Tuple


class MusicalAlphabet:
    """A class for working with musical notes.

    Attributes
    ----------
    None

    Methods
    -------
    get_note_name():
        Returns a tuple of note names.
    get_note_names():
        Returns a string of note names.

    Examples
    --------
    >>> musical_alphabet = MusicalAlphabet()
    >>> musical_alphabet.get_note_name()
    ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    >>> musical_alphabet.get_note_names()
    'ABCDEFG'
    """

    @staticmethod
    def get_note_name() -> Tuple[str, ...]:
        """Get note names.

        Returns
        -------
        tuple
            Tuple of note names as strings.

        Examples
        --------
        >>> MusicalAlphabet.get_note_name()
        ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        """
        return tuple(chr(i) for i in range(ord("A"), ord("H")))[:7]

    @staticmethod
    def get_note_names() -> str:
        """Get a string of note names.

        Returns
        -------
        str
            String of note names.

        Examples
        --------
        >>> MusicalAlphabet.get_note_names()
        'ABCDEFG'
        """
        return "".join(MusicalAlphabet.get_note_name())


NOTE_NAMES = MusicalAlphabet.get_note_name()
A, B, C, D, E, F, G = NOTE_NAMES


class Accidental:
    """A class for working with musical accidentals.

    Attributes
    ----------
    None

    Methods
    -------
    get_accidental():
        Returns a tuple of accidental symbols.
    get_accidentals():
        Returns a string of accidental symbols.

    Examples
    --------
    >>> accidental = Accidental()
    >>> accidental.get_accidental()
    >>> accidental.get_accidentals()

    Constants
    ---------
    DEFAULT_OCTAVE : int
        Default octave value.
    M : str
        Major symbol.
    m : str
        Minor symbol.
    MAJOR : List[str]
        List of major symbol variations.
    MINOR : List[str]
        List of minor symbol variations.
    """

    @staticmethod
    def get_accidental() -> Tuple[str, ...]:
        """Get accidental symbols.

        Returns
        -------
        tuple
            Tuple of accidental symbols as strings.

        Examples
        --------
        >>> Accidental.get_accidental()
        """
        return ("\u0078", "\u0023", "", "\u0062", "\U0001D12B")[:5]

    @staticmethod
    def get_accidentals() -> str:
        """Get a string of accidental symbols.

        Returns
        -------
        str
            String of accidental symbols.

        Examples
        --------
        >>> Accidental.get_accidentals()
        """
        return "".join(Accidental.get_accidental())


ACCIDENTALS = Accidental.get_accidental()
DOUBLE_SHARP, SHARP, NATURAL, FLAT, DOUBLE_FLAT = ACCIDENTALS

DEFAULT_OCTAVE = 4

M = "M"
m = "m"
MAJOR = ["MAJOR", "Major", "M"]
MINOR = ["MINOR", "Minor", "m"]
