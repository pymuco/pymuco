# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         Interval.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from enum import IntEnum

from .Enharmonic import Enharmonic
from .NoteFrequencyConverter import NoteFrequencyConverter
from .NoteMapping import NoteMapping
from .ScientificPitchNotation import ScientificPitchNotation


class IntervalName(IntEnum):
    """
    This is a Python class called "IntervalName" that inherits from the
    IntEnum class. It is used to represent the names of different musical
    intervals. The class defines several class variables, each with a name and
    a value in semitones. For example, the UNISON variable has a value of 0,
    and the MINOR_SECOND variable has a value of 1.
    """

    UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    TRITONE = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    OCTAVE = 12
    MINOR_NINTH = 13
    MAJOR_NINTH = 14
    MINOR_TENTH = 15
    MAJOR_TENTH = 16
    PERFECT_ELEVENTH = 17
    DIMINISHED_TWELFTH = 18
    AUGMENTED_ELEVENTH = 19
    PERFECT_TWELFTH = 20
    MINOR_THIRTEENTH = 21
    MAJOR_THIRTEENTH = 22
    MINOR_FOURTEENTH = 23
    MAJOR_FOURTEENTH = 24
    DOUBLE_OCTAVE = 25


class Interval:
    """
    Represents an interval between two notes.

    Attributes
    ----------
    _low_note : ScientificPitchNotation
        The lower note of the interval.
    _high_note : ScientificPitchNotation
        The higher note of the interval.
    _semitones : int
        The number of semitones between the two notes.

    Methods
    -------
    low_note() -> ScientificPitchNotation:
        Returns the lower note of the interval.
    high_note() -> ScientificPitchNotation:
        Returns the higher note of the interval.
    get_interval_name() -> str:
        Returns the name of the interval.
    get_interval_direction() -> bool:
        Returns whether the interval is ascending or descending.
    get_interval_inversion() -> str:
        Returns the name of the interval after inverting the notes.
    """

    def __init__(
        self,
        low_note: ScientificPitchNotation,
        high_note: ScientificPitchNotation,
    ):
        """
        Initialize an Interval object with the given lower and higher notes.

        Parameters
        ----------
        low_note : ScientificPitchNotation
            The lower note of the interval.
        high_note : ScientificPitchNotation
            The higher note of the interval.

        Attributes
        ----------
        _low_note : ScientificPitchNotation
            The lower note of the interval.
        _high_note : ScientificPitchNotation
            The higher note of the interval.
        _semitones : int
            The number of semitones between the two notes.

        Returns
        -------
        None
        """
        self._low_note = low_note
        self._high_note = high_note
        self._semitones = self._get_semitones()

    @property
    def low_note(self):
        return self._low_note

    @property
    def high_note(self):
        return self._high_note

    def get_interval_name(self):
        """
        Get the name of the interval.

        Returns
        -------
        str
            The name of the interval between the lower and higher notes of this
            Interval object.

        Raises
        ------
        None
            This method does not raise any exceptions.
        """
        return IntervalName(self._semitones).name

    def get_interval_direction(self):
        """
        Determine the direction of the interval between the lower and higher
        notes of this Interval object.

        Returns
        -------
        bool
            True if the interval is ascending, False if the interval is
            descending.

        Raises
        ------
        None
        """
        return self._verify_interval_direction()

    def get_interval_inversion(self):
        """
        Returns the name of the inverted interval between the lower and higher
        notes of this Interval object.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The name of the inverted interval as a string.

        Raises
        ------
        ValueError
            If the interval direction is neither ascending nor descending, or
            if the interval is greater than an octave.

        Notes
        -----
        If the interval direction is ascending, the lower note is raised by one
        octave and becomes the new higher note, while the higher note becomes
        the new lower note. If the interval direction is descending, the higher
        note is lowered by one octave and becomes the new lower note, while the
        lower note becomes the new higher note. The name of the inverted
        interval is determined by the number of semitones between the inverted
        notes.
        """
        interval_direction = self._verify_interval_direction()
        if interval_direction is True:
            self._low_note.octave += 1
            self._low_note, self._high_note = self._high_note, self._low_note
            semitones = self._get_semitones()
            interval_name = IntervalName(semitones)
            return interval_name.name.replace("_", " ")
        elif interval_direction is False:
            self._low_note.octave -= 1
            self._low_note, self._high_note = self._high_note, self._low_note
            semitones = self._get_semitones()
            interval_name = IntervalName(semitones)
            return interval_name.name.replace("_", " ")
        else:
            raise ValueError("Invalid interval.")

    def _get_semitones(self):
        """
        Calculates the number of semitones between the lower and higher notes
        of this Interval object.

        Args:
            None

        Returns:
            int: The number of semitones between the lower and higher notes as
            an integer.

        Raises:
            ValueError: If the interval between the notes is greater than an
            octave.
        """
        # Get note name mapping
        note_name_mapping = NoteMapping().get_note_mapping()
        # Get octave and pitch of lower and higher notes
        octave1 = self._low_note.octave
        octave2 = self._high_note.octave
        pitch1 = self._low_note.pitch
        pitch2 = self._high_note.pitch
        # Calculate the number of semitones
        semitones1 = note_name_mapping[pitch1]
        semitones2 = note_name_mapping[pitch2]
        semitones = (semitones2 - semitones1) + (octave2 - octave1) * 12
        if semitones < 0:
            return abs(semitones)
        # Raise an error if the interval is greater than an octave
        if semitones > 12:
            raise ValueError("Interval too large")
        else:
            return semitones

    def _verify_interval_direction(self):
        """
        This method verifies the direction of the interval between the low note
        and the high note of the Interval object. It returns a boolean value
        indicating whether the interval is ascending or descending.

        Returns:
        bool: True if the interval is ascending, False if the interval is
        descending.
        """
        note1_frequency = (
            NoteFrequencyConverter().get_frequency_from_note_name(
                self._low_note
            )
        )
        note2_frequency = (
            NoteFrequencyConverter().get_frequency_from_note_name(
                self._high_note
            )
        )
        if note1_frequency > note2_frequency:
            # Descending
            return False
        else:
            # Ascending
            return True


class IntervalCalculator:
    """
    The IntervalCalculator class provides methods for calculating intervals
    between notes, given a root note and an interval name.

    Parameters
    ----------
    None

    Attributes
    ----------
    None

    Methods
    -------
    calculate_ascending_interval(interval_name: IntervalName, root_note:
    ScientificPitchNotation) -> str:
        Calculates the interval between a root note and a note that is a given
        interval above the root note. Returns the name of the interval in
        string format.

    calculate_descending_interval(interval_name: IntervalName,
    root_note: ScientificPitchNotation) -> str:
        Calculates the interval between a root note and a note that is a given
        interval below the root note. Returns the name of the interval in
        string format.

    Notes
    -----
    The class uses a note name mapping to convert note names to numerical
    values, which are used to calculate the interval. The class also uses the
    Enharmonic class to calculate enharmonic equivalents of intervals.

    Examples
    --------
    To calculate an ascending interval:

    >>> ic = IntervalCalculator()
    >>> interval_name = IntervalName('M3')
    >>> root_note = ScientificPitchNotation('C4')
    >>> ic.calculate_ascending_interval(interval_name, root_note)
    'E4'

    To calculate a descending interval:

    >>> ic = IntervalCalculator()
    >>> interval_name = IntervalName('P5')
    >>> root_note = ScientificPitchNotation('A4')
    >>> ic.calculate_descending_interval(interval_name, root_note)
    'D4'

    """

    _NOTE_NAME_MAPPING = NoteMapping().get_note_mapping()

    def calculate_ascending_interval(
        self, interval_name: IntervalName, root_note: ScientificPitchNotation
    ):
        """
        Calculate the pitch of a note ascending a certain interval from a given
        root note.

        Parameters
        interval_name : IntervalName
        An instance of the IntervalName class representing the desired
        interval.
        root_note : ScientificPitchNotation
        An instance of the ScientificPitchNotation class representing the root
        note.

        Returns
        str
        The pitch of the note ascending the specified interval from the root
        note, as a string.

        Raises
        None

        Notes
        The method first retrieves the index of the root note in the mapping of
        note names to their corresponding indices. It then calculates the index
        of the note that is the specified interval above the root note, taking
        into account that the interval should wrap around to the beginning of
        the octave if necessary.

        Next, it retrieves the pitch of the note at the calculated index from
        the mapping of note names to their corresponding pitches. If the note
        name has a double sharp (x) or double flat (𝄫) accidental, the method
        replaces the note name with the appropriate enharmonic equivalent.

        Finally, if the root note and calculated note have different accidental
        markings, the method replaces the note name with the appropriate
        enharmonic equivalent. The method returns the resulting note name as a
        string.
        """
        root_note_str = str(root_note.pitch)
        root_note_index = self._NOTE_NAME_MAPPING[root_note_str]
        ascending_interval_index = (root_note_index + interval_name.value) % 12

        ascending_interval = [
            k
            for k, v in self._NOTE_NAME_MAPPING.items()
            if v == ascending_interval_index
        ][0]

        if len(ascending_interval) > 1 and ascending_interval[1] in ["x"]:
            ascending_interval = [
                k
                for k, v in self._NOTE_NAME_MAPPING.items()
                if v == ascending_interval_index
            ][1]
        elif len(ascending_interval) > 1 and ascending_interval[1] in ["𝄫"]:
            ascending_interval = [
                k
                for k, v in self._NOTE_NAME_MAPPING.items()
                if v == ascending_interval_index
            ][-1]

        # enharmonic from here
        if len(ascending_interval) == 1 and len(root_note_str) == 1:
            return ascending_interval

        elif ascending_interval[-1] == "#" and root_note_str[-1] == "𝄫":
            ascending_interval = (
                Enharmonic(ScientificPitchNotation(ascending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        elif ascending_interval[-1] == "#" and root_note_str[-1] == "b":
            ascending_interval = (
                Enharmonic(ScientificPitchNotation(ascending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        elif ascending_interval[-1] == "b" and root_note_str[-1] == "#":
            ascending_interval = (
                Enharmonic(ScientificPitchNotation(ascending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        return ascending_interval

    def calculate_descending_interval(
        self, interval_name: IntervalName, root_note: ScientificPitchNotation
    ):
        """
        Calculate the descending interval between a root note and a given
        interval name and return the resulting note as a string in scientific
        pitch notation.

        Parameters
        ----------
        interval_name : IntervalName
            An instance of the IntervalName class representing the desired
            interval.
        root_note : ScientificPitchNotation
            An instance of the ScientificPitchNotation class representing the
            root note for the interval calculation.

        Returns
        -------
        str
            The pitch of the note descending the specified interval from the
            root note, as a string in scientific pitch notation.

        Raises
        ------
        ValueError
            If the root_note is not a valid scientific pitch notation.

        Notes
        -----
        The method first converts the root_note to a string and looks up its
        corresponding index in the _NOTE_NAME_MAPPING dictionary. It then
        calculates the index of the desired descending interval using the given
        interval_name and the index of the root_note. The method retrieves the
        string representation of the resulting note by searching the
        _NOTE_NAME_MAPPING dictionary for the note with the calculated index.

        The method then applies enharmonic equivalents to the resulting note if
        needed. If the note has only one character, the method immediately
        returns it. Otherwise, it checks the last character of the root_note
        and the resulting note to see if they need to be enharmonically
        adjusted. If an adjustment is necessary, the method creates a
        ScientificPitchNotation object for the resulting note, applies the
        get_enharmonic method of the Enharmonic class to it, and converts the
        resulting object back to a string in ScientificPitchNotation format.

        Examples
        --------
        >>> from music_theory.interval_name import IntervalName
        >>> from music_theory.scientific_pitch_notation import
        ScientificPitchNotation
        >>> from music_theory.interval_calculator import IntervalCalculator
        >>> root_note = ScientificPitchNotation.from_pitch_string('C4')
        >>> interval_name = IntervalName.MAJOR_THIRD
        >>> interval_calculator = IntervalCalculator()
        >>> interval_calculator.calculate_descending_interval(interval_name,
        root_note)
        'A3'"""

        root_note_str = str(root_note.pitch)
        root_note_index = self._NOTE_NAME_MAPPING[root_note_str]
        descending_interval_index = (
            root_note_index - interval_name.value
        ) % 12

        descending_interval = [
            k
            for k, v in self._NOTE_NAME_MAPPING.items()
            if v == descending_interval_index
        ][0]

        if len(descending_interval) > 1 and descending_interval[1] in ["x"]:
            descending_interval = [
                k
                for k, v in self._NOTE_NAME_MAPPING.items()
                if v == descending_interval_index
            ][1]
        elif len(descending_interval) > 1 and descending_interval[1] in ["𝄫"]:
            descending_interval = [
                k
                for k, v in self._NOTE_NAME_MAPPING.items()
                if v == descending_interval_index
            ][-1]

        # enharmonic from here
        if len(descending_interval) == 1:
            return descending_interval

        elif len(root_note_str) == 1 and descending_interval[-1] == "#":
            descending_interval = (
                Enharmonic(ScientificPitchNotation(descending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        elif descending_interval[-1] == "#" and root_note_str[-1] == "𝄫":
            descending_interval = (
                Enharmonic(ScientificPitchNotation(descending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        elif descending_interval[-1] == "#" and root_note_str[-1] == "b":
            descending_interval = (
                Enharmonic(ScientificPitchNotation(descending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        elif descending_interval[-1] == "b" and root_note_str[-1] == "#":
            descending_interval = (
                Enharmonic(ScientificPitchNotation(descending_interval, 4))
                .get_enharmonic()
                .pitch
            )

        return descending_interval
