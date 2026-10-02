"""Generated from Smithy shape ``com.amazonaws.billing#GetCreditsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.credit_data_list


class GetCreditsResponse(TypedDict, closed=True):
    credits: NotRequired["capo_billing.types.credit_data_list.CreditDataList"]
    """<p>The list of credits matching the request. Returns an empty list when no credits exist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCreditsResponse) -> dict:
    out: dict = {}
    if "credits" in value:
        import capo_billing.types.credit_data_list

        out["credits"] = capo_billing.types.credit_data_list.serialize_aws_json_1_0(
            value["credits"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCreditsResponse:
    out: GetCreditsResponse = {}  # type: ignore[typeddict-item]
    if data.get("credits") is not None:
        import capo_billing.types.credit_data_list

        out["credits"] = capo_billing.types.credit_data_list.deserialize_aws_json_1_0(
            data["credits"]
        )
    return out
