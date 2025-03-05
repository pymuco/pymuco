from .AudioConverter import AudioConverter
from .Chord import Chord, ChordType
from .CircleOfFifths import CircleOfFifths
from .Enharmonic import Enharmonic
from .EnharmonicMapping import EnharmonicMapping
from .Interval import Interval
from .KeySignature import KeySignature
from .MIDIUtils import MIDINoteConverter
from .MidiGenerator import MidiGenerator
from .MusicComputationNotation import MusicComputationNotation
from .MusicData import (
    MusicalAlphabet,
    Accidental,
    NOTE_NAMES,
    A, B, C, D, E, F, G,
    ACCIDENTALS,
    DOUBLE_SHARP, SHARP, NATURAL, FLAT, DOUBLE_FLAT,
    DEFAULT_OCTAVE,
    M, m,
    MAJOR, MINOR
)
from .NoteDuration import NoteDuration
from .NoteFrequencyConverter import NoteFrequencyConverter
from .NoteMapping import NoteMapping
from .Player import Player
from .Scale import Scale
from .ScientificPitchNotation import ScientificPitchNotation
from .Tonality import Tonality

__version__ = "1.1.2"

__all__ = [
    'AudioConverter',
    'Chord',
    'ChordType',
    'CircleOfFifths',
    'Enharmonic',
    'EnharmonicMapping',
    'Interval',
    'KeySignature',
    'MIDINoteConverter',
    'MidiGenerator',
    'MusicComputationNotation',
    'MusicalAlphabet',
    'Accidental',
    'NOTE_NAMES',
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'ACCIDENTALS',
    'DOUBLE_SHARP', 'SHARP', 'NATURAL', 'FLAT', 'DOUBLE_FLAT',
    'DEFAULT_OCTAVE',
    'M', 'm',
    'MAJOR', 'MINOR',
    'NoteDuration',
    'NoteFrequencyConverter',
    'NoteMapping',
    'Player',
    'Scale',
    'ScientificPitchNotation',
    'Tonality',
] 