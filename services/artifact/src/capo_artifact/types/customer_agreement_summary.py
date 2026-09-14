"""Generated from Smithy shape ``com.amazonaws.artifact#CustomerAgreementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.agreement_terms
    import capo_artifact.types.agreement_type
    import capo_artifact.types.customer_agreement_id_attribute
    import capo_artifact.types.customer_agreement_state
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.short_string_attribute
    import capo_artifact.types.timestamp_attribute


class CustomerAgreementSummary(TypedDict, closed=True):
    name: NotRequired["capo_artifact.types.long_string_attribute.LongStringAttribute"]
    """<p>Name of the customer-agreement resource.</p>"""
    arn: NotRequired["capo_artifact.types.long_string_attribute.LongStringAttribute"]
    """<p>ARN of the customer-agreement resource.</p>"""
    id: NotRequired[
        "capo_artifact.types.customer_agreement_id_attribute.CustomerAgreementIdAttribute"
    ]
    """<p>Identifier of the customer-agreement resource.</p>"""
    agreement_arn: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>ARN of the agreement resource the customer-agreement resource represents.</p>"""
    aws_account_id: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>AWS account Id that owns the resource.</p>"""
    organization_arn: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>ARN of the organization that owns the resource.</p>"""
    effective_start: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the agreement became effective.</p>"""
    effective_end: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the agreement was terminated.</p>"""
    state: NotRequired[
        "capo_artifact.types.customer_agreement_state.CustomerAgreementState"
    ]
    """<p>State of the resource.</p>"""
    description: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Description of the resource.</p>"""
    acceptance_terms: NotRequired["capo_artifact.types.agreement_terms.AgreementTerms"]
    """<p>Terms required to accept the agreement resource.</p>"""
    terminate_terms: NotRequired["capo_artifact.types.agreement_terms.AgreementTerms"]
    """<p>Terms required to terminate the customer-agreement resource.</p>"""
    type: NotRequired["capo_artifact.types.agreement_type.AgreementType"]
    """<p>Type of the customer-agreement resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerAgreementSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "agreement_arn" in value:
        out["agreementArn"] = value["agreement_arn"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "organization_arn" in value:
        out["organizationArn"] = value["organization_arn"]
    if "effective_start" in value:
        import capo_artifact.types.timestamp_attribute

        out["effectiveStart"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["effective_start"]
        )
    if "effective_end" in value:
        import capo_artifact.types.timestamp_attribute

        out["effectiveEnd"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["effective_end"]
        )
    if "state" in value:
        import capo_artifact.types.customer_agreement_state

        out["state"] = capo_artifact.types.customer_agreement_state.serialize_json(
            value["state"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "acceptance_terms" in value:
        import capo_artifact.types.agreement_terms

        out["acceptanceTerms"] = capo_artifact.types.agreement_terms.serialize_json(
            value["acceptance_terms"]
        )
    if "terminate_terms" in value:
        import capo_artifact.types.agreement_terms

        out["terminateTerms"] = capo_artifact.types.agreement_terms.serialize_json(
            value["terminate_terms"]
        )
    if "type" in value:
        import capo_artifact.types.agreement_type

        out["type"] = capo_artifact.types.agreement_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> CustomerAgreementSummary:
    out: CustomerAgreementSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("agreementArn") is not None:
        out["agreement_arn"] = data["agreementArn"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("organizationArn") is not None:
        out["organization_arn"] = data["organizationArn"]
    if data.get("effectiveStart") is not None:
        import capo_artifact.types.timestamp_attribute

        out["effective_start"] = (
            capo_artifact.types.timestamp_attribute.deserialize_json(
                data["effectiveStart"]
            )
        )
    if data.get("effectiveEnd") is not None:
        import capo_artifact.types.timestamp_attribute

        out["effective_end"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["effectiveEnd"]
        )
    if data.get("state") is not None:
        import capo_artifact.types.customer_agreement_state

        out["state"] = capo_artifact.types.customer_agreement_state.deserialize_json(
            data["state"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("acceptanceTerms") is not None:
        import capo_artifact.types.agreement_terms

        out["acceptance_terms"] = capo_artifact.types.agreement_terms.deserialize_json(
            data["acceptanceTerms"]
        )
    if data.get("terminateTerms") is not None:
        import capo_artifact.types.agreement_terms

        out["terminate_terms"] = capo_artifact.types.agreement_terms.deserialize_json(
            data["terminateTerms"]
        )
    if data.get("type") is not None:
        import capo_artifact.types.agreement_type

        out["type"] = capo_artifact.types.agreement_type.deserialize_json(data["type"])
    return out
