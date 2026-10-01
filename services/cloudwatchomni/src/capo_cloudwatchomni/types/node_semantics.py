"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeSemantics``."""

from typing_extensions import NotRequired, TypedDict


class NodeSemantics(TypedDict, closed=True):
    purpose: NotRequired["str"]
    """What the service does."""
    language: NotRequired["str"]
    """The primary programming language the service is written in."""
    framework: NotRequired["str"]
    """The application framework the service is built on."""
    kind: NotRequired["str"]
    """The kind of workload the service is."""
    repository: NotRequired["str"]
    """The source repository the service is built from."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeSemantics) -> dict:
    out: dict = {}
    if "purpose" in value:
        out["purpose"] = value["purpose"]
    if "language" in value:
        out["language"] = value["language"]
    if "framework" in value:
        out["framework"] = value["framework"]
    if "kind" in value:
        out["kind"] = value["kind"]
    if "repository" in value:
        out["repository"] = value["repository"]
    return out


def deserialize_cbor(data: dict) -> NodeSemantics:
    out: NodeSemantics = {}  # type: ignore[typeddict-item]
    if data.get("purpose") is not None:
        out["purpose"] = data["purpose"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("framework") is not None:
        out["framework"] = data["framework"]
    if data.get("kind") is not None:
        out["kind"] = data["kind"]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    return out
