from typing import List

def to_ascii(c): return ord(c)

# convert string to bit list:m 
# byte = 8 bits
def normalize_string_to_bit_list(message):
    charcodes = [to_ascii(c) for c in message]
    bytes = []
    for char in charcodes:
        bytes.append(bin(char)[2:].zfill(8))
        
    bits: List[int] = []
    
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit))
    return bits

def chunker(bits, chunk_length=8):
    chunked = []
    for b in range(0, len(bits), chunk_length):
        chunked.append(bits[b:b+chunk_length])
    return chunked

# LE: add zeros to right
# BE add zero to left
def pad_with_zeros(bits: List[int], length=8, endian='LE'):
    l = len(bits)
    if endian == 'LE':
        for i in range(l, length):
            bits.append(0)
    else: 
        while l < length:
            # insert O(n)?
            bits.insert(0, 0)
            l = len(bits)
    return bits


def message_to_mm_bit_list_chunks(message):
    # get bit list rep of message - var length
    m_bits = normalize_string_to_bit_list(message)
    
    # get the bit list rep of the length of the message bit list
    l = len(m_bits)
    l_bits = [int(b) for b in bin(l)[2:].zfill(64)]
    
    # final preprocess
    if l < 448:
        m_bits.append(1)
        m_bits = pad_with_zeros(m_bits, 448, 'LE')
        m_bits = m_bits + l_bits
        return [m_bits]
    elif 448 <= l <= 512:
        m_bits.append(1)
        m_bits = pad_with_zeros(m_bits, 1024, 'LE')
        m_bits[-64:] = l_bits
        return chunker(m_bits, 512)
    else:
        m_bits.append(1)
        while (len(m_bits)+64) % 512 != 0:
            m_bits.append(0)
        m_bits = m_bits + l_bits
        return chunker(m_bits, 512)


# input: list[hex string]
# output: list[binary list] where binary list is list[int] of length 32 and is padded to left with zeros
#
# example: 
# input: ["0x0f0f","0x0a0a"]
# output: []
def normalize_hex_strings_to_bit_lists(values):
    # int(num_string,string_num_base): converts string rep of hex to int 
    # bin: int -> binary string
    # [2:]: strip the binary literal indicator '0b' from binary string
    binary_strings = [bin(int(v, 16))[2:] for v in values]
    
    # word: fixed size piece of data 
    # 
    words = []
    for binary_string in binary_strings:
        # convert binary_string to list[int]
        word = []
        for bit in binary_string:
            word.append(int(bit))
            
        # pad zeros to left so each word is "32 bits" but the numerical values dont change
        # does big endian actually have meaning here? - would say yes because
        # padding should never change the numerical value of the number and this in order to ensure
        # that you need to know if the buffer is storing the number in big endian or little endian
        words.append(pad_with_zeros(word, 32, 'BE'))
        
    return words

def b2Tob16(value):
  value = ''.join([str(x) for x in value])
  binaries = []
  for d in range(0, len(value), 4):
    binaries.append('0b' + value[d:d+4])
  hexes = ''
  for b in binaries:
    hexes += hex(int(b ,2))[2:]
  return hexes