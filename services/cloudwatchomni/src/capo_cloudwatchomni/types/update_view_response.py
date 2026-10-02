"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.view_type


class UpdateViewResponse(TypedDict, closed=True):
    name: "str"
    """The name of the view."""
    type: "capo_cloudwatchomni.types.view_type.ViewType"
    """The ownership category of the view."""
    description: NotRequired["str"]
    """The description of the view."""
    definition: "str"
    """The SQL query that defines the view."""
    created_at: "datetime.datetime"
    """The timestamp when the view was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the view was last updated."""
    arn: "str"
    """The ARN of the view."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateViewResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cloudwatchomni.types.view_type

    out["type"] = capo_cloudwatchomni.types.view_type.serialize_cbor(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    out["definition"] = value["definition"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    out["arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> UpdateViewResponse:
    out: UpdateViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateViewResponse.name required")
    if data.get("type") is not None:
        import capo_cloudwatchomni.types.view_type

        out["type"] = capo_cloudwatchomni.types.view_type.deserialize_cbor(data["type"])
    else:
        raise DeserializationError("UpdateViewResponse.type required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("UpdateViewResponse.definition required")
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateViewResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateViewResponse.updated_at required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateViewResponse.arn required")
    return out
