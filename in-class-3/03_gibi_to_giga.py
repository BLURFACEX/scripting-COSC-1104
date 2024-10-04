# Author: Kshitiz Pal, Sahil Patel
# Date: 2024/10/4
# Description: creating function gibi_to_giga and giga_to_gibi which will convert the values of gibi_bytes to giga_bytes and vice versa.


def gibi_to_giga(gibibytes):
    gigabytes = gibibytes * (1_073_741_824 / 1_000_000_000)  # Conversion calculation
    return gigabytes  # Return the converted value
def giga_to_gibi(gigabytes):
    gibibytes = gigabytes * (1_000_000_000 / 1_073_741_824)  # Conversion calculation
    return gibibytes  # Return the converted value

# Example usage
if __name__ == "__main__":
    gibibytes_in = 0.931323  # You can change this value to test with different Gibibytes
    gigabytes_result = gibi_to_giga(gibibytes_in)
    print(f"{gibibytes_in} GiB is equal to {gigabytes_result:.6f} GB.")


    gigabyt_in = 1  # You can change this value to test with different Gigabytes
    gibibytes_result = giga_to_gibi(gigabyt_in)
    print(f"{gigabyt_in} GB is equal to {gibibytes_result:.6f} GiB.")
