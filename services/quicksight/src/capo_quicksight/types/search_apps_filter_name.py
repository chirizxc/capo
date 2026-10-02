"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAppsFilterName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of a field that you can use to filter app search results. Valid values are:</p> <ul> <li> <p> <code>APP_ID</code> – The unique identifier of the app.</p> </li> <li> <p> <code>APP_NAME</code> – The display name of the app.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code> – An Amazon QuickSight user or group that is the sole direct owner.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_OWNER</code> – An Amazon QuickSight user or group with direct owner permissions.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_VIEWER_OR_OWNER</code> – An Amazon QuickSight user or group with direct viewer or owner permissions.</p> </li> </ul>"""
SearchAppsFilterName: TypeAlias = Literal[
    "APP_ID",
    "APP_NAME",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAppsFilterName) -> str:
    return value


def deserialize_json(data: str) -> SearchAppsFilterName:
    return cast(SearchAppsFilterName, data)
