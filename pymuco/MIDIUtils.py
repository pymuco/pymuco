# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         MIDIUtils.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .NoteMapping import NoteMapping
from .ScientificPitchNotation import ScientificPitchNotation


class MIDINoteConverter:
    """
    The MIDINoteConverter class is used to convert note names represented in
    Scientific Pitch Notation to their corresponding MIDI note numbers, and
    vice versa.

    Attributes:
    -----------
    note_name_mapping (Dict[str, int]):
    A dictionary containing the mapping of note names to their corresponding
    MIDI pitch values.

    Methods:
    --------
    init(self):
    Initializes a MIDINoteConverter object by creating a dictionary of note
    names and their corresponding MIDI pitch values using the NoteMapping
    class. The resulting dictionary is stored as a private attribute of the
    object for use in other methods.

    note_name_to_midi_note(self, note_name: ScientificPitchNotation) -> int:
    Takes an instance of the ScientificPitchNotation class representing a note
    name, validates it, and returns its corresponding MIDI note number.

    midi_note_to_note_name(self, midi_note: int) -> str:
    Takes a MIDI note number, validates it, and returns the corresponding note
    name represented in Scientific Pitch Notation.

    _validate_note_name(self, note_name: ScientificPitchNotation) -> int:
    A helper method used to validate the note name input and return its
    corresponding MIDI pitch value. This method raises a ValueError if the
    input note name is not a valid note name.

    _validate_midi_note_range(self, midi_note: int) -> None:
    A helper method used to validate that the input MIDI note number is within
    the valid range of 0 to 127. This method raises a ValueError if the input
    MIDI note number is not within the valid range.

    The MIDINoteConverter class provides a convenient and reliable tool for
    converting between note names and MIDI note numbers in a Python project.
    It is designed to be used in conjunction with the ScientificPitchNotation
    class, and can be easily integrated into larger music software projects.
    """

    def __init__(self):
        """Initializes a MIDINoteConverter object.

        The method initializes the object by creating a dictionary of note
        names and their corresponding MIDI pitch values using the NoteMapping
        class. The resulting dictionary is stored as a private attribute of
        the object for use in other methods.

        Args:
            None
        Returns:
            None
        """
        self._note_name_mapping = NoteMapping().get_note_mapping()

    def note_name_to_midi_note(
        self, note_name: ScientificPitchNotation
    ) -> int:
        """Converts a note name represented in Scientific Pitch Notation to
        its corresponding MIDI note number.

        Args:
        -----
            note_name (ScientificPitchNotation): An instance of the
            ScientificPitchNotation class representing the note name to
            convert.

        Returns:
        --------
            int: The MIDI note number corresponding to the input note name.

        Raises:
        -------
            ValueError: If the input note_name argument is not an instance of
            the ScientificPitchNotation class or if the note name is not a
            valid note name.
        """
        if not isinstance(note_name, ScientificPitchNotation):
            raise ValueError(
                "Invalid argument: note_name must be an instance of"
                "ScientificPitchNotation"
            )

        midi_note = (
            int(note_name.octave) + 1
        ) * 12 + self._validate_note_name(note_name.pitch)
        self._validate_midi_note_range(midi_note)
        return midi_note

    def _validate_note_name(self, note_name: str) -> int:
        """Validates the input note name and returns its corresponding MIDI
        pitch value.

        Args:
        -----
            note_name (str): The note name to validate.

        Returns:
        --------
            int: The MIDI pitch value corresponding to the input note name.

        Raises:
        -------
            ValueError: If the input note name is not a valid note name.
        """
        if note_name not in self._note_name_mapping:
            raise ValueError(f"{note_name} is not a valid note name")
        return self._note_name_mapping[note_name]

    def midi_note_to_note_name(self, midi_note: int) -> str:
        """Converts a MIDI note number to its corresponding note name
        represented in Scientific Pitch Notation.

        Args:
        -----
            midi_note (int): The MIDI note number to convert.

        Returns:
        --------
            str: The note name represented in Scientific Pitch Notation
            corresponding to the input MIDI note number.

        Raises:
        -------
            ValueError: If the input MIDI note number is not within the valid
            range of 0 to 127.
        """
        self._validate_midi_note_range(midi_note)
        for note, value in self._note_name_mapping.items():
            if value == (midi_note % 12):
                return note + str(midi_note // 12 - 1)
        return "Invalid Note"

    def _validate_midi_note_range(self, midi_note):
        """Validates that the input MIDI note number is within the valid range
        of 0 to 127.

        Args:
        -----
            midi_note (int): The MIDI note number to validate.

        Raises:
        -------
            ValueError: If the input MIDI note number is not within the valid
            range of 0 to 127.
        """
        if not 0 <= midi_note <= 127:
            raise ValueError(f"{midi_note} is not a valid MIDI note number")
