"""Generated from Smithy shape ``com.amazonaws.mq#DescribeSharedResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of_shared_resource
    import capo_mq.types.__string


class DescribeSharedResourcesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""
    shared_resources: NotRequired[
        "capo_mq.types.__list_of_shared_resource.__listOfSharedResource"
    ]
    """<p>A list of resources shared to the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSharedResourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "shared_resources" in value:
        import capo_mq.types.__list_of_shared_resource

        out["sharedResources"] = capo_mq.types.__list_of_shared_resource.serialize_json(
            value["shared_resources"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSharedResourcesResponse:
    out: DescribeSharedResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("sharedResources") is not None:
        import capo_mq.types.__list_of_shared_resource

        out["shared_resources"] = (
            capo_mq.types.__list_of_shared_resource.deserialize_json(
                data["sharedResources"]
            )
        )
    return out
