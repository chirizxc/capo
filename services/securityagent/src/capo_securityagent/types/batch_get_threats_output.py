"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_id_list
    import capo_securityagent.types.threat_list


class BatchGetThreatsOutput(TypedDict, closed=True):
    threats: NotRequired["capo_securityagent.types.threat_list.ThreatList"]
    """<p>The list of threats that were found.</p>"""
    not_found: NotRequired["capo_securityagent.types.threat_id_list.ThreatIdList"]
    """<p>The list of threat identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatsOutput) -> dict:
    out: dict = {}
    if "threats" in value:
        import capo_securityagent.types.threat_list

        out["threats"] = capo_securityagent.types.threat_list.serialize_json(
            value["threats"]
        )
    if "not_found" in value:
        import capo_securityagent.types.threat_id_list

        out["notFound"] = capo_securityagent.types.threat_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetThreatsOutput:
    out: BatchGetThreatsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threats") is not None:
        import capo_securityagent.types.threat_list

        out["threats"] = capo_securityagent.types.threat_list.deserialize_json(
            data["threats"]
        )
    if data.get("notFound") is not None:
        import capo_securityagent.types.threat_id_list

        out["not_found"] = capo_securityagent.types.threat_id_list.deserialize_json(
            data["notFound"]
        )
    return out
