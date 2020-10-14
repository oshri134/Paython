## Link to good exams online
https://www.codequizzes.com/python
(Note: this part is not included: https://www.codequizzes.com/python/beginner-III/sets)

## Exercise 1
* Create a python program that gets from the user a number as an input and prints the first elements of the Fibonacci numbers

for example:
```
Enter a number: 4

0 1 1 2
```

```
Enter a number: 9

0 1 1 2 3 5 8 13 21
```

## Result
```python
def fibonacci(amount):
    first=0
    second=1
    print(first,second,end=" ")
    for x in range(2,amount):
        temp=second
        second+=first
        first=temp
        print(second,end=" ")




fibonacci(4)
print()
fibonacci(9)
print()
```

output:
```
0 1 1 2 
0 1 1 2 3 5 8 13 21 
```
## Exercise 2
* given the following list:
```
["apple","applep","Orange","Banana"]
```
* get from the user a string as input
* print the index of the element that contains the given input - the highest times

```
Enter string: ab
output: 2 or 0

Enter string: abc
output: 0
```

## Result
```python
def get_count(my_str,my_search):
    appear_counter=0
    counter=0

    while counter< len(my_str):
        if my_str[counter]==my_search[0] and counter+len(my_search)-1 < len(my_str): 
            inner_counter=0   
            for inner_counter in range(0,len(my_search)):
                if my_str[counter+inner_counter]!=my_search[inner_counter]:
                    break
                
            if inner_counter==len(my_search)-1:
                appear_counter+=1
                counter+=len(my_search)
            else:
                counter+=1
        else:
            counter+=1
    return appear_counter



arr=["apple","applep","Orange","Banana"]
search_str=input("Please enter a string: ")

counter=0
max_index=0

for counter in range(0,len(arr)):
    if get_count(arr[counter],search_str) > get_count(arr[max_index],search_str):
        max_index=counter


print("end of program", max_index)

```


# Exercise 3
Sudoku Game - in Python
* Create a matrix 9X9 
* Run in a loop 
  * ask the user if he wants to exit the loop
    * if the user enters `Y` - break the loop
    * else - ask the user for:
      * `column index` 
      * `row index`
      * number to insert into this element in the matrix
* After the loop print to the user the natrix according to his input.   
For example:



```
Do you want to exit (Y/N) ? N

Enter row index: 4
Enter col index: 6
Enter element content: 9
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 0
Enter col index: 6
Enter element content: 4
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 8
Enter col index: 5
Enter element content: 6
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 3
Enter col index: 5
Enter element content: 7
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 0
Enter col index: 5
Enter element content: 2
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 5
Enter col index: 4
Enter element content: 8
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 3
Enter col index: 3
Enter element content: 1
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 4
Enter col index: 2
Enter element content: 5
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 7
Enter col index: 1
Enter element content: 1
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 4
Enter col index: 0
Enter element content: 3
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 1
Enter col index: 0
Enter element content: 7
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 0
Enter col index: 0
Enter element content: 8
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 1
Enter col index: 8
Enter element content: 9
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 3
Enter col index: 8
Enter element content: 2
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 6
Enter col index: 7
Enter element content: 7
-------------------
Do you want to exit (Y/N) ? N

Enter row index: 8
Enter col index: 7
Enter element content: 4
-------------------
Do you want to exit (Y/N) ? Y
```
The output is:
```
8 . . |. . 2 |4 . . 
7 . . |. . . |. . 9 
. . . |. . . |. . . 
------+------+------
. . . |1 . 7 |. . 2 
3 . 5 |. . . |9 . . 
. . . |. . . |. . . 
------+------+------
. . . |. 8 . |. 7 . 
. 1 . |. . . |. . . 
. . . |. . 6 |. 4 . 
```
* Add an algorithm that will fill the sudoku matrix. and then print the solved result.    
For example, to the above input, print:
```
8 5 9 |6 1 2 |4 3 7 
7 2 3 |8 5 4 |1 6 9 
1 6 4 |3 7 9 |5 2 8 
------+------+------
9 8 6 |1 4 7 |3 5 2 
3 7 5 |2 6 8 |9 1 4 
2 4 1 |5 9 3 |7 8 6 
------+------+------
4 3 2 |9 8 1 |6 7 5 
6 1 7 |4 2 5 |8 9 3 
5 9 8 |7 3 6 |2 4 1 
```
* Note: add validation chcking to the user input:
  * `row index` - can be only between 0-8
  * `col index` - can be only between 0-8
  * `element content` - can be only a number between 0-9 that does not appear in the col or row of the selected element, or in the inner 3X3 matrix that contains this element 
  
  
  
#### Good luck!!


