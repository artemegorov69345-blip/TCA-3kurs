import random
import sys

sys.setrecursionlimit(1_000_000)


def insertion_sort(a):
    cmp = 0
    n = len(a)
    for i in range(1, n):
        key = a[i]

        lo, hi = 0, i
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cmp += 1
            if a[mid] <= key:
                lo = mid + 1
            else:
                hi = mid

        for j in range(i - 1, lo - 1, -1):
            a[j + 1] = a[j]

        a[lo] = key
    return cmp


def selection_sort(a):
    cmp = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            cmp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return cmp


def partition_hoare(a, n, result, cmp):
    # cmp передаётся как список из одного элемента [0],
    # чтобы изменять его внутри функции (аналог long long& в C++)
    if n == 0:
        return result

    ref_el_index = (n - 1) // 2
    ref_el = a[ref_el_index]
    i = 0
    n_left = 0
    n_right = 0
    left_arr = []
    right_arr = []
    while True:
        if i == ref_el_index:
            i += 1
        else:
            cmp[0] += 1
            if a[i] <= ref_el:
                left_arr.append(a[i])
                n_left += 1
            else:
                right_arr.append(a[i])
                n_right += 1
            i += 1
        if not (i < n):
            break

    if n_left > 1:
        partition_hoare(left_arr, n_left, result, cmp)
    elif n_left == 1:
        result.append(left_arr[n_left - 1])
    result.append(ref_el)
    if n_right > 1:
        partition_hoare(right_arr, n_right, result, cmp)
    elif n_right == 1:
        result.append(right_arr[n_right - 1])
    return result


def generate_array(n, min_val, max_val):
    gen = random.SystemRandom()
    return [gen.randint(min_val, max_val) for _ in range(n)]


def print_array(a, limit=30):
    n = len(a)
    if n <= limit:
        print(" ".join(str(x) for x in a) + " ")
    else:
        print(" ".join(str(a[i]) for i in range(limit)) + f" ... (всего {n} элементов)")


def main():
    n = int(input("Введите количество элементов n: "))

    if n <= 0:
        print("n должно быть положительным")
        return 1

    min_val, max_val = -100, 100

    original = generate_array(n, min_val, max_val)

    print("\nИсходный массив: ", end="")
    print_array(original)

    work = original.copy()
    cmp_insertion = insertion_sort(work)

    work = original.copy()
    cmp_selection = selection_sort(work)

    work = original.copy()
    result = []
    cmp_quick = [0]
    partition_hoare(work, len(work), result, cmp_quick)

    print("\nОтсортированный массив: ", end="")
    print_array(result)

    print("\nКоличество сравнений:")
    print(f"Вставками: {cmp_insertion}")
    print(f"Перебором: {cmp_selection}")
    print(f"Хоара: {cmp_quick[0]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
