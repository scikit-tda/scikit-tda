"""How should this package be structured?

Should we expose each package at the sktda level?

"""


import sktda

def test_ripser():
    assert "ripser" in dir(sktda)
    assert callable(sktda.ripser)

def test_persim():
    assert "PersImage" in dir(sktda)
    assert "heat" in dir(sktda)
    assert "sliced_wasserstein" in dir(sktda)
    assert "plot_diagrams" in dir(sktda)

def test_tadasets():
    assert "dsphere" in dir(sktda.tadasets)
    assert "swiss_roll" in dir(sktda.tadasets)
