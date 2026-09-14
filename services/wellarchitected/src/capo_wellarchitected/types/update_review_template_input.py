"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.review_template_lens_aliases
    import capo_wellarchitected.types.template_arn
    import capo_wellarchitected.types.template_description
    import capo_wellarchitected.types.template_name


class UpdateReviewTemplateInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    template_name: NotRequired["capo_wellarchitected.types.template_name.TemplateName"]
    """<p>The review template name.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>The review template description.</p>"""
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    lenses_to_associate: NotRequired[
        "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
    ]
    """<p>A list of lens aliases or ARNs to apply to the review template.</p>"""
    lenses_to_disassociate: NotRequired[
        "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
    ]
    """<p>A list of lens aliases or ARNs to unapply to the review template. The <code>wellarchitected</code> lens cannot be unapplied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateInput) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "lenses_to_associate" in value:
        import capo_wellarchitected.types.review_template_lens_aliases

        out["LensesToAssociate"] = (
            capo_wellarchitected.types.review_template_lens_aliases.serialize_json(
                value["lenses_to_associate"]
            )
        )
    if "lenses_to_disassociate" in value:
        import capo_wellarchitected.types.review_template_lens_aliases

        out["LensesToDisassociate"] = (
            capo_wellarchitected.types.review_template_lens_aliases.serialize_json(
                value["lenses_to_disassociate"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateInput:
    out: UpdateReviewTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("LensesToAssociate") is not None:
        import capo_wellarchitected.types.review_template_lens_aliases

        out["lenses_to_associate"] = (
            capo_wellarchitected.types.review_template_lens_aliases.deserialize_json(
                data["LensesToAssociate"]
            )
        )
    if data.get("LensesToDisassociate") is not None:
        import capo_wellarchitected.types.review_template_lens_aliases

        out["lenses_to_disassociate"] = (
            capo_wellarchitected.types.review_template_lens_aliases.deserialize_json(
                data["LensesToDisassociate"]
            )
        )
    return out
