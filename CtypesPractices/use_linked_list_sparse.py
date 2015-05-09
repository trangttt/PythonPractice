import ctypes

lib = ctypes.cdll.LoadLibrary('linked_list_sparse.dylib')

class double_row_element(ctypes.Structure):
    pass

double_row_element._fields_= [("value", ctypes.c_double),
                                ("col_index", ctypes.c_int),
                                ("next_element", ctypes.POINTER(double_row_element))
                                ]

class double_sparse_matrix(ctypes.Structure) :
    _fields_ = [("nrows", ctypes.c_int),
                  ("ncols", ctypes.c_int),
                  ("nnz", ctypes.c_int),
                  ("rows", ctypes.POINTER(ctypes.POINTER(double_row_element)))
                  ]


double_sparse_pointer = ctypes.POINTER(double_sparse_matrix)

initialize_matrix = lib.initialize_matrix
initialize_matrix.restype = double_sparse_pointer
initialize_matrix.argtypes = [ctypes.c_int, ctypes.c_int]

free_matrix = lib.free_matrix
free_matrix.restype = ctypes.c_int
free_matrix.argtypes = [double_sparse_pointer]

set_value = lib.set_value
set_value.restype = ctypes.c_int
set_value.argtypes = [double_sparse_pointer, ctypes.c_int, ctypes.c_int, ctypes.c_double]


get_value = lib.get_value
get_value.restype = ctypes.c_double
get_value.argtypes = [double_sparse_pointer, ctypes.c_int, ctypes.c_int]



m = double_sparse_pointer()

m = initialize_matrix(ctypes.c_int(10), ctypes.c_int(10))

set_value(m, ctypes.c_int(4), ctypes.c_int(4), ctypes.c_double(5.0))
a  = get_value(m, ctypes.c_int(4), ctypes.c_int(4))

print a
#print m.contents.nrows

free_matrix(m)

class chair_t(ctypes.Structure):
    _fields_ = [
        ("leg", ctypes.c_int),
        ("seat", ctypes.c_int)
    ]

c_object_p = ctypes.POINTER(ctypes.c_void_p)

get_a_void_chair = lib.get_a_void_chair
get_a_void_chair.restype = c_object_p

get_a_real_chair = lib.get_a_real_chair
get_a_real_chair.restype = ctypes.POINTER(chair_t)


a_chair = get_a_real_chair()
print a_chair.contents.seat, " ", a_chair.contents.leg

a_void_chair = get_a_void_chair()
b = ctypes.cast(a_void_chair, ctypes.POINTER(chair_t))

print b.contents.seat, " ", b.contents.leg



