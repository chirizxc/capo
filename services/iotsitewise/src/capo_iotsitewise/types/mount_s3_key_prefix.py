"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountS3KeyPrefix``."""

from typing import TypeAlias

"""<p>An object key name prefix. If specified, the mount includes only objects whose keys begin with this prefix. The maximum prefix length is 1,024 characters. To include all objects at the access point, omit this field.</p>"""
MountS3KeyPrefix: TypeAlias = str
