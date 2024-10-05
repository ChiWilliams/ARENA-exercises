import time, functools

def print_all_args(*args,**kwargs):
    for arg in args:
        print(f"arg: {arg}")
    for key, value in kwargs.items():
        print(f"key is {key} and value is {value}")

def time_decarator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"The function took {end_time-start_time} seconds to evalute!")
        return result
    return wrapper

@time_decarator
def find_duplicates(nums: list[int]) -> set[int]:
    return set([num for num in nums if nums.count(num) > 1])

@time_decarator
def fast_find_duplicates(nums: list[int]) -> set[int]:
    seen = set()
    return {num for num in nums if num in seen or seen.add(num)}

@time_decarator
def difficult_operation():
    for x in range(1000):
        for y in range(1000):
            z = x+y
    print("done!")

def zip_and_unzip(nums1: list[int], nums2: list[int]):
    if len(nums1)!=len(nums2):
        raise ValueError("Lists are not of equal length")
    combined = zip(nums1,nums2)
    combined = [(a+b,a*b) for a,b in combined]
    return list(zip(*combined))

def find_prime(nums: list[int]) -> int:
    for num in nums:
        if num == 1:
            continue
        for a in range(2,num):
            if num % a == 0:
                break
        else:
            return num
    else:
        print("No primes here")
        return -1

from collections import defaultdict
def word_occurrence(sentence: str, target: str) -> int:
    words = sentence.lower().split()
    word_dict = defaultdict(lambda: -1)
    for word in words:
        word_dict[word] += 1
    return word_dict[target]

print(word_occurrence("I am a cat cat cat cat cat", "dog"))
#print(find_prime([4,4,8,1]))
#print(zip_and_unzip([1,2,3],[1,2,3]))
#difficult_operation()  
#print(find_duplicates([1,2,3,3]))
# import random
# array = [random.randint(1,20) for _ in range(20000)]
# print(find_duplicates(array))
# print(fast_find_duplicates(array))
