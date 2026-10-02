"""Generated from Smithy shape ``com.amazonaws.securityagent#ListThreatModelJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.threat_model_job_summary_list


class ListThreatModelJobsOutput(TypedDict, closed=True):
    threat_model_job_summaries: NotRequired[
        "capo_securityagent.types.threat_model_job_summary_list.ThreatModelJobSummaryList"
    ]
    """<p>The list of threat model job summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatModelJobsOutput) -> dict:
    out: dict = {}
    if "threat_model_job_summaries" in value:
        import capo_securityagent.types.threat_model_job_summary_list

        out["threatModelJobSummaries"] = (
            capo_securityagent.types.threat_model_job_summary_list.serialize_json(
                value["threat_model_job_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThreatModelJobsOutput:
    out: ListThreatModelJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelJobSummaries") is not None:
        import capo_securityagent.types.threat_model_job_summary_list

        out["threat_model_job_summaries"] = (
            capo_securityagent.types.threat_model_job_summary_list.deserialize_json(
                data["threatModelJobSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
