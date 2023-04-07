#include <Python.h>

void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode = (PyUnicodeObject *)p;

    if (!PyUnicode_Check(p)) {
        printf("TypeError: Can only print Python strings\n");
        return;
    }

    printf("%ls\n", unicode->str);
    printf("  size: %ld\n", PyUnicode_GET_SIZE(unicode));
    printf("  address: %p\n", (void *)p);
}
