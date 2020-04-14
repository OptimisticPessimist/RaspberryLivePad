from gpiozero import Motor


class GamePad:
    """ゲームパッドに割り振る操作を入れるクラス"""

    def __init__(self) -> None:
        self.front_motor = Motor(11, 12)
        self.right_motor = Motor(13, 15)
        self.left_motor = Motor(16, 18)

    def fork_lift_up(self, analog_input: float) -> None:
        """
        (アナログ入力)フォークリフトを入力した速度で上昇させる

        Args:
            analog_input(float): ゲームパッドのアナログ入力値
        """
        self.front_motor.forward(analog_input)

    def fork_lift_down(self, analog_input: float) -> None:
        """
        (アナログ入力)フォークリフトを入力した速度で下降させる

        Args:
            analog_input(float): ゲームパッドのアナログ入力値
        """
        self.front_motor.backward(-analog_input)

    def axis_vertical_right(self, stick_input: float, margin: float) -> None:
        """
        (スティック入力)入力した速度で右モータでの前後移動
        アナログスティックは完全な　(0, 0) 座標を返さないので入力にマージンを持たせる

        Args:
            stick_input(float): ゲームスティックのアナログ入力値 (-1.0 ~ 1.0)
            margin(float): 入力を無視する閾値
        """
        if stick_input > margin:
            self.right_motor.forward(stick_input)
        elif stick_input < -margin:
            self.right_motor.backward(-stick_input)
        else:
            self.right_motor.stop()

    def axis_vertical_left(self, stick_input: float, margin: float) -> None:
        """
        (スティック入力)入力した速度で左モータでの前後移動
        アナログスティックは完全な　(0, 0) 座標を返さないので入力にマージンを持たせる

        Args:
            stick_input(float): ゲームスティックのアナログ入力値 (-1.0 ~ 1.0)
            margin(float): 入力を無視する閾値
        """
        if stick_input > margin:
            self.left_motor.forward(stick_input)
        elif stick_input < -margin:
            self.left_motor.backward(-stick_input)
        else:
            self.left_motor.stop()
