"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelSelectorOperator``."""

from typing import Literal, TypeAlias, cast

"""<p>The operator that a label selector requirement applies to its key and values.</p> <ul> <li> <p>IN — the key's value must be one of the specified values.</p> </li> <li> <p>NOT_IN — the key's value must not be one of the specified values.</p> </li> <li> <p>EXISTS — the key must be present, regardless of its value.</p> </li> <li> <p>DOES_NOT_EXIST — the key must not be present.</p> </li> </ul>"""
EksLabelSelectorOperator: TypeAlias = Literal[
    "IN",
    "NOT_IN",
    "EXISTS",
    "DOES_NOT_EXIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: EksLabelSelectorOperator) -> str:
    return value


def deserialize_json(data: str) -> EksLabelSelectorOperator:
    return cast(EksLabelSelectorOperator, data)
