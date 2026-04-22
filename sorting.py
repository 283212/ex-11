import random


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



def selection_sort(values):

    a = len(values)
    z = 1
    p = 0

    for e in range(a - 1):

        min_index = p
        min_value = values[min_index]

        for i in range(z, len(values)):
            if values[i] < min_value:
                min_index = i
                min_value = values[i]

        print(min_index)

        values[p], values[min_index] = values[min_index], values[p]
        print(values)

        a -= 1
        z += 1
        p += 1

    return values



if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)

    selection_sort(values)