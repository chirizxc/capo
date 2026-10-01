"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LocationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_application_signals.types.code_location


class _LocationIdentifier_CodeLocation(TypedDict, closed=True):
    CodeLocation: "capo_application_signals.types.code_location.CodeLocation"


class _LocationIdentifier_LocationHash(TypedDict, closed=True):
    LocationHash: "str"


LocationIdentifier: TypeAlias = (
    _LocationIdentifier_CodeLocation | _LocationIdentifier_LocationHash
)


# --- restJson1 ser/de ---
def serialize_json(value: LocationIdentifier) -> dict:
    if "CodeLocation" in value:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.serialize_json(
                value["CodeLocation"]
            )
        }
    elif "LocationHash" in value:
        return {"LocationHash": value["LocationHash"]}
    else:
        raise SerializationError("LocationIdentifier: no variant present")


def deserialize_json(data: dict) -> LocationIdentifier:
    if data.get("CodeLocation") is not None:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.deserialize_json(
                data["CodeLocation"]
            )
        }
    elif data.get("LocationHash") is not None:
        return {"LocationHash": data["LocationHash"]}
    else:
        raise DeserializationError("LocationIdentifier: no recognized variant key")
