"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AmiWatermarkName``."""

from typing import TypeAlias

"""<p>The name of an AMI watermark. AMI watermarks are lineage markers that Image Builder attaches to output AMIs during the build process. AMI watermarks automatically propagate to derivative AMIs when the source AMI is copied or distributed.</p>"""
AmiWatermarkName: TypeAlias = str
