from operator import length_hint


def Find_s_smallest_s_largest(lst):
    length = len(lst)
    lst.sort()
    print("LARGEST ELEMET",lst[length-1])
    print("SMALLEST ELEMENT",lst[0])
    print("SECOND LARGEST IS",lst[length-2])
    print("SECOND SMALLEST IS ",lst[1])

array=[10,20,30,40,50]
Find_s_smallest_s_largest(array)