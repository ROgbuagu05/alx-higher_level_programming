#include <stdio.h>
#include <object.h>
#include <listobject.h>
#include <Python.h>
/**
 * print_python_list_info - prints information about a Python list
 * @p: pointer to the Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
