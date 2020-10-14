# Modulu
```python
num1=9
num2=4

print(num1/num2) #--> 2.25
print(num1%num2) #--> 1
print(num1-(num1%num2)/num2 )  #--> 2
print((num1/num2)-(num1/num2 %1))  #--> 2
```

### Program to print sum of digit (for 2 digits number)
```python
num=34
print(num%10+(num//10))
```

### Program to print sum of digit (for 3 digits number)
```python
num=342
print(num%10+((num%100)//10)+(num//100))
```

### Program to print sum of digit (for 4 digits number)
```python
num=3421
print(num%10+((num%100)//10)+((num%1000)//100)+(num//1000))
```