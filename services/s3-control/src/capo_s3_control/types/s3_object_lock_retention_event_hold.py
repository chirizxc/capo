"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockRetentionEventHold``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3ObjectLockRetentionEventHold: TypeAlias = Literal[
    "ON",
    "OFF",
]


# --- restXml ser/de ---
def to_xml_text(value: S3ObjectLockRetentionEventHold) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockRetentionEventHold:
    return cast(S3ObjectLockRetentionEventHold, text)


def serialize_xml(
    value: S3ObjectLockRetentionEventHold, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockRetentionEventHold:
    return from_xml_text(el.text or "")
