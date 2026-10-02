"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_error_code


class ResourceError(TypedDict, closed=True):
    code: NotRequired["capo_iotsitewise.types.resource_error_code.ResourceErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired["str"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceError) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_iotsitewise.types.resource_error_code

        out["code"] = capo_iotsitewise.types.resource_error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceError:
    out: ResourceError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.resource_error_code

        out["code"] = capo_iotsitewise.types.resource_error_code.deserialize_json(
            data["code"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
