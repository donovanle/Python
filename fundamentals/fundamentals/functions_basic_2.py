# Countdown
def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    print(new_list)
countdown(5)

# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#First Plus lenght
def first_plus_lenght(list):
    sum = list[0] + len(list)
    return sum
print(first_plus_lenght([1,2,3,4,5]))

#Value gReater than 2nd

def greater_than(list):
    list_two = []
    if len(list) < 2:
        return False
    else:
        for i in range(0, len(list)):
            if list[i] > list[1]:
                list_two.append(list[i])
        print(len(list_two))
        return list_two

print(greater_than([5,2,3,2,1 ,4]))
print(greater_than([3]))

#This Length 

def this_length(num1 , num2):           #num 1 equals lenght num 2 equals each number
    num_list = []
    for i in range(0, num1):
        num_list.append(num2)
    return num_list

print(this_length(4,7))
print(this_length(6,2))
