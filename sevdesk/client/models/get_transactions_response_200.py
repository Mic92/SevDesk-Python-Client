from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_account_transaction_response_model import (
        CheckAccountTransactionResponseModel,
    )


T = TypeVar("T", bound="GetTransactionsResponse200")


@attr.s(auto_attribs=True)
class GetTransactionsResponse200:
    """
    Attributes:
        objects (Union[Unset, List['CheckAccountTransactionResponseModel']]):
    """

    objects: Union[Unset, List["CheckAccountTransactionResponseModel"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()

                objects.append(objects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_account_transaction_response_model import (
            CheckAccountTransactionResponseModel,
        )

        d = src_dict.copy()
        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = CheckAccountTransactionResponseModel.from_dict(
                objects_item_data
            )

            objects.append(objects_item)

        get_transactions_response_200 = cls(
            objects=objects,
        )

        get_transactions_response_200.additional_properties = d
        return get_transactions_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
