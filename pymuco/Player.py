import os

from AudioConverter import AudioConverter


class Player:
    """
    The Player class provides a method to play audio samples using the
    appropriate command for the current platform. It uses the os module to
    determine the current platform and execute the appropriate command. After
    playing the audio sample, the file is removed from the system.

    Attributes:
    -----------

    None

    Methods:
    --------

    play(sample: AudioConverter): Plays the audio sample passed as an argument
    using the appropriate command for the current platform. If the platform is
    unsupported, it prints a message and returns. After playing the audio
    sample, it removes the file from the system.

    Parameters:
    -----------

    sample (AudioConverter): The audio sample to play.

    Returns:
    --------

    None

    Raises:
    --------

    None

    Note:
    -----

    This method uses the os module to determine the current platform and
    execute the appropriate command for playing the audio file.
    The audio file is removed from the system after playing.
    """

    def play(self, sample: AudioConverter):
        """
        Play the audio sample passed as an argument using the appropriate
        command for the current platform.

        Parameters
        ----------
        sample : AudioConverter
            The audio sample to play. Must be an instance of AudioConverter.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            If the `sample` argument is not an instance of `AudioConverter`.

        Notes
        -----
        This method uses the os module to determine the current platform and to
        execute the appropriate command for playing the audio file. The audio
        file is removed from the system after playing.

        - On Linux or macOS, this method uses `aplay` or `afplay` respectively.
        - On Windows, it uses the `powershell` command with the `Media.SoundPlayer`
          class to play the audio file.

        If the platform is unsupported, this method prints a message and returns.
        """
        if not isinstance(sample, AudioConverter):
            raise TypeError("Sample must be an instance of AudioConverter")

        if os.name == "posix":  # Linux or macOS
            if os.uname().sysname == "Linux":
                player = "aplay"
            elif os.uname().sysname == "Darwin":
                player = "afplay"
            else:
                print("Unsupported platform")
                return
        elif os.name == "nt":  # Windows
            player = 'powershell -c (New-Object Media.SoundPlayer "{0}").\
PlaySync();'
        else:
            print("Unsupported platform")
            return

        command = f'{player} "{sample._full_file_path}"'

        os.system(command)
        os.remove(sample._full_file_path)


"""
# Create a new MusicNotation object
notation = MusicComputationNotation()

# Create ScientificPitchNotation objects
C4 = ScientificPitchNotation("C", 4)
E4 = ScientificPitchNotation("E", 4)
G4 = ScientificPitchNotation("G", 4)
C5 = ScientificPitchNotation("C", 5)

# Create NoteDuration objects
whole_note = NoteDuration("WHOLE_NOTE")
half_note = NoteDuration(0.5)

notation.add_block(C4, whole_note, E4, whole_note,
                   G4, whole_note, C5, whole_note)

acorde = AudioConverter()
acorde.convert_to_audio(notation)

Player().play(acorde)
"""
