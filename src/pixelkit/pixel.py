import requests
from PIL import Image
import cv2
import io
import warnings
from typing import Optional, Union, Tuple
import numpy as np
from urllib.parse import urlparse
from src.pixelkit.decorators import property_checker, image_loader, image_operation, required_args, geometric_operation, enhancement_operation, analysis_operation, filter_operation, conversion_operation

#TODO: Add basic image properties, and operations, decorators

class Pixel(Image.Image):
    def __init__(self):
        pass

    # Basic properties
    @property
    @property_checker
    def shape(self) -> Tuple[int, int, int]:
        pass

    @property
    @property_checker
    def size(self) -> Tuple[int, int]:
        pass

    @property
    @property_checker
    def width(self) -> int:
        pass

    @property
    @property_checker
    def height(self) -> int:
        pass

    @property
    @property_checker
    def mode(self) -> str:
        pass

    @property
    @property_checker
    def channels(self) -> int:
        pass

    @property
    @property_checker
    def format(self) -> str:
        pass

    # Core methods
    @staticmethod
    def _make_pixel_instance(image: Image.Image) -> 'Pixel':
        pass

    @staticmethod
    @image_loader
    def load(self, image: Union[str, np.ndarray, Image.Image]) -> 'Pixel':
        pass
    
    @staticmethod
    @image_loader
    def load_url(self, url: str, verify_ssl: bool = True) -> 'Pixel':
        pass
    
    @staticmethod
    @image_loader
    def load_base64(self, base64: str) -> 'Pixel':
        pass

    # Basic operations
    @image_operation
    @required_args(['path'])
    def save(self):
        pass
    
    @image_operation
    def show(self):
        pass
    
    @image_operation
    def plot_bbox(self):
        pass

    # Geometric transformations
    @geometric_operation
    @required_args(['width', 'height'])
    def resize(self, width: int, height: int) -> 'Pixel':
        pass
    
    @geometric_operation
    def horizontal_flip(self):
        pass

    @geometric_operation
    def vertical_flip(self):
        pass

    @geometric_operation
    @required_args(['angle'])
    def rotate(self, angle: int):
        pass

    @geometric_operation
    @required_args(['bbox'])
    def crop(self, bbox: Tuple[int, int, int, int]):
        pass

    # Image enhancement
    @enhancement_operation
    def enhance(self):
        pass

    @enhancement_operation
    def sharpen(self):
        pass

    @enhancement_operation
    def blur(self):
        pass

    @enhancement_operation
    def denoise(self):
        pass
    
    @enhancement_operation
    def dehaze(self):
        pass

    # Image analysis
    @analysis_operation
    def histogram(self):
        pass

    @analysis_operation
    def edge_detection(self):
        pass

    @analysis_operation
    @required_args(['threshold1', 'threshold2'])
    def canny(self, threshold1: int = 100, threshold2: int = 200) -> 'Pixel':
        pass

    # Format conversions
    @conversion_operation
    def to_grayscale(self):
        pass

    @conversion_operation
    def to_numpy(self):
        pass

    @conversion_operation
    def to_base64(self):
        pass

    @conversion_operation
    def to_pil(self):
        pass

    @conversion_operation
    def to_tensor(self):
        pass

    # Filters
    @filter_operation
    def bilateral_filter(self):
        pass

    @filter_operation
    def gaussian_filter(self):
        pass

    @filter_operation
    def median_filter(self):
        pass

    @filter_operation
    def gabor_filter(self):
        pass

    def segment(self):
        pass

    def super_resolution(self):
        pass

    def histogram_equalization(self):
        pass

    def histogram_matching(self):
        pass

    def binary_threshold(self):
        pass

    def otsu_threshold(self):
        pass
    
    def curve_fit(self):
        pass

    def edge_enhancement(self):
        pass

    def box_filter(self):
        pass

    def fft(self):
        pass

    def ifft(self):
        pass

    def fftshift(self):
        pass

    def ifftshift(self):
        pass

    def fft2(self):
        pass

    def ifft2(self):
        pass

    def fftshift2(self):
        pass
    
    def wiener_filter(self):
        pass

    def fft_convolve(self):
        pass

    def fft_deconvolve(self):
        pass
    
    def convolve(self):
        pass

    def deconvolve(self):
        pass

    def lpf(self):
        pass

    def hpf(self):
        pass

    def bandpass(self):
        pass

    def bandstop(self):
        pass

    def bandreject(self):
        pass

    def notch(self):
        pass   

    def gabor_filters(self):
        pass

    def gabor_filters_bank(self):
        pass    