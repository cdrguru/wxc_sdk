from collections.abc import Generator

from wxc_sdk.api_child import ApiChild
from wxc_sdk.base import ApiModel
from wxc_sdk.base import SafeEnum as Enum
from typing import List, Optional
from pydantic import Field


__all__ = ['CreateRoomTabBody', 'ListRoomTabsResponse', 'RoomTab', 'RoomTabsApi', 'RoomType']


class RoomType(str, Enum):
    #: 1:1 room
    direct = 'direct'
    #: group room
    group = 'group'


class CreateRoomTabBody(ApiModel):
    #: A unique identifier for the room.
    room_id: Optional[str]
    #: URL of the Room Tab. Must use https protocol.
    content_url: Optional[str]
    #: User-friendly name for the room tab.
    display_name: Optional[str]


class RoomTab(CreateRoomTabBody):
    #: A unique identifier for the Room Tab.
    id: Optional[str]
    #: The room type.
    room_type: Optional[RoomType]
    #: The person ID of the person who created this Room Tab.
    creator_id: Optional[str]
    #: The date and time when the Room Tab was created.
    created: Optional[str]


class ListRoomTabsResponse(ApiModel):
    items: Optional[list[RoomTab]]


class RoomTabsApi(ApiChild, base='room/tabs'):
    """
    A Room Tab represents a URL shortcut that is added as a persistent tab to a Webex room (space) tab row. Use this API to list tabs of any Webex room that you belong to. Room Tabs can also be updated to point to a different content URL, or deleted to remove the tab from the room.
    Just like in the Webex app, you must be a member of the room in order to list its Room Tabs.
    """

    def list_tabs(self, room_id: str, **params) -> Generator[ListRoomTabsResponse, None, None]:
        """
        Lists all Room Tabs of a room specified by the roomId query parameter.

        :param room_id: ID of the room for which to list room tabs.
        :type room_id: str
        """
        if room_id is not None:
            params['roomId'] = room_id
        url = self.ep()
        return self.session.follow_pagination(url=url, model=ListRoomTabsResponse, params=params)

    def create_tab(self, room_id: str, content_url: str, display_name: str) -> RoomTab:
        """
        Add a tab with a specified URL to a room.

        :param room_id: A unique identifier for the room.
        :type room_id: str
        :param content_url: URL of the Room Tab. Must use https protocol.
        :type content_url: str
        :param display_name: User-friendly name for the room tab.
        :type display_name: str
        """
        body = {}
        if room_id is not None:
            body['roomId'] = room_id
        if content_url is not None:
            body['contentUrl'] = content_url
        if display_name is not None:
            body['displayName'] = display_name
        url = self.ep()
        data = super().post(url=url, json=body)
        return RoomTab.parse_obj(data)

    def tab_details(self, id: str) -> RoomTab:
        """
        Get details for a Room Tab with the specified room tab ID.

        :param id: The unique identifier for the Room Tab.
        :type id: str
        """
        url = self.ep(f'{id}')
        data = super().get(url=url)
        return RoomTab.parse_obj(data)

    def update_tab(self, id: str, room_id: str, content_url: str, display_name: str) -> RoomTab:
        """
        Updates the content URL of the specified Room Tab ID.

        :param id: The unique identifier for the Room Tab.
        :type id: str
        :param room_id: ID of the room that contains the room tab in question.
        :type room_id: str
        :param content_url: Content URL of the Room Tab. URL must use https protocol.
        :type content_url: str
        :param display_name: User-friendly name for the room tab.
        :type display_name: str
        """
        body = {}
        if room_id is not None:
            body['roomId'] = room_id
        if content_url is not None:
            body['contentUrl'] = content_url
        if display_name is not None:
            body['displayName'] = display_name
        url = self.ep(f'{id}')
        data = super().put(url=url, json=body)
        return RoomTab.parse_obj(data)

    def delete_tab(self, id: str):
        """
        Deletes a Room Tab with the specified ID.

        :param id: The unique identifier for the Room Tab to delete.
        :type id: str
        """
        url = self.ep(f'{id}')
        super().delete(url=url)
        return
