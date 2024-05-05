# Function to convert a list of 8 bits into an ASCII character
def bits_to_ascii_char(bits):
    if len(bits) != 8:
        return "Error: List must contain exactly 8 bits."
    ascii_code = bits_to_int(bits)
    return chr(ascii_code)

def bits_to_int(bits):
    return int("".join(str(bit) for bit in bits), 2)