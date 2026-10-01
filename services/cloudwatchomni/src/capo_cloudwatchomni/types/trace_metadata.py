"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TraceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.trace_metadata_attribute_map


class TraceMetadata(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_cloudwatchomni.types.trace_metadata_attribute_map.TraceMetadataAttributeMap"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TraceMetadata) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_cloudwatchomni.types.trace_metadata_attribute_map

        out["attributes"] = (
            capo_cloudwatchomni.types.trace_metadata_attribute_map.serialize_cbor(
                value["attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TraceMetadata:
    out: TraceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_cloudwatchomni.types.trace_metadata_attribute_map

        out["attributes"] = (
            capo_cloudwatchomni.types.trace_metadata_attribute_map.deserialize_cbor(
                data["attributes"]
            )
        )
    return out
