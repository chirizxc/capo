"""Generated from Smithy shape ``com.amazonaws.xray#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.edge_list
    import capo_xray.types.histogram
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_integer
    import capo_xray.types.service_names
    import capo_xray.types.service_statistics
    import capo_xray.types.string
    import capo_xray.types.timestamp


class Service(TypedDict, closed=True):
    reference_id: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>Identifier for the service. Unique within the service map.</p>"""
    name: NotRequired["capo_xray.types.string.String"]
    """<p>The canonical name of the service.</p>"""
    names: NotRequired["capo_xray.types.service_names.ServiceNames"]
    """<p>A list of names for the service, including the canonical name.</p>"""
    root: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates that the service was the first service to process a request.</p>"""
    account_id: NotRequired["capo_xray.types.string.String"]
    """<p>Identifier of the Amazon Web Services account in which the service runs.</p>"""
    type: NotRequired["capo_xray.types.string.String"]
    """<p>The type of service.</p> <ul> <li> <p>Amazon Web Services Resource - The type of an Amazon Web Services resource. For example, <code>AWS::EC2::Instance</code> for an application running on Amazon EC2 or <code>AWS::DynamoDB::Table</code> for an Amazon DynamoDB table that the application used.</p> </li> <li> <p>Amazon Web Services Service - The type of an Amazon Web Services service. For example, <code>AWS::DynamoDB</code> for downstream calls to Amazon DynamoDB that didn't target a specific table.</p> </li> <li> <p> <code>client</code> - Represents the clients that sent requests to a root service.</p> </li> <li> <p> <code>remote</code> - A downstream service of indeterminate type.</p> </li> </ul>"""
    state: NotRequired["capo_xray.types.string.String"]
    """<p>The service's state.</p>"""
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The start time of the first segment that the service generated.</p>"""
    end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The end time of the last segment that the service generated.</p>"""
    edges: NotRequired["capo_xray.types.edge_list.EdgeList"]
    """<p>Connections to downstream services.</p>"""
    summary_statistics: NotRequired[
        "capo_xray.types.service_statistics.ServiceStatistics"
    ]
    """<p>Aggregated statistics for the service.</p>"""
    duration_histogram: NotRequired["capo_xray.types.histogram.Histogram"]
    """<p>A histogram that maps the spread of service durations.</p>"""
    response_time_histogram: NotRequired["capo_xray.types.histogram.Histogram"]
    """<p>A histogram that maps the spread of service response times.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> dict:
    out: dict = {}
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import capo_xray.types.service_names

        out["Names"] = capo_xray.types.service_names.serialize_json(value["names"])
    if "root" in value:
        out["Root"] = value["root"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        out["State"] = value["state"]
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_xray.types.timestamp

        out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "edges" in value:
        import capo_xray.types.edge_list

        out["Edges"] = capo_xray.types.edge_list.serialize_json(value["edges"])
    if "summary_statistics" in value:
        import capo_xray.types.service_statistics

        out["SummaryStatistics"] = capo_xray.types.service_statistics.serialize_json(
            value["summary_statistics"]
        )
    if "duration_histogram" in value:
        import capo_xray.types.histogram

        out["DurationHistogram"] = capo_xray.types.histogram.serialize_json(
            value["duration_histogram"]
        )
    if "response_time_histogram" in value:
        import capo_xray.types.histogram

        out["ResponseTimeHistogram"] = capo_xray.types.histogram.serialize_json(
            value["response_time_histogram"]
        )
    return out


def deserialize_json(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Names") is not None:
        import capo_xray.types.service_names

        out["names"] = capo_xray.types.service_names.deserialize_json(data["Names"])
    if data.get("Root") is not None:
        out["root"] = data["Root"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("StartTime") is not None:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    if data.get("Edges") is not None:
        import capo_xray.types.edge_list

        out["edges"] = capo_xray.types.edge_list.deserialize_json(data["Edges"])
    if data.get("SummaryStatistics") is not None:
        import capo_xray.types.service_statistics

        out["summary_statistics"] = capo_xray.types.service_statistics.deserialize_json(
            data["SummaryStatistics"]
        )
    if data.get("DurationHistogram") is not None:
        import capo_xray.types.histogram

        out["duration_histogram"] = capo_xray.types.histogram.deserialize_json(
            data["DurationHistogram"]
        )
    if data.get("ResponseTimeHistogram") is not None:
        import capo_xray.types.histogram

        out["response_time_histogram"] = capo_xray.types.histogram.deserialize_json(
            data["ResponseTimeHistogram"]
        )
    return out
