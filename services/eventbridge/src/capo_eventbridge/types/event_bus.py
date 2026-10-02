"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventBus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_bus_description
    import capo_eventbridge.types.managed_by
    import capo_eventbridge.types.string
    import capo_eventbridge.types.timestamp


class EventBus(TypedDict, closed=True):
    name: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The name of the event bus.</p>"""
    arn: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The ARN of the event bus.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    policy: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The permissions policy of the event bus, describing which other Amazon Web Services accounts can write events to this event bus.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was last modified.</p>"""
    managed_by: NotRequired["capo_eventbridge.types.managed_by.ManagedBy"]
    """<p>If the event bus was created on behalf of your account by an Amazon Web Services service, this field displays the principal name of the service that created the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBus) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBus:
    out: EventBus = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("ManagedBy") is not None:
        out["managed_by"] = data["ManagedBy"]
    return out
