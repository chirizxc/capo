"""Generated from Smithy shape ``com.amazonaws.quicksight#AppVisibility``."""

from typing import Literal, TypeAlias, cast

"""<p>The visibility of an app. Valid values are:</p> <ul> <li> <p> <code>PRIVATE</code> – The app is reachable only by authorized Amazon QuickSight principals.</p> </li> <li> <p> <code>PUBLIC</code> – The published app is reachable by anyone on the internet without signing in.</p> </li> </ul>"""
AppVisibility: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppVisibility) -> str:
    return value


def deserialize_json(data: str) -> AppVisibility:
    return cast(AppVisibility, data)
