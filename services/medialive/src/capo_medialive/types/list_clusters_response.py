"""Generated from Smithy shape ``com.amazonaws.medialive#ListClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_describe_cluster_summary
    import capo_medialive.types.__string


class ListClustersResponse(TypedDict, closed=True):
    clusters: NotRequired[
        "capo_medialive.types.__list_of_describe_cluster_summary.__listOfDescribeClusterSummary"
    ]
    """A list of the Clusters that exist in your AWS account."""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """Token for the next result."""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_medialive.types.__list_of_describe_cluster_summary

        out["clusters"] = (
            capo_medialive.types.__list_of_describe_cluster_summary.serialize_json(
                value["clusters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if data.get("clusters") is not None:
        import capo_medialive.types.__list_of_describe_cluster_summary

        out["clusters"] = (
            capo_medialive.types.__list_of_describe_cluster_summary.deserialize_json(
                data["clusters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
