"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountS3AccessPointArn``."""

from typing import TypeAlias

"""<p>The Amazon Resource Name (ARN) of the Amazon S3 access point. The mount reads objects from the bucket associated with this access point. Access is governed by the access point policy and the task execution role's IAM permissions.</p>"""
MountS3AccessPointArn: TypeAlias = str
