from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CheckAccountTransactionUpdateModelSourceTransaction")


@attr.s(auto_attribs=True)
class CheckAccountTransactionUpdateModelSourceTransaction:
    """The check account transaction serving as the source of the rebooking

    Attributes:
        id (int): Unique identifier of the check account transaction
        object_name (str): Model name, which is 'CheckAccountTransaction' Default: 'CheckAccountTransaction'.
    """

    id: int
    object_name: str = "CheckAccountTransaction"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "objectName": object_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_name = d.pop("objectName")

        check_account_transaction_update_model_source_transaction = cls(
            id=id,
            object_name=object_name,
        )

        check_account_transaction_update_model_source_transaction.additional_properties = (
            d
        )
        return check_account_transaction_update_model_source_transaction

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
