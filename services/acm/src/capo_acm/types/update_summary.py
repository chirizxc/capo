"""Generated from Smithy shape ``com.amazonaws.acm#UpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_validation_method_update_summary
    import capo_acm.types.t_stamp
    import capo_acm.types.update_status
    import capo_acm.types.update_type


class UpdateSummary(TypedDict, closed=True):
    status: NotRequired["capo_acm.types.update_status.UpdateStatus"]
    """<p>The status of the certificate update. The following are valid values:</p> <ul> <li> <p> <code>PENDING_DOMAIN_VALIDATION</code> – The certificate update is waiting for domain ownership validation to complete.</p> </li> <li> <p> <code>SUCCESS</code> – The certificate was updated successfully.</p> </li> <li> <p> <code>FAILED</code> – The certificate update failed.</p> </li> </ul>"""
    type: NotRequired["capo_acm.types.update_type.UpdateType"]
    """<p>The type of update that was requested for the certificate. The following are valid values:</p> <ul> <li> <p> <code>DOMAIN_VALIDATION_METHOD</code> – The update changes the domain validation method for the certificate.</p> </li> </ul>"""
    domain_validation_method_update_summary: NotRequired[
        "capo_acm.types.domain_validation_method_update_summary.DomainValidationMethodUpdateSummary"
    ]
    """<p>Contains information about a domain validation method migration, including the previous and target validation methods.</p>"""
    requested_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate update was requested.</p>"""
    updated_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate update status was last changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_acm.types.update_status

        out["Status"] = capo_acm.types.update_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "type" in value:
        import capo_acm.types.update_type

        out["Type"] = capo_acm.types.update_type.serialize_aws_json_1_1(value["type"])
    if "domain_validation_method_update_summary" in value:
        import capo_acm.types.domain_validation_method_update_summary

        out["DomainValidationMethodUpdateSummary"] = (
            capo_acm.types.domain_validation_method_update_summary.serialize_aws_json_1_1(
                value["domain_validation_method_update_summary"]
            )
        )
    if "requested_at" in value:
        import capo_acm.types.t_stamp

        out["RequestedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["requested_at"]
        )
    if "updated_at" in value:
        import capo_acm.types.t_stamp

        out["UpdatedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSummary:
    out: UpdateSummary = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_acm.types.update_status

        out["status"] = capo_acm.types.update_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Type") is not None:
        import capo_acm.types.update_type

        out["type"] = capo_acm.types.update_type.deserialize_aws_json_1_1(data["Type"])
    if data.get("DomainValidationMethodUpdateSummary") is not None:
        import capo_acm.types.domain_validation_method_update_summary

        out["domain_validation_method_update_summary"] = (
            capo_acm.types.domain_validation_method_update_summary.deserialize_aws_json_1_1(
                data["DomainValidationMethodUpdateSummary"]
            )
        )
    if data.get("RequestedAt") is not None:
        import capo_acm.types.t_stamp

        out["requested_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RequestedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_acm.types.t_stamp

        out["updated_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
