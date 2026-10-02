"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatEvidenceShape``."""

from typing_extensions import NotRequired, TypedDict


class ThreatEvidenceShape(TypedDict, closed=True):
    package_id: NotRequired["str"]
    """<p>The package identifier containing the evidence file.</p>"""
    path: NotRequired["str"]
    """<p>The file path of the evidence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatEvidenceShape) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["packageId"] = value["package_id"]
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> ThreatEvidenceShape:
    out: ThreatEvidenceShape = {}  # type: ignore[typeddict-item]
    if data.get("packageId") is not None:
        out["package_id"] = data["packageId"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    return out
