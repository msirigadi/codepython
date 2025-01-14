"""
At the beginning of the serialization module, we mentioned that serialized
objects could be persisted in a database or sent via a network. This implies
another two functions corresponding to the pickle.dumps() and pickle.loads()
functions:

- pickle.dumps(object_to_be_pickled) – expects an initial object, returns a
byte object. This byte object should be passed to a database or network driver
to persist the data;
- pickle.loads(bytes_object) – expects the bytes object, returns the initial
object.
"""

import pickle

a_list = ['a', 123, [10, 100, 1000]]

bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you
# can deserialize it
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)