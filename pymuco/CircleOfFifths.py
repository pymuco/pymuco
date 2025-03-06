# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         CircleOfFifths.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from typing import List, Tuple, Union, ClassVar

from .Enharmonic import Enharmonic
from .Interval import IntervalCalculator, IntervalName
from .MusicData import (
    DEFAULT_OCTAVE,
    FLAT,
    SHARP,
    C,
    D,
    E,
    F,
    G,
)
from .ScientificPitchNotation import ScientificPitchNotation


class CircleOfFifths:
    """
    A class representing the Circle of Fifths, which is a diagram used to show
    the relationships between the 12 tones of the chromatic scale. It also
    calculates the relative minors for each key in the Circle of Fifths.

    The Circle of Fifths is created in two parts:
    1. First half: From C to F#/Gb (sharps)
    2. Second half: From Gb/F# to C (flats)

    Attributes
    ----------
    _FIFTH_INTERVAL : ClassVar[IntervalName]
        The interval of a perfect fifth (7 semitones).
    _MINOR_THIRD : ClassVar[IntervalName]
        The interval of a minor third (3 semitones).
    _ENHARMONIC_INDEX : ClassVar[int]
        The index in the circle where enharmonic equivalents occur (F#/Gb).
    _TOTAL_NOTES : ClassVar[int]
        The total number of notes in the chromatic scale (12).
    circle_of_fifths : List[Union[str, List[str]]]
        The complete Circle of Fifths as a list of notes.
    relative_minors : List[Union[str, List[str]]]
        The relative minor keys for each note in the Circle of Fifths.

    Methods
    -------
    __init__() -> None:
        Initialize a new instance with the Circle of Fifths and its relative
        minors.

    _calculate_circle_of_fifths() -> Tuple[List[Union[str, List[str]]], 
        List[Union[str, List[str]]]]:
        Calculate the Circle of Fifths and its relative minors.

    _create_circle_of_fifths() -> List[Union[str, List[str]]]:
        Create the Circle of Fifths as a list of notes.

    _create_next_note_in_circle(current_note: Union[str, List[str]]) -> str:
        Calculate the next note in the Circle of Fifths.

    _create_relative_minors(circle_of_fifths: List[Union[str, List[str]]]) -> 
        List[Union[str, List[str]]]:
        Create relative minors for each key in the Circle of Fifths.

    _create_relative_minor(current_note_index: int, current_note: str) -> 
        Union[str, List[str]]:
        Create the relative minor for a given key.

    _handle_enharmonic(note: str) -> Union[str, List[str]]:
        Handle enharmonic equivalents of notes.

    _get_enharmonic_pair(sharp_note: str, flat_note: str) -> List[str]:
        Get the enharmonic pair of notes (e.g., F#/Gb).
    """

    _FIFTH_INTERVAL: ClassVar[IntervalName] = IntervalName(7)
    _MINOR_THIRD: ClassVar[IntervalName] = IntervalName(3)
    _ENHARMONIC_INDEX: ClassVar[int] = 6  # F#/Gb position
    _TOTAL_NOTES: ClassVar[int] = 12

    # Class constants for enharmonic mappings
    _ENHARMONIC_MAPPING = {
        'C#': 'Db',
        'D#': 'Eb',
        'F#': 'Gb',
        'G#': 'Ab',
        'A#': 'Bb',
    }

    def __init__(self) -> None:
        """Initialize a new instance with the Circle of Fifths and its relative
        minors.

        The initialization creates both the Circle of Fifths and calculates
        its relative minors. The Circle of Fifths is created in two parts:
        1. First half: From C to F#/Gb (sharps)
        2. Second half: From Gb/F# to C (flats)

        Args:
        -----
            None

        Returns:
        --------
            None

        Raises:
        -------
            None
        """
        (
            self.circle_of_fifths,
            self.relative_minors,
        ) = self._calculate_circle_of_fifths()

    def _calculate_circle_of_fifths(
        self,
    ) -> Tuple[List[Union[str, List[str]]], List[Union[str, List[str]]]]:
        """Calculate the Circle of Fifths and its relative minors.

        Args:
        -----
            self: An instance of the class.

        Returns:
        --------
            A tuple containing:
                - The Circle of Fifths as a list of notes
                - The relative minors for each key in the Circle of Fifths

        Raises:
        -------
            None
        """
        circle_of_fifths = self._create_circle_of_fifths()
        relative_minors = self._create_relative_minors(circle_of_fifths)
        return circle_of_fifths, relative_minors

    def _create_circle_of_fifths(self) -> List[Union[str, List[str]]]:
        """Create the Circle of Fifths as a list of notes.

        The circle is created in two parts:
        1. First half: From C to F#/Gb (sharps)
        2. Second half: From Gb/F# to C (flats)

        Args:
        -----
            self: An instance of the class.

        Returns:
        --------
            A list of notes representing the Circle of Fifths.

        Raises:
        -------
            None
        """
        circle_of_fifths = [C]
        
        # Create the first half of the circle (sharps)
        for i in range(self._ENHARMONIC_INDEX):
            next_note = self._create_next_note_in_circle(circle_of_fifths[i])
            circle_of_fifths.append(next_note)
        
        # Handle the enharmonic case (F#/Gb)
        circle_of_fifths[self._ENHARMONIC_INDEX] = self._get_enharmonic_pair(
            F, G
        )
        
        # Create the second half of the circle (flats)
        for i in range(self._ENHARMONIC_INDEX, self._TOTAL_NOTES - 1):
            next_note = self._create_next_note_in_circle(circle_of_fifths[i])
            # Handle enharmonic notes in the second half
            if i >= self._ENHARMONIC_INDEX:
                next_note = self._ENHARMONIC_MAPPING.get(next_note, next_note)
            circle_of_fifths.append(next_note)
            
        return circle_of_fifths

    def _get_enharmonic_pair(
        self, sharp_note: str, flat_note: str
    ) -> List[str]:
        """Get the enharmonic pair of notes (e.g., F#/Gb).

        Args:
        -----
            self: An instance of the class.
            sharp_note (str): The note that will be sharpened.
            flat_note (str): The note that will be flattened.

        Returns:
        --------
            A list containing the enharmonic pair of notes.

        Raises:
        -------
            None
        """
        return [sharp_note + SHARP, flat_note + FLAT]

    def _create_next_note_in_circle(
        self, current_note: Union[str, List[str]]
    ) -> str:
        """Calculate the next note in the Circle of Fifths.

        Args:
        -----
            self: An instance of the class.
            current_note: The current note or list of enharmonic notes.

        Returns:
        --------
            The next note in the Circle of Fifths.

        Raises:
        -------
            None
        """
        # If current_note is a list (enharmonic pair), use the first note
        note = current_note[0] if isinstance(current_note, list) else current_note
        
        fifth_interval = IntervalCalculator().calculate_ascending_interval(
            self._FIFTH_INTERVAL,
            ScientificPitchNotation(note, DEFAULT_OCTAVE),
        )
        return fifth_interval

    def _create_relative_minors(
        self, circle_of_fifths: List[Union[str, List[str]]]
    ) -> List[Union[str, List[str]]]:
        """Create relative minors for each key in the Circle of Fifths.

        Args:
        -----
            self: An instance of the class.
            circle_of_fifths: The Circle of Fifths as a list of notes.

        Returns:
        --------
            A list of relative minor keys for each note in the Circle of Fifths.

        Raises:
        -------
            None
        """
        return [
            self._create_relative_minor(index, note)
            for index, note in enumerate(circle_of_fifths)
        ]

    def _create_relative_minor(
        self, current_note_index: int, current_note: str
    ) -> Union[str, List[str]]:
        """Create the relative minor for a given key.

        Args:
        -----
            self: An instance of the class.
            current_note_index: The index of the current note in the Circle of
                Fifths.
            current_note: The current note.

        Returns:
        --------
            The relative minor key for the given note.

        Raises:
        -------
            None
        """
        if current_note_index == self._ENHARMONIC_INDEX:
            return self._get_enharmonic_pair(D, E)
            
        relative_minor = IntervalCalculator().calculate_descending_interval(
            self._MINOR_THIRD,
            ScientificPitchNotation(current_note, DEFAULT_OCTAVE),
        )
        
        if current_note_index < self._ENHARMONIC_INDEX:
            return self._handle_enharmonic(relative_minor)
        return relative_minor

    def _handle_enharmonic(self, note: str) -> Union[str, List[str]]:
        """Handle enharmonic equivalents of notes.

        Args:
        -----
            self: An instance of the class.
            note: The note to check for enharmonic equivalents.

        Returns:
        --------
            The enharmonic equivalent of the note if it exists, otherwise the
            original note.

        Raises:
        -------
            None
        """
        spn = ScientificPitchNotation(note, DEFAULT_OCTAVE)
        enharmonic = Enharmonic(spn)
        if enharmonic.is_enharmonic():
            return enharmonic.get_enharmonic().pitch
        return note
