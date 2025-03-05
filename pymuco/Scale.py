# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         Scale.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from enum import Enum
from typing import List

from .CircleOfFifths import CircleOfFifths
from .Enharmonic import Enharmonic
from .KeySignature import KeySignature
from .MusicData import DEFAULT_OCTAVE, FLAT, MAJOR, MINOR, SHARP, A, C
from .NoteMapping import NoteMapping
from .ScientificPitchNotation import ScientificPitchNotation
from .Tonality import Tonality


class ScaleData(Enum):
    """
    An enumeration class for storing scale sequences for major
    and minor tonalities.

    Attributes
    ----------
    SCALE_SEQUENCE : dict
    A dictionary mapping tonality names to their corresponding
    scale sequences. The keys are strings representing
    tonality names ('Major' or 'Minor'), and the values are
    lists of integers representing the sequence of intervals
    between notes in the scale. The integers represent the number
    of half-steps between each note, where 0 represents
    the root note and 12 represents an octave higher than the
    root note. For example, a major scale starts with the
    root note (0), followed by a whole step (2), another whole
    step (4), a half step (5), another whole step (7),
    another whole step (9), another whole step (11), and finally
    an octave higher than the root note (12).

    Returns
    -------
    None

    Raises
    ------
    NotImplementedError
    If the subclass does not define SCALE_SEQUENCE.
    """

    SCALE_SEQUENCE = {
        "Major": [0, 2, 4, 5, 7, 9, 11, 12],
        "Minor": [0, 2, 3, 5, 7, 8, 10, 12],
    }


class Scale:
    """
    Class representing a musical scale with a given root note
    and tonality.

    Attributes
    ----------
    _NOTE_NAMES : dict
    A dictionary containing the pitch names of all the notes
    in the chromatic scale.
    _CIRCLE_OF_FIFTHS : list
    A list containing the pitch names of all the notes in the
    circle of fifths.
    _RELATIVE_MINORS : list
    A list containing the pitch names of all the relative minors
    for each note in the circle of fifths.
    _MAJOR : str
    A constant string representing the major tonality.
    _MINOR : str
    A constant string representing the minor tonality.

    Methods
    -------
    init(self, root_note: ScientificPitchNotation, tonality_name: Tonality):
    Initializes a new Scale instance with the given root note and
    tonality name.

    root_note(self) -> ScientificPitchNotation:
    Getter method for the _root_note attribute.

    tonality_name(self) -> Tonality:
    Getter method for the _tonality_name attribute.

    _get_note_names(self) -> dict:
    Returns the _NOTE_NAMES attribute.

    _calculate_root_note_position(self) -> int:
    Calculates the position of the root note in the chromatic scale.

    _generate_scale_sequence(self) -> List[int]:
    Returns the scale sequence for the given tonality name.

    _generate_scale_notes(self) -> List[str]:
    Generates the notes for the current scale.

    _get_key_signature(self) -> List[str]:
    Returns the key signature notes for the current scale.

    _convert_enharmonic(self, notes: List[str]) -> List[str]:
    Converts any enharmonic notes in the scale to their
    corresponding key signature note.

    get_scale(self) -> List[str]:
    Returns the notes of the current scale in a list.

    Returns
    -------
    None

    Raises
    ------
    NotImplementedError
    If any of the subclass methods are not implemented.
    """

    _NOTE_NAMES = NoteMapping().get_note_mapping()
    _CIRCLE_OF_FIFTHS = CircleOfFifths().circle_of_fifths
    _RELATIVE_MINORS = CircleOfFifths().relative_minors
    _MAJOR = "Major"
    _MINOR = "Minor"

    def __init__(
        self, root_note: ScientificPitchNotation, tonality_name: Tonality
    ):
        """
        The __init__ method of the Scale class initializes an instance of the
        class with a root note and a tonality name. It first sets the root note
        and tonality name to the corresponding arguments passed in. It then
        checks if the provided root note is valid by checking whether it is in
        the _RELATIVE_MINORS or _CIRCLE_OF_FIFTHS lists. If the root note is
        not valid, it raises a ValueError.

        The method also sets the tonality name to either "Major" or "Minor"
        based on the input, and raises a ValueError if the tonality name is not
        valid. The method initializes an empty list _new_scale.

        Parameters:
        -----------

        root_note (ScientificPitchNotation): The root note of the scale.
        tonality_name (Tonality): The tonality of the scale.

        Raises:
        -------

        ValueError: If the provided root note is not in the _RELATIVE_MINORS or
        _CIRCLE_OF_FIFTHS lists.
        ValueError: If the provided tonality name is not valid.

        Returns:
        --------

        None.
        """
        self._root_note = root_note
        self._tonality_name = tonality_name

        if (
            self._root_note.pitch not in self._RELATIVE_MINORS
            and self._root_note.pitch not in self._CIRCLE_OF_FIFTHS
            and self._root_note.pitch != "Gb"
            and self._root_note.pitch != "D#"
        ):
            raise ValueError(
                f"{self._root_note.pitch} is not a valid root note for a chord"
            )

        if self._tonality_name in MAJOR:
            self._tonality_name = self._MAJOR
        elif self._tonality_name in MINOR:
            self._tonality_name = self._MINOR

        if self._tonality_name not in ScaleData.SCALE_SEQUENCE.value.keys():
            raise ValueError(f"Invalid tonality name: {self._tonality_name}")

        self._new_scale = []

    @property
    def root_note(self):
        return self._root_note

    @property
    def tonality_name(self):
        return self._tonality_name

    def _get_note_names(self):
        """
        Returns a dictionary that maps all available note names in the current
        tuning system to their corresponding MIDI values.

        Returns
        -------
        dict
            A dictionary that maps all available note names in the current
            tuning system to their corresponding MIDI values.
        """
        return self._NOTE_NAMES

    def _calculate_root_note_position(self):
        """
        Calculate the position of the root note of a scale in the current
        tuning system.

        Returns:
        -------
        int:
            The position of the root note in the current tuning system.

        Notes:
        ------
        This method retrieves the MIDI value of the root note from the
        `_root_note` attribute and uses it as a key to index the dictionary of
        available note names and their corresponding MIDI values obtained from
        the `_get_note_names()` method.

        """
        return self._get_note_names()[self._root_note.pitch]

    def _generate_scale_sequence(self):
        """
        Generate the list of semitone intervals that corresponds to the
        sequence of scale degrees for the current tonality.

        Returns
        -------
        List[int]
            A list of semitone intervals corresponding to the sequence of scale
            degrees for the current tonality.

        Notes
        -----
        This method retrieves the scale sequence by accessing the
        SCALE_SEQUENCE dictionary in the ScaleData class and retrieving the
        list of intervals that corresponds to the key provided in the
        _tonality_name attribute.

        Example
        -------
        If the _tonality_name attribute is "Major", this method will return
        [2, 2, 1, 2, 2, 2, 1], which corresponds to the sequence of intervals
        for the major scale.
        """
        return ScaleData.SCALE_SEQUENCE.value[self._tonality_name]

    def _generate_scale_notes(self) -> List[str]:
        """
        Generate a list of note names belonging to the scale of the chord.

        This method calculates the position of the root note using the
        `_calculate_root_note_position()` method and obtains the sequence of
        intervals for the scale using the `_generate_scale_sequence()` method.
        It then generates the note names for the scale by finding the index of
        the root note position plus each interval in the scale sequence,
        wrapping around to the beginning of the list if necessary. The method
        returns the list of note names for the scale.

        Returns
        -------
        list of str
            A list of strings representing the note names in the scale of the
            chord.
        """
        root_note_position = self._calculate_root_note_position()
        scale_sequence = self._generate_scale_sequence()
        notes = [
            list(self._get_note_names().keys())[
                list(self._get_note_names().values()).index(
                    (root_note_position + i) % 12
                )
            ]
            for i in scale_sequence
        ]
        return notes

    def _get_key_signature(self):
        """
        Returns the notes in the key signature of the current chord.

        This method creates a `KeySignature` object using the root note and
        tonality name of the chord and then calls the `get_key_signature_notes`
        method of the `KeySignature` object to get the notes in the key
        signature.

        Returns:
            A list of strings representing the notes in the key signature of
            the current chord.
        """
        return KeySignature(
            ScientificPitchNotation(self._root_note.pitch, DEFAULT_OCTAVE),
            self._tonality_name,
        ).get_key_signature_notes()

    def _convert_enharmonic(self, notes: List[str]) -> List[str]:
        """
        Converts the notes to their enharmonic equivalent based on the key
        signature of the chord.

        Parameters
        ----------
        notes : list of str
            A list of notes in the chord.

        Returns
        -------
        list of str
            A list of notes in the chord with notes converted to their
            enharmonic equivalent.

        Notes
        -----
        This method first obtains the key signature of the chord by calling the
        _get_key_signature() method. Then, if the root note of the chord is
        not C major or A minor, it converts the notes in the chord to their
        enharmonic equivalent based on the key signature. If the key signature
        has sharps, it converts flats to sharps, and if the key signature has
        flats, it converts sharps to flats.

        Examples
        --------
        To convert the notes of a chord to their enharmonic equivalent:

        >>> chord = Chord("C7")
        >>> notes = ["C", "E", "G", "Bb"]
        >>> chord._convert_enharmonic(notes)
        ["C", "E", "G", "A#"]
        """
        key_signature = self._get_key_signature()

        if (
            self._root_note.pitch == C
            and self.tonality_name == self._MAJOR
            or self._root_note.pitch == A
            and self.tonality_name == self._MINOR
        ):
            return notes

        elif SHARP == key_signature[0][1]:
            for n in key_signature:
                if n not in notes:
                    for i, note in enumerate(notes):
                        x = (
                            Enharmonic(
                                ScientificPitchNotation(n, DEFAULT_OCTAVE)
                            )
                            .get_enharmonic()
                            .pitch
                        )
                        if x == note:
                            notes[i] = n

        elif FLAT == key_signature[0][1]:
            for n in key_signature:
                if n not in notes:
                    for i, note in enumerate(notes):
                        x = (
                            Enharmonic(
                                ScientificPitchNotation(n, DEFAULT_OCTAVE)
                            )
                            .get_enharmonic()
                            .pitch
                        )
                        if x == note:
                            notes[i] = n

        return notes

    def get_scale(self) -> List[str]:
        """
        Return a list of note names that make up the scale for the chord,
        after converting any enharmonic notes based on the chord's key
        signature.

        Returns
        -------
        List[str]
            A list of note names as strings that make up the scale for the
            chord, after converting any enharmonic notes based on the chord's
            key signature.
        """
        notes = self._generate_scale_notes()
        notes = self._convert_enharmonic(notes)
        return notes
