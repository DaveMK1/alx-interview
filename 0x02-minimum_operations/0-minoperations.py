'''The minimum operations coding challenge.
'''


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
