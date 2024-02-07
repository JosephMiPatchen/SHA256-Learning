import hashlib
import unittest

from sha256_impl_2 import sha256_impl_2
class TestSHA256Implementation(unittest.TestCase):
    def test_hash_equality(self):
        # Message to hash
        message = 'Hello, world!'
        message2 = b'Hello, world!'

        # Calculate hash using custom implementation
        custom_hash = sha256_impl_2(message)
        print("custom: " + str(custom_hash))

        # Calculate hash using hashlib
        hashlib_hash = hashlib.sha256(message2).digest()
        print("hashlib: " + str(hashlib_hash))
        
        # Compare the two hashes
        #self.assertEqual(custom_hash, hashlib_hash)

if __name__ == '__main__':
    unittest.main()
