"""Generated from Smithy shape ``com.amazonaws.glue#DistributionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.bin_edges
    import capo_glue.types.count
    import capo_glue.types.name_string


class DistributionData(TypedDict, closed=True):
    bin_edges: NotRequired["capo_glue.types.bin_edges.BinEdges"]
    """<p>The bin edge values for the distribution.</p>"""
    count: NotRequired["capo_glue.types.count.Count"]
    """<p>The frequency count for each bin in the distribution.</p>"""
    data_type: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The data type of the column for the distribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionData) -> dict:
    out: dict = {}
    if "bin_edges" in value:
        import capo_glue.types.bin_edges

        out["BinEdges"] = capo_glue.types.bin_edges.serialize_aws_json_1_1(
            value["bin_edges"]
        )
    if "count" in value:
        import capo_glue.types.count

        out["Count"] = capo_glue.types.count.serialize_aws_json_1_1(value["count"])
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributionData:
    out: DistributionData = {}  # type: ignore[typeddict-item]
    if data.get("BinEdges") is not None:
        import capo_glue.types.bin_edges

        out["bin_edges"] = capo_glue.types.bin_edges.deserialize_aws_json_1_1(
            data["BinEdges"]
        )
    if data.get("Count") is not None:
        import capo_glue.types.count

        out["count"] = capo_glue.types.count.deserialize_aws_json_1_1(data["Count"])
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out
