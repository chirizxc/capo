"""Generated from Smithy shape ``com.amazonaws.outposts#CreatePrivateConnectivityConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.outpost_id
    import capo_outposts.types.private_connectivity_config


class CreatePrivateConnectivityConfigOutput(TypedDict, closed=True):
    private_connectivity_config: NotRequired[
        "capo_outposts.types.private_connectivity_config.PrivateConnectivityConfig"
    ]
    """<p>The private connectivity configuration for the Outpost.</p>"""
    outpost_id: NotRequired["capo_outposts.types.outpost_id.OutpostId"]
    """<p>The ID of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateConnectivityConfigOutput) -> dict:
    out: dict = {}
    if "private_connectivity_config" in value:
        import capo_outposts.types.private_connectivity_config

        out["PrivateConnectivityConfig"] = (
            capo_outposts.types.private_connectivity_config.serialize_json(
                value["private_connectivity_config"]
            )
        )
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    return out


def deserialize_json(data: dict) -> CreatePrivateConnectivityConfigOutput:
    out: CreatePrivateConnectivityConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("PrivateConnectivityConfig") is not None:
        import capo_outposts.types.private_connectivity_config

        out["private_connectivity_config"] = (
            capo_outposts.types.private_connectivity_config.deserialize_json(
                data["PrivateConnectivityConfig"]
            )
        )
    if data.get("OutpostId") is not None:
        out["outpost_id"] = data["OutpostId"]
    return out
