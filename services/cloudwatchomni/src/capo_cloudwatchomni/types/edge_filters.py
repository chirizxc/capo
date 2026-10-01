"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EdgeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.context_graph_id
    import capo_cloudwatchomni.types.edge_type
    import capo_cloudwatchomni.types.key_filter_list
    import capo_cloudwatchomni.types.source_set
    import capo_cloudwatchomni.types.string_set

EdgeFilters = TypedDict(
    "EdgeFilters",
    {
        "edge_id": NotRequired[
            "capo_cloudwatchomni.types.context_graph_id.ContextGraphId"
        ],
        "from": NotRequired[
            "capo_cloudwatchomni.types.context_graph_id.ContextGraphId"
        ],
        "to": NotRequired["capo_cloudwatchomni.types.context_graph_id.ContextGraphId"],
        "edge_type": NotRequired["capo_cloudwatchomni.types.edge_type.EdgeType"],
        "operations": NotRequired["capo_cloudwatchomni.types.string_set.StringSet"],
        "telemetry_attributes": NotRequired[
            "capo_cloudwatchomni.types.key_filter_list.KeyFilterList"
        ],
        "sources": NotRequired["capo_cloudwatchomni.types.source_set.SourceSet"],
    },
    closed=True,
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EdgeFilters) -> dict:
    out: dict = {}
    if "edge_id" in value:
        out["edgeId"] = value["edge_id"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    if "edge_type" in value:
        import capo_cloudwatchomni.types.edge_type

        out["edgeType"] = capo_cloudwatchomni.types.edge_type.serialize_cbor(
            value["edge_type"]
        )
    if "operations" in value:
        import capo_cloudwatchomni.types.string_set

        out["operations"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["operations"]
        )
    if "telemetry_attributes" in value:
        import capo_cloudwatchomni.types.key_filter_list

        out["telemetryAttributes"] = (
            capo_cloudwatchomni.types.key_filter_list.serialize_cbor(
                value["telemetry_attributes"]
            )
        )
    if "sources" in value:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.serialize_cbor(
            value["sources"]
        )
    return out


def deserialize_cbor(data: dict) -> EdgeFilters:
    out: EdgeFilters = {}  # type: ignore[typeddict-item]
    if data.get("edgeId") is not None:
        out["edge_id"] = data["edgeId"]
    if data.get("from") is not None:
        out["from"] = data["from"]
    if data.get("to") is not None:
        out["to"] = data["to"]
    if data.get("edgeType") is not None:
        import capo_cloudwatchomni.types.edge_type

        out["edge_type"] = capo_cloudwatchomni.types.edge_type.deserialize_cbor(
            data["edgeType"]
        )
    if data.get("operations") is not None:
        import capo_cloudwatchomni.types.string_set

        out["operations"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["operations"]
        )
    if data.get("telemetryAttributes") is not None:
        import capo_cloudwatchomni.types.key_filter_list

        out["telemetry_attributes"] = (
            capo_cloudwatchomni.types.key_filter_list.deserialize_cbor(
                data["telemetryAttributes"]
            )
        )
    if data.get("sources") is not None:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.deserialize_cbor(
            data["sources"]
        )
    return out
