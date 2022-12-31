# 0x03-PYTHON_DATA_STRUCTURES

Can I hear you scream :scream:. For some of us who are just coming from the rigours of C, here is your liberations.</br>In thi srepo, we are first introduced to data structures which can be as elegant as ``dictionaries``  or as large as the ``int`` ***no offense to C though***

## FILES :scroll:

There are different files, both C and python, Below are some of the files in this directory :open_file_folder:

### **Header Files** :punch:

[lists.h](./lists.h): IT contains the function prototypes for the functions in the file ``13-is_palindrome.c``

## ***C***

|**FILE**|**FUNCTION**|**ACTION**|
|:---|:---:|---:|
|[13-is_palindrome.c](./13-is_palindrome.c)|``listint_t *reverse_listint(listint_t **head)``</br>``int is_palindrome(listint_t **head)``|* It reverses a single linked list</br>It checks if a linked list is a palindrome|
|[100-print_python_list_info.c](./100-print_python_list_info.c)|``void print_python_list_info(PyObject *p)``|It uses C to print information about a python list</br>This function can then be called in Python|

## ***PYTHON***

|**FILE**|**FUNCTION**|**ACTION**|
|:---|:---:|---:
|[0-print_list_integer.py](./0-print_list_integer.py)|``def print_list_integer(my_list=[]):``|Prints all the members of a list of integers|
|[1-element_at.py](./1-element_at.py)|``def element_at(my_list, idx):``|It returns the element at a particular index|
|[2-replace_in_list.py](./2-replace_in_list.py)|``def replace_in_list(my_list, idx, element):``|It returns the element at a particular index|
|[3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)|``def print_reversed_list_integer(my_list=[]):``|It prints a list of integers in reverse|
|[4-new_in_list.py](./4-new_in_list.py)|``def new_in_list(my_list, idx, element):``|It replaces an elemt at a given index without modifying the original list, thus in essence creating a new list|
|[5-no_c.py](./5-no_c.py)|``def no_c(my_string):``|It removes all instances of C from astring without modifying the original string|
|[6-print_matrix_integer.py](./6-print_matrix_integer.py||``def print_matrix_integer(matrix=[[]]):``|It prints out a matrix of integers|
|[7-add_tuple.py](./7-add_tuple.py)|``def add_tuple(tuple_a=(), tuple_b=()):``|It adds up a tuple|
|[8-multiple_returns.py](./8-multiple_returns.py)|``def multiple_returns(sentence):``|It returns the lenght of a string and its initial character|
|[9-max_integer.py](./9-max_integer.py)|``def max_integer(my_list=[]):``|It returns the maximum integer in a list of numbers|
|[10-divisible_by_2.py](./10-divisible_by_2.py)|``def divisible_by_2(my_list=[]):``|It returns a list which tells us if the value at the index of the original string is divisible by 2 or not|
|[11-delete_at.py](./11-delete_at.py)|``def delete_at(my_list=[], idx=0):``|It deletes the element of a list at a specified index|
|[12-switch.py](./12-switch.py)||It swaps the values of two variables|
