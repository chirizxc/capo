"""Generated from Smithy shape ``com.amazonaws.batch#InstanceRequirementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string_list


class InstanceRequirementsRequest(TypedDict, closed=True):
    allowed_instance_types: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>A list of specific instance types or instance families that Amazon ECS can launch (for example, <code>m5.large</code> or <code>g5</code>). When specified, only these instance types are used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceRequirementsRequest) -> dict:
    out: dict = {}
    if "allowed_instance_types" in value:
        import capo_batch.types.string_list

        out["allowedInstanceTypes"] = capo_batch.types.string_list.serialize_json(
            value["allowed_instance_types"]
        )
    return out


def deserialize_json(data: dict) -> InstanceRequirementsRequest:
    out: InstanceRequirementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("allowedInstanceTypes") is not None:
        import capo_batch.types.string_list

        out["allowed_instance_types"] = capo_batch.types.string_list.deserialize_json(
            data["allowedInstanceTypes"]
        )
    return out
