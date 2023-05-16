# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         NoteDuration.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
class NoteDurationMapping:
    """
    A class for mapping note duration names to their corresponding values.

    Attributes
    ----------
    _DURATION_NAME : list of str
    A list of note duration names in order of descending duration, from longest
    to shortest.

    Methods
    -------
    get_note_duration() -> List[Tuple[str, float]]:
    Returns a list of tuples, where each tuple contains a note duration name
    and its corresponding value. The list is sorted in descending order of
    duration, from longest to shortest.

    Examples
    --------
    To get a list of note durations and their values:
    >>> NoteDurationMapping.get_note_duration()
    [('WHOLE_NOTE', 1.0), ('HALF_NOTE', 0.5), ('QUARTER_NOTE', 0.25),
    ('EIGHTH_NOTE', 0.125), ('SIXTEENTH_NOTE', 0.0625),
    ('THIRTY_SECOND_NOTE', 0.03125)]
    """

    _DURATION_NAME = [
        "WHOLE_NOTE",
        "HALF_NOTE",
        "QUARTER_NOTE",
        "EIGHTH_NOTE",
        "SIXTEENTH_NOTE",
        "THIRTY_SECOND_NOTE",
    ]

    @staticmethod
    def get_note_duration():
        """
        Get a list of tuples that maps note duration names to their
        corresponding values.

        Returns:
        --------
            A list of tuples, where each tuple contains a note duration name
            and its corresponding value. The list is sorted in descending order
            of duration, from longest to shortest.

        Example:
        --------
            >>> NoteDurationMapping.get_note_duration()
            [('WHOLE_NOTE', 1.0),
             ('HALF_NOTE', 0.5),
             ('QUARTER_NOTE', 0.25),
             ('EIGHTH_NOTE', 0.125),
             ('SIXTEENTH_NOTE', 0.0625),
             ('THIRTY_SECOND_NOTE', 0.03125)]
        """
        duration_value = 1.0
        duration_name = NoteDurationMapping._DURATION_NAME[0]
        result = [(duration_name, duration_value)]
        for duration_name in NoteDurationMapping._DURATION_NAME[1:]:
            duration_value /= 2
            result.append((duration_name, duration_value))
        return result


class NoteDuration:
    """
    Class representing the duration of a musical note.

    This class provides functionality for working with note durations in both
    string and float formats. Users can create a new NoteDuration object by
    passing in a duration as either a string or a float. The string format
    accepts note duration names, such as "quarter" or "eighth", and the float
    format accepts decimal values, such as 0.25 or 0.125.

    Attributes:
    -----------
    duration_type : str
    The name of the note duration.
    duration_length : float
    The duration of the note in beats.

    Methods:
    --------
    init(duration: Union[str, float]) -> None
    Initializes a new NoteDuration object.
    validate_duration(duration: Union[str, float]) -> float
    Validates the user input and returns a float duration value in beats.
    get_duration_type(duration: float) -> str
    Returns the name of the note duration given a duration length in beats.
    get_duration_length(duration_type: str) -> float
    Returns the duration length in beats given a note duration name.

    Raises:
    -------
    InvalidDurationError
    If an invalid duration is used.
    """

    _NOTE_DURATION = NoteDurationMapping.get_note_duration()
    """This constant holds a list of tuples containing the names and values of
    different note durations. The first item of each tuple is a string
    representing the name of the note duration, and the second item is the
    value associated with that duration."""

    def __init__(self, duration):
        """
        Initialize a new NoteDuration object.

        Parameters
        ----------
        duration : Union[str, float]
            The duration of the note. It can be a string with the name of the
            duration (e.g. "quarter") or a float with the duration length
            (e.g. 0.25).

        Raises
        ------
        ValueError
            If duration is not a string or a float.

        """
        if isinstance(duration, str):
            self._duration_type = self._validate_duration_type(duration)
            self._duration_length = next(
                (
                    duration
                    for name, duration in self._NOTE_DURATION
                    if name == self._duration_type
                ),
                None,
            )
        elif isinstance(duration, float):
            self._duration_length = self._validate_duration_length(duration)
            self._duration_type = self._get_type_by_duration_length(
                self._duration_length
            )
        else:
            raise ValueError("Duration must be a string or float")

    @classmethod
    def _validate_duration_type(cls, duration_type: str) -> str:
        """
        Validate that the duration type is allowed.

        Parameters
        ----------
        duration_type : str
            The type of the duration to validate.

        Returns
        -------
        str
            The duration type if it's valid.

        Raises
        ------
        InvalidDurationError
            If the duration type is not valid.

        """
        if duration_type not in [
            name for name, duration in cls._NOTE_DURATION
        ]:
            raise InvalidDurationError(
                f"Invalid duration type: {duration_type}"
            )
        return duration_type

    @classmethod
    def _validate_duration_length(cls, duration_length: float) -> float:
        """
        Validate that the duration length is allowed.

        Parameters
        ----------
        duration_length : float
            The length of the duration to validate.

        Returns
        -------
        float
            The duration length if it's valid.

        Raises
        ------
        InvalidDurationError
            If the duration length is not valid.

        """
        if duration_length not in [
            duration for name, duration in cls._NOTE_DURATION
        ]:
            raise InvalidDurationError(
                f"Invalid duration length: {duration_length}"
            )
        return duration_length

    @classmethod
    def _get_type_by_duration_length(cls, duration_length: float) -> str:
        """
        Get the duration type by the duration length.

        Parameters
        ----------
        duration_length : float
            The length of the duration to validate.

        Returns
        -------
        str
            The duration type if it's valid.

        Raises
        ------
        InvalidDurationError
            If the duration length is not valid.

        """
        duration_name = next(
            (
                name
                for name, duration in cls._NOTE_DURATION
                if duration == duration_length
            ),
            None,
        )
        if duration_name is None:
            raise InvalidDurationError(
                f"Invalid duration length: {duration_length}"
            )
        return duration_name

    @property
    def duration_type(self) -> str:
        return self._duration_type

    @property
    def duration_length(self) -> float:
        if self._duration_length is None:
            raise InvalidDurationError("Invalid duration length")
        return self._duration_length


class InvalidDurationError(ValueError):
    """
    Exception raised when an invalid duration is used.
    """

    pass
