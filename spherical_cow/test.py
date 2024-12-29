import unittest
from evol_nums import evol_nums
from evol_nums_prime import evol_nums_prime

class TestEvolNumsPrime(unittest.TestCase):
    def test_reconstruct_c_and_seed(self):
        """Test the reconstruction of c and seed from last three buffer elements."""
        A, B, C, n = 192, 384, 382, 9
        x = 3
        
        # Reverse engineer a valid (c, seed=[x, y]) solution
        c, seed = evol_nums_prime(A, B, C, n, x=x)
        
        # Expected results
        self.assertEqual(c, 2)
        self.assertEqual(seed, [3, 1])

    def test_verification_buffer(self):
        """Verify that the reconstructed (c, seed) reproduces the correct buffer."""
        A, B, C, n = 192, 384, 382, 9
        x = 3
        
        # Reverse engineer a valid (c, seed=[x, y]) solution
        c, seed = evol_nums_prime(A, B, C, n, x=x)
        
        # Run Evol Numbers forward
        buff_check = evol_nums(n, seed, c)
        
        # Verify the last three elements
        self.assertEqual(buff_check[-3:], [192, 384, 382])

class TestEvolNums(unittest.TestCase):
    def test_standard_case(self):
        """Test standard functionality of evol_nums."""
        n = 9
        seed = [3, 1]
        c = 2

        # Expected buffer
        expected_buff = [3, 6, 12, 24, 48, 96, 192, 384, 382]

        # Generate buffer
        buff = evol_nums(n, seed, c)
        self.assertEqual(buff, expected_buff)


if __name__ == "__main__":
    unittest.main()

