def main():
    i = 2
    while True:
        if check_prime(i) != -1:
            mersenne_prime(check_prime(i))
        i+=1

#function to generate mersenne prime 
def mersenne_prime(n):
    print((2**n) - 1)

#function to check if said number is prime 
def check_prime(n):
    is_prime = 1
    if n == 2:
        is_prime =1
    elif n == 3:
        is_prime = 1
    else:
        i = 2
        while i <= int(n**0.5):
            if n % i == 0 :
                is_prime = 0
                break
            i=i+1
    if is_prime == 1:
        return n
    else:
        return -1
main()
