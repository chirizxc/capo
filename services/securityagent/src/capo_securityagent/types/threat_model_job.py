"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.document_list
    import capo_securityagent.types.error_information
    import capo_securityagent.types.integrated_repository_list
    import capo_securityagent.types.job_status
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.source_code_repository_list


class ThreatModelJob(TypedDict, closed=True):
    threat_model_job_id: NotRequired["str"]
    """<p>The unique identifier of the threat model job.</p>"""
    threat_model_id: NotRequired["str"]
    """<p>The unique identifier of the threat model associated with the job.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""
    title: NotRequired["str"]
    """<p>The title of the threat model job.</p>"""
    status: NotRequired["capo_securityagent.types.job_status.JobStatus"]
    """<p>The current status of the threat model job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job was last updated, in UTC format.</p>"""
    execution_start_time: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job execution started, in UTC format.</p>"""
    execution_end_time: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model job execution ended, in UTC format.</p>"""
    source_code: NotRequired[
        "capo_securityagent.types.source_code_repository_list.SourceCodeRepositoryList"
    ]
    """<p>The list of source code repositories used for threat modeling.</p>"""
    integrated_repositories: NotRequired[
        "capo_securityagent.types.integrated_repository_list.IntegratedRepositoryList"
    ]
    """<p>The list of integrated repositories used for threat modeling.</p>"""
    documents: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The list of documents used for threat modeling.</p>"""
    scope_docs: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The scoped documents for the agent to focus on during threat modeling.</p>"""
    error_information: NotRequired[
        "capo_securityagent.types.error_information.ErrorInformation"
    ]
    """<p>Error information if the threat model job encountered an error.</p>"""
    system_overview: NotRequired["str"]
    """<p>The system overview generated during threat modeling.</p>"""
    report_destination: NotRequired[
        "capo_securityagent.types.report_destination.ReportDestination"
    ]
    """<p>The destination for publishing scan reports to an integrated document provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJob) -> dict:
    out: dict = {}
    if "threat_model_job_id" in value:
        out["threatModelJobId"] = value["threat_model_job_id"]
    if "threat_model_id" in value:
        out["threatModelId"] = value["threat_model_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "status" in value:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "execution_start_time" in value:
        import capo_securityagent._protocol.serialize

        out["executionStartTime"] = (
            capo_securityagent._protocol.serialize.fmt_date_time(
                value["execution_start_time"]
            )
        )
    if "execution_end_time" in value:
        import capo_securityagent._protocol.serialize

        out["executionEndTime"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["execution_end_time"]
        )
    if "source_code" in value:
        import capo_securityagent.types.source_code_repository_list

        out["sourceCode"] = (
            capo_securityagent.types.source_code_repository_list.serialize_json(
                value["source_code"]
            )
        )
    if "integrated_repositories" in value:
        import capo_securityagent.types.integrated_repository_list

        out["integratedRepositories"] = (
            capo_securityagent.types.integrated_repository_list.serialize_json(
                value["integrated_repositories"]
            )
        )
    if "documents" in value:
        import capo_securityagent.types.document_list

        out["documents"] = capo_securityagent.types.document_list.serialize_json(
            value["documents"]
        )
    if "scope_docs" in value:
        import capo_securityagent.types.document_list

        out["scopeDocs"] = capo_securityagent.types.document_list.serialize_json(
            value["scope_docs"]
        )
    if "error_information" in value:
        import capo_securityagent.types.error_information

        out["errorInformation"] = (
            capo_securityagent.types.error_information.serialize_json(
                value["error_information"]
            )
        )
    if "system_overview" in value:
        out["systemOverview"] = value["system_overview"]
    if "report_destination" in value:
        import capo_securityagent.types.report_destination

        out["reportDestination"] = (
            capo_securityagent.types.report_destination.serialize_json(
                value["report_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThreatModelJob:
    out: ThreatModelJob = {}  # type: ignore[typeddict-item]
    if data.get("threatModelJobId") is not None:
        out["threat_model_job_id"] = data["threatModelJobId"]
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("status") is not None:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.deserialize_json(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("executionStartTime") is not None:
        import datetime

        out["execution_start_time"] = datetime.datetime.fromisoformat(
            data["executionStartTime"].replace("Z", "+00:00")
        )
    if data.get("executionEndTime") is not None:
        import datetime

        out["execution_end_time"] = datetime.datetime.fromisoformat(
            data["executionEndTime"].replace("Z", "+00:00")
        )
    if data.get("sourceCode") is not None:
        import capo_securityagent.types.source_code_repository_list

        out["source_code"] = (
            capo_securityagent.types.source_code_repository_list.deserialize_json(
                data["sourceCode"]
            )
        )
    if data.get("integratedRepositories") is not None:
        import capo_securityagent.types.integrated_repository_list

        out["integrated_repositories"] = (
            capo_securityagent.types.integrated_repository_list.deserialize_json(
                data["integratedRepositories"]
            )
        )
    if data.get("documents") is not None:
        import capo_securityagent.types.document_list

        out["documents"] = capo_securityagent.types.document_list.deserialize_json(
            data["documents"]
        )
    if data.get("scopeDocs") is not None:
        import capo_securityagent.types.document_list

        out["scope_docs"] = capo_securityagent.types.document_list.deserialize_json(
            data["scopeDocs"]
        )
    if data.get("errorInformation") is not None:
        import capo_securityagent.types.error_information

        out["error_information"] = (
            capo_securityagent.types.error_information.deserialize_json(
                data["errorInformation"]
            )
        )
    if data.get("systemOverview") is not None:
        out["system_overview"] = data["systemOverview"]
    if data.get("reportDestination") is not None:
        import capo_securityagent.types.report_destination

        out["report_destination"] = (
            capo_securityagent.types.report_destination.deserialize_json(
                data["reportDestination"]
            )
        )
    return out
