#include "Python.h"
#include <structmember.h>
#include "pkyfd.h"

typedef struct {
	PyObject_HEAD
	void* config;
	void* decoder;
} pkyfd_IndexObject;

// create object
static PyObject* pkyfd_Index_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
	pkyfd_IndexObject* self;
	self = (pkyfd_IndexObject*)type->tp_alloc(type, 0);
	if(self == NULL) {
		return PyErr_NoMemory();
	}
	return (PyObject*)self;
}

// destroy object
static PyObject* pkyfd_Index_dealloc(pkyfd_IndexObject* self) 
{
    if( self->decoder != NULL ) {
		destroy_decoder(self->decoder, self->config);
		self->config  = NULL;
		self->decoder = NULL;
    }
	self->ob_type->tp_free((PyObject*) self);
	Py_RETURN_NONE;
}

// corresponds to __init__()
static int pkyfd_Index_init(pkyfd_IndexObject* self, PyObject* args, PyObject* kwds)
{
	if(self != NULL) {
		self->config  = NULL;
		self->decoder = NULL;
	}
	return 0;
}

// methods
static PyObject* init(pkyfd_IndexObject* self, PyObject* args)
{
	int argc;
	char** argv;
	char* config_path;

	if ( !PyArg_ParseTuple(args, "s", &kyfd_path) ) {
		m_error("error : parameter parsing");
		return NULL; // it raises exception in python
	}

	if(self->config == NULL) {
		self->decoder = create_decoder(argc, argv, &self->config);
	} else {
		Py_RETURN_NONE;
	}
	if( self->config == NULL ) {
		m_error("create_decoder() fail");
		return PyErr_NoMemory();
	}

	Py_RETURN_NONE;
}

// methods
static PyObject* analyze( pkyfd_IndexObject *self, PyObject *args )
{
	int					ret;
	char*				in=NULL;
	PyObject* 			py_out;

	if (!PyArg_ParseTuple(args, "s|iiii", &in)) {
		m_error("parameter parsing error");
		return NULL;
	}		
	
	if ( self->config == NULL ) {
		m_error("object isn't initialized yet");
		return NULL;
	}
	if( strlen(in) == 0 ) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	// run_decoder()

	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef pkyfd_Index_methods[] = {
	{"init",           (PyCFunction)init,            METH_VARARGS, "initialize handler"},
	{"analyze",        (PyCFunction)analyze,         METH_VARARGS, "analyze input"},
	{NULL, NULL}
};

static PyMemberDef pkyfd_Index_members[] = {
	{NULL}
};

static PyTypeObject pkyfd_IndexType = {
    PyObject_HEAD_INIT(NULL)
    0,                                  /*ob_size*/
    "pkyfd.Index",                       /*tp_name*/
    sizeof(pkyfd_IndexObject),           /*tp_basicsize*/
    0,                                  /*tp_itemsize*/
    (destructor) pkyfd_Index_dealloc,    /*tp_dealloc*/
    0,                                  /*tp_print*/
    0,                                  /*tp_getattr*/
    0,                                  /*tp_setattr*/
    0,                                  /*tp_compare*/
    0,                                  /*tp_repr*/
    0,                                  /*tp_as_number*/
    0,                                  /*tp_as_sequence*/
    0,                                  /*tp_as_mapping*/
    0,                                  /*tp_hash */
    0,                                  /*tp_call*/
    0,                                  /*tp_str*/
    0,                                  /*tp_getattro*/
    0,                                  /*tp_setattro*/
    0,                                  /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "Index() -> new pkyfd object",             /* tp_doc */
    0,		                                  /* tp_traverse */
    0,		                                  /* tp_clear */
    0,		                                  /* tp_richcompare */
    0,		                                  /* tp_weaklistoffset */
    0,		                                  /* tp_iter */
    0,		                                  /* tp_iternext */
    pkyfd_Index_methods,                       /* tp_methods */
    pkyfd_Index_members,                       /* tp_members */
    0,                                        /* tp_getset */
    0,                                        /* tp_base */
    0,                                        /* tp_dict */
    0,                                        /* tp_descr_get */
    0,                                        /* tp_descr_set */
    0,                                        /* tp_dictoffset */
    (initproc) pkyfd_Index_init,               /* tp_init */
    0,                                        /* tp_alloc */
    pkyfd_Index_new,                           /* tp_new */
};

static PyMethodDef pkyfd_methods[] = {
    {NULL}  /* Sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
initlibpkyfd(void) 
{
    PyObject* m;

    if (PyType_Ready(&pkyfd_IndexType) < 0)
        return;

    m = Py_InitModule3("libpkyfd", pkyfd_methods, "kyfd python wrapper");
    
    if (m == NULL) {
        return;
    }

    Py_INCREF(&pkyfd_IndexType);
    PyModule_AddObject(m, "Index", (PyObject *)&pkyfd_IndexType);
}
