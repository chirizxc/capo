"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteConnectorV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.enablement_status


class DeleteConnectorV2Response(TypedDict, closed=True):
    enablement_status: NotRequired[
        "capo_securityhub.types.enablement_status.EnablementStatus"
    ]
    """<p>The enablement status of the connector after deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorV2Response) -> dict:
    out: dict = {}
    if "enablement_status" in value:
        import capo_securityhub.types.enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteConnectorV2Response:
    out: DeleteConnectorV2Response = {}  # type: ignore[typeddict-item]
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    return out
