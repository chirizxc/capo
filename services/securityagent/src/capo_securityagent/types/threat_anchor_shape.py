"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatAnchorShape``."""

from typing_extensions import NotRequired, TypedDict


class ThreatAnchorShape(TypedDict, closed=True):
    kind: NotRequired["str"]
    """<p>The kind of DFD element.</p>"""
    id: NotRequired["str"]
    """<p>The identifier of the DFD element.</p>"""
    package_id: NotRequired["str"]
    """<p>The package identifier containing the DFD element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatAnchorShape) -> dict:
    out: dict = {}
    if "kind" in value:
        out["kind"] = value["kind"]
    if "id" in value:
        out["id"] = value["id"]
    if "package_id" in value:
        out["packageId"] = value["package_id"]
    return out


def deserialize_json(data: dict) -> ThreatAnchorShape:
    out: ThreatAnchorShape = {}  # type: ignore[typeddict-item]
    if data.get("kind") is not None:
        out["kind"] = data["kind"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("packageId") is not None:
        out["package_id"] = data["packageId"]
    return out
