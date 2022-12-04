#include <stdio.h>
#include <stdlib.h>
#include <objects.h>
#include <listobjects.h>
void print_python_list_info(PyObject *p)
{
	ssize_t i = PyList_Size(p);
	for (j = 0, j < i; j++)
		printf("%s", PyList_GetItem(p, i))
}
