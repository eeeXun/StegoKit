from pydub import AudioSegment


class StegoAudio:
    def __init__(self, file: str, format: str):
        self.data = AudioSegment.from_file(file, format=format)

    def hide(self, input_data: bytes, output_file: str):
        """
        Hide data with LSB steganography.
        Hide data length in first 16 bits of samples. So maximum of data would be 65536 bit.
        """
        index = 0
        samples = self.data.get_array_of_samples()

        # hide data length in first 16 bits of samples
