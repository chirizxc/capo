"""Generated from Smithy shape ``com.amazonaws.xray#SamplingRuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.attribute_map
    import capo_xray.types.host
    import capo_xray.types.http_method
    import capo_xray.types.nullable_double
    import capo_xray.types.nullable_integer
    import capo_xray.types.resource_arn
    import capo_xray.types.rule_name
    import capo_xray.types.sampling_rate_boost
    import capo_xray.types.service_name
    import capo_xray.types.service_type
    import capo_xray.types.string
    import capo_xray.types.url_path


class SamplingRuleUpdate(TypedDict, closed=True):
    rule_name: NotRequired["capo_xray.types.rule_name.RuleName"]
    """<p>The name of the sampling rule. Specify a rule by either name or ARN, but not both.</p>"""
    rule_arn: NotRequired["capo_xray.types.string.String"]
    """<p>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</p>"""
    resource_arn: NotRequired["capo_xray.types.resource_arn.ResourceARN"]
    """<p>Matches the ARN of the Amazon Web Services resource on which the service runs.</p>"""
    priority: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>The priority of the sampling rule.</p>"""
    fixed_rate: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The percentage of matching requests to instrument, after the reservoir is exhausted.</p>"""
    reservoir_size: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</p>"""
    host: NotRequired["capo_xray.types.host.Host"]
    """<p>Matches the hostname from a request URL.</p>"""
    service_name: NotRequired["capo_xray.types.service_name.ServiceName"]
    """<p>Matches the <code>name</code> that the service uses to identify itself in segments.</p>"""
    service_type: NotRequired["capo_xray.types.service_type.ServiceType"]
    """<p>Matches the <code>origin</code> that the service uses to identify its type in segments.</p>"""
    http_method: NotRequired["capo_xray.types.http_method.HTTPMethod"]
    """<p>Matches the HTTP method of a request.</p>"""
    url_path: NotRequired["capo_xray.types.url_path.URLPath"]
    """<p>Matches the path from a request URL.</p>"""
    attributes: NotRequired["capo_xray.types.attribute_map.AttributeMap"]
    """<p>Matches attributes derived from the request.</p>"""
    sampling_rate_boost: NotRequired[
        "capo_xray.types.sampling_rate_boost.SamplingRateBoost"
    ]
    """<p>Specifies the multiplier applied to the base sampling rate. This boost allows you to temporarily increase sampling without changing the rule's configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingRuleUpdate) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleARN"] = value["rule_arn"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "fixed_rate" in value:
        out["FixedRate"] = (
            "NaN"
            if value["fixed_rate"] != value["fixed_rate"]
            else "Infinity"
            if value["fixed_rate"] == float("inf")
            else "-Infinity"
            if value["fixed_rate"] == float("-inf")
            else value["fixed_rate"]
        )
    if "reservoir_size" in value:
        out["ReservoirSize"] = value["reservoir_size"]
    if "host" in value:
        out["Host"] = value["host"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "service_type" in value:
        out["ServiceType"] = value["service_type"]
    if "http_method" in value:
        out["HTTPMethod"] = value["http_method"]
    if "url_path" in value:
        out["URLPath"] = value["url_path"]
    if "attributes" in value:
        import capo_xray.types.attribute_map

        out["Attributes"] = capo_xray.types.attribute_map.serialize_json(
            value["attributes"]
        )
    if "sampling_rate_boost" in value:
        import capo_xray.types.sampling_rate_boost

        out["SamplingRateBoost"] = capo_xray.types.sampling_rate_boost.serialize_json(
            value["sampling_rate_boost"]
        )
    return out


def deserialize_json(data: dict) -> SamplingRuleUpdate:
    out: SamplingRuleUpdate = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("RuleARN") is not None:
        out["rule_arn"] = data["RuleARN"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("FixedRate") is not None:
        out["fixed_rate"] = float(data["FixedRate"])
    if data.get("ReservoirSize") is not None:
        out["reservoir_size"] = data["ReservoirSize"]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    if data.get("ServiceType") is not None:
        out["service_type"] = data["ServiceType"]
    if data.get("HTTPMethod") is not None:
        out["http_method"] = data["HTTPMethod"]
    if data.get("URLPath") is not None:
        out["url_path"] = data["URLPath"]
    if data.get("Attributes") is not None:
        import capo_xray.types.attribute_map

        out["attributes"] = capo_xray.types.attribute_map.deserialize_json(
            data["Attributes"]
        )
    if data.get("SamplingRateBoost") is not None:
        import capo_xray.types.sampling_rate_boost

        out["sampling_rate_boost"] = (
            capo_xray.types.sampling_rate_boost.deserialize_json(
                data["SamplingRateBoost"]
            )
        )
    return out
