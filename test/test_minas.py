from src.minas import generaMinas

def test_generaMinas():
    assert len(generaMinas(10)) == 10