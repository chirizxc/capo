from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_cloudwatchomni._services.async_cloud_watch_omni import (
        AsyncCloudWatchOmniClient,
    )
    from capo_cloudwatchomni._services.cloud_watch_omni import (
        CloudWatchOmniClient,
    )


class SpaceResource:
    def __init__(self, service: CloudWatchOmniClient) -> None:
        self._service = service


class AsyncSpaceResource:
    def __init__(self, service: AsyncCloudWatchOmniClient) -> None:
        self._service = service
