"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockEventHold``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3ObjectLockEventHold: TypeAlias = Literal[
    "ON",
    "OFF",
]


# --- restXml ser/de ---
def to_xml_text(value: S3ObjectLockEventHold) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockEventHold:
    return cast(S3ObjectLockEventHold, text)


def serialize_xml(value: S3ObjectLockEventHold, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockEventHold:
    return from_xml_text(el.text or "")
