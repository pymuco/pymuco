# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         EnharmonicMapping.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .MusicData import (
    DOUBLE_FLAT,
    DOUBLE_SHARP,
    FLAT,
    NATURAL,
    SHARP,
    Accidental,
    B,
    C,
    E,
    F,
    MusicalAlphabet,
)

_NOTE_NAME = MusicalAlphabet.get_note_name()
_ACCIDENTAL = Accidental.get_accidental()


class EnharmonicMapping:
    def enharmonic_mapping(self):
        """
        Computes the enharmonic mapping of the notes in the current key.

        Returns a dictionary that maps each note name with its accidental to
        its enharmonic equivalent.

        The enharmonic equivalents are computed according to the following
        rules:

        * A double sharp note is mapped to the next note in the circle of
        fifths with a sharp.
        * A sharp note is mapped to the next note in the circle of fifths with
        a flat.
        * A natural note is mapped to itself.
        * A flat note is mapped to the previous note in the circle of fifths
        with a sharp.
        * A double flat note is mapped to the previous note in the circle of
        fifths with a flat.

        If a note name with a given accidental does not have an enharmonic
        equivalent according to these rules, it is not included in the output
        dictionary.

        The mapping is based on the current key, which is determined by the
        instance variables of the class.

        Returns
        -------
        dict
            A dictionary that maps note names with accidentals to their
            enharmonic equivalents.

        Examples
        --------
        >>> key = Key('C', ScaleType.MAJOR)
        >>> enharmonic_mapping = key.get_enharmonic_mapping()
        >>> enharmonic_mapping
        {'C': 'C', 'C#': 'Db', 'D': 'D', 'D#': 'Eb', 'E': 'E', 'F': 'F',
        'F#': 'Gb', 'G': 'G', 'G#': 'Ab', 'A': 'A', 'A#': 'Bb', 'B': 'B'}

        Notes
        -----
        The mapping is based on the current key, which is determined by the
        instance variables of the class.

        """
        notes = {}
        i = 0
        for note in _NOTE_NAME:
            for accidental in _ACCIDENTAL:
                if accidental == DOUBLE_SHARP:
                    if note in [B, E]:
                        if accidental == DOUBLE_SHARP:
                            notes[note + accidental] = (
                                _NOTE_NAME[(i + 1) % len(_NOTE_NAME)] + SHARP
                            )
                    else:
                        notes[note + accidental] = _NOTE_NAME[
                            (i + 1) % len(_NOTE_NAME)
                        ]
                elif accidental == SHARP:
                    if note in [B, E]:
                        if accidental == SHARP:
                            notes[note + accidental] = _NOTE_NAME[
                                (i + 1) % len(_NOTE_NAME)
                            ]
                    else:
                        notes[note + accidental] = (
                            _NOTE_NAME[(i + 1) % len(_NOTE_NAME)] + FLAT
                        )
                elif accidental == NATURAL:
                    notes[note + accidental] = note
                elif accidental == FLAT:
                    if note in [C, F]:
                        if accidental == FLAT:
                            notes[note + accidental] = _NOTE_NAME[
                                (i - 1) % len(_NOTE_NAME)
                            ]
                    else:
                        notes[note + accidental] = (
                            _NOTE_NAME[(i - 1) % len(_NOTE_NAME)] + SHARP
                        )
                elif accidental == DOUBLE_FLAT:
                    if note in [C, F]:
                        if accidental == DOUBLE_FLAT:
                            notes[note + accidental] = (
                                _NOTE_NAME[(i - 1) % len(_NOTE_NAME)] + FLAT
                            )
                    else:
                        notes[note + accidental] = _NOTE_NAME[
                            (i - 1) % len(_NOTE_NAME)
                        ]
            i += 1
        return notes
