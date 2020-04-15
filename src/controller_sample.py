class DummyPad:
    """ゲームパッドに割り振る操作を入れるクラス"""

    def __init__(self) -> None:
        pass

    def analog_up(self, analog_input: float) -> None:
        """
        (アナログ入力)入力した速度で上昇させる

        Args:
            analog_input(float): ゲームパッドのアナログ入力値
        """
        pass

    def analog_down(self, analog_input: float) -> None:
        """
        (アナログ入力)入力した速度で下降させる

        Args:
            analog_input(float): ゲームパッドのアナログ入力値
        """
        pass

    def axis_vertical_right(self, stick_input: float, margin: float) -> None:
        """
        (スティック入力)入力した速度で前後移動
        アナログスティックは完全な　(0, 0) 座標を返さないので入力にマージンを持たせる

        Args:
            stick_input(float): ゲームスティックのアナログ入力値 (-1.0 ~ 1.0)
            margin(float): 入力を無視する閾値
        """
        if stick_input > margin:
            pass
        elif stick_input < -margin:
            pass
        else:
            pass

    def axis_vertical_left(self, stick_input: float, margin: float) -> None:
        """
        (スティック入力)入力した速度で前後移動
        アナログスティックは完全な　(0, 0) 座標を返さないので入力にマージンを持たせる

        Args:
            stick_input(float): ゲームスティックのアナログ入力値 (-1.0 ~ 1.0)
            margin(float): 入力を無視する閾値
        """
        if stick_input > margin:
            pass
        elif stick_input < -margin:
            pass
        else:
            pass
