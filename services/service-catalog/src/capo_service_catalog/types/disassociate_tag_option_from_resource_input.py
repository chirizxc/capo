"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateTagOptionFromResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.resource_id
    import capo_service_catalog.types.tag_option_id


class DisassociateTagOptionFromResourceInput(TypedDict, closed=True):
    resource_id: "capo_service_catalog.types.resource_id.ResourceId"
    """<p>The resource identifier.</p>"""
    tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateTagOptionFromResourceInput) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["TagOptionId"] = value["tag_option_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateTagOptionFromResourceInput:
    out: DisassociateTagOptionFromResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "DisassociateTagOptionFromResourceInput.resource_id required"
        )
    if data.get("TagOptionId") is not None:
        out["tag_option_id"] = data["TagOptionId"]
    else:
        raise DeserializationError(
            "DisassociateTagOptionFromResourceInput.tag_option_id required"
        )
    return out
