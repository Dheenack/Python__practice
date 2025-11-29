from my_code import add

def test_divide():
    assert add(4,2)==6
    print("test 1 done")
    assert add("a","b")==None
    print("test 2 done")

test_divide()