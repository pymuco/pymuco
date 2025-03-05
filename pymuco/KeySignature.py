# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         KeySignature.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .CircleOfFifths import CircleOfFifths
from .Enharmonic import Enharmonic
from .MusicData import FLAT, MAJOR, MINOR, SHARP, M, m
from .ScientificPitchNotation import ScientificPitchNotation


class KeySignature:
    """
    A class that represents a key signature in music notation.

    Attributes:
    -----------
    _CIRCLE_OF_FIFTHS (list): A list of notes in the circle of fifths.
    _RELATIVE_MINORS (list): A list of relative minor keys for each note in
    the circle of fifths.
    _KEY_SIGNATURE_TYPES (dict): A dictionary that maps key signature types
    (major or minor) to their respective circle of fifths or relative minor
    list.

    Methods:
    --------
    init(self, note: ScientificPitchNotation, mode: str) -> None: Initializes
    a KeySignature object with a given note and mode.

    _get_key_signature_type(self): A private method that returns the key
    signature type (circle of fifths or relative minors) based on the mode of
    the key signature.

    _get_num_of_sharps(self, key_signature_type): A private method that
    returns the number of sharps in a key signature based on the note and key
    signature type.

    _get_num_of_flats(self, key_signature_type): A private method that returns
    the number of flats in a key signature based on the note and key signature
    type.

    get_key_signature(self): Returns the key signature of the object in string
    format.

    get_key_signature_notes(self): Returns a list of notes that have
    accidentals in the key signature.
    """

    _CIRCLE_OF_FIFTHS = CircleOfFifths().circle_of_fifths
    _RELATIVE_MINORS = CircleOfFifths().relative_minors

    _KEY_SIGNATURE_TYPES = {M: _CIRCLE_OF_FIFTHS, m: _RELATIVE_MINORS}

    def __init__(self, note: ScientificPitchNotation, mode: str) -> None:
        """
        The __init__ method initializes a Chord object with a specified note
        in scientific pitch notation and mode. It raises a ValueError if either
        note or mode is not provided.

        Parameters:
        -----------

        note: A ScientificPitchNotation object representing the root note of
        the chord.
        mode: A string representing the mode of the chord, either "major" or
        "minor".

        Returns:
        --------

        None.

        Raises:
        -------

        ValueError: If note or mode is not provided.
        The method sets the self._note attribute to the pitch of the note.
        If the mode is "major", it sets the self._mode attribute to M, and if
        the mode is "minor", it sets the self._mode attribute to m. The method
        also initializes an empty list self._accidental_note to store any
        additional notes that may have an accidental.
        """
        if not note or not mode:
            raise ValueError("Note and mode must be provided")

        self._note = note.pitch
        if mode in MAJOR:
            self._mode = M
        elif mode in MINOR:
            self._mode = m
        self._accidental_note = []

    def _get_key_signature_type(self):
        """
        Returns the type of the key signature for the current mode.

        Returns:
        --------
            A string representing the type of the key signature.

        Note:
        -----
            This method should only be called internally by the KeySignature
            class.
        """
        return KeySignature._KEY_SIGNATURE_TYPES.get(self._mode)

    def _get_num_of_sharps(self, key_signature_type):
        """
        Calculates the number of sharps in the current note's key signature.

        Args:
        -----
            key_signature_type: A string representing the type of the key
            signature.

        Returns:
        --------
            An integer representing the number of sharps in the key signature
            for the current note, or None if the note is not in the given key
            signature.

        Note:
        -----
            This method should only be called internally by the KeySignature
            class.
        """
        for i, note in enumerate(key_signature_type):
            if i <= 5 and self._note == note:
                return i
            elif isinstance(note, list) and i == 6:
                for sub_item in note:
                    if sub_item == self._note and self._note[1] == SHARP:
                        return 6
        return None

    def _get_num_of_flats(self, key_signature_type):
        """
        Calculates the number of flats in the current note's key signature.

        Args:
        -----
            key_signature_type: A string representing the type of the key
            signature.

        Returns:
        --------
            An integer representing the number of flats in the key signature
            for the current note, or None if the note
            is not in the given key signature.

        Note:
        -----
            This method should only be called internally by the KeySignature
            class.
        """
        for i, note in enumerate(key_signature_type):
            if isinstance(note, list) and i == 6:
                for sub_item in note:
                    if sub_item == self._note and self._note[1] == FLAT:
                        return 6
            elif i > 6 and self._note == note:
                return 6 - (i - 6)
        return None

    def get_key_signature(self):
        """
        Calculates the key signature for the current note based on its mode
        and accidental.

        Returns:
        --------
            A string representing the key signature for the current note,
            which could be one of the following formats: '0' (for a key
            signature with no sharps or flats), '1#' to '7#' (for key
            signatures with sharps), or '1b' to '7b' (for key signatures with
            flats). Returns None if the current note's mode is not recognized.

        Note:
        -----
            This method should be called on an instance of the Note class.
        """
        key_signature_type = self._get_key_signature_type()
        if not key_signature_type:
            return None

        num_of_sharps = self._get_num_of_sharps(key_signature_type)
        if num_of_sharps is not None:
            return (
                f"{num_of_sharps}"
                if num_of_sharps == 0
                else f"{num_of_sharps}" + str(SHARP)
            )

        num_of_flats = self._get_num_of_flats(key_signature_type)
        if num_of_flats is not None:
            return (
                f"{num_of_flats}"
                if num_of_flats == 0
                else f"{num_of_flats}" + str(FLAT)
            )

        return None

    def get_key_signature_notes(self):
        """
        Returns a list of notes with accidentals in the current key signature.

        Returns:
        --------
            A list of strings representing the notes with accidentals in the
            current key signature.

        Note:
        -----
            This method should be called on an instance of the Note class.
        """
        key_signature = self.get_key_signature()

        if key_signature is None:
            return None

        if SHARP in key_signature:
            self._accidental_note.insert(
                0, self._CIRCLE_OF_FIFTHS[-1] + str(SHARP)
            )
            for i, note in enumerate(self._CIRCLE_OF_FIFTHS, start=2):
                if i <= int(key_signature[:-1]):
                    self._accidental_note.append(note + str(SHARP))
        elif FLAT in key_signature:
            for index, value in enumerate(reversed(self._CIRCLE_OF_FIFTHS)):
                if index <= int(key_signature[:-1]) and index != 0:
                    if FLAT in value:
                        self._accidental_note.append(value)
                    else:
                        for sub_item in value:
                            if FLAT in sub_item:
                                self._accidental_note.append(sub_item)
                            elif (
                                FLAT not in sub_item and SHARP not in sub_item
                            ):
                                self._accidental_note.append(
                                    Enharmonic(
                                        ScientificPitchNotation(sub_item, 4)
                                    )
                                    .get_enharmonic()
                                    .pitch
                                )
        return self._accidental_note
