import functools
from typing import List, Callable, Any
import warnings
from PIL import Image
import numpy as np

def image_loader(func: Callable) -> Callable:
    """Decorator for image loading methods that handles different input types and error checking"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise ValueError("Failed to load image")
            return result
        except Exception as e:
            raise ValueError(f"Error loading image: {str(e)}")
    return wrapper

def image_operation(func: Callable) -> Callable:
    """Decorator for image processing operations that ensures valid image state"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_image') or self._image is None:
            raise ValueError("No image loaded")
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error during image operation: {str(e)}")
    return wrapper

def required_args(required: List[str]) -> Callable:
    """Decorator to check if required arguments are provided"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Convert args to kwargs for checking
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            params = bound_args.arguments

            missing = [arg for arg in required if arg not in params or params[arg] is None]
            if missing:
                raise ValueError(f"Missing required arguments: {', '.join(missing)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def property_checker(func: Callable) -> Callable:
    """Decorator for property methods to ensure image exists"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_image') or self._image is None:
            raise ValueError("No image loaded")
        return func(self, *args, **kwargs)
    return wrapper

def geometric_operation(func: Callable) -> Callable:
    """Decorator for geometric transformations that validates dimensions"""
    @functools.wraps(func)
    @image_operation
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            if result is not None and not isinstance(result, (Image.Image, np.ndarray)):
                raise ValueError("Invalid transformation result")
            return result
        except Exception as e:
            raise ValueError(f"Error during geometric transformation: {str(e)}")
    return wrapper

def enhancement_operation(func: Callable) -> Callable:
    """Decorator for image enhancement operations"""
    @functools.wraps(func)
    @image_operation
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error during image enhancement: {str(e)}")
    return wrapper

def analysis_operation(func: Callable) -> Callable:
    """Decorator for image analysis operations"""
    @functools.wraps(func)
    @image_operation
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error during image analysis: {str(e)}")
    return wrapper

def filter_operation(func: Callable) -> Callable:
    """Decorator for filter operations"""
    @functools.wraps(func)
    @image_operation
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error during filter operation: {str(e)}")
    return wrapper

def conversion_operation(func: Callable) -> Callable:
    """Decorator for format conversion operations"""
    @functools.wraps(func)
    @image_operation
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            if result is None:
                raise ValueError("Conversion failed")
            return result
        except Exception as e:
            raise ValueError(f"Error during format conversion: {str(e)}")
    return wrapper
