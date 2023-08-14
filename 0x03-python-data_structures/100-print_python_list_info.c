#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - prints information about a Python list object
 * @python_list: pointer to a PyObject of PyListObject type
 *
 * Return: always void.
 */
void print_python_list_info(PyObject *python_list)
{
	PyListObject *py_list = NULL;
	ssize_t list_size = 0;
	ssize_t index = 0;
	const char *element_type = NULL;

	list_size = PyList_Size(python_list);
	py_list = (PyListObject *)python_list;
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));

	while (index < list_size)
	{
		element_type = Py_TYPE(py_list->ob_item[index])->tp_name;
		printf("Element %ld: %s\n", index, element_type);
		index++;
	}
}
