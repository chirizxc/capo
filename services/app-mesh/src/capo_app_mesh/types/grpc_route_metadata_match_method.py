"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRouteMetadataMatchMethod``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.header_match
    import capo_app_mesh.types.match_range


class _GrpcRouteMetadataMatchMethod_exact(TypedDict, closed=True):
    exact: "capo_app_mesh.types.header_match.HeaderMatch"


class _GrpcRouteMetadataMatchMethod_regex(TypedDict, closed=True):
    regex: "capo_app_mesh.types.header_match.HeaderMatch"


class _GrpcRouteMetadataMatchMethod_range(TypedDict, closed=True):
    range: "capo_app_mesh.types.match_range.MatchRange"


class _GrpcRouteMetadataMatchMethod_prefix(TypedDict, closed=True):
    prefix: "capo_app_mesh.types.header_match.HeaderMatch"


class _GrpcRouteMetadataMatchMethod_suffix(TypedDict, closed=True):
    suffix: "capo_app_mesh.types.header_match.HeaderMatch"


GrpcRouteMetadataMatchMethod: TypeAlias = (
    _GrpcRouteMetadataMatchMethod_exact
    | _GrpcRouteMetadataMatchMethod_regex
    | _GrpcRouteMetadataMatchMethod_range
    | _GrpcRouteMetadataMatchMethod_prefix
    | _GrpcRouteMetadataMatchMethod_suffix
)


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRouteMetadataMatchMethod) -> dict:
    if "exact" in value:
        return {"exact": value["exact"]}
    elif "regex" in value:
        return {"regex": value["regex"]}
    elif "range" in value:
        import capo_app_mesh.types.match_range

        return {"range": capo_app_mesh.types.match_range.serialize_json(value["range"])}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    elif "suffix" in value:
        return {"suffix": value["suffix"]}
    else:
        raise SerializationError("GrpcRouteMetadataMatchMethod: no variant present")


def deserialize_json(data: dict) -> GrpcRouteMetadataMatchMethod:
    if data.get("exact") is not None:
        return {"exact": data["exact"]}
    elif data.get("regex") is not None:
        return {"regex": data["regex"]}
    elif data.get("range") is not None:
        import capo_app_mesh.types.match_range

        return {
            "range": capo_app_mesh.types.match_range.deserialize_json(data["range"])
        }
    elif data.get("prefix") is not None:
        return {"prefix": data["prefix"]}
    elif data.get("suffix") is not None:
        return {"suffix": data["suffix"]}
    else:
        raise DeserializationError(
            "GrpcRouteMetadataMatchMethod: no recognized variant key"
        )
