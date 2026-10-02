"""Generated from Smithy shape ``com.amazonaws.acm#AcmeDomainValidationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_acm.types.acme_domain_validation_arn
    import capo_acm.types.acme_domain_validation_status
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.domain_name
    import capo_acm.types.failure_details
    import capo_acm.types.prevalidation_details
    import capo_acm.types.prevalidation_type


class AcmeDomainValidationSummary(TypedDict, closed=True):
    acme_domain_validation_arn: NotRequired[
        "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ACME domain validation.</p>"""
    acme_endpoint_arn: NotRequired["capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    domain_name: NotRequired["capo_acm.types.domain_name.DomainName"]
    """<p>The domain name being validated.</p>"""
    prevalidation_type: NotRequired[
        "capo_acm.types.prevalidation_type.PrevalidationType"
    ]
    """<p>The type of prevalidation used.</p>"""
    prevalidation_details: NotRequired[
        "capo_acm.types.prevalidation_details.PrevalidationDetails"
    ]
    """<p>Details about the prevalidation configuration.</p>"""
    status: NotRequired[
        "capo_acm.types.acme_domain_validation_status.AcmeDomainValidationStatus"
    ]
    """<p>The status of the domain validation.</p>"""
    failure_details: NotRequired["capo_acm.types.failure_details.FailureDetails"]
    """<p>Details about the failure, if the validation failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time at which the domain validation was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time at which the domain validation was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeDomainValidationSummary) -> dict:
    out: dict = {}
    if "acme_domain_validation_arn" in value:
        out["AcmeDomainValidationArn"] = value["acme_domain_validation_arn"]
    if "acme_endpoint_arn" in value:
        out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "prevalidation_type" in value:
        import capo_acm.types.prevalidation_type

        out["PrevalidationType"] = (
            capo_acm.types.prevalidation_type.serialize_aws_json_1_1(
                value["prevalidation_type"]
            )
        )
    if "prevalidation_details" in value:
        import capo_acm.types.prevalidation_details

        out["PrevalidationDetails"] = (
            capo_acm.types.prevalidation_details.serialize_aws_json_1_1(
                value["prevalidation_details"]
            )
        )
    if "status" in value:
        import capo_acm.types.acme_domain_validation_status

        out["Status"] = (
            capo_acm.types.acme_domain_validation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_details" in value:
        import capo_acm.types.failure_details

        out["FailureDetails"] = capo_acm.types.failure_details.serialize_aws_json_1_1(
            value["failure_details"]
        )
    if "created_at" in value:
        import capo_acm.types._prelude.timestamp

        out["CreatedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_acm.types._prelude.timestamp

        out["UpdatedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcmeDomainValidationSummary:
    out: AcmeDomainValidationSummary = {}  # type: ignore[typeddict-item]
    if data.get("AcmeDomainValidationArn") is not None:
        out["acme_domain_validation_arn"] = data["AcmeDomainValidationArn"]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("PrevalidationType") is not None:
        import capo_acm.types.prevalidation_type

        out["prevalidation_type"] = (
            capo_acm.types.prevalidation_type.deserialize_aws_json_1_1(
                data["PrevalidationType"]
            )
        )
    if data.get("PrevalidationDetails") is not None:
        import capo_acm.types.prevalidation_details

        out["prevalidation_details"] = (
            capo_acm.types.prevalidation_details.deserialize_aws_json_1_1(
                data["PrevalidationDetails"]
            )
        )
    if data.get("Status") is not None:
        import capo_acm.types.acme_domain_validation_status

        out["status"] = (
            capo_acm.types.acme_domain_validation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("FailureDetails") is not None:
        import capo_acm.types.failure_details

        out["failure_details"] = (
            capo_acm.types.failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["created_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["updated_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
