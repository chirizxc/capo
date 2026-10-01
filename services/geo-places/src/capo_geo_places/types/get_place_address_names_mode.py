"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceAddressNamesMode``."""

from typing import Literal, TypeAlias, cast

GetPlaceAddressNamesMode: TypeAlias = Literal["Administrative",]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceAddressNamesMode) -> str:
    return value


def deserialize_json(data: str) -> GetPlaceAddressNamesMode:
    return cast(GetPlaceAddressNamesMode, data)
