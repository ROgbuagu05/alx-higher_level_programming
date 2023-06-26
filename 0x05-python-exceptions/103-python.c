#include <Python.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Invalid PyListObject\n");
		return;
	}
	
	Py_ssize_t size = PyList_Size(p);
	
	printf("[*] Python list info\n");
	printf("[*] Size of the list = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *itemType = Py_TYPE(item)->tp_name;
		
		printf("Element %ld: %s\n", i, itemType);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Invalid PyBytesObject\n");
		return;
	}
	
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t maxBytes = (size < 10) ? size : 10;
	
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", maxBytes);
	
	for (Py_ssize_t i = 0; i < maxBytes; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		
		if (i != maxBytes - 1)
		{
			printf(" ");
		}
	}
	
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Invalid PyFloatObject\n");
		return;
	}
	
	double value = PyFloat_AsDouble(p);
	
	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}

