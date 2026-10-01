"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TrainingMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.metrics
    import capo_customer_profiles.types.recommender_version_name
    import capo_customer_profiles.types.timestamp


class TrainingMetrics(TypedDict, closed=True):
    time: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when these training metrics were recorded.</p>"""
    metrics: NotRequired["capo_customer_profiles.types.metrics.Metrics"]
    """<p>A collection of performance metrics and statistics from the training process.</p>"""
    recommender_version_name: NotRequired[
        "capo_customer_profiles.types.recommender_version_name.RecommenderVersionName"
    ]
    """<p>The name of the recommender version that produced these training metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingMetrics) -> dict:
    out: dict = {}
    if "time" in value:
        import capo_customer_profiles.types.timestamp

        out["Time"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["time"]
        )
    if "metrics" in value:
        import capo_customer_profiles.types.metrics

        out["Metrics"] = capo_customer_profiles.types.metrics.serialize_json(
            value["metrics"]
        )
    if "recommender_version_name" in value:
        out["RecommenderVersionName"] = value["recommender_version_name"]
    return out


def deserialize_json(data: dict) -> TrainingMetrics:
    out: TrainingMetrics = {}  # type: ignore[typeddict-item]
    if data.get("Time") is not None:
        import capo_customer_profiles.types.timestamp

        out["time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["Time"]
        )
    if data.get("Metrics") is not None:
        import capo_customer_profiles.types.metrics

        out["metrics"] = capo_customer_profiles.types.metrics.deserialize_json(
            data["Metrics"]
        )
    if data.get("RecommenderVersionName") is not None:
        out["recommender_version_name"] = data["RecommenderVersionName"]
    return out
