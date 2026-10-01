"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EcrUri``."""

from typing import TypeAlias

"""<p>The Amazon ECR image URI for the container.</p> <p>Supported formats:</p> <ul> <li>Private: <code>{account-id}.dkr.ecr.{region}.amazonaws.com/{repository}:{tag}</code></li> <li>Public: <code>public.ecr.aws/{registry-alias}/{repository}:{tag}</code></li> </ul> <p>Tags and digests (<code>@sha256:...</code>) are optional. If omitted, <code>latest</code> is used. The image must be accessible from the task execution role.</p>"""
EcrUri: TypeAlias = str
