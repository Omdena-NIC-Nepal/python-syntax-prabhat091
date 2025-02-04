def format_string(name, age):

    return f"My name is {name} and I am {age} years old"

def conditional_check(number):

    if(number > 10):
        return "Greater"
    elif(number < 10):
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):

    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum
        

def list_operations(numbers):

    return (sum(numbers), max(numbers), min(numbers))

def dict_operations(students_dict):

    top_students = []
    
    for name, marks in students_dict.items():
        if(marks > 80):
            top_students.append(name)
    
    return top_students


def set_operations(list1, list2):

    return list1.intersection(list2)

def arithmetic_ops(a, b):

    return {
        "add": a + b,
        "subtract": a - b,
        "product": a * b,
        }

def logical_ops(x, y):

    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }

def bitwise_ops(a, b):

    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }
