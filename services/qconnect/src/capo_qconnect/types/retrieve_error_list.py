"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.retrieve_error

RetrieveErrorList: TypeAlias = list["capo_qconnect.types.retrieve_error.RetrieveError"]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveErrorList) -> list:
    import capo_qconnect.types.retrieve_error

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.retrieve_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetrieveErrorList:
    import capo_qconnect.types.retrieve_error

    out: RetrieveErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.retrieve_error.deserialize_json(item))
    return out
