def select_first_base(base_dict):
    while True:
        print("\nSelect a base the integer will be coverted from: ")
        for key, value in base_dict.items():
            print(f"{key}. {value}")
        user_input = input()
        
        for key, value in base_dict.items():
            if user_input == key or user_input == value:
                user_input2 = input(f"\nInput integer to be converted in {value}: ")
                return value, user_input2
            
def select_second_base(base_dict):
    while True:
        print("\nSelect a base the integer will be coverted to: ")
        for key, value in base_dict.items():
            print(f"{key}. {value}")
        user_input = input()
            
        for key, value in base_dict.items():
            if user_input == key or user_input == value:
                return value
    
def coversion(first_base, second_base, integer_to_convert):
    if first_base == 'binary':
        if (isinstance(())):
            pass
    # while True:
    # if first_base == 'binary':
    #     integers = integer_to_convert
    #     for integer in integers:
    #         # print(integer, integers)
    #         if integer <= '1':
    #             pass
    #         else:
    #             print("Integer is not in binary")
    
    
def main():
    base_dict = {"1":"binary", "2":"octal", "3":"decimal", "4":"octaldecimal"}
    first_base, integer_to_be_converted = select_first_base(base_dict)
    second_base = select_second_base(base_dict)
    print(f"{first_base} to {second_base}")
    coversions = coversion(first_base, second_base, integer_to_be_converted)
    
if __name__ == "__main__":
    main()