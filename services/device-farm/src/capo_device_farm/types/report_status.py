"""Generated from Smithy shape ``com.amazonaws.devicefarm#ReportStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an insights report. Possible values are:</p> <ul> <li> <p>PENDING: The service has queued the report and generation has not started.</p> </li> <li> <p>RUNNING: The service is generating the report.</p> </li> <li> <p>COMPLETED: The service successfully generated the report.</p> </li> <li> <p>SKIPPED: The service did not generate the report because the necessary conditions were not met. For more information about why the service could not generate the report, view the <code>message</code> field in <code>TestReport</code> or <code>JobReport</code>.</p> </li> <li> <p>ERRORED: An error occurred while generating the report. For more information about why the service could not generate the report, view the <code>message</code> field in <code>TestReport</code> or <code>JobReport</code>.</p> </li> </ul>"""
ReportStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "COMPLETED",
    "SKIPPED",
    "ERRORED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatus:
    return cast(ReportStatus, data)
