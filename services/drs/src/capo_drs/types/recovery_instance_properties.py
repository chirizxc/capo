"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.cpus
    import capo_drs.types.identification_hints
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.network_interfaces
    import capo_drs.types.os
    import capo_drs.types.positive_integer
    import capo_drs.types.recovery_instance_disks


class RecoveryInstanceProperties(TypedDict, closed=True):
    last_updated_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time the Recovery Instance properties were last updated on.</p>"""
    identification_hints: NotRequired[
        "capo_drs.types.identification_hints.IdentificationHints"
    ]
    """<p>Hints used to uniquely identify a machine.</p>"""
    network_interfaces: NotRequired[
        "capo_drs.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>An array of network interfaces.</p>"""
    disks: NotRequired["capo_drs.types.recovery_instance_disks.RecoveryInstanceDisks"]
    """<p>An array of disks.</p>"""
    cpus: NotRequired["capo_drs.types.cpus.Cpus"]
    """<p>An array of CPUs.</p>"""
    ram_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of RAM in bytes.</p>"""
    os: NotRequired["capo_drs.types.os.OS"]
    """<p>Operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceProperties) -> dict:
    out: dict = {}
    if "last_updated_date_time" in value:
        out["lastUpdatedDateTime"] = value["last_updated_date_time"]
    if "identification_hints" in value:
        import capo_drs.types.identification_hints

        out["identificationHints"] = capo_drs.types.identification_hints.serialize_json(
            value["identification_hints"]
        )
    if "network_interfaces" in value:
        import capo_drs.types.network_interfaces

        out["networkInterfaces"] = capo_drs.types.network_interfaces.serialize_json(
            value["network_interfaces"]
        )
    if "disks" in value:
        import capo_drs.types.recovery_instance_disks

        out["disks"] = capo_drs.types.recovery_instance_disks.serialize_json(
            value["disks"]
        )
    if "cpus" in value:
        import capo_drs.types.cpus

        out["cpus"] = capo_drs.types.cpus.serialize_json(value["cpus"])
    out["ramBytes"] = value.get("ram_bytes", 0)
    if "os" in value:
        import capo_drs.types.os

        out["os"] = capo_drs.types.os.serialize_json(value["os"])
    return out


def deserialize_json(data: dict) -> RecoveryInstanceProperties:
    out: RecoveryInstanceProperties = {}  # type: ignore[typeddict-item]
    if data.get("lastUpdatedDateTime") is not None:
        out["last_updated_date_time"] = data["lastUpdatedDateTime"]
    if data.get("identificationHints") is not None:
        import capo_drs.types.identification_hints

        out["identification_hints"] = (
            capo_drs.types.identification_hints.deserialize_json(
                data["identificationHints"]
            )
        )
    if data.get("networkInterfaces") is not None:
        import capo_drs.types.network_interfaces

        out["network_interfaces"] = capo_drs.types.network_interfaces.deserialize_json(
            data["networkInterfaces"]
        )
    if data.get("disks") is not None:
        import capo_drs.types.recovery_instance_disks

        out["disks"] = capo_drs.types.recovery_instance_disks.deserialize_json(
            data["disks"]
        )
    if data.get("cpus") is not None:
        import capo_drs.types.cpus

        out["cpus"] = capo_drs.types.cpus.deserialize_json(data["cpus"])
    if data.get("ramBytes") is not None:
        out["ram_bytes"] = data["ramBytes"]
    else:
        out["ram_bytes"] = 0
    if data.get("os") is not None:
        import capo_drs.types.os

        out["os"] = capo_drs.types.os.deserialize_json(data["os"])
    return out
