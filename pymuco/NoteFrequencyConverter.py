# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         NoteFrequencyConverter.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .MIDIUtils import MIDINoteConverter
from .ScientificPitchNotation import ScientificPitchNotation


class NoteFrequencyConverter:
    """
    A utility class for converting between Scientific Pitch Notation
    (note names), MIDI note numbers, and frequencies.

    This class provides utility functions to convert between Scientific Pitch
    Notation (note names), MIDI note numbers, and frequencies. The class
    contains two static methods.

    Attributes
    ----------
    None

    Methods
    -------
    get_frequency_from_midi_number(note_number):
        Returns the corresponding frequency in Hz using the formula
        frequency = 440 * 2 ** ((note_number - 69) / 12).

        Parameters
        ----------
        note_number : int
            The MIDI note number to convert.

        Returns
        -------
        float
            The frequency in Hz.

    get_frequency_from_note_name(musical_note):
        Returns the corresponding frequency in Hz from a note name in
        Scientific Pitch Notation.

        Parameters
        ----------
        musical_note : str or ScientificPitchNotation
            The note name to convert. It can be either a string in
            Scientific Pitch Notation or an instance of ScientificPitchNotation
            class.

        Returns
        -------
        float
            The frequency in Hz.

        Raises
        ------
        ValueError
            If the musical_note argument is not a valid instance of
            ScientificPitchNotation class or a valid note name in Scientific
            Pitch Notation.

    Notes
    -----
    The class uses the MIDINoteConverter class from the MIDIUtils module to
    convert the note name to a MIDI note number. The returned frequency is
    rounded to 2 decimal places.
    """

    note_converter = MIDINoteConverter()

    @staticmethod
    def get_frequency_from_midi_number(note_number: int) -> float:
        """
        Given a MIDI note number, returns the corresponding frequency in Hz
        using the formula frequency = 440 * 2 ** ((note_number - 69) / 12)
        This formula is based on the equal temperament tuning system.

        Args:
        -----
        - note_number (int): MIDI note number (integer between 0 and 127)

        Returns:
        --------
        float: frequency in Hz
        """
        return round(440 * 2 ** ((note_number - 69) / 12), 2)

    @staticmethod
    def get_frequency_from_note_name(
        note_name: ScientificPitchNotation,
    ) -> float:
        """
        Given a note name in Scientific Pitch Notation, returns the
        corresponding frequency in Hz.

        Args:
        -----
        - note_name (str): note name in Scientific Pitch Notation
        (e.g. "C4", "A#3")

        Returns:
        --------
        float: frequency in Hz
        """
        if not isinstance(note_name, ScientificPitchNotation):
            raise ValueError(
                "Invalid argument: musical_note must be an instance of "
                "ScientificPitchNotation"
            )

        midi_note_number = (
            NoteFrequencyConverter.note_converter.note_name_to_midi_note(
                note_name
            )
        )
        if midi_note_number is None:
            raise ValueError(
                "Invalid note name. Please provide a valid note name in "
                "Scientific Pitch Notation (e.g. C4, A#3)"
            )

        return round(
            NoteFrequencyConverter.get_frequency_from_midi_number(
                midi_note_number
            ),
            2,
        )
