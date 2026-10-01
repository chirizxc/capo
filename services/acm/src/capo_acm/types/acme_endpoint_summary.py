"""Generated from Smithy shape ``com.amazonaws.acm#AcmeEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_acm.types.acme_authorization_behavior
    import capo_acm.types.acme_contact
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.acme_endpoint_status
    import capo_acm.types.certificate_authority
    import capo_acm.types.tag_list


class AcmeEndpointSummary(TypedDict, closed=True):
    acme_endpoint_arn: NotRequired["capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    endpoint_url: NotRequired["str"]
    """<p>The URL of the ACME endpoint.</p>"""
    status: NotRequired["capo_acm.types.acme_endpoint_status.AcmeEndpointStatus"]
    """<p>The status of the ACME endpoint.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason the ACME endpoint failed, if applicable.</p>"""
    authorization_behavior: NotRequired[
        "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior"
    ]
    """<p>The authorization behavior of the ACME endpoint.</p>"""
    contact: NotRequired["capo_acm.types.acme_contact.AcmeContact"]
    """<p>Whether ACME clients must provide contact information during account registration.</p>"""
    certificate_authority: NotRequired[
        "capo_acm.types.certificate_authority.CertificateAuthority"
    ]
    """<p>The certificate authority configuration for the ACME endpoint.</p>"""
    certificate_tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>Tags applied to certificates issued through this ACME endpoint.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time at which the ACME endpoint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time at which the ACME endpoint was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeEndpointSummary) -> dict:
    out: dict = {}
    if "acme_endpoint_arn" in value:
        out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "status" in value:
        import capo_acm.types.acme_endpoint_status

        out["Status"] = capo_acm.types.acme_endpoint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "authorization_behavior" in value:
        import capo_acm.types.acme_authorization_behavior

        out["AuthorizationBehavior"] = (
            capo_acm.types.acme_authorization_behavior.serialize_aws_json_1_1(
                value["authorization_behavior"]
            )
        )
    if "contact" in value:
        import capo_acm.types.acme_contact

        out["Contact"] = capo_acm.types.acme_contact.serialize_aws_json_1_1(
            value["contact"]
        )
    if "certificate_authority" in value:
        import capo_acm.types.certificate_authority

        out["CertificateAuthority"] = (
            capo_acm.types.certificate_authority.serialize_aws_json_1_1(
                value["certificate_authority"]
            )
        )
    if "certificate_tags" in value:
        import capo_acm.types.tag_list

        out["CertificateTags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(
            value["certificate_tags"]
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


def deserialize_aws_json_1_1(data: dict) -> AcmeEndpointSummary:
    out: AcmeEndpointSummary = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    if data.get("EndpointUrl") is not None:
        out["endpoint_url"] = data["EndpointUrl"]
    if data.get("Status") is not None:
        import capo_acm.types.acme_endpoint_status

        out["status"] = capo_acm.types.acme_endpoint_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("AuthorizationBehavior") is not None:
        import capo_acm.types.acme_authorization_behavior

        out["authorization_behavior"] = (
            capo_acm.types.acme_authorization_behavior.deserialize_aws_json_1_1(
                data["AuthorizationBehavior"]
            )
        )
    if data.get("Contact") is not None:
        import capo_acm.types.acme_contact

        out["contact"] = capo_acm.types.acme_contact.deserialize_aws_json_1_1(
            data["Contact"]
        )
    if data.get("CertificateAuthority") is not None:
        import capo_acm.types.certificate_authority

        out["certificate_authority"] = (
            capo_acm.types.certificate_authority.deserialize_aws_json_1_1(
                data["CertificateAuthority"]
            )
        )
    if data.get("CertificateTags") is not None:
        import capo_acm.types.tag_list

        out["certificate_tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(
            data["CertificateTags"]
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
