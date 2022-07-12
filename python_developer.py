import random

def main():

    input_list = list(map(int, input().split()))

    input_list_len = len(input_list)
    
    while True:
        k = int(input())
        if k <= input_list_len:
            break

    if k == len(input_list):
        print(input_list)
        exit()

    input_list_copy = input_list[:]
    result = []

    for i in range(k):
        list_len = len(input_list_copy)
        index = random.randint(0, (list_len - 1))
        result.append(input_list_copy[index])
        del input_list_copy[index]
    
    print(result)
    
if __name__ == "__main__":
    main()
