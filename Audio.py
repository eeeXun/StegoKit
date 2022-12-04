from pydub import AudioSegment


class StegoAudio:
    def __init__(self, file: str, format: str):
        self.data = AudioSegment.from_file(file, format=format)

    def hide(self, input_data: bytes, output_file: str):
        index = 0
        samples = self.data.get_array_of_samples()
