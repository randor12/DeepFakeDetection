"""
:author: Ryan Nicholas
:description: Wave Reader for sound
"""

import struct


class WavFileHelper():

    def __init__(self):
        """
        Initialize WavFileHelper
        """
        pass

    def read_file_properties(self, filename):
        """
        Read wave function
        :param filename: filename
        :return: (num_channels, sample_rate, bit_depth)
        """

        wave_file = open(filename, "rb")

        riff = wave_file.read(12)
        fmt = wave_file.read(36)

        num_channels_string = fmt[10:12]

        num_channels = struct.unpack('<H', num_channels_string)[0]

        sample_rate_string = fmt[12:16]
        sample_rate = struct.unpack('<I', sample_rate_string)[0]

        bit_depth_string = fmt[22:24]
        bit_depth = struct.unpack('<H', bit_depth_string)[0]

        return (num_channels, sample_rate, bit_depth)