from television import Television


class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_power_on(self):
        self.tv.power()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_power_off(self):
        self.tv.power()
        self.tv.power()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute_on_muted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_mute_on_unmuted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.mute()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'

    def test_mute_off_muted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute_off_unmuted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up_off(self):
        self.tv.channel_up()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_channel_up_on(self):
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 1, Volume = 0'

    def test_channel_up_past_maximum(self):
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down_off(self):
        self.tv.channel_down()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_channel_down_on(self):
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        assert str(self.tv) == 'Power = True, Channel = 1, Volume = 0'

    def test_channel_down_past_minimum(self):
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up_off(self):
        self.tv.volume_up()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_volume_up_on(self):
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'

    def test_volume_up_muted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_up_past_maximum(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down_off(self):
        self.tv.volume_down()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_volume_down_on(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'

    def test_volume_down_muted(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'

    def test_volume_down_past_minimum(self):
        self.tv.power()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
