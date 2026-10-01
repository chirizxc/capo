"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.context_graph_attribute_map
    import capo_cloudwatchomni.types.context_graph_id
    import capo_cloudwatchomni.types.context_graph_name
    import capo_cloudwatchomni.types.edge_list
    import capo_cloudwatchomni.types.intelligence_tag_map
    import capo_cloudwatchomni.types.metadata
    import capo_cloudwatchomni.types.node_properties
    import capo_cloudwatchomni.types.node_type
    import capo_cloudwatchomni.types.operation_details
    import capo_cloudwatchomni.types.signal_set
    import capo_cloudwatchomni.types.source_set
    import capo_cloudwatchomni.types.string_set


class Node(TypedDict, closed=True):
    node_id: NotRequired["capo_cloudwatchomni.types.context_graph_id.ContextGraphId"]
    """The unique identifier of the node within the context graph."""
    node_type: NotRequired["capo_cloudwatchomni.types.node_type.NodeType"]
    """Whether the node is a service, a resource, or a remote service."""
    name: NotRequired["capo_cloudwatchomni.types.context_graph_name.ContextGraphName"]
    """The primary display name of the node."""
    alternate_names: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Other names this node was observed under. A node that merged across sources reports one resolved name, and the names it was merged away from appear here."""
    tags: NotRequired[
        "capo_cloudwatchomni.types.intelligence_tag_map.IntelligenceTagMap"
    ]
    """The tags observed on the underlying resource."""
    node_properties: NotRequired[
        "capo_cloudwatchomni.types.node_properties.NodeProperties"
    ]
    """Identity attributes promoted out of the flat attribute map onto typed members."""
    telemetry_attributes: NotRequired[
        "capo_cloudwatchomni.types.context_graph_attribute_map.ContextGraphAttributeMap"
    ]
    """The node's OpenTelemetry (OTel) attributes, as emitted by telemetry — the raw values, as opposed to the normalized `nodeProperties`. A key promoted onto a `nodeProperties` member is removed here, so no value appears twice."""
    operation_details: NotRequired[
        "capo_cloudwatchomni.types.operation_details.OperationDetails"
    ]
    """The operations observed on this node, keyed by operation name. Each value lists the dimension sets that identify the metric series for that operation."""
    signal_types: NotRequired["capo_cloudwatchomni.types.signal_set.SignalSet"]
    """The kinds of telemetry signal observed on this node."""
    sources: NotRequired["capo_cloudwatchomni.types.source_set.SourceSet"]
    """The discovery sources that contributed this node."""
    metadata: NotRequired["capo_cloudwatchomni.types.metadata.Metadata"]
    """Descriptive metadata about the node. Present only when the request sets includeMetadata."""
    first_observed_at: NotRequired["datetime.datetime"]
    """When this node was first observed (UTC), at minute granularity. For a node that merged across sources, this is the earliest value any source reported."""
    last_observed_at: NotRequired["datetime.datetime"]
    """When this node was most recently observed (UTC), at minute granularity. For a node that merged across sources, this is the latest value any source reported."""
    edges: NotRequired["capo_cloudwatchomni.types.edge_list.EdgeList"]
    """Outbound edges originating from this node. Each edge carries its `from`."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Node) -> dict:
    out: dict = {}
    if "node_id" in value:
        out["nodeId"] = value["node_id"]
    if "node_type" in value:
        import capo_cloudwatchomni.types.node_type

        out["nodeType"] = capo_cloudwatchomni.types.node_type.serialize_cbor(
            value["node_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "alternate_names" in value:
        import capo_cloudwatchomni.types.string_set

        out["alternateNames"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["alternate_names"]
        )
    if "tags" in value:
        import capo_cloudwatchomni.types.intelligence_tag_map

        out["tags"] = capo_cloudwatchomni.types.intelligence_tag_map.serialize_cbor(
            value["tags"]
        )
    if "node_properties" in value:
        import capo_cloudwatchomni.types.node_properties

        out["nodeProperties"] = (
            capo_cloudwatchomni.types.node_properties.serialize_cbor(
                value["node_properties"]
            )
        )
    if "telemetry_attributes" in value:
        import capo_cloudwatchomni.types.context_graph_attribute_map

        out["telemetryAttributes"] = (
            capo_cloudwatchomni.types.context_graph_attribute_map.serialize_cbor(
                value["telemetry_attributes"]
            )
        )
    if "operation_details" in value:
        import capo_cloudwatchomni.types.operation_details

        out["operationDetails"] = (
            capo_cloudwatchomni.types.operation_details.serialize_cbor(
                value["operation_details"]
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
    if "edges" in value:
        import capo_cloudwatchomni.types.edge_list

        out["edges"] = capo_cloudwatchomni.types.edge_list.serialize_cbor(
            value["edges"]
        )
    return out


def deserialize_cbor(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("nodeId") is not None:
        out["node_id"] = data["nodeId"]
    if data.get("nodeType") is not None:
        import capo_cloudwatchomni.types.node_type

        out["node_type"] = capo_cloudwatchomni.types.node_type.deserialize_cbor(
            data["nodeType"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("alternateNames") is not None:
        import capo_cloudwatchomni.types.string_set

        out["alternate_names"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["alternateNames"]
        )
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.intelligence_tag_map

        out["tags"] = capo_cloudwatchomni.types.intelligence_tag_map.deserialize_cbor(
            data["tags"]
        )
    if data.get("nodeProperties") is not None:
        import capo_cloudwatchomni.types.node_properties

        out["node_properties"] = (
            capo_cloudwatchomni.types.node_properties.deserialize_cbor(
                data["nodeProperties"]
            )
        )
    if data.get("telemetryAttributes") is not None:
        import capo_cloudwatchomni.types.context_graph_attribute_map

        out["telemetry_attributes"] = (
            capo_cloudwatchomni.types.context_graph_attribute_map.deserialize_cbor(
                data["telemetryAttributes"]
            )
        )
    if data.get("operationDetails") is not None:
        import capo_cloudwatchomni.types.operation_details

        out["operation_details"] = (
            capo_cloudwatchomni.types.operation_details.deserialize_cbor(
                data["operationDetails"]
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
    if data.get("edges") is not None:
        import capo_cloudwatchomni.types.edge_list

        out["edges"] = capo_cloudwatchomni.types.edge_list.deserialize_cbor(
            data["edges"]
        )
    return out
