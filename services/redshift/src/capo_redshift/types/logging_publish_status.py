"""Generated from Smithy shape ``com.amazonaws.redshift#LoggingPublishStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.s3_table_publish_status


class LoggingPublishStatus(TypedDict, closed=True):
    s3_tables: NotRequired[
        "capo_redshift.types.s3_table_publish_status.S3TablePublishStatus"
    ]
    """<p>The status of system table publishing to S3 Tables.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoggingPublishStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3_tables" in value:
        import capo_redshift.types.s3_table_publish_status

        capo_redshift.types.s3_table_publish_status.serialize_query(
            value["s3_tables"], pairs, f"{key_prefix}S3Tables"
        )


def deserialize_query(el: Element) -> LoggingPublishStatus:
    out: LoggingPublishStatus = {}  # type: ignore[typeddict-item]
    child_s3_tables = el.find("S3Tables")
    if child_s3_tables is not None:
        import capo_redshift.types.s3_table_publish_status

        out["s3_tables"] = (
            capo_redshift.types.s3_table_publish_status.deserialize_query(
                child_s3_tables
            )
        )
    return out
