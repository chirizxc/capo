"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.filter_action
    import capo_guardduty.types.filter_description
    import capo_guardduty.types.filter_name
    import capo_guardduty.types.filter_rank
    import capo_guardduty.types.filter_version
    import capo_guardduty.types.finding_criteria
    import capo_guardduty.types.tag_map
    import capo_guardduty.types.timestamp


class GetFilterResponse(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""
    description: NotRequired[
        "capo_guardduty.types.filter_description.FilterDescription"
    ]
    """<p>The description of the filter.</p>"""
    action: NotRequired["capo_guardduty.types.filter_action.FilterAction"]
    """<p>Specifies the action that is to be applied to the findings that match the filter.</p>"""
    rank: NotRequired["capo_guardduty.types.filter_rank.FilterRank"]
    """<p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>"""
    finding_criteria: NotRequired[
        "capo_guardduty.types.finding_criteria.FindingCriteria"
    ]
    """<p>Represents the criteria to be used in the filter for querying findings.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags of the filter resource.</p>"""
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the filter was created. This field is not available for filters that were created before the lifecycle metadata feature was enabled (legacy filters).</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the filter was last updated. For legacy filters, this field is present only after the filter has been updated at least once since the lifecycle metadata feature was enabled.</p>"""
    version: NotRequired["capo_guardduty.types.filter_version.FilterVersion"]
    """<p>The version of the filter. Every time the filter is updated, the version increments by 1. This field is not available for legacy filters that were created before the lifecycle metadata feature was enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFilterResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "action" in value:
        import capo_guardduty.types.filter_action

        out["action"] = capo_guardduty.types.filter_action.serialize_json(
            value["action"]
        )
    if "rank" in value:
        out["rank"] = value["rank"]
    if "finding_criteria" in value:
        import capo_guardduty.types.finding_criteria

        out["findingCriteria"] = capo_guardduty.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    if "created_at" in value:
        import capo_guardduty.types.timestamp

        out["createdAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetFilterResponse:
    out: GetFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("action") is not None:
        import capo_guardduty.types.filter_action

        out["action"] = capo_guardduty.types.filter_action.deserialize_json(
            data["action"]
        )
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    if data.get("findingCriteria") is not None:
        import capo_guardduty.types.finding_criteria

        out["finding_criteria"] = (
            capo_guardduty.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if data.get("tags") is not None:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    if data.get("createdAt") is not None:
        import capo_guardduty.types.timestamp

        out["created_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
