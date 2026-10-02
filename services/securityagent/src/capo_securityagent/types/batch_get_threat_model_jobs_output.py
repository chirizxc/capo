"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job_id_list
    import capo_securityagent.types.threat_model_job_list


class BatchGetThreatModelJobsOutput(TypedDict, closed=True):
    threat_model_jobs: NotRequired[
        "capo_securityagent.types.threat_model_job_list.ThreatModelJobList"
    ]
    """<p>The list of threat model jobs that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.threat_model_job_id_list.ThreatModelJobIdList"
    ]
    """<p>The list of threat model job identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelJobsOutput) -> dict:
    out: dict = {}
    if "threat_model_jobs" in value:
        import capo_securityagent.types.threat_model_job_list

        out["threatModelJobs"] = (
            capo_securityagent.types.threat_model_job_list.serialize_json(
                value["threat_model_jobs"]
            )
        )
    if "not_found" in value:
        import capo_securityagent.types.threat_model_job_id_list

        out["notFound"] = (
            capo_securityagent.types.threat_model_job_id_list.serialize_json(
                value["not_found"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelJobsOutput:
    out: BatchGetThreatModelJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelJobs") is not None:
        import capo_securityagent.types.threat_model_job_list

        out["threat_model_jobs"] = (
            capo_securityagent.types.threat_model_job_list.deserialize_json(
                data["threatModelJobs"]
            )
        )
    if data.get("notFound") is not None:
        import capo_securityagent.types.threat_model_job_id_list

        out["not_found"] = (
            capo_securityagent.types.threat_model_job_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out
