"""Generated from Smithy shape ``com.amazonaws.acm#ValidationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_status
    import capo_acm.types.validation_challenge
    import capo_acm.types.validation_method


class ValidationConfiguration(TypedDict, closed=True):
    validation_method: NotRequired["capo_acm.types.validation_method.ValidationMethod"]
    """<p>The validation method for this configuration. Valid values:</p> <ul> <li> <p> <code>DNS</code> – Validation using a CNAME record added to your DNS configuration.</p> </li> <li> <p> <code>EMAIL</code> – Validation using an approval email sent to domain contacts.</p> </li> <li> <p> <code>HTTP</code> – Validation using an HTTP resource placed on your web server.</p> </li> </ul>"""
    validation_challenge: NotRequired[
        "capo_acm.types.validation_challenge.ValidationChallenge"
    ]
    """<p>The validation challenge details for this configuration. The structure varies by validation method: for DNS validation, contains a <code>DnsValidationChallenge</code> with the CNAME record to add; for email validation, contains an <code>EmailValidationChallenge</code> with the validation email addresses.</p>"""
    validation_status: NotRequired["capo_acm.types.domain_status.DomainStatus"]
    """<p>The validation status for this domain. Valid values:</p> <ul> <li> <p> <code>PENDING_VALIDATION</code> – The domain is waiting for validation to complete.</p> </li> <li> <p> <code>SUCCESS</code> – Validation completed successfully.</p> </li> <li> <p> <code>FAILED</code> – Validation failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationConfiguration) -> dict:
    out: dict = {}
    if "validation_method" in value:
        import capo_acm.types.validation_method

        out["ValidationMethod"] = (
            capo_acm.types.validation_method.serialize_aws_json_1_1(
                value["validation_method"]
            )
        )
    if "validation_challenge" in value:
        import capo_acm.types.validation_challenge

        out["ValidationChallenge"] = (
            capo_acm.types.validation_challenge.serialize_aws_json_1_1(
                value["validation_challenge"]
            )
        )
    if "validation_status" in value:
        import capo_acm.types.domain_status

        out["ValidationStatus"] = capo_acm.types.domain_status.serialize_aws_json_1_1(
            value["validation_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationConfiguration:
    out: ValidationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ValidationMethod") is not None:
        import capo_acm.types.validation_method

        out["validation_method"] = (
            capo_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        )
    if data.get("ValidationChallenge") is not None:
        import capo_acm.types.validation_challenge

        out["validation_challenge"] = (
            capo_acm.types.validation_challenge.deserialize_aws_json_1_1(
                data["ValidationChallenge"]
            )
        )
    if data.get("ValidationStatus") is not None:
        import capo_acm.types.domain_status

        out["validation_status"] = (
            capo_acm.types.domain_status.deserialize_aws_json_1_1(
                data["ValidationStatus"]
            )
        )
    return out
