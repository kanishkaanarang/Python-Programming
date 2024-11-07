from fuel import convert,gauge
def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/5")==20.0


def test_gauge():
    assert gauge("20.0")=="20.0%"


if __name__ == "__main__":
    main()
