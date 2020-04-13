def rectangle_method(func, a, b, intervals):
    step = float(b - a) / intervals
    begin = a + (step / 2)
    result = float(0)
    for i in range(intervals):
        result += func(begin + i * step) * step
    return result


def trapeze_method(func, a, b, intervals):
    step = float(b - a) / intervals
    result = float(0)
    for i in range(intervals):
        result += (func(a + i * step) + func(a + (i + 1) * step)) / 2 * step
    return result


def simpson_method(func, a, b, intervals):
    step = float(b - a) / intervals
    begin = a + (step / 2)
    result = float(0)
    for i in range(intervals):
        result += step / 6 * (func(a + i * step) + 4 * func(begin + i * step) + func(a + (i+1) * step))
    return result