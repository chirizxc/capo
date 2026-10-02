"""Generated from Smithy shape ``com.amazonaws.ssm#ValidateCloudConnectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.validation_finding_list


class ValidateCloudConnectorResult(TypedDict, closed=True):
    validation_findings: NotRequired[
        "capo_ssm.types.validation_finding_list.ValidationFindingList"
    ]
    """<p>A list of validation findings for the cloud connector.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateCloudConnectorResult) -> dict:
    out: dict = {}
    if "validation_findings" in value:
        import capo_ssm.types.validation_finding_list

        out["ValidationFindings"] = (
            capo_ssm.types.validation_finding_list.serialize_aws_json_1_1(
                value["validation_findings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateCloudConnectorResult:
    out: ValidateCloudConnectorResult = {}  # type: ignore[typeddict-item]
    if data.get("ValidationFindings") is not None:
        import capo_ssm.types.validation_finding_list

        out["validation_findings"] = (
            capo_ssm.types.validation_finding_list.deserialize_aws_json_1_1(
                data["ValidationFindings"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
