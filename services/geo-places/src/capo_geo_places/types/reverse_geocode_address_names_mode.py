"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeAddressNamesMode``."""

from typing import Literal, TypeAlias, cast

ReverseGeocodeAddressNamesMode: TypeAlias = Literal["Administrative",]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeAddressNamesMode) -> str:
    return value


def deserialize_json(data: str) -> ReverseGeocodeAddressNamesMode:
    return cast(ReverseGeocodeAddressNamesMode, data)
