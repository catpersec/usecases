def my_sum(*args):
    sum = 0
    for element in args:
        sum += element
    print(sum)

my_sum(1,2,3,4,5)