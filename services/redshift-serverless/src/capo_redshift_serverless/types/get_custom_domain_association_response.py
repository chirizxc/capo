"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCustomDomainAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.workgroup_name


class GetCustomDomainAssociationResponse(TypedDict, closed=True):
    custom_domain_name: NotRequired[
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    ]
    """<p>The custom domain name associated with the workgroup.</p>"""
    workgroup_name: NotRequired[
        "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    ]
    """<p>The name of the workgroup associated with the database.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""
    custom_domain_certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The expiration time for the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCustomDomainAssociationResponse) -> dict:
    out: dict = {}
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "custom_domain_certificate_arn" in value:
        out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    if "custom_domain_certificate_expiry_time" in value:
        import capo_redshift_serverless._protocol.serialize

        out["customDomainCertificateExpiryTime"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["custom_domain_certificate_expiry_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCustomDomainAssociationResponse:
    out: GetCustomDomainAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    if data.get("customDomainCertificateArn") is not None:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    if data.get("customDomainCertificateExpiryTime") is not None:
        import datetime

        out["custom_domain_certificate_expiry_time"] = datetime.datetime.fromisoformat(
            data["customDomainCertificateExpiryTime"].replace("Z", "+00:00")
        )
    return out
