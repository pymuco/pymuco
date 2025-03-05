# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         Tonality.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
from .ScientificPitchNotation import ScientificPitchNotation


class Tonality:
    """
    A class representing a musical tonality, defined by a root note and a
    tonality type.

    Parameters
    ----------
    root_note : ScientificPitchNotation
        The root note of the tonality, specified as a ScientificPitchNotation
        object.
    tonality_type : str
        The type of the tonality, such as "major" or "minor".

    Attributes
    ----------
    _root_note : ScientificPitchNotation
        The root note of the tonality.
    _tonality_type : str
        The type of the tonality.
    """

    def __init__(self, root_note: ScientificPitchNotation, tonality_type):
        self._root_note = root_note
        self._tonality_type = tonality_type
