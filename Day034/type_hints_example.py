# Type Hints

# int, float, bool, str


def police_check(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False


print(police_check(10))