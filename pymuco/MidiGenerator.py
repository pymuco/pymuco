# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         MidiGenerator.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import logging

from typing import List, Tuple

from .logging_utils import setup_logger
from .MIDIUtils import MIDINoteConverter


class MidiGenerator:
    """
    A class to generate MIDI files from musical notation.

    Attributes:
    -----------
    NOTE_ON (int): Constant value representing the 'Note On' MIDI event.
    NOTE_OFF (int): Constant value representing the 'Note Off' MIDI event.
    midi_converter (MIDINoteConverter): An instance of the MIDINoteConverter
    class to handle note-to-MIDI conversions.

    Methods:
    --------
    __init__(self, logger: logging.Logger = None) -> None:
        Initializes the MidiGenerator class and sets up the logger.

    _write_variable_length(self, value: int) -> List[int]:
        Converts a time value to the MIDI variable-length format.

    _write_note_on(self, track_data: List[int], delta_time: int,
        note_name: str, velocity: int) -> None:
        Writes a 'Note On' event to the MIDI track data.

    _write_note_off(self, track_data: List[int], delta_time: int,
        note_name: str, velocity: int) -> None:
        Writes a 'Note Off' event to the MIDI track data.

    create_midi_file(self, music_computation_notation: List[Tuple],
        file_name: str = "output.mid") -> None:
        Creates and saves a MIDI file using the provided musical notation.

    _create_header_chunk(self) -> List[int]:
        Creates the header chunk for the MIDI file.

    _create_track_data(self, music_computation_notation:
        List[Tuple]) -> List[int]:
        Creates the track data for the MIDI file.

    _insert_track_length(self, track_data: List[int]) -> None:
        Inserts the track length into the MIDI track data.

    _save_midi_file(self, header_chunk: List[int], track_data: List[int],
        file_name: str) -> None:
        Saves the MIDI file to disk by combining the header and track data.
    """

    NOTE_ON = 0x90
    NOTE_OFF = 0x80

    def __init__(self, logger: logging.Logger = None) -> None:
        """
        The __init__ method initializes the MidiGenerator object, along with
        a MIDI note converter and a logger. If no logger is provided, a default
        logger will be set up.

        Parameters:
        -----------

        logger: A logging.Logger object to handle logging messages. If None,
        a default logger will be created.

        Returns:
        --------
        None.
        """
        self.midi_converter = MIDINoteConverter()
        self.logger = logger or setup_logger(__name__)

    def _write_variable_length(self, value: int) -> List[int]:
        """
        Converts a duration value into a variable-length format suitable for
        MIDI file storage.

        Parameters:
        -----------

        value: An integer representing the duration in ticks.

        Returns:
        --------
        List[int]: A list of integers representing the value in a MIDI
        variable-length format.
        """
        buffer = value & 0x7F
        while value > 0x7F:
            value >>= 7
            buffer <<= 8
            buffer |= (value & 0x7F) | 0x80
        result = []
        while True:
            result.append(buffer & 0xFF)
            if buffer & 0x80:
                buffer >>= 8
            else:
                break
        return result

    def _write_note_on(
        self,
        track_data: List[int],
        delta_time: int,
        note_name: str,
        velocity: int,
    ) -> None:
        """
        Writes a 'Note On' event to the MIDI track data for a specified note
        name, velocity, and delta time.

        Parameters:
        -----------

        track_data: A list to which the MIDI event data will be appended.
        delta_time: An integer representing the time in ticks before the note
        event.
        note_name: A string representing the note name (e.g., "C4").
        velocity: An integer (0-127) representing the velocity of the note.

        Returns:
        --------
        None.
        """
        midi_note = self.midi_converter.note_name_to_midi_note(note_name)
        track_data.extend(self._write_variable_length(delta_time))
        track_data.append(self.NOTE_ON)
        track_data.append(midi_note)
        track_data.append(velocity)

    def _write_note_off(
        self,
        track_data: List[int],
        delta_time: int,
        note_name: str,
        velocity: int,
    ) -> None:
        """
        Writes a 'Note Off' event to the MIDI track data for a specified note
        name, velocity, and delta time.

        Parameters:
        -----------

        track_data: A list to which the MIDI event data will be appended.
        delta_time: An integer representing the time in ticks before the note
        event.
        note_name: A string representing the note name (e.g., "C4").
        velocity: An integer (0-127) representing the velocity of the note.

        Returns:
        --------
        None.
        """
        midi_note = self.midi_converter.note_name_to_midi_note(note_name)
        track_data.extend(self._write_variable_length(delta_time))
        track_data.append(self.NOTE_OFF)
        track_data.append(midi_note)
        track_data.append(velocity)

    def create_midi_file(
        self,
        music_computation_notation: List[Tuple],
        file_name: str = "output.mid",
    ) -> None:
        """
        Creates a MIDI file using the provided music computation notation
        blocks.

        Parameters:
        -----------

        music_computation_notation: A list of tuples where each tuple contains
        a ScientificPitchNotation object and a NoteDuration object.
        file_name: A string representing the output file name.

        Returns:
        --------
        None.

        Raises:
        -------
        ValueError: If the provided music_computation_notation is not a list.
        """
        if not isinstance(music_computation_notation, list):
            self.logger.error("music_computation_notation must be a list")
            return
        if not isinstance(file_name, str):
            self.logger.error("The file name must be a string")
            return

        try:
            self.logger.info(f"Creating MIDI file: {file_name}")

            # Create MIDI header and track data
            header_chunk = self._create_header_chunk()
            track_data = self._create_track_data(music_computation_notation)

            # Insert track length and save the file
            self._insert_track_length(track_data)
            self._save_midi_file(header_chunk, track_data, file_name)

            self.logger.info(f"MIDI file {file_name} created successfully.")
        except Exception as e:
            self.logger.error(f"Error creating MIDI file: {e}")

    def _create_header_chunk(self) -> List[int]:
        """
        Creates the header chunk for the MIDI file, which includes file format,
        number of tracks, and time division.

        Returns:
        --------
        List[int]: A list of integers representing the MIDI header chunk.
        """
        return [
            0x4D,
            0x54,
            0x68,
            0x64,  # Chunk type "MThd"
            0x00,
            0x00,
            0x00,
            0x06,  # Header length
            0x00,
            0x01,  # Format type (1: multiple tracks)
            0x00,
            0x01,  # Number of tracks
            0x00,
            0x60,  # Division (96 ticks per quarter note)
        ]

    def _create_track_data(self, music_computation_notation: List[Tuple]) -> List[int]:
        """
        Creates the track data for the MIDI file based on the provided notation
        blocks, each containing a note and its duration.

        Parameters:
        -----------

        music_computation_notation: A list of tuples where each tuple contains
        a ScientificPitchNotation object and a NoteDuration object.

        Returns:
        --------
        List[int]: A list of integers representing the MIDI track data.
        """
        track_data = [
            0x4D,
            0x54,
            0x72,
            0x6B,  # Chunk type "MTrk"
            0x00,
            0x00,
            0x00,
            0x00,
        ]  # Placeholder for track length

        running_time = 0

        for spn, duration in music_computation_notation:
            note_name = spn
            duration_ticks = int(duration.duration_length * 96)
            velocity = 64  # Default velocity

            self._write_note_on(track_data, running_time, note_name, velocity)
            running_time = 0
            self._write_note_off(track_data, duration_ticks, note_name, velocity)
        track_data.extend([0x00, 0xFF, 0x2F, 0x00])  # Meta event: End of track
        return track_data

    def _insert_track_length(self, track_data: List[int]) -> None:
        """
        Calculates and inserts the track length into the track data.

        Parameters:
        -----------

        track_data: A list of track data to insert the length into.

        Returns:
        --------
        None.
        """
        track_length = len(track_data) - 8
        track_data[4] = (track_length >> 24) & 0xFF
        track_data[5] = (track_length >> 16) & 0xFF
        track_data[6] = (track_length >> 8) & 0xFF
        track_data[7] = track_length & 0xFF

    def _save_midi_file(
        self, header_chunk: List[int], track_data: List[int], file_name: str
    ) -> None:
        """
        Saves the MIDI file to disk by combining the header and track data.

        Parameters:
        -----------

        header_chunk: A list of integers representing the MIDI header.
        track_data: A list of integers representing the track data.
        file_name: A string representing the file name for the saved MIDI file.

        Returns:
        --------
        None.

        Raises:
        -------
        IOError: If there is an issue saving the file.
        """
        try:
            with open(file_name, "wb") as midi_file:
                midi_file.write(bytearray(header_chunk + track_data))
            self.logger.info(f"File saved as {file_name}")
        except IOError as e:
            self.logger.error(f"Failed to save MIDI file: {e}")
