# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         Chord.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from enum import Enum

from .CircleOfFifths import CircleOfFifths
from .Enharmonic import Enharmonic
from .Interval import IntervalCalculator, IntervalName
from .KeySignature import KeySignature
from .MusicData import DEFAULT_OCTAVE, m
from .ScientificPitchNotation import ScientificPitchNotation


class ChordType(Enum):
    """
    An enumeration class that represents the type of a chord.

    Attributes:
    -----------
        MAJOR (Tuple[IntervalName]): A major chord represented by a tuple of
        intervals, consisting of a major third and perfect fifth.
        MINOR (Tuple[IntervalName]): A minor chord represented by a tuple of
        intervals, consisting of a minor third and perfect fifth.
        DIMINISHED (Tuple[IntervalName]): A diminished chord represented by a
        tuple of intervals, consisting of a minor third and tritone.
        AUGMENTED (Tuple[IntervalName]): An augmented chord represented by a
        tuple of intervals, consisting of a major third and minor sixth.
        MAJOR_SEVENTH (Tuple[IntervalName]): A major seventh chord represented
        by a tuple of intervals, consisting of a major third, perfect fifth,
        and major seventh.
        MINOR_SEVENTH (Tuple[IntervalName]): A minor seventh chord represented
        by a tuple of intervals, consisting of a minor third, perfect fifth,
        and minor seventh.
        DOMINANT_SEVENTH (Tuple[IntervalName]): A dominant seventh chord
        represented by a tuple of intervals, consisting of a major third,
        perfect fifth, and minor seventh.
        HALF_DIMINISHED (Tuple[IntervalName]): A half-diminished chord
        represented by a tuple of intervals, consisting of a minor third,
        tritone, and minor seventh.
        SUSPENDED_SECOND (Tuple[IntervalName]): A suspended second chord
        represented by a tuple of intervals, consisting of a major second and
        perfect fifth.
        SUSPENDED_FOURTH (Tuple[IntervalName]): A suspended fourth chord
        represented by a tuple of intervals, consisting of a perfect fourth
        and perfect fifth.
    """

    MAJOR = (IntervalName.MAJOR_THIRD, IntervalName.PERFECT_FIFTH)
    MINOR = (IntervalName.MINOR_THIRD, IntervalName.PERFECT_FIFTH)
    DIMINISHED = (IntervalName.MINOR_THIRD, IntervalName.TRITONE)
    AUGMENTED = (IntervalName.MAJOR_THIRD, IntervalName.MINOR_SIXTH)
    MAJOR_SEVENTH = (
        IntervalName.MAJOR_THIRD,
        IntervalName.PERFECT_FIFTH,
        IntervalName.MAJOR_SEVENTH,
    )
    MINOR_SEVENTH = (
        IntervalName.MINOR_THIRD,
        IntervalName.PERFECT_FIFTH,
        IntervalName.MINOR_SEVENTH,
    )
    DOMINANT_SEVENTH = (
        IntervalName.MAJOR_THIRD,
        IntervalName.PERFECT_FIFTH,
        IntervalName.MINOR_SEVENTH,
    )
    HALF_DIMINISHED = (
        IntervalName.MINOR_THIRD,
        IntervalName.TRITONE,
        IntervalName.MINOR_SEVENTH,
    )
    SUSPENDED_SECOND = (IntervalName.MAJOR_SECOND, IntervalName.PERFECT_FIFTH)
    SUSPENDED_FOURTH = (
        IntervalName.PERFECT_FOURTH,
        IntervalName.PERFECT_FIFTH,
    )


class Chord:
    """
    Represents a musical chord, defined by a root note and a chord type.

    Attributes
    ----------
    _CIRCLE_OF_FIFTHS : list of str
        A list of notes in the circle of fifths.
    _RELATIVE_MINORS : list of str
        A list of relative minor notes.

    Methods
    -------
    __init__(root_note, chord_type)
        Initializes a new Chord object with the specified root note and chord
        type.

        Parameters
        ----------
        root_note : ScientificPitchNotation
            The root note of the chord.
        chord_type : ChordType
            The type of the chord.

    get_chord_notes()
        Returns the notes of the chord represented by this object.

        Returns
        -------
        list of str
            The notes of the chord.

    _calculate_chord()
        Calculates the notes of the chord represented by this object.

    _calculate_chord_notes()
        Calculates the notes of the chord based on its root note and chord
        type.
    """

    _CIRCLE_OF_FIFTHS = CircleOfFifths().circle_of_fifths
    _RELATIVE_MINORS = CircleOfFifths().relative_minors

    def __init__(
        self, root_note: ScientificPitchNotation, chord_type: ChordType
    ):
        """
        Initializes a new Chord object with the specified root note and chord
        type.

        Args:
        -----
        - root_note: The root note of the chord, specified as a
        ScientificPitchNotation object.
        - chord_type: The type of chord, specified as a ChordType enumeration
        value.
        """
        self._root_note = root_note
        self._chord_type = chord_type

    def get_chord_notes(self):
        """
        Returns the notes of the chord represented by this object.
        If the root note is a relative minor or a note in the circle of fifths,
        returns the chord as calculated by _calculate_chord(). Otherwise,
        returns the chord notes as calculated by _calculate_chord_notes().
        """
        if self._root_note.pitch not in (
            self._RELATIVE_MINORS + self._CIRCLE_OF_FIFTHS
        ):
            return self._calculate_chord_notes()
        else:
            return self._calculate_chord()

    def _calculate_chord(self):
        """
        Calculates the notes of the chord represented by this object by first
        calculating the chord notes using the _calculate_chord_notes method,
        and then transposing them to match the key signature of the chord.

        Returns:
        --------
        - A list of the notes of the chord, transposed to match the key
        signature.
        """
        notes = self._calculate_chord_notes()

        chord_type_name = []
        for key in ChordType.__members__:
            chord_type_name.append(key)

        if self._chord_type.name in chord_type_name:
            if self._chord_type.name == "SUSPENDED_FOURTH":
                return self._calculate_chord_notes()

            if (
                KeySignature(
                    self._root_note,
                    self._chord_type.value[0].name.split("_")[0],
                ).get_key_signature_notes()
                is None
            ):
                key_signature_notes = KeySignature(
                    self._root_note, m
                ).get_key_signature_notes()
            else:
                key_signature_notes = KeySignature(
                    self._root_note,
                    self._chord_type.value[0].name.split("_")[0],
                ).get_key_signature_notes()

            if key_signature_notes is None:
                return notes

            for note in notes:
                for key in key_signature_notes:
                    if (
                        Enharmonic(
                            ScientificPitchNotation(note, DEFAULT_OCTAVE)
                        ).is_enharmonic()
                        is True
                    ):
                        if (
                            Enharmonic(
                                ScientificPitchNotation(note, DEFAULT_OCTAVE)
                            )
                            .get_enharmonic()
                            .pitch
                            == key
                        ):
                            notes[notes.index(note)] = key

        return notes

    def _calculate_chord_notes(self):
        """Calculates the notes of the chord based on its root note and chord
        type.

        Returns:
        --------
            A list of Note objects representing the notes of the chord.
        """
        interval = IntervalCalculator()
        notes = [self._root_note.pitch] + [
            interval.calculate_ascending_interval(
                interval_name, self._root_note
            )
            for interval_name in self._chord_type.value
        ]
        return notes
