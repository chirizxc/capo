"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterId``."""

from typing import TypeAlias

"""<p>A unique identifier for a LoRA adapter within a recommendation job request. The ID must start and end with an alphanumeric character, can contain hyphens between alphanumeric characters, and can be up to 63 characters long. This ID is used as the inference component name when the adapter is deployed.</p>"""
AIAdapterId: TypeAlias = str
