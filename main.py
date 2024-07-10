def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min), end=' ')
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
