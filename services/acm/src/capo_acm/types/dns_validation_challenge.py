"""Generated from Smithy shape ``com.amazonaws.acm#DnsValidationChallenge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.resource_record


class DnsValidationChallenge(TypedDict, closed=True):
    resource_record: NotRequired["capo_acm.types.resource_record.ResourceRecord"]
    """<p>The CNAME record that ACM creates for DNS validation. Add this record to your DNS configuration to prove that you own or control the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsValidationChallenge) -> dict:
    out: dict = {}
    if "resource_record" in value:
        import capo_acm.types.resource_record

        out["ResourceRecord"] = capo_acm.types.resource_record.serialize_aws_json_1_1(
            value["resource_record"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsValidationChallenge:
    out: DnsValidationChallenge = {}  # type: ignore[typeddict-item]
    if data.get("ResourceRecord") is not None:
        import capo_acm.types.resource_record

        out["resource_record"] = (
            capo_acm.types.resource_record.deserialize_aws_json_1_1(
                data["ResourceRecord"]
            )
        )
    return out
