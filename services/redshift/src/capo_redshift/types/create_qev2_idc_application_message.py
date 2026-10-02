"""Generated from Smithy shape ``com.amazonaws.redshift#CreateQev2IdcApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.idc_display_name_string
    import capo_redshift.types.qev2_idc_application_name
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateQev2IdcApplicationMessage(TypedDict, closed=True):
    idc_instance_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance used to create the Amazon Redshift Query Editor (QEV2) managed application.</p>"""
    qev2_idc_application_name: NotRequired[
        "capo_redshift.types.qev2_idc_application_name.Qev2IdcApplicationName"
    ]
    """<p>The name of the Amazon Redshift Query Editor (QEV2) application in IAM Identity Center.</p>"""
    idc_display_name: NotRequired[
        "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
    ]
    """<p>The display name for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application. It appears in the console.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tags to associate with the application. Tags are key-value pairs that you can use to organize and identify your resources.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateQev2IdcApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "idc_instance_arn" in value:
        pairs.append((f"{key_prefix}IdcInstanceArn", str(value["idc_instance_arn"])))
    if "qev2_idc_application_name" in value:
        pairs.append(
            (
                f"{key_prefix}Qev2IdcApplicationName",
                str(value["qev2_idc_application_name"]),
            )
        )
    if "idc_display_name" in value:
        pairs.append((f"{key_prefix}IdcDisplayName", str(value["idc_display_name"])))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateQev2IdcApplicationMessage:
    out: CreateQev2IdcApplicationMessage = {}  # type: ignore[typeddict-item]
    child_idc_instance_arn = el.find("IdcInstanceArn")
    if child_idc_instance_arn is not None:
        out["idc_instance_arn"] = str(child_idc_instance_arn.text or "")
    child_qev2_idc_application_name = el.find("Qev2IdcApplicationName")
    if child_qev2_idc_application_name is not None:
        out["qev2_idc_application_name"] = str(
            child_qev2_idc_application_name.text or ""
        )
    child_idc_display_name = el.find("IdcDisplayName")
    if child_idc_display_name is not None:
        out["idc_display_name"] = str(child_idc_display_name.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
