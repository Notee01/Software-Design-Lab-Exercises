def MinMax(list):

    if list:
        max, *min = list

        if min:
            minimum, maximum = MinMax(min)

            return [max, minimum][minimum < max], [max, maximum][maximum > max]

        return max, max

print()
print(MinMax([7,2,5,8,4,3,52,13,25]))
print()
