"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEventbusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEventsEventbusDetails(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the account permitted to write events to the current account.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the event bus.</p>"""
    policy: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The policy that enables the external account to send events to your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEventbusDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> AwsEventsEventbusDetails:
    out: AwsEventsEventbusDetails = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
