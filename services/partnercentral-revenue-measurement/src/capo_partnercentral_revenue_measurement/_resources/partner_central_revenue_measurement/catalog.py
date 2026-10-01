from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_partnercentral_revenue_measurement._services.async_partner_central_revenue_measurement import (
        AsyncPartnerCentralRevenueMeasurementClient,
    )
    from capo_partnercentral_revenue_measurement._services.partner_central_revenue_measurement import (
        PartnerCentralRevenueMeasurementClient,
    )


class Catalog:
    def __init__(self, service: PartnerCentralRevenueMeasurementClient) -> None:
        self._service = service


class AsyncCatalog:
    def __init__(self, service: AsyncPartnerCentralRevenueMeasurementClient) -> None:
        self._service = service
