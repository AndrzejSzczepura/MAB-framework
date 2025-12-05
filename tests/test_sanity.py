def test_import_root():
    try:
        import multi_agent_bandits
    except ImportError:
        assert False

def test_placeholder():
    assert True
