"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ecr_scan_frequency


class EcrRepositoryMetadata(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the Amazon ECR repository.</p>"""
    scan_frequency: NotRequired[
        "capo_inspector2.types.ecr_scan_frequency.EcrScanFrequency"
    ]
    """<p>The frequency of scans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrRepositoryMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "scan_frequency" in value:
        out["scanFrequency"] = value["scan_frequency"]
    return out


def deserialize_json(data: dict) -> EcrRepositoryMetadata:
    out: EcrRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("scanFrequency") is not None:
        out["scan_frequency"] = data["scanFrequency"]
    return out
