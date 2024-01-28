def adjacent_digits(k: int) -> list[int]:
    return_value = []
    if k == 1:
        for i in range(10):
            return_value.append(i)
    elif k > 1:
        previous_list = adjacent_digits(k - 1)
        for candidate in previous_list:
            if candidate != 0:
                for i in [-1, 0, 1]:
                    if 0 <= i + (candidate % 10) <= 9:
                        return_value.append(candidate * 10 + i + (candidate % 10))
    return return_value
