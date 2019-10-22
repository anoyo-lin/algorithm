def search(array, l, r, target):
    if l == target:
        return l
    if r == target:
        return r

    if l == r:
        return -1

    return search(array, l+1, r-1, target)


search a target in an unsorted array
