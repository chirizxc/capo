"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details
    import capo_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails(
    TypedDict, closed=True
):
    prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Prefix text for matching objects.</p>"""
    tag: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails"
    ]
    """<p>A tag that is assigned to matching objects.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of filter value. Valid values are <code>LifecyclePrefixPredicate</code> or <code>LifecycleTagPredicate</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails,
) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "tag" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details

        out["Tag"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details.serialize_json(
                value["tag"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails = {}  # type: ignore[typeddict-item]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("Tag") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details

        out["tag"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details.deserialize_json(
                data["Tag"]
            )
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
