"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidationMethodUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.validation_method

DomainValidationMethodUpdateSummary = TypedDict(
    "DomainValidationMethodUpdateSummary",
    {
        "from": NotRequired["capo_acm.types.validation_method.ValidationMethod"],
        "to": NotRequired["capo_acm.types.validation_method.ValidationMethod"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationMethodUpdateSummary) -> dict:
    out: dict = {}
    if "from" in value:
        import capo_acm.types.validation_method

        out["From"] = capo_acm.types.validation_method.serialize_aws_json_1_1(
            value["from"]
        )
    if "to" in value:
        import capo_acm.types.validation_method

        out["To"] = capo_acm.types.validation_method.serialize_aws_json_1_1(value["to"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainValidationMethodUpdateSummary:
    out: DomainValidationMethodUpdateSummary = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        import capo_acm.types.validation_method

        out["from"] = capo_acm.types.validation_method.deserialize_aws_json_1_1(
            data["From"]
        )
    if data.get("To") is not None:
        import capo_acm.types.validation_method

        out["to"] = capo_acm.types.validation_method.deserialize_aws_json_1_1(
            data["To"]
        )
    return out
