"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyQev2IdcApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.qev2_idc_application


class ModifyQev2IdcApplicationResult(TypedDict, closed=True):
    qev2_idc_application: NotRequired[
        "capo_redshift.types.qev2_idc_application.Qev2IdcApplication"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyQev2IdcApplicationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "qev2_idc_application" in value:
        import capo_redshift.types.qev2_idc_application

        capo_redshift.types.qev2_idc_application.serialize_query(
            value["qev2_idc_application"], pairs, f"{key_prefix}Qev2IdcApplication"
        )


def deserialize_query(el: Element) -> ModifyQev2IdcApplicationResult:
    out: ModifyQev2IdcApplicationResult = {}  # type: ignore[typeddict-item]
    child_qev2_idc_application = el.find("Qev2IdcApplication")
    if child_qev2_idc_application is not None:
        import capo_redshift.types.qev2_idc_application

        out["qev2_idc_application"] = (
            capo_redshift.types.qev2_idc_application.deserialize_query(
                child_qev2_idc_application
            )
        )
    return out
