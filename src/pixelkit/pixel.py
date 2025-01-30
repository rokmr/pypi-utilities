import requests
from PIL import Image
import cv2
import io
import warnings
from typing import Optional, Union
import numpy as np
from urllib.parse import urlparse
from decorators import image_loader, image_operation, required_args

#TODO: Add basic image properties, and operations, decorators

class Pixel():
    def __init__(self):
        self.image = None

    @image_loader
    def load(self, image: Union[str, np.ndarray, Image.Image]) -> 'Pixel':
        """
        Load an image from a file, numpy array, or PIL Image object.
        Returns self for method chaining.

        Args:
            image (Union[str, np.ndarray, Image.Image]): The image to load. Can be:
                - A string path to an image file
                - A numpy array containing image data
                - A PIL Image object

        Returns:
            Pixel: The loaded Pixel object.

        Raises:
            ValueError: If the input type is invalid or if loading fails
            FileNotFoundError: If the image file is not found
            IOError: If there is an error reading the image file

        Examples:
            >>> # Load from file
            >>> img = load_image('path/to/image.jpg')
            >>> # Load from numpy array
            >>> img = load_image(np.array([...]))
            >>> # Load from PIL Image
            >>> img = load_image(Image.open('image.jpg'))
        """
        try:
            if isinstance(image, str):
                return Image.open(image)
            elif isinstance(image, np.ndarray):
                # Handle numpy arrays with values in [0, 1] range
                if image.dtype == np.float32 or image.dtype == np.float64:
                    if np.min(image) >= 0 and np.max(image) <= 1:
                        image = (image * 255).astype(np.uint8)
                # Handle numpy arrays with values in [0, 255] range
                elif image.dtype == np.uint8:
                    pass
                else:
                    raise ValueError("Numpy array must be uint8 (0-255) or float (0-1)")
                return Image.fromarray(image)
            elif isinstance(image, Image.Image):
                return image
            else:
                raise ValueError(f"Invalid image type: {type(image)}. Expected str, numpy.ndarray, or PIL.Image.Image")
        except (FileNotFoundError, IOError) as e:
            raise ValueError(f"Failed to load image file: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error loading image: {str(e)}")
        
    
    @image_loader
    def load_url(self, url: str, verify_ssl: bool = True) -> 'Pixel':
        """
        Download an image from a URL.
        Returns self for method chaining.

        Args:
            url (str): The URL of the image to download
            verify_ssl (bool): Whether to verify SSL certificates. Default is True.
                Set to False only if you trust the source and are having SSL issues.

        Returns:
            Pixel: The loaded Pixel object.

        Raises:
            ValueError: If the URL is invalid
            requests.exceptions.RequestException: If the download fails
            PIL.UnidentifiedImageError: If the downloaded data is not a valid image

        Examples:
            >>> img = image_from_url('https://example.com/image.jpg')
            >>> if img is not None:
            >>>     print(f"Image size: {img.size}")
            >>>     print(f"Image mode: {img.mode}")
        """
        # Validate URL
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Invalid URL format")
        except Exception as e:
            raise ValueError(f"Invalid URL: {str(e)}")

        try:
            # Show warning if SSL verification is disabled
            if not verify_ssl:
                warnings.warn(
                    "SSL verification is disabled. This is not recommended for security reasons.",
                    UserWarning
                )

            # Download the image
            response = requests.get(url, verify=verify_ssl, timeout=10)
            response.raise_for_status()

            # Convert to PIL Image
            img = Image.open(io.BytesIO(response.content))
            
            return img

        except requests.exceptions.SSLError:
            warnings.warn(
                "SSL verification failed. Try setting verify_ssl=False if you trust the source.",
                UserWarning
            )
            return None
        except requests.exceptions.RequestException as e:
            warnings.warn(f"Failed to download image: {str(e)}", UserWarning)
            return None
        except Exception as e:
            warnings.warn(f"Error processing image: {str(e)}", UserWarning)
            return None
    
    @image_loader
    def load_base64(self, base64: str) -> 'Pixel':
        """
        Load an image from a base64 encoded string.
        Returns self for method chaining.
        """
        try:
            img = Image.open(io.BytesIO(base64.decode('base64')))
            return img
        except Exception as e:
            warnings.warn(f"Error processing image: {str(e)}", UserWarning)
            return None
        
    @image_operation
    def canny(self, threshold1: int = 100, threshold2: int = 200) -> 'Pixel':
        """
        Apply Canny edge detection to the image.
        Returns self for method chaining.
        """
        # Convert PIL Image to numpy array
        img_array = np.array(self.image)
        # Apply Canny edge detection
        edges = cv2.Canny(img_array, threshold1, threshold2)
        # Convert back to PIL Image
        return Image.fromarray(edges)
    
    @image_operation
    @required_args
    def resize(self, width: int, height: int) -> 'Pixel':
        """
        Resize the image to the specified width and height.
        width: Change in x-axis dimension
        height: Change in y-axis dimension
        Returns self for method chaining.
        """
        self.image = self.image.resize((width, height))
        return self
    
    @image_operation
    def save(self, path: str) -> 'Pixel':
        """
        Save the image to the specified path.
        Returns self for method chaining.
        """
        self.image.save(path)
        return self 
    
    @image_operation
    def show(self) -> 'Pixel':
        """
        Display the image.
        Returns self for method chaining.
        """
        self.image.show()
        return self