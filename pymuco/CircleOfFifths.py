from typing import List, Tuple

from Enharmonic import Enharmonic
from Interval import IntervalCalculator, IntervalName
from MusicData import DEFAULT_OCTAVE, FLAT, SHARP, C, D, E, F, G
from ScientificPitchNotation import ScientificPitchNotation


class CircleOfFifths:
    """
    A class representing the Circle of Fifths, which is a diagram used to show
    the relationships between the 12 tones of the chromatic scale. It also
    calculates the relative minors for each key in the Circle of Fifths.

    Attributes
    ----------
    _FIFTH_INTERVAL : int
        The interval of a perfect fifth, represented as an `IntervalName`
        object with a value of 7.
    _MINOR_THIRD : int
        The interval of a minor third, represented as an `IntervalName` object
        with a value of 3.

    Methods
    -------
    __init__() -> None:
        Initializes a new instance of the CircleOfFifths class with the Circle
        of Fifths and its relative minors.

    _calculate_circle_of_fifths() -> Tuple[List[str], List[str]]:
        Calculates the Circle of Fifths and its relative minors.

    _create_circle_of_fifths() -> List[str]:
        Creates the Circle of Fifths as a list of strings.

    _create_next_note_in_circle(current_note: str) -> str:
        Calculates the next note in the Circle of Fifths given the current
        note.

    _create_relative_minors(circle_of_fifths: List[str]) -> List[str]:
        Creates a list of relative minors for each key in the Circle of Fifths.

    _create_relative_minor(current_note_index: int, current_note: str) -> str:
        Creates the relative minor for a given key.

    _handle_enharmonic(note: str) -> str:
        Handles the special case of keys with sharps or flats in their name.
    """

    _FIFTH_INTERVAL: int = IntervalName(7)
    _MINOR_THIRD: int = IntervalName(3)

    def __init__(self) -> None:
        """Initialize a new instance of the class with the Circle of Fifths
        and its relative minors.

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

    def _calculate_circle_of_fifths(self) -> Tuple[List[str], List[str]]:
        """Calculate the Circle of Fifths and its relative minors.

        Args:
        -----
            self: An instance of the class.

        Returns:
        --------
            A tuple containing two lists:
                - The first list is the Circle of Fifths as a list of strings.
                - The second list is the relative minors for each key in the
                Circle of Fifths, also as a list of strings.

        Raises:
        -------
            None

        """
        circle_of_fifths = self._create_circle_of_fifths()
        relative_minors = self._create_relative_minors(circle_of_fifths)
        return circle_of_fifths, relative_minors

    def _create_circle_of_fifths(self) -> List[str]:
        """Create the Circle of Fifths as a list of strings.

        Args:
        -----
            self: An instance of the class.

        Returns:
        --------
            A list of strings representing the Circle of Fifths.

        Raises:
        -------
            None

        """
        circle_of_fifths = [C]
        for i in range(11):
            next_note = self._create_next_note_in_circle(circle_of_fifths[i])
            circle_of_fifths.append(next_note)
            if i == 6:
                circle_of_fifths[6] = [F + SHARP, G + FLAT]
        for i in range(6, 11):
            next_note = circle_of_fifths[i + 1]
            enharmonic = self._handle_enharmonic(next_note)
            circle_of_fifths[i + 1] = enharmonic
        return circle_of_fifths

    def _create_next_note_in_circle(self, current_note: str) -> str:
        """Calculate the next note in the Circle of Fifths given the current
        note.

        Args:
        -----
            self: An instance of the class.
            current_note (str): A string representing the current note.

        Returns:
        --------
            A string representing the next note in the Circle of Fifths.

        Raises:
        -------
            None

        """
        fifth_interval = IntervalCalculator().calculate_ascending_interval(
            self._FIFTH_INTERVAL,
            ScientificPitchNotation(current_note, DEFAULT_OCTAVE),
        )
        return fifth_interval

    def _create_relative_minors(
        self, circle_of_fifths: List[str]
    ) -> List[str]:
        """Create a list of relative minors for each key in the Circle of
        Fifths.

        Args:
        -----
            self: An instance of the class.
            circle_of_fifths (List[str]): A list of strings representing the
            Circle of Fifths.

        Returns:
        --------
            A list of strings representing the relative minor for each key in
            the Circle of Fifths.

        Raises:
        -------
            None
        """
        relative_minors = [
            self._create_relative_minor(index, note)
            for index, note in enumerate(circle_of_fifths)
        ]
        return relative_minors

    def _create_relative_minor(
        self, current_note_index: int, current_note: str
    ) -> str:
        """Create the relative minor for a given key.

        Args:
        -----
            self: An instance of the class.
            current_note_index (int): An integer representing the index of the
            current note in the Circle of Fifths.
            current_note (str): A string representing the current note.

        Returns:
        --------
            A string representing the relative minor for the given key.

        Raises:
        -------
            None

        """
        if current_note_index < 6:
            relative_minor = (
                IntervalCalculator().calculate_descending_interval(
                    self._MINOR_THIRD,
                    ScientificPitchNotation(current_note, DEFAULT_OCTAVE),
                )
            )
            enharmonic = self._handle_enharmonic(relative_minor)
            return enharmonic
        elif current_note_index == 6:
            return [D + SHARP, E + FLAT]
        elif current_note_index >= 7:
            relative_minor = (
                IntervalCalculator().calculate_descending_interval(
                    self._MINOR_THIRD,
                    ScientificPitchNotation(current_note, DEFAULT_OCTAVE),
                )
            )
            return relative_minor

    def _handle_enharmonic(self, note: str) -> str:
        """Handle the special case of keys with sharps or flats in their name.

        Args:
        -----
            self: An instance of the class.
            note (str): A string representing a note.

        Returns:
        --------
            A string representing the enharmonic equivalent of the note, if
            one exists; otherwise, the original note.

        Raises:
        -------
            None

        """
        spn = ScientificPitchNotation(note, DEFAULT_OCTAVE)
        enharmonic = Enharmonic(spn)
        return (
            enharmonic.get_enharmonic().pitch
            if enharmonic.is_enharmonic()
            else spn.pitch
        )
