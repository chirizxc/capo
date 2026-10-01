"""Generated from Smithy shape ``com.amazonaws.acm#CreateAcmeExternalAccountBindingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_external_account_binding


class CreateAcmeExternalAccountBindingResponse(TypedDict, closed=True):
    external_account_binding: NotRequired[
        "capo_acm.types.acme_external_account_binding.AcmeExternalAccountBinding"
    ]
    """<p>The created external account binding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcmeExternalAccountBindingResponse) -> dict:
    out: dict = {}
    if "external_account_binding" in value:
        import capo_acm.types.acme_external_account_binding

        out["ExternalAccountBinding"] = (
            capo_acm.types.acme_external_account_binding.serialize_aws_json_1_1(
                value["external_account_binding"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcmeExternalAccountBindingResponse:
    out: CreateAcmeExternalAccountBindingResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExternalAccountBinding") is not None:
        import capo_acm.types.acme_external_account_binding

        out["external_account_binding"] = (
            capo_acm.types.acme_external_account_binding.deserialize_aws_json_1_1(
                data["ExternalAccountBinding"]
            )
        )
    return out
