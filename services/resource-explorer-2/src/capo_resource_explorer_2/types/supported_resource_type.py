"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#SupportedResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.cfn_resource_type_list


class SupportedResourceType(TypedDict, closed=True):
    service: NotRequired["str"]
    """<p>The Amazon Web Services service that is associated with the resource type. This is the primary service that lets you create and interact with resources of this type.</p>"""
    resource_type: NotRequired["str"]
    """<p>The unique identifier of the resource type.</p>"""
    cfn_resource_types: NotRequired[
        "capo_resource_explorer_2.types.cfn_resource_type_list.CFNResourceTypeList"
    ]
    """<p>The CloudFormation resource type identifiers for this resource type, such as <code>AWS::EC2::Instance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedResourceType) -> dict:
    out: dict = {}
    if "service" in value:
        out["Service"] = value["service"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "cfn_resource_types" in value:
        import capo_resource_explorer_2.types.cfn_resource_type_list

        out["CFNResourceTypes"] = (
            capo_resource_explorer_2.types.cfn_resource_type_list.serialize_json(
                value["cfn_resource_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> SupportedResourceType:
    out: SupportedResourceType = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("CFNResourceTypes") is not None:
        import capo_resource_explorer_2.types.cfn_resource_type_list

        out["cfn_resource_types"] = (
            capo_resource_explorer_2.types.cfn_resource_type_list.deserialize_json(
                data["CFNResourceTypes"]
            )
        )
    return out
