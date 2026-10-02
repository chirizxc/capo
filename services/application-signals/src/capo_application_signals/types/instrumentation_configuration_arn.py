"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationArn``."""

from typing import TypeAlias

"""ARN for an instrumentation configuration Format: arn:${Partition}:application-signals:${Region}:${Account}:instrumentationConfig/${service}/${environment}/${signalType}/${locationHash} Note: service and environment can contain '/' and ':', so we use a permissive pattern that only validates the ARN prefix structure and the 16-character lowercase hex locationHash suffix."""
InstrumentationConfigurationArn: TypeAlias = str
