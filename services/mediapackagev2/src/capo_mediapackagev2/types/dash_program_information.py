"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashProgramInformation``."""

from typing_extensions import NotRequired, TypedDict


class DashProgramInformation(TypedDict, closed=True):
    title: NotRequired["str"]
    """<p>The title for the manifest.</p>"""
    source: NotRequired["str"]
    """<p>Information about the content provider.</p>"""
    copyright: NotRequired["str"]
    """<p>A copyright statement about the content.</p>"""
    language_code: NotRequired["str"]
    """<p>The language code for this manifest.</p>"""
    more_information_url: NotRequired["str"]
    """<p>An absolute URL that contains more information about this content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashProgramInformation) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "source" in value:
        out["Source"] = value["source"]
    if "copyright" in value:
        out["Copyright"] = value["copyright"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "more_information_url" in value:
        out["MoreInformationUrl"] = value["more_information_url"]
    return out


def deserialize_json(data: dict) -> DashProgramInformation:
    out: DashProgramInformation = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("Copyright") is not None:
        out["copyright"] = data["Copyright"]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("MoreInformationUrl") is not None:
        out["more_information_url"] = data["MoreInformationUrl"]
    return out
