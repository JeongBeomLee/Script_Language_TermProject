#include <Python.h>

int compare_info_calories(const void* a, const void* b, void* list) {
    PyObject* dict_a = PyList_GetItem(list, *(Py_ssize_t*)a);
    PyObject* dict_b = PyList_GetItem(list, *(Py_ssize_t*)b);

    PyObject* calories_a = PyDict_GetItemString(dict_a, "INFO_FAT");
    PyObject* calories_b = PyDict_GetItemString(dict_b, "INFO_FAT");

    double val_a = PyFloat_AsDouble(calories_a);
    double val_b = PyFloat_AsDouble(calories_b);

    if (val_a < val_b)
        return -1;
    else if (val_a > val_b)
        return 1;
    else
        return 0;
}

static PyObject* spam_sortByCalories(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    Py_ssize_t length = PyList_Size(list);
    Py_ssize_t* indices = (Py_ssize_t*)malloc(length * sizeof(Py_ssize_t));
    for (Py_ssize_t i = 0; i < length; i++) {
        indices[i] = i;
    }
    qsort(indices, length, sizeof(Py_ssize_t), compare_info_calories, list);

    PyObject* result = PyList_New(length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyList_SetItem(result, i, PyLong_FromSsize_t(indices[i]));
    }
    free(indices);

    return result;
}

int compare_info_car(const void* a, const void* b, void* list) {
    PyObject* dict_a = PyList_GetItem(list, *(Py_ssize_t*)a);
    PyObject* dict_b = PyList_GetItem(list, *(Py_ssize_t*)b);

    PyObject* car_a = PyDict_GetItemString(dict_a, "INFO_FAT");
    PyObject* car_b = PyDict_GetItemString(dict_b, "INFO_FAT");

    double val_a = PyFloat_AsDouble(car_a);
    double val_b = PyFloat_AsDouble(car_b);

    if (val_a < val_b)
        return -1;
    else if (val_a > val_b)
        return 1;
    else
        return 0;
}

static PyObject* spam_sortByCar(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    Py_ssize_t length = PyList_Size(list);
    Py_ssize_t* indices = (Py_ssize_t*)malloc(length * sizeof(Py_ssize_t));
    for (Py_ssize_t i = 0; i < length; i++) {
        indices[i] = i;
    }
    qsort(indices, length, sizeof(Py_ssize_t), compare_info_car, list);

    PyObject* result = PyList_New(length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyList_SetItem(result, i, PyLong_FromSsize_t(indices[i]));
    }
    free(indices);

    return result;
}

int compare_info_pro(const void* a, const void* b, void* list) {
    PyObject* dict_a = PyList_GetItem(list, *(Py_ssize_t*)a);
    PyObject* dict_b = PyList_GetItem(list, *(Py_ssize_t*)b);

    PyObject* pro_a = PyDict_GetItemString(dict_a, "INFO_FAT");
    PyObject* pro_b = PyDict_GetItemString(dict_b, "INFO_FAT");

    double val_a = PyFloat_AsDouble(pro_a);
    double val_b = PyFloat_AsDouble(pro_b);

    if (val_a < val_b)
        return -1;
    else if (val_a > val_b)
        return 1;
    else
        return 0;
}

static PyObject* spam_sortByPro(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    Py_ssize_t length = PyList_Size(list);
    Py_ssize_t* indices = (Py_ssize_t*)malloc(length * sizeof(Py_ssize_t));
    for (Py_ssize_t i = 0; i < length; i++) {
        indices[i] = i;
    }
    qsort(indices, length, sizeof(Py_ssize_t), compare_info_pro, list);

    PyObject* result = PyList_New(length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyList_SetItem(result, i, PyLong_FromSsize_t(indices[i]));
    }
    free(indices);

    return result;
}

int compare_info_fat(const void* a, const void* b, void* list) {
    PyObject* dict_a = PyList_GetItem(list, *(Py_ssize_t*)a);
    PyObject* dict_b = PyList_GetItem(list, *(Py_ssize_t*)b);

    PyObject* fat_a = PyDict_GetItemString(dict_a, "INFO_FAT");
    PyObject* fat_b = PyDict_GetItemString(dict_b, "INFO_FAT");

    double val_a = PyFloat_AsDouble(fat_a);
    double val_b = PyFloat_AsDouble(fat_b);

    if (val_a < val_b)
        return -1;
    else if (val_a > val_b)
        return 1;
    else
        return 0;
}

static PyObject* spam_sortByFat(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    Py_ssize_t length = PyList_Size(list);
    Py_ssize_t* indices = (Py_ssize_t*)malloc(length * sizeof(Py_ssize_t));
    for (Py_ssize_t i = 0; i < length; i++) {
        indices[i] = i;
    }
    qsort(indices, length, sizeof(Py_ssize_t), compare_info_fat, list);

    PyObject* result = PyList_New(length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyList_SetItem(result, i, PyLong_FromSsize_t(indices[i]));
    }
    free(indices);

    return result;
}

int compare_info_na(const void* a, const void* b, void* list) {
    PyObject* dict_a = PyList_GetItem(list, *(Py_ssize_t*)a);
    PyObject* dict_b = PyList_GetItem(list, *(Py_ssize_t*)b);

    PyObject* na_a = PyDict_GetItemString(dict_a, "INFO_NA");
    PyObject* na_b = PyDict_GetItemString(dict_b, "INFO_NA");

    double val_a = PyFloat_AsDouble(na_a);
    double val_b = PyFloat_AsDouble(na_b);

    if (val_a < val_b)
        return -1;
    else if (val_a > val_b)
        return 1;
    else
        return 0;
}

static PyObject* spam_sortByNa(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    Py_ssize_t length = PyList_Size(list);
    Py_ssize_t* indices = (Py_ssize_t*)malloc(length * sizeof(Py_ssize_t));
    for (Py_ssize_t i = 0; i < length; i++) {
        indices[i] = i;
    }
    qsort(indices, length, sizeof(Py_ssize_t), compare_info_na, list);

    PyObject* result = PyList_New(length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyList_SetItem(result, i, PyLong_FromSsize_t(indices[i]));
    }
    free(indices);

    return result;
}

static PyMethodDef SpamMethods[] = {
    {"sortByCalories", spam_sortByCalories, METH_VARARGS, "Sort recipes by calories"},
    {"sortByCar", spam_sortByCar, METH_VARARGS, "Sort recipes by carbohydrate"},
    {"sortByPro", spam_sortByPro, METH_VARARGS, "Sort recipes by protein"},
    {"sortByFat", spam_sortByFat, METH_VARARGS, "Sort recipes by fat"},
    {"sortByNa", spam_sortByNa, METH_VARARGS, "Sort recipes by Na"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    "It is test module.",
    -1,
    SpamMethods
};

PyMODINIT_FUNC PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
