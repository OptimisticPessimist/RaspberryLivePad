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
            List[str]:　GamePadクラス内の関数のリスト
        """
        return sorted(self.function_names)

    @staticmethod
    def print_docstring(function: str) -> str:
        """
        GamePadクラス内の関数からdocstringを呼び出す

        Args:
            function(str): docstringを呼び出したい関数

        Returns:
            (str): 関数のdocstring
        """
        return eval(f"GamePad.{function}.__doc__")
