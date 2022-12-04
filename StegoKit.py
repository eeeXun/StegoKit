import magic

from Audio import StegoAudio


class StegoKit:
    def __init__(self, file: str):
        self.file: str = file

    def hide(self, input: str, output: str, input_type: str = "string"):
        """
        input_type should be "string" or "file", default is "string"

        If input_type is "string", input should be string
        If input_type is "file"", input should be file name

        output should be file name to save after hide data

        ex.
        StegoKit("a.png").hide(input="ABCD", output="b.png", input_type="string")
        StegoKit("a.png").hide(input="a.txt", output="b.png", input_type="file")
        """
        input_data: bytes
        mime_type = magic.from_file(self.file, mime=True).split("/")
        _type = mime_type[0]
        _subtype = mime_type[1]

        if input_type == "string":
            input_data = input.encode("utf-8")
        elif input_type == "file":
            input_data = open(input, "rb")

        if _type == "image":
            ...
        elif _type == "audio":
            StegoAudio(self.file, format=_subtype).hide(input_data, output)
