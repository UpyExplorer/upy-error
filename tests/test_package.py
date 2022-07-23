from upy_error import format_exception


def test_error_log():
    try:
        print(x)
    except Exception as error:
        format_exception(error=error, log=True)
        
        assert NameError == type(error)

def test_error_print():
    try:
        1 / 0
    except Exception as error:
        print(format_exception(error=error))

        assert ZeroDivisionError == type(error)
