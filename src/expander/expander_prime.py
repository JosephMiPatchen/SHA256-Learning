from src.helper import chunker
from src.utils.utils import bits_to_int, bits_to_ascii_char

def expander_prime(sub_chunks):
    # remove last 48 expanded sub_chunks (signature)
    sub_chunks = sub_chunks[:-48]
    
    # convert sub_chunks into chunk
    chunk = [bit for sublist in sub_chunks for bit in sublist]
    
    # only support size class 1 for now
    # get message
    message = None
    if len(chunk) == 512:
        l_bits = chunk[448:]
        length = bits_to_int(l_bits)
        m_bits = chunk[:length]
        message = "".join([bits_to_ascii_char(byte) for byte in chunker(m_bits,8)])
    else:
        raise NotImplementedError("Does not support message size")
    
    return message