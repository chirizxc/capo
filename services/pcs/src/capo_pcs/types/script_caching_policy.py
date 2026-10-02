"""Generated from Smithy shape ``com.amazonaws.pcs#ScriptCachingPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>The caching policy for a node lifecycle script. Valid values:</p> <ul> <li> <p> <code>CACHE_ONCE</code> – Downloads the script once and reuses it on subsequent boots.</p> </li> <li> <p> <code>REFRESH_ON_REBOOT</code> – Downloads the script on every boot.</p> </li> </ul>"""
ScriptCachingPolicy: TypeAlias = Literal[
    "CACHE_ONCE",
    "REFRESH_ON_REBOOT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScriptCachingPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScriptCachingPolicy:
    return cast(ScriptCachingPolicy, data)
