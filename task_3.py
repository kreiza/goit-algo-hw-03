def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        move_disk(source, target, state)
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        move_disk(source, target, state)
        hanoi(n - 1, auxiliary, target, source, state)


def move_disk(from_peg, to_peg, state):
    disk = state[from_peg].pop()
    state[to_peg].append(disk)
    print(f"Перемістити диск з {from_peg} на {to_peg}: {disk}")
    print(f"Проміжний стан: {state}")


if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    state = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    print(f"Початковий стан: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"Кінцевий стан: {state}")
