"""Generated from Smithy shape ``com.amazonaws.securityagent#ListThreatModelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.threat_model_summary_list


class ListThreatModelsOutput(TypedDict, closed=True):
    threat_model_summaries: NotRequired[
        "capo_securityagent.types.threat_model_summary_list.ThreatModelSummaryList"
    ]
    """<p>The list of threat model summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatModelsOutput) -> dict:
    out: dict = {}
    if "threat_model_summaries" in value:
        import capo_securityagent.types.threat_model_summary_list

        out["threatModelSummaries"] = (
            capo_securityagent.types.threat_model_summary_list.serialize_json(
                value["threat_model_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThreatModelsOutput:
    out: ListThreatModelsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelSummaries") is not None:
        import capo_securityagent.types.threat_model_summary_list

        out["threat_model_summaries"] = (
            capo_securityagent.types.threat_model_summary_list.deserialize_json(
                data["threatModelSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
