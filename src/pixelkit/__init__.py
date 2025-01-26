import requests
from PIL import Image
import io
import warnings
from typing import Optional
from urllib.parse import urlparse

def image_from_url(url: str, verify_ssl: bool = True) -> Optional[Image.Image]:
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
