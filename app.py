def convert(n):
    result = ""

    digits = [[10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

    for d in digits:
        limit = d[0]
        glyph = d[1]

        while n >= limit:
            result += glyph
            n -= limit

    return result


def test_convert():
    assert convert(1) == "I"
    assert convert(2) == "II"
    assert convert(4) == "IV"
    assert convert(5) == "V"
    assert convert(6) == "VI"
    assert convert(9) == "IX"
    assert convert(10) == "X"
    assert convert(20) == "XX"
