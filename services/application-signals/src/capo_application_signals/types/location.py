"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Location``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_application_signals.types.code_location


class _Location_CodeLocation(TypedDict, closed=True):
    CodeLocation: "capo_application_signals.types.code_location.CodeLocation"


Location: TypeAlias = _Location_CodeLocation


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    if "CodeLocation" in value:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.serialize_json(
                value["CodeLocation"]
            )
        }
    else:
        raise SerializationError("Location: no variant present")


def deserialize_json(data: dict) -> Location:
    if data.get("CodeLocation") is not None:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.deserialize_json(
                data["CodeLocation"]
            )
        }
    else:
        raise DeserializationError("Location: no recognized variant key")
