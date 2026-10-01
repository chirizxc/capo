"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteQev2IdcApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteQev2IdcApplicationMessage(TypedDict, closed=True):
    qev2_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteQev2IdcApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "qev2_idc_application_arn" in value:
        pairs.append(
            (
                f"{key_prefix}Qev2IdcApplicationArn",
                str(value["qev2_idc_application_arn"]),
            )
        )


def deserialize_query(el: Element) -> DeleteQev2IdcApplicationMessage:
    out: DeleteQev2IdcApplicationMessage = {}  # type: ignore[typeddict-item]
    child_qev2_idc_application_arn = el.find("Qev2IdcApplicationArn")
    if child_qev2_idc_application_arn is not None:
        out["qev2_idc_application_arn"] = str(child_qev2_idc_application_arn.text or "")
    return out
