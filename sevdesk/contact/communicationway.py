from __future__ import annotations

from enum import Enum, auto
from typing import Any, Union

import attrs

from .. import UNSET, Client, Unset
from ..client.api.communication_way import (
    create_communication_way,
    delete_communication_way,
    update_communication_way,
)
from ..client.models.communication_way_model import (
    CommunicationWayModel,
    CommunicationWayModelType,
)
from ..client.models.communication_way_model_key import (
    CommunicationWayModelKey,
)
from ..client.models.communication_way_model_contact import CommunicationWayModelContact
from ..common import ApiObject, ApiObjectCache, ApiObjectType, SevDesk


class CommunicationWayKey(str, Enum):
    """
    Define how this communication way will be used
    """

    COMM_WAY_KEY_WORK = "COMM_WAY_KEY_WORK"
    COMM_WAY_KEY_AUTOBOX = "COMM_WAY_KEY_AUTOBOX"
    COMM_WAY_KEY_FAX = "COMM_WAY_KEY_FAX"
    COMM_WAY_KEY_MOBILE = "COMM_WAY_KEY_MOBILE"
    COMM_WAY_KEY_NEWSLETTER = "COMM_WAY_KEY_NEWSLETTER"
    COMM_WAY_KEY_PRIVAT = "COMM_WAY_KEY_PRIVAT"
    COMM_WAY_KEY_INVOICE_ADDRESS = "COMM_WAY_KEY_INVOICE_ADDRESS"
    COMM_WAY_KEY_EMPTY = "COMM_WAY_KEY_EMPTY"

    def _get_api_model(self, client: Client) -> CommunicationWayModelKey:
        """
        Get the API-Model for the given Communication Way Key
        """
        cache = ApiObjectCache(client=client)
        item: ApiObject = cache.get(ApiObjectType.COMMUNICATION_WAY_KEY)[self]

        return CommunicationWayModelKey(item.id, "CommunicationWayKey")

    @staticmethod
    def get_by_id(client: Client, id: str) -> CommunicationWayKey:
        cache = ApiObjectCache(client=client)
        keys = cache.get(ApiObjectType.COMMUNICATION_WAY_KEY).sort_by_id()
        key = keys[id]

        return CommunicationWayKey[key.translationCode]


class CommuncationWayType(Enum):
    """
    The communication type
    """

    EMAIL = auto()
    PHONE = auto()
    WEB = auto()
    MOBILE = auto()

    def _get_api_model(self, client: Client) -> CommunicationWayModelType:
        map = {
            CommuncationWayType.EMAIL: CommunicationWayModelType.EMAIL,
            CommuncationWayType.PHONE: CommunicationWayModelType.PHONE,
            CommuncationWayType.WEB: CommunicationWayModelType.WEB,
            CommuncationWayType.MOBILE: CommunicationWayModelType.MOBILE,
        }

        return map[self]


@attrs.define()
class CommunicationWay:
    """
    The Communication Way - can only be added to a Contact
    """

    value: str
    type_: CommuncationWayType
    key: CommunicationWayKey = CommunicationWayKey.COMM_WAY_KEY_WORK
    parent: Union[Unset, Any] = UNSET
    id: Union[Unset, str] = UNSET

    def _get_api_model(self, client: Client) -> CommunicationWayModel:
        """
        Get the API Model to create or update a specific communication way
        """
        return CommunicationWayModel(
            type=self.type_._get_api_model(client),
            value=self.value,
            key=self.key._get_api_model(client),
            contact=CommunicationWayModelContact(id=self.parent.id),
        )

    def create(self, client: Client):
        """
        Create the communication way by appending it to the given client
        """
        if not self.parent:
            raise ValueError("Cannt create Communication Way without a parent.")

        response = create_communication_way.sync_detailed(
            client=client, json_body=self._get_api_model(client)
        )
        SevDesk.raise_for_status(response, "creating communication-way")

        # Update ID from result
        self.id = response.parsed.objects.id

    def update(self, client: Client, create: bool = True):
        """
        Updating a communication way
        """
        if not self.id and create:
            return self.create(client)

        if not self.id:
            raise ValueError("Communication Way ID not set, cannot update unknown.")

        response = update_communication_way.sync_detailed(
            communication_way_id=self.id,
            client=client,
            json_body=self._get_api_model(client),
        )

        SevDesk.raise_for_status(response, "updating communication-way")

    def delete(self, client: Client):
        """
        Deleting the given communication way by its ID
        """
        if not self.id:
            raise ValueError("Communication-Way-ID not set, cannot delete unknown.")

        response = delete_communication_way.sync_detailed(
            communication_way_id=self.id, client=client
        )
        SevDesk.raise_for_status(response, "deleting communication-way")


@attrs.define()
class Email(CommunicationWay):
    """
    Communication way using E-Mail
    """

    type_: CommuncationWayType = CommuncationWayType.EMAIL

    def update(self, client: Client, create: bool = True):
        super().update(client, create)

        if self.parent:
            self.parent.email = self

    def delete(self, client: Client):
        super().delete(client)

        if self.parent:
            self.parent.email = UNSET


@attrs.define()
class Phone(CommunicationWay):
    """
    Communication way using Phone
    """

    type_: CommuncationWayType = CommuncationWayType.PHONE

    def update(self, client: Client, create: bool = True):
        super().update(client, create)

        if self.parent:
            self.parent.phone = self

    def delete(self, client: Client):
        super().delete(client)

        if self.parent:
            self.parent.phone = UNSET
