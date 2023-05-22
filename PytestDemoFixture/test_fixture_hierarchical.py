def test_1(fn_scope):
    print("First test")


def test_2(cls_scope):
    print("second test")


def test_3(session_scope):
    print("third test")


def test_4(module_scope):
    print("fourth test", module_scope)


def test_5(package_scope):
    print("fifth test")
