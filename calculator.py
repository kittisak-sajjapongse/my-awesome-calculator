
def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return a / b

def sub(a: int, b: int) -> int:
    return a - b

def add(a: int, b: int) -> int:
    return a + b

def triangle_area(width, height):
    return 0.5 * width * height

if __name__ == "__main__":

    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 - 3 = {sub(2, 3)}")
    print(f"5 - 3 = {sub(5, 3)}")
    print(f"7 - 3 = {sub(7, 3)}")
    print(f"10 * 4 = {mul(10, 4)}")
    print(f"triangle {triangle_area(3,5)}")
