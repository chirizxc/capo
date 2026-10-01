"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#JsonataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string


class JsonataConfiguration(TypedDict, closed=True):
    expression: "capo_eventbridgev2.types.string.String"
    """JSONata expression to transform the event. Must be wrapped in {% %} delimiters."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JsonataConfiguration) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    return out


def deserialize_cbor(data: dict) -> JsonataConfiguration:
    out: JsonataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("JsonataConfiguration.expression required")
    return out
