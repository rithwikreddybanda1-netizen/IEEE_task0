#IEEE task 0 Q1

#Getting input of the numbeer of elements and the elements of the list from the user
print("Enter the number of elements in the list:")
N = int(input())
print("Enter the elements of the list:")

#initializing an empty list to store the elements
list1 = []

#filling the list with user input
for i in range(N):
    element = int(input())
    list1.append(element)

#declaring variables to store the smallest and largest numbers, sum of even and odd numbers, and the reversed list
smallest_num=list1[0]
largest_num=list1[0]
even_sum=0
odd_sum=0
list_rev=[]

#finding the smallest and largest numbers, and calculating the sum of even and odd numbers and creating the reversed list
for i in range(N):
    
    if list1[i] < smallest_num:
        smallest_num = list1[i]
    if list1[i] > largest_num:
        largest_num = list1[i]
    if list1[i] % 2 == 0:
        even_sum += list1[i]   
    else:
        odd_sum += list1[i]

    list_rev.append(list1[N-i-1])

#printing the results
print("Smallest number:", smallest_num)
print("Largest number:", largest_num)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Reversed list:", list_rev)