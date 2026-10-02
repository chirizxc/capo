"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyQev2IdcApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.idc_display_name_string
    import capo_redshift.types.string


class ModifyQev2IdcApplicationMessage(TypedDict, closed=True):
    qev2_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the Amazon Redshift Query Editor (QEV2) application that integrates with IAM Identity Center.</p>"""
    idc_display_name: NotRequired[
        "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
    ]
    """<p>The display name for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application. It appears in the console.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyQev2IdcApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "qev2_idc_application_arn" in value:
        pairs.append(
            (
                f"{key_prefix}Qev2IdcApplicationArn",
                str(value["qev2_idc_application_arn"]),
            )
        )
    if "idc_display_name" in value:
        pairs.append((f"{key_prefix}IdcDisplayName", str(value["idc_display_name"])))


def deserialize_query(el: Element) -> ModifyQev2IdcApplicationMessage:
    out: ModifyQev2IdcApplicationMessage = {}  # type: ignore[typeddict-item]
    child_qev2_idc_application_arn = el.find("Qev2IdcApplicationArn")
    if child_qev2_idc_application_arn is not None:
        out["qev2_idc_application_arn"] = str(child_qev2_idc_application_arn.text or "")
    child_idc_display_name = el.find("IdcDisplayName")
    if child_idc_display_name is not None:
        out["idc_display_name"] = str(child_idc_display_name.text or "")
    return out
