"""Generated from Smithy shape ``com.amazonaws.acm#EmailValidationChallenge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_name_string
    import capo_acm.types.validation_email_list


class EmailValidationChallenge(TypedDict, closed=True):
    validation_emails: NotRequired[
        "capo_acm.types.validation_email_list.ValidationEmailList"
    ]
    """<p>A list of email addresses that ACM uses to send domain validation emails.</p>"""
    validation_domain: NotRequired["capo_acm.types.domain_name_string.DomainNameString"]
    """<p>The domain name that ACM uses to send validation emails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailValidationChallenge) -> dict:
    out: dict = {}
    if "validation_emails" in value:
        import capo_acm.types.validation_email_list

        out["ValidationEmails"] = (
            capo_acm.types.validation_email_list.serialize_aws_json_1_1(
                value["validation_emails"]
            )
        )
    if "validation_domain" in value:
        out["ValidationDomain"] = value["validation_domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailValidationChallenge:
    out: EmailValidationChallenge = {}  # type: ignore[typeddict-item]
    if data.get("ValidationEmails") is not None:
        import capo_acm.types.validation_email_list

        out["validation_emails"] = (
            capo_acm.types.validation_email_list.deserialize_aws_json_1_1(
                data["ValidationEmails"]
            )
        )
    if data.get("ValidationDomain") is not None:
        out["validation_domain"] = data["ValidationDomain"]
    return out
