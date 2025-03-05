# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         MusicComputationNotation.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from typing import List, Tuple

from .NoteDuration import NoteDuration
from .ScientificPitchNotation import ScientificPitchNotation


class MusicComputationNotation:
    """A class that represents a computational music notation capable of
    storing notes in blocks.

    Each block is comprised of a pitch and its corresponding duration.

    Attributes
    ----------
    notation : List[Tuple[ScientificPitchNotation, NoteDuration]]
        The notation as a list of tuples, where each tuple contains a
        ScientificPitchNotation object and a NoteDuration object.

    Methods
    -------
    add_block(pitch: ScientificPitchNotation, duration: NoteDuration):
        Add a block to the notation.
    remove_block(index: int):
        Remove a block from the notation.
    clear_notation():
        Clear the notation.

    Examples
    --------
    >>> notation = ComputationalNotation()
    >>> pitch = ScientificPitchNotation("C4")
    >>> duration = NoteDuration(4)
    >>> notation.add_block(pitch, duration)
    >>> notation.notation
    [(ScientificPitchNotation(octave=4, step='C', accidental=''),
    NoteDuration(value=4))]

    """

    def __init__(self):
        self._notation = []

    @property
    def notation(self) -> List[Tuple[ScientificPitchNotation, NoteDuration]]:
        """
        Returns the notation as a list of tuples.

        Returns:
        --------
            The notation as a list of tuples, where each tuple contains a
            ScientificPitchNotation object and a NoteDuration object.

        Return Type:
        ------------
            List[Tuple[ScientificPitchNotation, NoteDuration]]
        """
        return self._notation

    def add_block(self, *args):
        """
        Adds a block of notes to the notation.

        Args:
        -----
            *args: Variable-length argument list of pitch and duration pairs.
                Each pair should consist of a ScientificPitchNotation object
                and either a NoteDuration object or a number representing the
                duration in quarter notes.

        Raises:
        -------
            TypeError: If a pitch is not an instance of
            ScientificPitchNotation, if a duration is not an instance of
            NoteDuration (or a number), or if an invalid duration type is
            provided.

        Returns:
        --------
            None: This method does not return anything.
        """
        for i in range(0, len(args), 2):
            spn = args[i]
            duration = args[i + 1]
            if not isinstance(spn, ScientificPitchNotation):
                raise TypeError(
                    "Note pitch must be an instance of "
                    "ScientificPitchNotation."
                )
            if isinstance(duration, NoteDuration):
                duration = duration.duration_length
            elif isinstance(duration, (int, float)):
                raise TypeError(
                    "Duration must be an instance of NoteDuration."
                )
            else:
                raise TypeError("Invalid duration type.")
            self._notation.append((spn.spn, duration))
