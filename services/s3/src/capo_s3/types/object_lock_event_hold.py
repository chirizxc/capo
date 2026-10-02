"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockEventHold``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ObjectLockEventHold: TypeAlias = Literal[
    "ON",
    "OFF",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLockEventHold) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockEventHold:
    return cast(ObjectLockEventHold, text)


def serialize_xml(value: ObjectLockEventHold, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockEventHold:
    return from_xml_text(el.text or "")
