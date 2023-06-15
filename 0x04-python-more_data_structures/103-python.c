#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_list - Print list information
 * @p: Python Object
 * Return: No return
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: p is not a valid PyListObject\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (int i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
/**
 * print_python_bytes - Print bytes information
 * @p: Python Object
 * Return: No return
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: p is not a valid PyBytesObject\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);
	for (int i = 0; i < (PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10); i++)
	{
		printf("%02x%c", (unsigned char)PyBytes_AsString(p)[i], i == 9 ? '\n' : ' ');
	}
}
