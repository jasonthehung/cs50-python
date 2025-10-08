import sys


def main():
    # Tuple
    coordinates_tuple = (42.376, -71.115)
    latitude_tuple, longitude_tuple = coordinates_tuple
    print(f"latitude_tuple: {latitude_tuple}")
    print(f"longitude_tuple: {longitude_tuple}")
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")  # less bytes

    # List
    coordinates_list = [42.376, -71.115]
    latitude_list, longitude_list = coordinates_list
    print(f"latitude_list: {latitude_list}")
    print(f"longitude_list: {longitude_list}")
    print(f"{sys.getsizeof(coordinates_list)} bytes")  # more bytes


main()
