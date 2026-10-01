"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CaptureBlob``."""

import base64
from typing import TypeAlias

"""<p>A binary blob containing video data.</p>"""
CaptureBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: CaptureBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> CaptureBlob:
    return base64.b64decode(data)
