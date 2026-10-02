"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MultiviewLayoutType``."""

from typing import Literal, TypeAlias, cast

"""<p>A tile layout for a multiview channel. Each layout determines how many source tiles are composited into the output and how those tiles are arranged.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>LAYOUT_2EH</code> – Two tiles of equal size, arranged horizontally.</p> </li> <li> <p> <code>LAYOUT_2PL</code> – Two tiles, with one larger primary tile.</p> </li> <li> <p> <code>LAYOUT_3EL</code> – Three tiles of equal size, arranged in two columns.</p> </li> <li> <p> <code>LAYOUT_3PL</code> – Three tiles, with one larger primary tile on the left and two stacked on the right.</p> </li> <li> <p> <code>LAYOUT_4E</code> – Four tiles of equal size, arranged in a two-by-two grid.</p> </li> <li> <p> <code>LAYOUT_4PL</code> – Four tiles, with one larger primary tile on the left and three stacked on the right.</p> </li> </ul>"""
MultiviewLayoutType: TypeAlias = Literal[
    "LAYOUT_2EH",
    "LAYOUT_2PL",
    "LAYOUT_3EL",
    "LAYOUT_3PL",
    "LAYOUT_4E",
    "LAYOUT_4PL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiviewLayoutType) -> str:
    return value


def deserialize_json(data: str) -> MultiviewLayoutType:
    return cast(MultiviewLayoutType, data)
