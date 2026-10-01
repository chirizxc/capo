from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
    )
    from capo_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
    )


class TriggerResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service


class AsyncTriggerResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service
