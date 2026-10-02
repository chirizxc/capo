"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeExternalAccountBindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_external_account_binding_list


class ListAcmeExternalAccountBindingsResponse(TypedDict, closed=True):
    external_account_bindings: NotRequired[
        "capo_acm.types.acme_external_account_binding_list.AcmeExternalAccountBindingList"
    ]
    """<p>The list of external account bindings.</p>"""
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeExternalAccountBindingsResponse) -> dict:
    out: dict = {}
    if "external_account_bindings" in value:
        import capo_acm.types.acme_external_account_binding_list

        out["ExternalAccountBindings"] = (
            capo_acm.types.acme_external_account_binding_list.serialize_aws_json_1_1(
                value["external_account_bindings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeExternalAccountBindingsResponse:
    out: ListAcmeExternalAccountBindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExternalAccountBindings") is not None:
        import capo_acm.types.acme_external_account_binding_list

        out["external_account_bindings"] = (
            capo_acm.types.acme_external_account_binding_list.deserialize_aws_json_1_1(
                data["ExternalAccountBindings"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
