"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSnsTopicDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_sns_topic_subscription_list
    import capo_securityhub.types.non_empty_string


class AwsSnsTopicDetails(TypedDict, closed=True):
    kms_master_key_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of an Amazon Web Services managed key for Amazon SNS or a customer managed key.</p>"""
    subscription: NotRequired[
        "capo_securityhub.types.aws_sns_topic_subscription_list.AwsSnsTopicSubscriptionList"
    ]
    """<p>Subscription is an embedded property that describes the subscription endpoints of an Amazon SNS topic.</p>"""
    topic_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon SNS topic.</p>"""
    owner: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The subscription's owner.</p>"""
    sqs_success_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p>"""
    sqs_failure_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p>"""
    application_success_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint. </p>"""
    firehose_success_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint. </p>"""
    firehose_failure_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint. </p>"""
    http_success_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p>"""
    http_failure_feedback_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSnsTopicDetails) -> dict:
    out: dict = {}
    if "kms_master_key_id" in value:
        out["KmsMasterKeyId"] = value["kms_master_key_id"]
    if "subscription" in value:
        import capo_securityhub.types.aws_sns_topic_subscription_list

        out["Subscription"] = (
            capo_securityhub.types.aws_sns_topic_subscription_list.serialize_json(
                value["subscription"]
            )
        )
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "sqs_success_feedback_role_arn" in value:
        out["SqsSuccessFeedbackRoleArn"] = value["sqs_success_feedback_role_arn"]
    if "sqs_failure_feedback_role_arn" in value:
        out["SqsFailureFeedbackRoleArn"] = value["sqs_failure_feedback_role_arn"]
    if "application_success_feedback_role_arn" in value:
        out["ApplicationSuccessFeedbackRoleArn"] = value[
            "application_success_feedback_role_arn"
        ]
    if "firehose_success_feedback_role_arn" in value:
        out["FirehoseSuccessFeedbackRoleArn"] = value[
            "firehose_success_feedback_role_arn"
        ]
    if "firehose_failure_feedback_role_arn" in value:
        out["FirehoseFailureFeedbackRoleArn"] = value[
            "firehose_failure_feedback_role_arn"
        ]
    if "http_success_feedback_role_arn" in value:
        out["HttpSuccessFeedbackRoleArn"] = value["http_success_feedback_role_arn"]
    if "http_failure_feedback_role_arn" in value:
        out["HttpFailureFeedbackRoleArn"] = value["http_failure_feedback_role_arn"]
    return out


def deserialize_json(data: dict) -> AwsSnsTopicDetails:
    out: AwsSnsTopicDetails = {}  # type: ignore[typeddict-item]
    if data.get("KmsMasterKeyId") is not None:
        out["kms_master_key_id"] = data["KmsMasterKeyId"]
    if data.get("Subscription") is not None:
        import capo_securityhub.types.aws_sns_topic_subscription_list

        out["subscription"] = (
            capo_securityhub.types.aws_sns_topic_subscription_list.deserialize_json(
                data["Subscription"]
            )
        )
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("SqsSuccessFeedbackRoleArn") is not None:
        out["sqs_success_feedback_role_arn"] = data["SqsSuccessFeedbackRoleArn"]
    if data.get("SqsFailureFeedbackRoleArn") is not None:
        out["sqs_failure_feedback_role_arn"] = data["SqsFailureFeedbackRoleArn"]
    if data.get("ApplicationSuccessFeedbackRoleArn") is not None:
        out["application_success_feedback_role_arn"] = data[
            "ApplicationSuccessFeedbackRoleArn"
        ]
    if data.get("FirehoseSuccessFeedbackRoleArn") is not None:
        out["firehose_success_feedback_role_arn"] = data[
            "FirehoseSuccessFeedbackRoleArn"
        ]
    if data.get("FirehoseFailureFeedbackRoleArn") is not None:
        out["firehose_failure_feedback_role_arn"] = data[
            "FirehoseFailureFeedbackRoleArn"
        ]
    if data.get("HttpSuccessFeedbackRoleArn") is not None:
        out["http_success_feedback_role_arn"] = data["HttpSuccessFeedbackRoleArn"]
    if data.get("HttpFailureFeedbackRoleArn") is not None:
        out["http_failure_feedback_role_arn"] = data["HttpFailureFeedbackRoleArn"]
    return out
