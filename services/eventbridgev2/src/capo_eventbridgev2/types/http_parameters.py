"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#HttpParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.header_parameters_map
    import capo_eventbridgev2.types.path_parameter_list
    import capo_eventbridgev2.types.query_string_parameters_map
    import capo_eventbridgev2.types.string


class HttpParameters(TypedDict, closed=True):
    path_parameter_values: NotRequired[
        "capo_eventbridgev2.types.path_parameter_list.PathParameterList"
    ]
    header_parameters: NotRequired[
        "capo_eventbridgev2.types.header_parameters_map.HeaderParametersMap"
    ]
    query_string_parameters: NotRequired[
        "capo_eventbridgev2.types.query_string_parameters_map.QueryStringParametersMap"
    ]
    invocation_timeout_seconds: NotRequired["capo_eventbridgev2.types.string.String"]
    """Timeout in seconds for each invocation of the target (1-30). String-typed (not integer) so the value may be a JSONata expression."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpParameters) -> dict:
    out: dict = {}
    if "path_parameter_values" in value:
        import capo_eventbridgev2.types.path_parameter_list

        out["PathParameterValues"] = (
            capo_eventbridgev2.types.path_parameter_list.serialize_cbor(
                value["path_parameter_values"]
            )
        )
    if "header_parameters" in value:
        import capo_eventbridgev2.types.header_parameters_map

        out["HeaderParameters"] = (
            capo_eventbridgev2.types.header_parameters_map.serialize_cbor(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import capo_eventbridgev2.types.query_string_parameters_map

        out["QueryStringParameters"] = (
            capo_eventbridgev2.types.query_string_parameters_map.serialize_cbor(
                value["query_string_parameters"]
            )
        )
    if "invocation_timeout_seconds" in value:
        out["InvocationTimeoutSeconds"] = value["invocation_timeout_seconds"]
    return out


def deserialize_cbor(data: dict) -> HttpParameters:
    out: HttpParameters = {}  # type: ignore[typeddict-item]
    if data.get("PathParameterValues") is not None:
        import capo_eventbridgev2.types.path_parameter_list

        out["path_parameter_values"] = (
            capo_eventbridgev2.types.path_parameter_list.deserialize_cbor(
                data["PathParameterValues"]
            )
        )
    if data.get("HeaderParameters") is not None:
        import capo_eventbridgev2.types.header_parameters_map

        out["header_parameters"] = (
            capo_eventbridgev2.types.header_parameters_map.deserialize_cbor(
                data["HeaderParameters"]
            )
        )
    if data.get("QueryStringParameters") is not None:
        import capo_eventbridgev2.types.query_string_parameters_map

        out["query_string_parameters"] = (
            capo_eventbridgev2.types.query_string_parameters_map.deserialize_cbor(
                data["QueryStringParameters"]
            )
        )
    if data.get("InvocationTimeoutSeconds") is not None:
        out["invocation_timeout_seconds"] = data["InvocationTimeoutSeconds"]
    return out
