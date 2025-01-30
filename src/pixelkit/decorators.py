from PIL import Image
from functools import wraps

# Decorators for different operation types
def image_loader(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if isinstance(result, Image.Image):
            self.image = result
            return self
        return result
    return wrapper

def image_operation(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'image'):
            raise ValueError("No image loaded. Please load an image first.")
        result = func(self, *args, **kwargs)
        if isinstance(result, Image.Image):
            self.image = result
            return self
        return result
    return wrapper

#Add decorator where filed args are compulsory.
def required_args(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not all(kwargs.values()):
            raise ValueError("All arguments are required.")
        return func(self, *args, **kwargs)
    return wrapper