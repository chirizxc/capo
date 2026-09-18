"""Generated from Smithy shape ``com.amazonaws.rekognition#Label``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.instances
    import capo_rekognition.types.label_aliases
    import capo_rekognition.types.label_categories
    import capo_rekognition.types.parents
    import capo_rekognition.types.percent
    import capo_rekognition.types.string


class Label(TypedDict, closed=True):
    name: NotRequired["capo_rekognition.types.string.String"]
    """<p>The name (label) of the object or scene.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence.</p>"""
    instances: NotRequired["capo_rekognition.types.instances.Instances"]
    """<p>If <code>Label</code> represents an object, <code>Instances</code> contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.</p>"""
    parents: NotRequired["capo_rekognition.types.parents.Parents"]
    """<p>The parent labels for a label. The response includes all ancestor labels.</p>"""
    aliases: NotRequired["capo_rekognition.types.label_aliases.LabelAliases"]
    """<p>A list of potential aliases for a given label.</p>"""
    categories: NotRequired["capo_rekognition.types.label_categories.LabelCategories"]
    """<p>A list of the categories associated with a given label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Label) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "instances" in value:
        import capo_rekognition.types.instances

        out["Instances"] = capo_rekognition.types.instances.serialize_aws_json_1_1(
            value["instances"]
        )
    if "parents" in value:
        import capo_rekognition.types.parents

        out["Parents"] = capo_rekognition.types.parents.serialize_aws_json_1_1(
            value["parents"]
        )
    if "aliases" in value:
        import capo_rekognition.types.label_aliases

        out["Aliases"] = capo_rekognition.types.label_aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "categories" in value:
        import capo_rekognition.types.label_categories

        out["Categories"] = (
            capo_rekognition.types.label_categories.serialize_aws_json_1_1(
                value["categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Label:
    out: Label = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Instances") is not None:
        import capo_rekognition.types.instances

        out["instances"] = capo_rekognition.types.instances.deserialize_aws_json_1_1(
            data["Instances"]
        )
    if data.get("Parents") is not None:
        import capo_rekognition.types.parents

        out["parents"] = capo_rekognition.types.parents.deserialize_aws_json_1_1(
            data["Parents"]
        )
    if data.get("Aliases") is not None:
        import capo_rekognition.types.label_aliases

        out["aliases"] = capo_rekognition.types.label_aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if data.get("Categories") is not None:
        import capo_rekognition.types.label_categories

        out["categories"] = (
            capo_rekognition.types.label_categories.deserialize_aws_json_1_1(
                data["Categories"]
            )
        )
    return out
