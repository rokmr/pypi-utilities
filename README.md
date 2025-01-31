<div align="center">
  <img src="assets/pixelkit.png" alt="Pixelkit Logo" width="200"/>
  <h1>Pixelkit</h1>
</div>

# Pixelkit 🎨

A powerful and intuitive Python library for image processing, built on top of PIL, OpenCV, and NumPy. Pixelkit provides a fluent interface for common image operations with an emphasis on elegance and ease of use.

## ✨ Features

- 🖼️ **Versatile Image Loading**
  - Load from files, URLs, base64 strings, or NumPy arrays
  - Built-in error handling and format validation
  - Automatic format detection

- 🔄 **Format Conversions** 
  - Seamless conversion between PIL, NumPy, base64, and tensor formats
  - Preserve image quality during conversions
  - Type-safe operations

- 🎨 **Image Processing**
  - Enhancement: sharpen, blur, denoise, dehaze
  - Geometric: resize, rotate, flip, crop
  - Analysis: histograms, edge detection, Canny edge detection
  - Filters: bilateral, Gaussian, median, Gabor

- 📊 **Advanced Operations**
  - Frequency domain processing (FFT)
  - Convolution and deconvolution
  - Image segmentation
  - Super-resolution

## 🚀 Installation

```bash
pip install pixelkit
```

## 🎯 Quick Start

```python
from pixelkit import Pixel

# Load and process an image with method chaining
processed = (
    Pixel.load("input.jpg")
    .resize(width=800, height=600)
    .enhance()
    .to_grayscale()
    .canny(threshold1=100, threshold2=200)
    .save("output.jpg")
)

# Load from URL
image = Pixel.load_url("https://example.com/image.jpg")

# Load from base64
image = Pixel.load_base64(base64_string)
```

## 📚 Documentation

### Basic Operations

```python
# Image properties
image.width    # Get image width
image.height   # Get image height
image.channels # Get number of channels
image.mode     # Get color mode
image.format   # Get image format

# Geometric transformations
image.resize(width=400, height=300)
image.rotate(angle=45)
image.horizontal_flip()
image.vertical_flip()
image.crop(bbox=(x1, y1, x2, y2))

# Enhancement
image.enhance()
image.sharpen()
image.denoise()
image.dehaze()

# Analysis
image.histogram()
image.edge_detection()
image.canny(threshold1=100, threshold2=200)
```

### Advanced Features

```python
# Filters
image.bilateral_filter()
image.gaussian_filter()
image.median_filter()
image.gabor_filter()

# Frequency domain
image.fft()
image.ifft()
image.lpf()  # Low-pass filter
image.hpf()  # High-pass filter

# Segmentation
image.segment()
image.binary_threshold()
image.otsu_threshold()
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## 🙏 Acknowledgments

Built with ❤️ using:
- 🖼️ PIL (Python Imaging Library)
- 🎥 OpenCV
- 🔢 NumPy

### ✨ Contributors

-  [avnCode](https://github.com/avnCode)
-  [rokmr](https://github.com/rokmr)

Want to contribute? Join our growing community! 🌟