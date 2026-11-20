class Television:
    """
    A television with a power status, a mute setting, a volume and a channel.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Set the tv to off, unmuted, with the minimum volume and minimum channel.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the tv on or off by changing the value of the status variable.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the tv, only when the tv is on, by changing the value of the muted variable.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel when the tv is on. At the maximum channel it goes back to the minimum channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel when the tv is on. At the minimum channel it goes to the maximum channel.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Unmute the tv and increase the volume when the tv is on. At the maximum volume it stays there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Unmute the tv and decrease the volume when the tv is on. At the minimum volume it stays there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Show the tv values. The volume shows as the minimum volume while the tv is muted.
        :return: the power, channel and volume of the tv as text
        """
        if self.__muted:
            volume: int = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
