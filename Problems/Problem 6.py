def square_sum(nr):
    return (nr*(nr+1)*(2*nr +1))/6
def sum_square(nr):
    return ((nr*(nr +1))/2)**2
print(square_sum(100)-sum_square(100))
