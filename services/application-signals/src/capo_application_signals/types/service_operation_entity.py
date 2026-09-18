"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceOperationEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.service_entity


class ServiceOperationEntity(TypedDict, closed=True):
    service: NotRequired["capo_application_signals.types.service_entity.ServiceEntity"]
    """<p>The service entity that contains this operation.</p>"""
    operation: NotRequired["str"]
    """<p>The name of the operation.</p>"""
    metric_type: NotRequired["str"]
    """<p>The type of metric associated with this service operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOperationEntity) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_application_signals.types.service_entity

        out["Service"] = capo_application_signals.types.service_entity.serialize_json(
            value["service"]
        )
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "metric_type" in value:
        out["MetricType"] = value["metric_type"]
    return out


def deserialize_json(data: dict) -> ServiceOperationEntity:
    out: ServiceOperationEntity = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_application_signals.types.service_entity

        out["service"] = capo_application_signals.types.service_entity.deserialize_json(
            data["Service"]
        )
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("MetricType") is not None:
        out["metric_type"] = data["MetricType"]
    return out
