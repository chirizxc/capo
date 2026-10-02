"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_enablement_status


class DeleteConnectorResponse(TypedDict, closed=True):
    enablement_status: NotRequired[
        "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
    ]
    """<p>The enablement status of the connector after the delete request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorResponse) -> dict:
    out: dict = {}
    if "enablement_status" in value:
        import capo_securityhub.types.cspm_enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.cspm_enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteConnectorResponse:
    out: DeleteConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.cspm_enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.cspm_enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    return out
