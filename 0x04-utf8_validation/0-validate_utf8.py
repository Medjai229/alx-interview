#!/usr/bin/python3

def validUTF8(data):

    number_of_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_n_bytes = 1 << 7 

        if number_of_bytes == 0:

            while mask_n_bytes & i:
                number_of_bytes += 1
                mask_n_bytes = mask_n_bytes >> 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
            
        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False
            
        number_of_bytes -= 1

    if number_of_bytes == 0:
        return True
    
    return False