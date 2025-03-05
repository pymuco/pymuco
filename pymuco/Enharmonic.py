# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         Enharmonic.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .EnharmonicMapping import EnharmonicMapping
from .MusicData import DEFAULT_OCTAVE
from .ScientificPitchNotation import ScientificPitchNotation


class Enharmonic:
    """
    Represents a musical note and provides functionality to determine its
    enharmonics.

    Attributes:
    -----------
        _note_name (ScientificPitchNotation): a ScientificPitchNotation object
        representing the note
        _is_enharmonic (bool): a boolean value indicating whether the note has
        an enharmonic
        _enharmonics (dict): a dictionary of notes and their enharmonics

    Methods:
    --------
        __init__(self, note):
            Initializes an Enharmonic object with a ScientificPitchNotation
            object representing a musical note. The _note_name instance
            variable is set to the input note, and the _is_enharmonic instance
            variable is set to True if the note has an enharmonic, and False
            otherwise. The _enharmonics instance variable is created by calling
            the enharmonic_mapping() method of the EnharmonicMapping class,
            which returns a dictionary of notes and their enharmonics.

        get_enharmonic(self):
            Returns a string representing the enharmonic of the note, or the
            original note name if it has no enharmonic.

        get_all_enharmonics(self):
            Returns a list of all the note names that are enharmonics of the
            original note, or a list containing only the original note name if
            it has no enharmonic.

        is_enharmonic(self):
            Returns True if the note has an enharmonic, and False otherwise.

        _calculate_enharmonic(self):
            Calculates the enharmonic of the note by looking up the _note_name
            instance variable in the _enharmonics instance variable. If the
            note is not found as a key, it looks up the value and returns the
            corresponding key.
    """

    def __init__(self, note: ScientificPitchNotation):
        """
        Initializes an Enharmonic object with a ScientificPitchNotation object
        representing a musical note.

        Args:
        -----
            note (ScientificPitchNotation): A ScientificPitchNotation object
            representing a musical note.

        Raises:
        -------
            ValueError: if the input note is not a valid scientific pitch
            notation.

        Attributes:
        -----------
            _note_name (ScientificPitchNotation): a ScientificPitchNotation
            object representing the note
            _is_enharmonic (bool): a boolean value indicating whether the note
            has an enharmonic
            _enharmonics (dict): a dictionary of notes and their enharmonics
        """
        self._enharmonics = EnharmonicMapping().enharmonic_mapping()
        self._note_name = note.pitch
        self._is_enharmonic = self.is_enharmonic()

    def get_enharmonic(self) -> str:
        """
        Returns a string representing the enharmonic of the note, or the
        original note name if it has no enharmonic.

        Returns:
        --------
            str: A string representing the enharmonic of the note, or the
            original note name if it has no enharmonic.
        """
        if self._is_enharmonic is False:
            return self._note_name
        self._note_name = self._calculate_enharmonic()
        return ScientificPitchNotation(self._note_name, DEFAULT_OCTAVE)

    def get_all_enharmonics(self) -> list:
        """
        Returns a list of all the note names that are enharmonics of the
        original note, or a list containing only the original note name if it
        has no enharmonic.

        Returns:
        --------
            list: A list of all the note names that are enharmonics of the
            original note, or a list containing only the original note name if
            it has no enharmonic.
        """
        if self._is_enharmonic is False:
            return [self._note_name]
        return [
            key if value == self._note_name else value
            for key, value in self._enharmonics.items()
            if key == self._note_name or value == self._note_name
        ]

    def is_enharmonic(self) -> bool:
        """
        Returns True if the note has an enharmonic, and False otherwise.

        Returns:
        --------
            bool: True if the note has an enharmonic, and False otherwise.
        """
        return self._note_name in self._enharmonics

    def _calculate_enharmonic(self) -> str:
        """
        Calculate the note name of this note's enharmonic equivalent.

        Returns:
        --------
        - A string representing the note name of this note's enharmonic
        equivalent, if it has one.
        - None, if this note has no enharmonic equivalent.

        Raises:
        -------
        - No exceptions are explicitly raised by this method.
        """
        return self._enharmonics.get(self._note_name) or next(
            (
                key
                for key, value in self._enharmonics.items()
                if value == self._note_name
            ),
            None,
        )
