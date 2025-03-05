# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         NoteMapping.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .Enharmonic import Enharmonic
from .MusicData import SHARP, B, C, E, MusicalAlphabet
from .ScientificPitchNotation import ScientificPitchNotation

_NOTE_NAME = MusicalAlphabet.get_note_name()


class NoteMapping:
    """
    Class for creating and manipulating musical note mappings.

    Methods
    -------
    get_note_mapping():
        Generates a complete note mapping dictionary by creating a chromatic
        scale using `_create_chromatic_scale()`, and then creating an
        enharmonic dictionary using `_get_enharmonic_dict()`.

    Attributes
    ----------
    None

    Raises
    ------
    None

    See Also
    --------
    None

    Notes
    -----
    The `NoteMapping` class provides a way to create and manipulate musical
    note mappings, which can be useful in a variety of music-related
    applications.

    Private Methods
    ---------------
    _create_chromatic_scale():
        Creates a chromatic scale by generating a list of note names and
        adding accidentals where necessary.
    _add_accidentals(notes):
        Adds accidentals to a list of note names, except for E and B.
    _get_chromatic_base():
        Generates a dictionary mapping each note name in the chromatic scale
        to its corresponding index.
    _get_enharmonic_dict(note_dict):
        Generates a dictionary mapping each note name and its enharmonics to
        its corresponding index.

    Examples
    --------
    >>> note_mapping = NoteMapping()
    >>> note_mapping.get_note_mapping()
    {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
    'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10,
    'B': 11}

    """

    def _create_chromatic_scale(self):
        """
        Create a chromatic scale consisting of twelve notes.

        This function generates a list of all the note names using the
        `_NOTE_NAME` constant, rearranges it so that it starts with the note
        `C` and ends with the note `B`, adds accidentals to the notes using
        the `_add_accidentals()` method, and returns the resulting list.

        Returns
        -------
        list
            A list of twelve note names representing the chromatic scale.

        Notes
        -----
        The chromatic scale consists of twelve notes, with each note being one
        semitone (half step) away from the previous note. The notes are named
        using a combination of the letters A through G, along with sharps (#)
        and flats (b).

        Examples
        --------
        >>> create_chromatic_scale()
        ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        """
        notes = [note for note in _NOTE_NAME]
        notes = notes[notes.index(C) :] + notes[: notes.index(C)]
        return self._add_accidentals(notes)

    def _add_accidentals(self, notes):
        """
        Add accidentals to a list of note names.

        This method appends a sharp symbol to each note name in the list except
        for `E` and `B`, which already have natural semitones between them and
        the adjacent notes. The resulting list represents a chromatic scale
        with all the notes named using letters A through G, along with sharps
        (#) and flats (b).

        Parameters
        ----------
        notes : list
            A list of note names to which accidentals will be added.

        Returns
        -------
        list
            A modified list of note names with accidentals added where
            necessary.

        Notes
        -----
        A chromatic scale consists of twelve notes, with each note being one
        semitone (half step) away from the previous note. Accidentals are used
        to represent the notes that fall between the natural semitones.

        Examples
        --------
        >>> notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        >>> _add_accidentals(notes)
        ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        """
        result = []
        for note in notes:
            result.append(note)
            result.append(note + SHARP) if note not in {E, B} else None
        return result

    def _get_chromatic_base(self):
        """
        Generate a chromatic base of notes with their corresponding index
        values. A chromatic base is a collection of twelve notes that
        represents all the possible semitones (half-steps) in an octave. This
        method creates a chromatic scale by calling the
        `_create_chromatic_scale()` method, and then creates a dictionary that
        maps each note in the chromatic scale to its index position in the
        list, using the `enumerate()` function.

        Returns
        -------
        dict
            A dictionary mapping each note in the chromatic scale to its index
            position.

        Notes
        -----
        In music theory, an octave is a set of eight notes, with the eighth
        note being a repetition of the first note but at double the frequency.
        In Western music, an octave is divided into twelve equal parts, each
        representing a semitone.

        Examples
        --------
        >>> _get_chromatic_base()
        {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7,
        'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
        """
        chromatic_scale = self._create_chromatic_scale()
        return {note: i for i, note in enumerate(chromatic_scale)}

    def _get_enharmonic_dict(self, note_dict):
        """
        Generate an enharmonic dictionary based on the given note dictionary.

        In music theory, an enharmonic equivalent is a note that has a
        different name but represents the same pitch. For example, the notes
        C# and Db are enharmonic equivalents. This method takes a dictionary
        of notes and their corresponding values and generates an enharmonic
        dictionary that includes all the enharmonic equivalents of each note.

        Parameters
        ----------
        note_dict : dict
            A dictionary of note names and their corresponding values.

        Returns
        -------
        dict
            An enharmonic dictionary mapping each note in the input dictionary
            to its corresponding value and all its enharmonic equivalents.

        Notes
        -----
        In Western music, there are twelve different pitch classes that make
        up the chromatic scale. Each pitch class can have multiple note names
        that represent the same pitch, depending on the context and key
        signature.

        Examples
        --------
        >>> note_dict = {'C': 0, 'D#': 3, 'Gb': 6, 'Bb': 10}
        >>> _get_enharmonic_dict(note_dict)
        {'C': 0, 'B#': 0, 'Dbb': 0, 'C#': 1, 'Db': 1, 'B##': 3, 'Ebbb': 3,
        'D#': 3, 'Eb': 3, 'Fbbb': 3, 'Cbb': 6, 'Bbbb': 6, 'Fb': 6, 'Gb': 6,
        'Abb': 8, 'G#': 8, 'A#bb': 10, 'Bb': 10, 'A##': 10, 'Cb': 10}
        """
        return {
            note: value
            for key, value in note_dict.items()
            for note in [key]
            + Enharmonic(ScientificPitchNotation(key, 4)).get_all_enharmonics()
        }

    def get_note_mapping(self):
        """
        Generate a note mapping dictionary that includes all enharmonic
        equivalents of each note.

        Returns:
        -------
        dict:
            A note mapping dictionary that includes all enharmonic
            equivalents of each note and their corresponding index values in
            the chromatic scale.

        Notes:
        ------
        The method generates a chromatic base using the `_get_chromatic_base()`
        method, and then creates an enharmonic dictionary based on the
        chromatic base using the `_get_enharmonic_dict()` method. The resulting
        dictionary maps each note name and its enharmonic equivalents to their
        corresponding index values in the chromatic scale.
        """
        note_value_mapping = self._get_chromatic_base()
        return self._get_enharmonic_dict(note_value_mapping)
