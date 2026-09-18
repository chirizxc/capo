"""Generated from Smithy shape ``com.amazonaws.securityhub#CustomDataIdentifiersDetections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.occurrences


class CustomDataIdentifiersDetections(TypedDict, closed=True):
    count: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The total number of occurrences of sensitive data that were detected.</p>"""
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the custom identifier that was used to detect the sensitive data.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>he name of the custom identifier that detected the sensitive data.</p>"""
    occurrences: NotRequired["capo_securityhub.types.occurrences.Occurrences"]
    """<p>Details about the sensitive data that was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifiersDetections) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "occurrences" in value:
        import capo_securityhub.types.occurrences

        out["Occurrences"] = capo_securityhub.types.occurrences.serialize_json(
            value["occurrences"]
        )
    return out


def deserialize_json(data: dict) -> CustomDataIdentifiersDetections:
    out: CustomDataIdentifiersDetections = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Occurrences") is not None:
        import capo_securityhub.types.occurrences

        out["occurrences"] = capo_securityhub.types.occurrences.deserialize_json(
            data["Occurrences"]
        )
    return out
