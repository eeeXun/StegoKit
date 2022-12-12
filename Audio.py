from pydub import AudioSegment


class StegoAudio:
    def __init__(self, file: str, format: str):
        self.samples = AudioSegment.from_file(file, format=format).get_array_of_samples()

    def hide(self, input_data: list[str], output_file: str):
        """
        Hide data with LSB steganography.
        Hide data length in first 16 samples. So maximum of data would be 65536 bit.
        """
        index = 0

        # hide data length in first 16 bits of samples
        data_len = len(input_data) * 8
        if len(self.samples) < data_len + 16:
            raise Exception("The amount of samples is too small to hide data")
        elif data_len > 65536:
            raise Exception("The data exceed the maximum number(65536) you can hide")
        else:
            # hide length
            data_len_bin = bin(data_len)[2:].rjust(16, "0")
            for c in data_len_bin:
                self.samples[index] = (self.samples & 0xFFFFFFFFFFFFFFFE) | int(c)
                index += 1
            # hide data
            for bin_str in input_data:
                for c in bin_str:
                    self.samples[index] = (self.samples & 0xFFFFFFFFFFFFFFFE) | int(c)
                    index += 1
