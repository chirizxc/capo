"""Generated from Smithy shape ``com.amazonaws.eks#AllowedValuesConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.allowed_values_list


class AllowedValuesConstraint(TypedDict, closed=True):
    allowed_values: NotRequired["capo_eks.types.allowed_values_list.AllowedValuesList"]
    """<p>The list of allowed values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedValuesConstraint) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        import capo_eks.types.allowed_values_list

        out["allowedValues"] = capo_eks.types.allowed_values_list.serialize_json(
            value["allowed_values"]
        )
    return out


def deserialize_json(data: dict) -> AllowedValuesConstraint:
    out: AllowedValuesConstraint = {}  # type: ignore[typeddict-item]
    if data.get("allowedValues") is not None:
        import capo_eks.types.allowed_values_list

        out["allowed_values"] = capo_eks.types.allowed_values_list.deserialize_json(
            data["allowedValues"]
        )
    return out
