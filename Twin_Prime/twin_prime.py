# Find twin primes up to n number

class TwinPrime:
    # Determine if number is a prime or not
    def is_prime(self, n_value: int) -> bool:
        # If n is divisible by any i, then its not a prime
        for i in range(2, n_value):
            if n_value % i == 0:
                return False
        # If n is not divisible by i, then n is a prime
        return True

    # Find all primes up to n number
    def prime_array(self, n_value: int) -> list[int]:
        prime_list = []

        # Loop through 2 to n number
        for i in range(2, n_value):
            # If i is prime, add to prime list
            if self.is_prime(i):
                prime_list.append(i)
        return prime_list  # Returns list of all prime number up to n

    # Takes list of prime and find prime twins
    def twin_primes(self, prime_list: list[int]) -> list[list[int]]:
        twin_prime_list = []

        # Loop through prime_list length
        for i in range(len(prime_list)):
            # Make sure i is less than length of the array minus 1, otherwise out of bound will occur
            if i < len(prime_list) - 1:
                # Check if current index element plus 2 equals next element in the list, if so, add to twin_prime_list
                if prime_list[i] + 2 == prime_list[i + 1]:
                    twin_prime_list.append([prime_list[i], prime_list[i + 1]])
        return twin_prime_list  # Returns 2d list of all prime twins up to n


def main() -> None:
    number_to_find_prime_twins = int(input("Enter a number you want to find prime twin of: "))
    prime_object = TwinPrime()
    prime_object_list = prime_object.prime_array(number_to_find_prime_twins)
    prime_object_twins_list = prime_object.twin_primes(prime_object_list)
    print(prime_object_twins_list)


if __name__ == "__main__":
    main()
