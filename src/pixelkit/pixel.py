import requests
from PIL import Image
import io
import warnings
from typing import Optional, Union
import numpy as np
from urllib.parse import urlparse

#TODO: Add basic image properties, and operations
class Pixel():
    def __init__(self):
        pass

    def load_image(self, image: Union[str, np.ndarray, Image.Image]) -> Optional[Image.Image]:
        """
        Load an image from a file, numpy array, or PIL Image object.

        Args:
            image (Union[str, np.ndarray, Image.Image]): The image to load. Can be:
                - A string path to an image file
                - A numpy array containing image data
                - A PIL Image object

        Returns:
            PIL.Image.Image: A PIL Image object containing the image data.
                Returns None if loading fails.

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
                return Image.fromarray(image)
            elif isinstance(image, Image.Image):
                return image
            else:
                raise ValueError(f"Invalid image type: {type(image)}. Expected str, numpy.ndarray, or PIL.Image.Image")
        except (FileNotFoundError, IOError) as e:
            raise ValueError(f"Failed to load image file: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error loading image: {str(e)}")
        
    
    def loadimage_from_url(self, url: str, verify_ssl: bool = True) -> Optional[Image.Image]:
        """
        Download an image from a URL and return it as a PIL Image object.

        Args:
            url (str): The URL of the image to download
            verify_ssl (bool): Whether to verify SSL certificates. Default is True.
                Set to False only if you trust the source and are having SSL issues.

        Returns:
            PIL.Image.Image: A PIL Image object containing the image data.
                Returns None if download or conversion fails.

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
