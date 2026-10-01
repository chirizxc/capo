"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeQev2IdcApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.qev2_idc_application_list
    import capo_redshift.types.string


class DescribeQev2IdcApplicationsResult(TypedDict, closed=True):
    qev2_idc_applications: NotRequired[
        "capo_redshift.types.qev2_idc_application_list.Qev2IdcApplicationList"
    ]
    """<p>The list of Amazon Redshift Query Editor (QEV2) IAM Identity Center applications.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeQev2IdcApplicationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "qev2_idc_applications" in value:
        import capo_redshift.types.qev2_idc_application_list

        capo_redshift.types.qev2_idc_application_list.serialize_query(
            value["qev2_idc_applications"], pairs, f"{key_prefix}Qev2IdcApplications"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeQev2IdcApplicationsResult:
    out: DescribeQev2IdcApplicationsResult = {}  # type: ignore[typeddict-item]
    child_qev2_idc_applications = el.find("Qev2IdcApplications")
    if child_qev2_idc_applications is not None:
        import capo_redshift.types.qev2_idc_application_list

        out["qev2_idc_applications"] = (
            capo_redshift.types.qev2_idc_application_list.deserialize_query(
                child_qev2_idc_applications
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
