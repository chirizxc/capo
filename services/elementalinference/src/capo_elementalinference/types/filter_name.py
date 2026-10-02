"""Generated from Smithy shape ``com.amazonaws.elementalinference#FilterName``."""

from typing import Literal, TypeAlias, cast

FilterName: TypeAlias = Literal["COMPETITOR",]


# --- restJson1 ser/de ---
def serialize_json(value: FilterName) -> str:
    return value


def deserialize_json(data: str) -> FilterName:
    return cast(FilterName, data)
