"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationFindingScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string
    import capo_ssm.types.validation_finding_scope_type


class ValidationFindingScope(TypedDict, closed=True):
    type: NotRequired[
        "capo_ssm.types.validation_finding_scope_type.ValidationFindingScopeType"
    ]
    """<p>The type of the resource scope.</p>"""
    id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of the resource within the scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationFindingScope) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ssm.types.validation_finding_scope_type

        out["Type"] = (
            capo_ssm.types.validation_finding_scope_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationFindingScope:
    out: ValidationFindingScope = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_ssm.types.validation_finding_scope_type

        out["type"] = (
            capo_ssm.types.validation_finding_scope_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
