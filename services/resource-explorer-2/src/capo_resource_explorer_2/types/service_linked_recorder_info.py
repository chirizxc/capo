"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ServiceLinkedRecorderInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.recorder_type


class ServiceLinkedRecorderInfo(TypedDict, closed=True):
    service_principal: NotRequired["str"]
    """<p>The service principal of the Amazon Web Services service that owns the service-linked recorder, such as <code>observabilityadmin.amazonaws.com</code>.</p>"""
    recorder_name: NotRequired["str"]
    """<p>The name of the service-linked recorder, such as <code>AWSConfigurationRecorderForObservabilityAdmin</code>.</p>"""
    recorder_type: NotRequired[
        "capo_resource_explorer_2.types.recorder_type.RecorderType"
    ]
    """<p>The type of the recorder. Valid values are <code>AWS</code> and <code>THIRD_PARTY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLinkedRecorderInfo) -> dict:
    out: dict = {}
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "recorder_name" in value:
        out["RecorderName"] = value["recorder_name"]
    if "recorder_type" in value:
        out["RecorderType"] = value["recorder_type"]
    return out


def deserialize_json(data: dict) -> ServiceLinkedRecorderInfo:
    out: ServiceLinkedRecorderInfo = {}  # type: ignore[typeddict-item]
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    if data.get("RecorderName") is not None:
        out["recorder_name"] = data["RecorderName"]
    if data.get("RecorderType") is not None:
        out["recorder_type"] = data["RecorderType"]
    return out
