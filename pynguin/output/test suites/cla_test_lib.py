import pytest
from sty.lib import mute, unmute
from sty.primitive import Register

class MockRegister(Register):
    def __init__(self):
        self.is_muted = False
        
    def mute(self):
        self.is_muted = True
        
    def unmute(self):
        self.is_muted = False

def test_mute_single_register():
    reg = MockRegister()
    mute(reg)
    assert reg.is_muted == True

def test_mute_multiple_registers():
    reg1 = MockRegister()
    reg2 = MockRegister()
    mute(reg1, reg2)
    assert reg1.is_muted == True
    assert reg2.is_muted == True

def test_unmute_single_register():
    reg = MockRegister()
    reg.is_muted = True
    unmute(reg)
    assert reg.is_muted == False

def test_unmute_multiple_registers():
    reg1 = MockRegister()
    reg2 = MockRegister()
    reg1.is_muted = True
    reg2.is_muted = True
    unmute(reg1, reg2)
    assert reg1.is_muted == False
    assert reg2.is_muted == False

def test_mute_invalid_object():
    with pytest.raises(ValueError):
        mute("not a register")

def test_unmute_invalid_object():
    with pytest.raises(ValueError):
        unmute("not a register")

def test_mute_no_args():
    mute()  # Should not raise any error

def test_unmute_no_args():
    unmute()  # Should not raise any error