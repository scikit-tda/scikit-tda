"""How should this package be structured?

Should we expose each package at the sktda level?

"""


import sktda


def test_ripser():
    assert "ripser" in dir(sktda)
    assert callable(sktda.ripser.ripser)


def test_persim():
    assert "persim" in dir(sktda)
    assert "PersImage" in dir(sktda.persim)
    assert "heat" in dir(sktda.persim)
    assert "sliced_wasserstein" in dir(sktda.persim)
    assert "plot_diagrams" in dir(sktda.persim)
    assert "landscapes" in dir(sktda.persim)


def test_tadasets():
    assert "tadasets" in dir(sktda)
    assert "dsphere" in dir(sktda.tadasets)
    assert "swiss_roll" in dir(sktda.tadasets)
