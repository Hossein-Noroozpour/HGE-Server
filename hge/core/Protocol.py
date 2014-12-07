__author__ = 'Hossein Noroozpour'

id_size = 4


def get_id(data):
    user_id = data[0]
    for i in range(1, id_size):
        user_id += (data[i] << (8 * i))
    return user_id