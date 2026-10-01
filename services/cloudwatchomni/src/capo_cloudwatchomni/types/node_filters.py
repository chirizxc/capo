"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.context_graph_id
    import capo_cloudwatchomni.types.context_graph_name
    import capo_cloudwatchomni.types.key_filter_list
    import capo_cloudwatchomni.types.node_category_set
    import capo_cloudwatchomni.types.node_type
    import capo_cloudwatchomni.types.source_set
    import capo_cloudwatchomni.types.string_set


class NodeFilters(TypedDict, closed=True):
    node_id: NotRequired["capo_cloudwatchomni.types.context_graph_id.ContextGraphId"]
    """Match only the node with this identifier."""
    node_type: NotRequired["capo_cloudwatchomni.types.node_type.NodeType"]
    """Match only nodes of this type."""
    name: NotRequired["capo_cloudwatchomni.types.context_graph_name.ContextGraphName"]
    """Match only nodes with this name."""
    tags: NotRequired["capo_cloudwatchomni.types.key_filter_list.KeyFilterList"]
    """Match nodes by the tags on the underlying resource."""
    telemetry_attributes: NotRequired[
        "capo_cloudwatchomni.types.key_filter_list.KeyFilterList"
    ]
    """Match nodes by their OpenTelemetry (OTel) telemetry attributes."""
    region: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Match nodes in any of these regions."""
    cloud_provider: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Match nodes on any of these cloud providers."""
    source_account_id: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Match nodes discovered from telemetry produced by any of these accounts."""
    namespace: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Match nodes in any of these logical service groupings."""
    category: NotRequired["capo_cloudwatchomni.types.node_category_set.NodeCategorySet"]
    """Match nodes of any of these categories."""
    stage: NotRequired["capo_cloudwatchomni.types.string_set.StringSet"]
    """Match nodes observed in any of these deployment environments."""
    sources: NotRequired["capo_cloudwatchomni.types.source_set.SourceSet"]
    """Match nodes contributed by any of these discovery sources."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeFilters) -> dict:
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
    if "tags" in value:
        import capo_cloudwatchomni.types.key_filter_list

        out["tags"] = capo_cloudwatchomni.types.key_filter_list.serialize_cbor(
            value["tags"]
        )
    if "telemetry_attributes" in value:
        import capo_cloudwatchomni.types.key_filter_list

        out["telemetryAttributes"] = (
            capo_cloudwatchomni.types.key_filter_list.serialize_cbor(
                value["telemetry_attributes"]
            )
        )
    if "region" in value:
        import capo_cloudwatchomni.types.string_set

        out["region"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["region"]
        )
    if "cloud_provider" in value:
        import capo_cloudwatchomni.types.string_set

        out["cloudProvider"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["cloud_provider"]
        )
    if "source_account_id" in value:
        import capo_cloudwatchomni.types.string_set

        out["sourceAccountId"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["source_account_id"]
        )
    if "namespace" in value:
        import capo_cloudwatchomni.types.string_set

        out["namespace"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["namespace"]
        )
    if "category" in value:
        import capo_cloudwatchomni.types.node_category_set

        out["category"] = capo_cloudwatchomni.types.node_category_set.serialize_cbor(
            value["category"]
        )
    if "stage" in value:
        import capo_cloudwatchomni.types.string_set

        out["stage"] = capo_cloudwatchomni.types.string_set.serialize_cbor(
            value["stage"]
        )
    if "sources" in value:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.serialize_cbor(
            value["sources"]
        )
    return out


def deserialize_cbor(data: dict) -> NodeFilters:
    out: NodeFilters = {}  # type: ignore[typeddict-item]
    if data.get("nodeId") is not None:
        out["node_id"] = data["nodeId"]
    if data.get("nodeType") is not None:
        import capo_cloudwatchomni.types.node_type

        out["node_type"] = capo_cloudwatchomni.types.node_type.deserialize_cbor(
            data["nodeType"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.key_filter_list

        out["tags"] = capo_cloudwatchomni.types.key_filter_list.deserialize_cbor(
            data["tags"]
        )
    if data.get("telemetryAttributes") is not None:
        import capo_cloudwatchomni.types.key_filter_list

        out["telemetry_attributes"] = (
            capo_cloudwatchomni.types.key_filter_list.deserialize_cbor(
                data["telemetryAttributes"]
            )
        )
    if data.get("region") is not None:
        import capo_cloudwatchomni.types.string_set

        out["region"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["region"]
        )
    if data.get("cloudProvider") is not None:
        import capo_cloudwatchomni.types.string_set

        out["cloud_provider"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["cloudProvider"]
        )
    if data.get("sourceAccountId") is not None:
        import capo_cloudwatchomni.types.string_set

        out["source_account_id"] = (
            capo_cloudwatchomni.types.string_set.deserialize_cbor(
                data["sourceAccountId"]
            )
        )
    if data.get("namespace") is not None:
        import capo_cloudwatchomni.types.string_set

        out["namespace"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["namespace"]
        )
    if data.get("category") is not None:
        import capo_cloudwatchomni.types.node_category_set

        out["category"] = capo_cloudwatchomni.types.node_category_set.deserialize_cbor(
            data["category"]
        )
    if data.get("stage") is not None:
        import capo_cloudwatchomni.types.string_set

        out["stage"] = capo_cloudwatchomni.types.string_set.deserialize_cbor(
            data["stage"]
        )
    if data.get("sources") is not None:
        import capo_cloudwatchomni.types.source_set

        out["sources"] = capo_cloudwatchomni.types.source_set.deserialize_cbor(
            data["sources"]
        )
    return out
