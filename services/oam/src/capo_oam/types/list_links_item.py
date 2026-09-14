"""Generated from Smithy shape ``com.amazonaws.oam#ListLinksItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.resource_types_output


class ListLinksItem(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The ARN of the link.</p>"""
    id: NotRequired["str"]
    """<p>The random ID string that Amazon Web Services generated as part of the link ARN.</p>"""
    label: NotRequired["str"]
    """<p>The label that was assigned to this link at creation, with the variables resolved to their actual values.</p>"""
    resource_types: NotRequired[
        "capo_oam.types.resource_types_output.ResourceTypesOutput"
    ]
    """<p>The resource types supported by this link.</p>"""
    sink_arn: NotRequired["str"]
    """<p>The ARN of the sink that this link is attached to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinksItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "resource_types" in value:
        import capo_oam.types.resource_types_output

        out["ResourceTypes"] = capo_oam.types.resource_types_output.serialize_json(
            value["resource_types"]
        )
    if "sink_arn" in value:
        out["SinkArn"] = value["sink_arn"]
    return out


def deserialize_json(data: dict) -> ListLinksItem:
    out: ListLinksItem = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("ResourceTypes") is not None:
        import capo_oam.types.resource_types_output

        out["resource_types"] = capo_oam.types.resource_types_output.deserialize_json(
            data["ResourceTypes"]
        )
    if data.get("SinkArn") is not None:
        out["sink_arn"] = data["SinkArn"]
    return out
