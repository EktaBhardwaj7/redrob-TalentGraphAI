from src.common.text import normalize_text


def test_normalize_text_preserves_programming_tokens():
    assert normalize_text("Python, C++, C# / ML!") == "python c++ c# / ml"
