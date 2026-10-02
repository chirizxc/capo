"""Generated from Smithy shape ``com.amazonaws.connect#RulesSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.rule_attribute_filter


class RulesSearchFilter(TypedDict, closed=True):
    attribute_filter: NotRequired[
        "capo_connect.types.rule_attribute_filter.RuleAttributeFilter"
    ]
    """<p>An object that can be used to specify tag conditions inside the <code>SearchFilter</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RulesSearchFilter) -> dict:
    out: dict = {}
    if "attribute_filter" in value:
        import capo_connect.types.rule_attribute_filter

        out["AttributeFilter"] = (
            capo_connect.types.rule_attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> RulesSearchFilter:
    out: RulesSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("AttributeFilter") is not None:
        import capo_connect.types.rule_attribute_filter

        out["attribute_filter"] = (
            capo_connect.types.rule_attribute_filter.deserialize_json(
                data["AttributeFilter"]
            )
        )
    return out
