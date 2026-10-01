"""Generated from Smithy shape ``com.amazonaws.elementalinference#CroppingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.template_group_list


class CroppingConfig(TypedDict, closed=True):
    template_groups: NotRequired[
        "capo_elementalinference.types.template_group_list.TemplateGroupList"
    ]
    """<p>An array of template groups for the crop output. Each template group provides the graphics-compositing templates that Elemental Inference applies to the cropped video. You can specify from 1 to 4 template groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CroppingConfig) -> dict:
    out: dict = {}
    if "template_groups" in value:
        import capo_elementalinference.types.template_group_list

        out["templateGroups"] = (
            capo_elementalinference.types.template_group_list.serialize_json(
                value["template_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> CroppingConfig:
    out: CroppingConfig = {}  # type: ignore[typeddict-item]
    if data.get("templateGroups") is not None:
        import capo_elementalinference.types.template_group_list

        out["template_groups"] = (
            capo_elementalinference.types.template_group_list.deserialize_json(
                data["templateGroups"]
            )
        )
    return out
