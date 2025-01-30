import unittest
import numpy as np
from PIL import Image
import os
from pixelkit import Pixel

class TestPixel(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.pixel = Pixel()
        # Create a simple test image
        self.test_array = np.zeros((100, 100, 3), dtype=np.uint8)
        self.test_array[25:75, 25:75] = 255  # White square on black background
        self.test_image = Image.fromarray(self.test_array)
        
        # Save test image temporarily
        self.test_image_path = "test_image.png"
        self.test_image.save(self.test_image_path)
        
        # Test URL for image loading
        self.test_url = "https://raw.githubusercontent.com/rokmr/pypi-utilities/main/tests/test_image.png"

    def tearDown(self):
        """Clean up after each test method"""
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists("output_test.png"):
            os.remove("output_test.png")

    def test_load_from_path(self):
        """Test loading image from file path"""
        result = self.pixel.load(self.test_image_path)
        self.assertIsInstance(result, Pixel)
        self.assertIsInstance(result.image, Image.Image)

    def test_load_from_array(self):
        """Test loading image from numpy array"""
        result = self.pixel.load(self.test_array)
        self.assertIsInstance(result, Pixel)
        self.assertIsInstance(result.image, Image.Image)

    def test_load_from_pil(self):
        """Test loading image from PIL Image"""
        result = self.pixel.load(self.test_image)
        self.assertIsInstance(result, Pixel)
        self.assertIsInstance(result.image, Image.Image)

    def test_load_url(self):
        """Test loading image from URL"""
        result = self.pixel.load_url(self.test_url)
        self.assertIsInstance(result, Pixel)
        self.assertIsInstance(result.image, Image.Image)

    def test_resize(self):
        """Test image resizing"""
        self.pixel.load(self.test_image)
        result = self.pixel.resize(width=50, height=50)
        self.assertEqual(result.image.size, (50, 50))

    def test_canny(self):
        """Test Canny edge detection"""
        self.pixel.load(self.test_image)
        result = self.pixel.canny(threshold1=100, threshold2=200)
        self.assertIsInstance(result, Pixel)
        self.assertIsInstance(result.image, Image.Image)

    def test_save(self):
        """Test saving image"""
        self.pixel.load(self.test_image)
        result = self.pixel.save("output_test.png")
        self.assertTrue(os.path.exists("output_test.png"))
        self.assertIsInstance(result, Pixel)

    def test_chaining(self):
        """Test method chaining"""
        result = (
            self.pixel
            .load(self.test_image)
            .resize(width=50, height=50)
            .canny()
            .save("output_test.png")
        )
        self.assertIsInstance(result, Pixel)
        self.assertTrue(os.path.exists("output_test.png"))

    def test_invalid_image_path(self):
        """Test loading invalid image path"""
        with self.assertRaises(ValueError):
            self.pixel.load("nonexistent_image.jpg")

    def test_invalid_resize_args(self):
        """Test resize with invalid arguments"""
        self.pixel.load(self.test_image)
        with self.assertRaises(ValueError):
            self.pixel.resize(width=None, height=50)

if __name__ == '__main__':
    unittest.main() 