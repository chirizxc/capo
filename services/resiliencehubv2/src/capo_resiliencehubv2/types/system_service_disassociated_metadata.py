"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemServiceDisassociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.user_journey_name_list


class SystemServiceDisassociatedMetadata(TypedDict, closed=True):
    service_name: NotRequired["str"]
    """<p>The name of the disassociated service.</p>"""
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    user_journeys_affected: NotRequired[
        "capo_resiliencehubv2.types.user_journey_name_list.UserJourneyNameList"
    ]
    """<p>The user journeys affected by the disassociation.</p>"""
    comment: NotRequired["str"]
    """<p>A comment about the disassociation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemServiceDisassociatedMetadata) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "user_journeys_affected" in value:
        import capo_resiliencehubv2.types.user_journey_name_list

        out["userJourneysAffected"] = (
            capo_resiliencehubv2.types.user_journey_name_list.serialize_json(
                value["user_journeys_affected"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> SystemServiceDisassociatedMetadata:
    out: SystemServiceDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("userJourneysAffected") is not None:
        import capo_resiliencehubv2.types.user_journey_name_list

        out["user_journeys_affected"] = (
            capo_resiliencehubv2.types.user_journey_name_list.deserialize_json(
                data["userJourneysAffected"]
            )
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
