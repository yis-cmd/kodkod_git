from typing import Generic, TypeVar

T = TypeVar("T")


class lst(Generic[T]):
    def __init__(self) -> None:
        self._list: list[T] = []
        self._type = None

    def append(self, value: T):
        if not self._list:
            self._type = type(value)
            self._list.append(value)
        else:
            assert isinstance(self._type, type)
            if isinstance(value, self._type):
                self._list.append(value)
            else:
                raise ValueError(
                    f"unexpected type expected {self._type} got {type(value)}"
                )


a: lst[str] = lst()
a.append("a")
print(a._list)


