"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Checksum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.checksum_string
    import capo_sagemaker_edge.types.checksum_type


class Checksum(TypedDict, closed=True):
    type: NotRequired["capo_sagemaker_edge.types.checksum_type.ChecksumType"]
    """<p>The type of the checksum.</p>"""
    sum: NotRequired["capo_sagemaker_edge.types.checksum_string.ChecksumString"]
    """<p>The checksum of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Checksum) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker_edge.types.checksum_type

        out["Type"] = capo_sagemaker_edge.types.checksum_type.serialize_json(
            value["type"]
        )
    if "sum" in value:
        out["Sum"] = value["sum"]
    return out


def deserialize_json(data: dict) -> Checksum:
    out: Checksum = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_sagemaker_edge.types.checksum_type

        out["type"] = capo_sagemaker_edge.types.checksum_type.deserialize_json(
            data["Type"]
        )
    if data.get("Sum") is not None:
        out["sum"] = data["Sum"]
    return out
