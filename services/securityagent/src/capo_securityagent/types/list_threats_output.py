"""Generated from Smithy shape ``com.amazonaws.securityagent#ListThreatsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.threat_summary_list


class ListThreatsOutput(TypedDict, closed=True):
    threats: NotRequired[
        "capo_securityagent.types.threat_summary_list.ThreatSummaryList"
    ]
    """<p>The list of threat summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatsOutput) -> dict:
    out: dict = {}
    if "threats" in value:
        import capo_securityagent.types.threat_summary_list

        out["threats"] = capo_securityagent.types.threat_summary_list.serialize_json(
            value["threats"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThreatsOutput:
    out: ListThreatsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threats") is not None:
        import capo_securityagent.types.threat_summary_list

        out["threats"] = capo_securityagent.types.threat_summary_list.deserialize_json(
            data["threats"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
