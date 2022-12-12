import magic


class StegoKit:
    def __init__(self, file: str):
        self.file: str = file

    def hide(self, input: str, output_file: str, input_type: str = "string"):
        """
        input_type should be "string" or "file", default is "string"

        If input_type is "string", input should be string
        If input_type is "file"", input should be file name

        output_file should be file name to save after hiding data

        ex.
        StegoKit("a.png").hide(input="ABCD", output_file="b.png", input_type="string")
        StegoKit("a.png").hide(input="a.txt", output_file="b.png", input_type="file")
        """
        input_data: list[str]
        mime_type = magic.from_file(self.file, mime=True).split("/")
        _type = mime_type[0]
        _subtype = mime_type[1]

        if input_type == "string":
            input_data = [bin(ord(c))[2:].rjust(8, "0") for c in input]
        elif input_type == "file":
            with open("input", "rb") as f:
                data = f.read()
                input_data = [bin(b)[2:].rjust(8, "0") for b in data]

        if _type == "image":
            ...
        elif _type == "audio":
            ...
