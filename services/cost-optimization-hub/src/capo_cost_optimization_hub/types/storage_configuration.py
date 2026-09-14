"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#StorageConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class StorageConfiguration(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The storage type.</p>"""
    size_in_gb: NotRequired["float"]
    """<p>The storage volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "size_in_gb" in value:
        out["sizeInGb"] = (
            "NaN"
            if value["size_in_gb"] != value["size_in_gb"]
            else "Infinity"
            if value["size_in_gb"] == float("inf")
            else "-Infinity"
            if value["size_in_gb"] == float("-inf")
            else value["size_in_gb"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = float(data["sizeInGb"])
    return out
