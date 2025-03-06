# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         __init__.py
# Purpose:      Pymuco Package
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .AudioConverter import AudioConverter
from .Chord import Chord, ChordType
from .CircleOfFifths import CircleOfFifths
from .Enharmonic import Enharmonic
from .EnharmonicMapping import EnharmonicMapping
from .Interval import Interval, IntervalCalculator, IntervalName
from .KeySignature import KeySignature
from .MIDIUtils import MIDINoteConverter
from .MidiGenerator import MidiGenerator
from .MusicComputationNotation import MusicComputationNotation
from .MusicData import (
    ACCIDENTALS,
    DEFAULT_OCTAVE,
    FLAT,
    MAJOR,
    MINOR,
    M,
    m,
    NOTE_NAMES,
    SHARP,
    C,
    G
)
from .NoteDuration import NoteDuration, NoteDurationMapping
from .NoteFrequencyConverter import NoteFrequencyConverter
from .NoteMapping import NoteMapping
from .Player import Player
from .Scale import Scale, ScaleData
from .ScientificPitchNotation import ScientificPitchNotation
from .Tonality import Tonality

__version__ = "1.1.6"

__all__ = [
    "AudioConverter",
    "Chord",
    "ChordType",
    "CircleOfFifths",
    "Enharmonic",
    "EnharmonicMapping",
    "Interval",
    "IntervalCalculator",
    "IntervalName",
    "KeySignature",
    "MIDINoteConverter",
    "MidiGenerator",
    "MusicComputationNotation",
    "NoteDuration",
    "NoteDurationMapping",
    "NoteFrequencyConverter",
    "NoteMapping",
    "Player",
    "Scale",
    "ScaleData",
    "ScientificPitchNotation",
    "Tonality",
    # Constants
    "ACCIDENTALS",
    "DEFAULT_OCTAVE",
    "FLAT",
    "MAJOR",
    "MINOR",
    "M",
    "m",
    "NOTE_NAMES",
    "SHARP",
    "C",
    "G"
] 