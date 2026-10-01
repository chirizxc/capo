"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.ai_details


class ResourceInfo(TypedDict, closed=True):
    ai_details: NotRequired["capo_securityhub.types.ai_details.AIDetails"]
    """<p>Details that are specific to self-hosted AI resources and their host resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInfo) -> dict:
    out: dict = {}
    if "ai_details" in value:
        import capo_securityhub.types.ai_details

        out["AIDetails"] = capo_securityhub.types.ai_details.serialize_json(
            value["ai_details"]
        )
    return out


def deserialize_json(data: dict) -> ResourceInfo:
    out: ResourceInfo = {}  # type: ignore[typeddict-item]
    if data.get("AIDetails") is not None:
        import capo_securityhub.types.ai_details

        out["ai_details"] = capo_securityhub.types.ai_details.deserialize_json(
            data["AIDetails"]
        )
    return out
