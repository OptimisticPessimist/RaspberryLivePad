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

    @staticmethod
    def print_docstring(function) -> str:
        """
        関数のdocstringを呼び出す

        Args:
            function: docstringを呼び出したい関数

        Returns:
            (str): 関数のdocstring
        """
        return function.__doc__
