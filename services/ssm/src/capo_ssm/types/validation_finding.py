"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string
    import capo_ssm.types.validation_finding_code
    import capo_ssm.types.validation_finding_scope
    import capo_ssm.types.validation_finding_type


class ValidationFinding(TypedDict, closed=True):
    type: NotRequired["capo_ssm.types.validation_finding_type.ValidationFindingType"]
    """<p>The type of the validation finding.</p>"""
    code: NotRequired["capo_ssm.types.validation_finding_code.ValidationFindingCode"]
    """<p>A code that identifies the specific validation finding.</p>"""
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>A message that describes the validation finding.</p>"""
    provider_message: NotRequired["capo_ssm.types.string.String"]
    """<p>A message from the third-party cloud provider related to the validation finding.</p>"""
    scope: NotRequired["capo_ssm.types.validation_finding_scope.ValidationFindingScope"]
    """<p>The scope of the validation finding, identifying the specific resource affected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationFinding) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ssm.types.validation_finding_type

        out["Type"] = capo_ssm.types.validation_finding_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "code" in value:
        import capo_ssm.types.validation_finding_code

        out["Code"] = capo_ssm.types.validation_finding_code.serialize_aws_json_1_1(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "provider_message" in value:
        out["ProviderMessage"] = value["provider_message"]
    if "scope" in value:
        import capo_ssm.types.validation_finding_scope

        out["Scope"] = capo_ssm.types.validation_finding_scope.serialize_aws_json_1_1(
            value["scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationFinding:
    out: ValidationFinding = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_ssm.types.validation_finding_type

        out["type"] = capo_ssm.types.validation_finding_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Code") is not None:
        import capo_ssm.types.validation_finding_code

        out["code"] = capo_ssm.types.validation_finding_code.deserialize_aws_json_1_1(
            data["Code"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ProviderMessage") is not None:
        out["provider_message"] = data["ProviderMessage"]
    if data.get("Scope") is not None:
        import capo_ssm.types.validation_finding_scope

        out["scope"] = capo_ssm.types.validation_finding_scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    return out
