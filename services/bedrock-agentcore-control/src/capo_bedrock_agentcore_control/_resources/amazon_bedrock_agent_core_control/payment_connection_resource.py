from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
    )


class PaymentConnectionResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service


class AsyncPaymentConnectionResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
