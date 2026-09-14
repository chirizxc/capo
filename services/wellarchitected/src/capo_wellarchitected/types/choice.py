"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Choice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.additional_resources_list
    import capo_wellarchitected.types.choice_content
    import capo_wellarchitected.types.choice_description
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.choice_title


class Choice(TypedDict, closed=True):
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]
    title: NotRequired["capo_wellarchitected.types.choice_title.ChoiceTitle"]
    description: NotRequired[
        "capo_wellarchitected.types.choice_description.ChoiceDescription"
    ]
    helpful_resource: NotRequired[
        "capo_wellarchitected.types.choice_content.ChoiceContent"
    ]
    """<p>The helpful resource (both text and URL) for a particular choice.</p> <p>This field only applies to custom lenses. Each choice can have only one helpful resource.</p>"""
    improvement_plan: NotRequired[
        "capo_wellarchitected.types.choice_content.ChoiceContent"
    ]
    """<p>The improvement plan (both text and URL) for a particular choice.</p> <p>This field only applies to custom lenses. Each choice can have only one improvement plan.</p>"""
    additional_resources: NotRequired[
        "capo_wellarchitected.types.additional_resources_list.AdditionalResourcesList"
    ]
    """<p>The additional resources for a choice in a custom lens.</p> <p>A choice can have up to two additional resources: one of type <code>HELPFUL_RESOURCE</code>, one of type <code>IMPROVEMENT_PLAN</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Choice) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "helpful_resource" in value:
        import capo_wellarchitected.types.choice_content

        out["HelpfulResource"] = (
            capo_wellarchitected.types.choice_content.serialize_json(
                value["helpful_resource"]
            )
        )
    if "improvement_plan" in value:
        import capo_wellarchitected.types.choice_content

        out["ImprovementPlan"] = (
            capo_wellarchitected.types.choice_content.serialize_json(
                value["improvement_plan"]
            )
        )
    if "additional_resources" in value:
        import capo_wellarchitected.types.additional_resources_list

        out["AdditionalResources"] = (
            capo_wellarchitected.types.additional_resources_list.serialize_json(
                value["additional_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> Choice:
    out: Choice = {}  # type: ignore[typeddict-item]
    if data.get("ChoiceId") is not None:
        out["choice_id"] = data["ChoiceId"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("HelpfulResource") is not None:
        import capo_wellarchitected.types.choice_content

        out["helpful_resource"] = (
            capo_wellarchitected.types.choice_content.deserialize_json(
                data["HelpfulResource"]
            )
        )
    if data.get("ImprovementPlan") is not None:
        import capo_wellarchitected.types.choice_content

        out["improvement_plan"] = (
            capo_wellarchitected.types.choice_content.deserialize_json(
                data["ImprovementPlan"]
            )
        )
    if data.get("AdditionalResources") is not None:
        import capo_wellarchitected.types.additional_resources_list

        out["additional_resources"] = (
            capo_wellarchitected.types.additional_resources_list.deserialize_json(
                data["AdditionalResources"]
            )
        )
    return out
