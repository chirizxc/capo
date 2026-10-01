"""Generated from Smithy shape ``com.amazonaws.redshift#Qev2IdcApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.qev2_idc_application

Qev2IdcApplicationList: TypeAlias = list[
    "capo_redshift.types.qev2_idc_application.Qev2IdcApplication"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: Qev2IdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.qev2_idc_application

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_redshift.types.qev2_idc_application.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Qev2IdcApplicationList:
    import capo_redshift.types.qev2_idc_application

    out: Qev2IdcApplicationList = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.qev2_idc_application.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Qev2IdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.qev2_idc_application

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_redshift.types.qev2_idc_application.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Qev2IdcApplicationList:
    import capo_redshift.types.qev2_idc_application

    out: Qev2IdcApplicationList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.qev2_idc_application.deserialize_query(child))
    return out
