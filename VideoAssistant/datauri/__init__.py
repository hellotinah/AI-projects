from __future__ import annotations

from typing import Generator
import base64
import contextlib
import mimetypes
import os
import re
import tempfile

__all__ = (
    "from_file",
    "from_bytes",
    "parse",
    "as_tempfile",
)


def from_file(file_path, mime_type=None) -> str:
    if mime_type is None:
        mime_type = mimetypes.guess_type(file_path)[0]
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded_string}"


def from_bytes(bytes: bytes, mime_type: str) -> str:
    encoded_string = base64.b64encode(bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded_string}"


def parse(data_uri: str) -> tuple[bytes, str]:
    match = re.match(r"data:(?P<mime_type>.*?);base64,(?P<encoded_string>.*)", data_uri)
    if match is None:
        raise ValueError("Invalid data URI")
    return (
        base64.b64decode(match["encoded_string"]),
        match["mime_type"].split(";")[0].strip(),
    )


@contextlib.contextmanager
def as_tempfile(data_uri: str) -> Generator[str, None, None]:
    bytes, mime_type = parse(data_uri)
    with tempfile.NamedTemporaryFile(
        suffix=mimetypes.guess_extension(mime_type), delete=False
    ) as file:
        file.write(bytes)
        file.flush()
        file.close()
        try:
            yield file.name
        finally:
            os.unlink(file.name)
