"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Edge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.context_graph_attribute_map
    import capo_cloudwatchomni.types.context_graph_id
    import capo_cloudwatchomni.types.edge_properties
    import capo_cloudwatchomni.types.edge_type
    import capo_cloudwatchomni.types.metadata
    import capo_cloudwatchomni.types.signal_set
    import capo_cloudwatchomni.types.source_set
    import capo_cloudwatchomni.types.string_set

Edge = TypedDict(
    "Edge",
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
        "edge_properties": NotRequired[
            "capo_cloudwatchomni.types.edge_properties.EdgeProperties"
        ],
        "telemetry_attributes": NotRequired[
            "capo_cloudwatchomni.types.context_graph_attribute_map.ContextGraphAttributeMap"
        ],
        "signal_types": NotRequired["capo_cloudwatchomni.types.signal_set.SignalSet"],
        "sources": NotRequired["capo_cloudwatchomni.types.source_set.SourceSet"],
        "metadata": NotRequired["capo_cloudwatchomni.types.metadata.Metadata"],
        "first_observed_at": NotRequired["datetime.datetime"],
        "last_observed_at": NotRequired["datetime.datetime"],
    },
    closed=True,
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Edge) -> dict:
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
    if "edge_properties" in value:
        import capo_cloudwatchomni.types.edge_properties

        out["edgeProperties"] = (
            capo_cloudwatchomni.types.edge_properties.serialize_cbor(
                value["edge_properties"]
            )
        )
    if "telemetry_attributes" in value:
        import capo_cloudwatchomni.types.context_graph_attribute_map

        out["telemetryAttributes"] = (
            capo_cloudwatchomni.types.context_graph_attribute_map.serialize_cbor(
                value["telemetry_attributes"]
            )
        )
    if "signal_types" in value:
        import capo_cloudwatchomni.types.signal_set

        out["signalTypes"] = capo_cloudwatchomni.types.signal_set.serialize_cbor(
            value["signal_types"]
        )
    if "sources" in value:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.serialize_cbor(
            value["sources"]
        )
    if "metadata" in value:
        import capo_cloudwatchomni.types.metadata

        out["metadata"] = capo_cloudwatchomni.types.metadata.serialize_cbor(
            value["metadata"]
        )
    if "first_observed_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["firstObservedAt"] = (
            capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
                value["first_observed_at"]
            )
        )
    if "last_observed_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["lastObservedAt"] = (
            capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
                value["last_observed_at"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Edge:
    out: Edge = {}  # type: ignore[typeddict-item]
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
    if data.get("edgeProperties") is not None:
        import capo_cloudwatchomni.types.edge_properties

        out["edge_properties"] = (
            capo_cloudwatchomni.types.edge_properties.deserialize_cbor(
                data["edgeProperties"]
            )
        )
    if data.get("telemetryAttributes") is not None:
        import capo_cloudwatchomni.types.context_graph_attribute_map

        out["telemetry_attributes"] = (
            capo_cloudwatchomni.types.context_graph_attribute_map.deserialize_cbor(
                data["telemetryAttributes"]
            )
        )
    if data.get("signalTypes") is not None:
        import capo_cloudwatchomni.types.signal_set

        out["signal_types"] = capo_cloudwatchomni.types.signal_set.deserialize_cbor(
            data["signalTypes"]
        )
    if data.get("sources") is not None:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.deserialize_cbor(
            data["sources"]
        )
    if data.get("metadata") is not None:
        import capo_cloudwatchomni.types.metadata

        out["metadata"] = capo_cloudwatchomni.types.metadata.deserialize_cbor(
            data["metadata"]
        )
    if data.get("firstObservedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["first_observed_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["firstObservedAt"]
            )
        )
    if data.get("lastObservedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["last_observed_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["lastObservedAt"]
            )
        )
    return out
