"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateReviewTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.review_template_lenses
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.template_description
    import capo_wellarchitected.types.template_name


class CreateReviewTemplateInput(TypedDict, closed=True):
    template_name: NotRequired["capo_wellarchitected.types.template_name.TemplateName"]
    """<p>Name of the review template.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>The review template description.</p>"""
    lenses: NotRequired[
        "capo_wellarchitected.types.review_template_lenses.ReviewTemplateLenses"
    ]
    """<p>Lenses applied to the review template.</p>"""
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    tags: NotRequired["capo_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the review template.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateReviewTemplateInput) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lenses" in value:
        import capo_wellarchitected.types.review_template_lenses

        out["Lenses"] = (
            capo_wellarchitected.types.review_template_lenses.serialize_json(
                value["lenses"]
            )
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "tags" in value:
        import capo_wellarchitected.types.tag_map

        out["Tags"] = capo_wellarchitected.types.tag_map.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateReviewTemplateInput:
    out: CreateReviewTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Lenses") is not None:
        import capo_wellarchitected.types.review_template_lenses

        out["lenses"] = (
            capo_wellarchitected.types.review_template_lenses.deserialize_json(
                data["Lenses"]
            )
        )
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("Tags") is not None:
        import capo_wellarchitected.types.tag_map

        out["tags"] = capo_wellarchitected.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
