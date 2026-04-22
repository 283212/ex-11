import random
import matplotlib.pyplot as plt


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



def bubble_sort(values):
    plt.ion()
    plt.show()


    velikost = len(values)

    for e in range(velikost):

        swap = False

        p = 0

        for j in range(velikost - 1):
            prvni_index = p
            druhy_index = p + 1

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if values[prvni_index] > values[druhy_index]:
                values[prvni_index], values[druhy_index] = values[druhy_index], values[prvni_index]

                swap = True

            p += 1

        if swap == False:
            return values

        print(values)

        velikost -= 1

    plt.ioff()
    plt.show()

    return values









if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)

    #selection_sort(values)
    bubble_sort(values)