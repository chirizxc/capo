"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CaptureConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_application_signals.types.code_capture_configuration


class _CaptureConfiguration_CodeCapture(TypedDict, closed=True):
    CodeCapture: "capo_application_signals.types.code_capture_configuration.CodeCaptureConfiguration"


CaptureConfiguration: TypeAlias = _CaptureConfiguration_CodeCapture


# --- restJson1 ser/de ---
def serialize_json(value: CaptureConfiguration) -> dict:
    if "CodeCapture" in value:
        import capo_application_signals.types.code_capture_configuration

        return {
            "CodeCapture": capo_application_signals.types.code_capture_configuration.serialize_json(
                value["CodeCapture"]
            )
        }
    else:
        raise SerializationError("CaptureConfiguration: no variant present")


def deserialize_json(data: dict) -> CaptureConfiguration:
    if data.get("CodeCapture") is not None:
        import capo_application_signals.types.code_capture_configuration

        return {
            "CodeCapture": capo_application_signals.types.code_capture_configuration.deserialize_json(
                data["CodeCapture"]
            )
        }
    else:
        raise DeserializationError("CaptureConfiguration: no recognized variant key")
