"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ProviderPrefix``."""

from typing_extensions import TypedDict


class ProviderPrefix(TypedDict, closed=True):
    strip: "bool"
    """<p>Whether clients can omit the provider prefix from model IDs. If <code>true</code>, the gateway accepts model IDs without the prefix and restores the full prefixed form before forwarding to the provider. The default is <code>false</code>.</p>"""
    separator: "str"
    """<p>The single character that separates the provider prefix from the model name (for example, <code>.</code>). The default is <code>.</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderPrefix) -> dict:
    out: dict = {}
    out["strip"] = value.get("strip", False)
    out["separator"] = value.get("separator", ".")
    return out


def deserialize_json(data: dict) -> ProviderPrefix:
    out: ProviderPrefix = {}  # type: ignore[typeddict-item]
    if data.get("strip") is not None:
        out["strip"] = data["strip"]
    else:
        out["strip"] = False
    if data.get("separator") is not None:
        out["separator"] = data["separator"]
    else:
        out["separator"] = "."
    return out
