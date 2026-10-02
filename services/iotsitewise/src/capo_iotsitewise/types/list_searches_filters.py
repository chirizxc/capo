"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListSearchesFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.group_id_filter_list
    import capo_iotsitewise.types.search_status_filter_list
    import capo_iotsitewise.types.search_type_filter_list


class ListSearchesFilters(TypedDict, closed=True):
    status_filter: NotRequired[
        "capo_iotsitewise.types.search_status_filter_list.SearchStatusFilterList"
    ]
    """<p>Returns only searches whose status is one of the listed values.</p>"""
    started_after: NotRequired["datetime.datetime"]
    """<p>Returns only searches started at or after this time.</p>"""
    started_before: NotRequired["datetime.datetime"]
    """<p>Returns only searches started at or before this time.</p>"""
    group_id_filter: NotRequired[
        "capo_iotsitewise.types.group_id_filter_list.GroupIdFilterList"
    ]
    """<p>Returns only searches whose <code>groupId</code> is one of the listed values.</p>"""
    search_type_filter: NotRequired[
        "capo_iotsitewise.types.search_type_filter_list.SearchTypeFilterList"
    ]
    """<p>Returns only searches whose <code>searchType</code> is one of the listed values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchesFilters) -> dict:
    out: dict = {}
    if "status_filter" in value:
        import capo_iotsitewise.types.search_status_filter_list

        out["statusFilter"] = (
            capo_iotsitewise.types.search_status_filter_list.serialize_json(
                value["status_filter"]
            )
        )
    if "started_after" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["startedAfter"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["started_after"]
        )
    if "started_before" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["startedBefore"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["started_before"]
        )
    if "group_id_filter" in value:
        import capo_iotsitewise.types.group_id_filter_list

        out["groupIdFilter"] = (
            capo_iotsitewise.types.group_id_filter_list.serialize_json(
                value["group_id_filter"]
            )
        )
    if "search_type_filter" in value:
        import capo_iotsitewise.types.search_type_filter_list

        out["searchTypeFilter"] = (
            capo_iotsitewise.types.search_type_filter_list.serialize_json(
                value["search_type_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSearchesFilters:
    out: ListSearchesFilters = {}  # type: ignore[typeddict-item]
    if data.get("statusFilter") is not None:
        import capo_iotsitewise.types.search_status_filter_list

        out["status_filter"] = (
            capo_iotsitewise.types.search_status_filter_list.deserialize_json(
                data["statusFilter"]
            )
        )
    if data.get("startedAfter") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["started_after"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["startedAfter"]
            )
        )
    if data.get("startedBefore") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["started_before"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["startedBefore"]
            )
        )
    if data.get("groupIdFilter") is not None:
        import capo_iotsitewise.types.group_id_filter_list

        out["group_id_filter"] = (
            capo_iotsitewise.types.group_id_filter_list.deserialize_json(
                data["groupIdFilter"]
            )
        )
    if data.get("searchTypeFilter") is not None:
        import capo_iotsitewise.types.search_type_filter_list

        out["search_type_filter"] = (
            capo_iotsitewise.types.search_type_filter_list.deserialize_json(
                data["searchTypeFilter"]
            )
        )
    return out
