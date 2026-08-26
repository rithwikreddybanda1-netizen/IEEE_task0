#IEEE task 0 Q2

#creating the function to do the tasks on the list
def process_list(numbers):

    new_list=[]

    #making a copy of the original list to avoid modifying it
    new_list = (numbers.copy())

    #removing negative numbers from the list
    for num in new_list:
        if num < 0:
            new_list.remove(num)

    #adding 0 to the end of the list and sorting the list in ascending order
    new_list.append(0)
    new_list.sort()
    return new_list

#getting input of the number of elements
print("Enter the number of elements in the list:")
N=int(input())

original = []
print("Enter the number of elements in the list:")
#filling the list with user input
for i in range(N):
    element = int(input())
    original.append(element)

#calling the function to process the list
result = process_list(original)

#printing the results
print("Original:", original)
print("Result:", result)
        