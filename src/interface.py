from typing import List
from src.controller import GamePad


class Interface(GamePad):

    def __init__(self) -> None:
        super().__init__()
        self.function_names: List[str] = [f for f in dir(GamePad) if not f.startswith("_")]

    def sorted_function_names(self) -> List[str]:
        """
        controller.pyのGamePadクラスで定義した関数名をソートして返す

        Returns:
            List[str]:
        """
        return sorted(self.function_names)


interface = Interface()
print(interface.function_names)
print()
print(interface.sorted_function_names())