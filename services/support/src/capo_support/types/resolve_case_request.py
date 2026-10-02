"""Generated from Smithy shape ``com.amazonaws.support#ResolveCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.case_id
    import capo_support.types.nullable_boolean_type


class ResolveCaseRequest(TypedDict, closed=True):
    case_id: NotRequired["capo_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually resolving the case. When set to <code>true</code>, the request is validated but the case isn't resolved, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolveCaseRequest) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolveCaseRequest:
    out: ResolveCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
