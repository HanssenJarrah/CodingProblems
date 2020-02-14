"""
The gen_primes function has been sourced from (and implementation of the Sieve of Erastothenes):
https://stackoverflow.com/questions/567222/simple-prime-generator-in-python
"""


def gen_primes(maximum):
    """
    Generates a sequence of prime numbers less then or equal to 'maximum.'
    Can be made infinite simply by using, "while True" instead.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while q <= maximum:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def main():
    # gen_primes() is a generator not a function and is therefore called using a loop
    for prime in gen_primes(100):
        print(prime, end=" ")


if __name__ == "__main__":
    main()
