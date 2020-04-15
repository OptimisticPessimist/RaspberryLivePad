from abc import ABC, abstractmethod
from typing import List
from src.controller import GamePad
from src.controller_sample import DummyPad


class Root(ABC):
    """インターフェース用の抽象基底クラス"""

    def sorted_function_names(self) -> List[str]:
        """
        controller.pyのGamePadクラスで定義した関数名をソートして返す

        Returns:
            List[str]:　GamePadクラス内の関数のリスト
        """
        return sorted(self.function_names)

    @staticmethod
    @abstractmethod
    def print_docstring(function: str) -> str:
        """
        GamePadクラス内の関数からdocstringを呼び出す

        Args:
            function(str): docstringを呼び出したい関数

        Returns:
            (str): 関数のdocstring
        """
        pass


class RunMode(Root, GamePad):
    """実動クラス"""

    def __init__(self) -> None:
        super().__init__()
        self.function_names: List[str] = [f for f in dir(GamePad) if not f.startswith("_")]

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


class TestMode(Root, DummyPad):
    """テスト用クラス"""

    def __init__(self) -> None:
        super().__init__()
        self.function_names: List[str] = [f for f in dir(DummyPad) if not f.startswith("_")]

    @staticmethod
    def print_docstring(function: str) -> str:
        """
        GamePadクラス内の関数からdocstringを呼び出す

        Args:
            function(str): docstringを呼び出したい関数

        Returns:
            (str): 関数のdocstring
        """
        return eval(f"DummyPad.{function}.__doc__")
