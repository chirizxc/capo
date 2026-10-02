from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_parse_arn,
    get_attr,
    interpolate,
    is_valid_host_label,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        Region: str | None = None,
        UseFIPS: bool | None = None,
        UseDualStack: bool | None = None,
        Endpoint: str | None = None,
        AccountId: str | None = None,
        EventBusArn: str | None = None,
        AccountIdEndpointMode: str | None = None,
    ):
        self.Region = Region
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.AccountId = AccountId if AccountId is not None else None
        self.EventBusArn = EventBusArn if EventBusArn is not None else None
        self.AccountIdEndpointMode = (
            AccountIdEndpointMode if AccountIdEndpointMode is not None else None
        )


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        if p.UseDualStack is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: Dualstack and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    _locals["PartitionResult"] = aws_partition(p.Region)
    if _locals["PartitionResult"] is not None:
        if p.AccountIdEndpointMode is not None:
            if not (
                string_equals(
                    p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                )
            ):
                if p.EventBusArn is not None:
                    _locals["ParsedBusArn"] = aws_parse_arn(p.EventBusArn)
                    if _locals["ParsedBusArn"] is not None:
                        if string_equals(
                            get_attr(
                                _locals["ParsedBusArn"],
                                interpolate("service", p, _locals),
                            ),
                            interpolate("events", p, _locals),
                        ):
                            if is_valid_host_label(
                                get_attr(
                                    _locals["ParsedBusArn"],
                                    interpolate("accountId", p, _locals),
                                ),
                                False,
                            ):
                                if p.UseFIPS is True:
                                    if p.UseDualStack is True:
                                        if True is get_attr(
                                            _locals["PartitionResult"],
                                            interpolate("supportsFIPS", p, _locals),
                                        ):
                                            if True is get_attr(
                                                _locals["PartitionResult"],
                                                interpolate(
                                                    "supportsDualStack", p, _locals
                                                ),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{ParsedBusArn#accountId}.eventsv2-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "metricValues": [
                                                            interpolate("O", p, _locals)
                                                        ]
                                                    },
                                                    headers={},
                                                )
                                        raise EndpointError(
                                            interpolate(
                                                "FIPS and DualStack are enabled, but this partition does not support one or both",
                                                p,
                                                _locals,
                                            )
                                        )
                                if p.UseFIPS is True:
                                    if True is get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("supportsFIPS", p, _locals),
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://{ParsedBusArn#accountId}.eventsv2-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "metricValues": [
                                                    interpolate("O", p, _locals)
                                                ]
                                            },
                                            headers={},
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "FIPS is enabled but this partition does not support FIPS",
                                            p,
                                            _locals,
                                        )
                                    )
                                if p.UseDualStack is True:
                                    if True is get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("supportsDualStack", p, _locals),
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://{ParsedBusArn#accountId}.eventsv2.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "metricValues": [
                                                    interpolate("O", p, _locals)
                                                ]
                                            },
                                            headers={},
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "DualStack is enabled but this partition does not support DualStack",
                                            p,
                                            _locals,
                                        )
                                    )
                                return Endpoint(
                                    url=interpolate(
                                        "https://{ParsedBusArn#accountId}.eventsv2.{Region}.{PartitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "metricValues": [interpolate("O", p, _locals)]
                                    },
                                    headers={},
                                )
        if p.AccountIdEndpointMode is not None:
            if not (
                string_equals(
                    p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                )
            ):
                if p.AccountId is not None:
                    if is_valid_host_label(p.AccountId, False):
                        if p.UseFIPS is True:
                            if p.UseDualStack is True:
                                if True is get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("supportsFIPS", p, _locals),
                                ):
                                    if True is get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("supportsDualStack", p, _locals),
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://{AccountId}.eventsv2-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "metricValues": [
                                                    interpolate("O", p, _locals)
                                                ]
                                            },
                                            headers={},
                                        )
                                raise EndpointError(
                                    interpolate(
                                        "FIPS and DualStack are enabled, but this partition does not support one or both",
                                        p,
                                        _locals,
                                    )
                                )
                        if p.UseFIPS is True:
                            if True is get_attr(
                                _locals["PartitionResult"],
                                interpolate("supportsFIPS", p, _locals),
                            ):
                                return Endpoint(
                                    url=interpolate(
                                        "https://{AccountId}.eventsv2-fips.{Region}.{PartitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "metricValues": [interpolate("O", p, _locals)]
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "FIPS is enabled but this partition does not support FIPS",
                                    p,
                                    _locals,
                                )
                            )
                        if p.UseDualStack is True:
                            if True is get_attr(
                                _locals["PartitionResult"],
                                interpolate("supportsDualStack", p, _locals),
                            ):
                                return Endpoint(
                                    url=interpolate(
                                        "https://{AccountId}.eventsv2.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "metricValues": [interpolate("O", p, _locals)]
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "DualStack is enabled but this partition does not support DualStack",
                                    p,
                                    _locals,
                                )
                            )
                        return Endpoint(
                            url=interpolate(
                                "https://{AccountId}.eventsv2.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={"metricValues": [interpolate("O", p, _locals)]},
                            headers={},
                        )
                    raise EndpointError(
                        interpolate(
                            "Credentials-sourced account ID parameter is invalid",
                            p,
                            _locals,
                        )
                    )
        if p.AccountIdEndpointMode is not None:
            if string_equals(
                p.AccountIdEndpointMode, interpolate("required", p, _locals)
            ):
                raise EndpointError(
                    interpolate(
                        "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                        p,
                        _locals,
                    )
                )
        if p.UseFIPS is True:
            if p.UseDualStack is True:
                if True is get_attr(
                    _locals["PartitionResult"], interpolate("supportsFIPS", p, _locals)
                ):
                    if True is get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsDualStack", p, _locals),
                    ):
                        return Endpoint(
                            url=interpolate(
                                "https://eventsv2-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                raise EndpointError(
                    interpolate(
                        "FIPS and DualStack are enabled, but this partition does not support one or both",
                        p,
                        _locals,
                    )
                )
        if p.UseFIPS is True:
            if True is get_attr(
                _locals["PartitionResult"], interpolate("supportsFIPS", p, _locals)
            ):
                return Endpoint(
                    url=interpolate(
                        "https://eventsv2-fips.{Region}.{PartitionResult#dnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            raise EndpointError(
                interpolate(
                    "FIPS is enabled but this partition does not support FIPS",
                    p,
                    _locals,
                )
            )
        if p.UseDualStack is True:
            if True is get_attr(
                _locals["PartitionResult"], interpolate("supportsDualStack", p, _locals)
            ):
                return Endpoint(
                    url=interpolate(
                        "https://eventsv2.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            raise EndpointError(
                interpolate(
                    "DualStack is enabled but this partition does not support DualStack",
                    p,
                    _locals,
                )
            )
        return Endpoint(
            url=interpolate(
                "https://eventsv2.{Region}.{PartitionResult#dnsSuffix}", p, _locals
            ),
            properties={},
            headers={},
        )
    raise EndpointError("No endpoint rules matched")
