"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.resource_unique_id
    import capo_iotfleetwise.types.timestamp


class StateTemplateSummary(TypedDict, closed=True):
    name: NotRequired["capo_iotfleetwise.types.resource_name.resourceName"]
    """<p>The name of the state template.</p>"""
    arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the state template.</p>"""
    signal_catalog_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the signal catalog associated with the state template.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    creation_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the state template was created, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the state template was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    id: NotRequired["capo_iotfleetwise.types.resource_unique_id.ResourceUniqueId"]
    """<p>The unique ID of the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StateTemplateSummary:
    out: StateTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if data.get("lastModificationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
