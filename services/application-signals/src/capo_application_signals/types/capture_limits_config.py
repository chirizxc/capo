"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CaptureLimitsConfig``."""

from typing_extensions import NotRequired, TypedDict


class CaptureLimitsConfig(TypedDict, closed=True):
    max_hits: NotRequired["int"]
    """<p>The maximum number of times the instrumentation point can be hit before it is automatically disabled. Defaults to 100.</p>"""
    max_string_length: NotRequired["int"]
    """<p>The maximum length of captured string values in characters. Strings longer than this are truncated. Defaults to 128.</p>"""
    max_collection_width: NotRequired["int"]
    """<p>The maximum number of items to capture from any collection to prevent large payloads. Defaults to 10.</p>"""
    max_collection_depth: NotRequired["int"]
    """<p>The maximum nesting depth to traverse inside collections. Defaults to 3.</p>"""
    max_stack_frames: NotRequired["int"]
    """<p>The maximum number of stack frames to capture in stack traces. Defaults to 2.</p>"""
    max_stack_trace_size: NotRequired["int"]
    """<p>The maximum total size, in bytes, of a captured stack trace. Defaults to 1000.</p>"""
    max_object_depth: NotRequired["int"]
    """<p>The maximum depth for nested object traversal when capturing structured data. Defaults to 3.</p>"""
    max_fields_per_object: NotRequired["int"]
    """<p>The maximum number of fields to capture for any object. Defaults to 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaptureLimitsConfig) -> dict:
    out: dict = {}
    if "max_hits" in value:
        out["MaxHits"] = value["max_hits"]
    if "max_string_length" in value:
        out["MaxStringLength"] = value["max_string_length"]
    if "max_collection_width" in value:
        out["MaxCollectionWidth"] = value["max_collection_width"]
    if "max_collection_depth" in value:
        out["MaxCollectionDepth"] = value["max_collection_depth"]
    if "max_stack_frames" in value:
        out["MaxStackFrames"] = value["max_stack_frames"]
    if "max_stack_trace_size" in value:
        out["MaxStackTraceSize"] = value["max_stack_trace_size"]
    if "max_object_depth" in value:
        out["MaxObjectDepth"] = value["max_object_depth"]
    if "max_fields_per_object" in value:
        out["MaxFieldsPerObject"] = value["max_fields_per_object"]
    return out


def deserialize_json(data: dict) -> CaptureLimitsConfig:
    out: CaptureLimitsConfig = {}  # type: ignore[typeddict-item]
    if data.get("MaxHits") is not None:
        out["max_hits"] = data["MaxHits"]
    if data.get("MaxStringLength") is not None:
        out["max_string_length"] = data["MaxStringLength"]
    if data.get("MaxCollectionWidth") is not None:
        out["max_collection_width"] = data["MaxCollectionWidth"]
    if data.get("MaxCollectionDepth") is not None:
        out["max_collection_depth"] = data["MaxCollectionDepth"]
    if data.get("MaxStackFrames") is not None:
        out["max_stack_frames"] = data["MaxStackFrames"]
    if data.get("MaxStackTraceSize") is not None:
        out["max_stack_trace_size"] = data["MaxStackTraceSize"]
    if data.get("MaxObjectDepth") is not None:
        out["max_object_depth"] = data["MaxObjectDepth"]
    if data.get("MaxFieldsPerObject") is not None:
        out["max_fields_per_object"] = data["MaxFieldsPerObject"]
    return out
