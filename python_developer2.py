import random

def main():

    input_list = list(map(int, input().split()))

    input_list_len = len(input_list)
    
    prob = [random.randint(0, 10)*0.1 for i in range(input_list_len)] 
    
    while True:
        k = int(input())
        if k <= input_list_len:
            break

    if k == len(input_list):
        print(input_list)
        exit()

    indexes = []
    
    while len(indexes) != k:
        
        random_value = random.randint(0, 10) * 0.1
        
        for key, value in enumerate(prob):
            if random_value <= value and key not in indexes:
                indexes.append(key)
                
    
    result = []
    
    for element in indexes:
        result.append(input_list[element])
    
    print(result)
        

if __name__ == "__main__":
    main()

