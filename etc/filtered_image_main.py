import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.fft import fft2, ifft2, fftshift, ifftshift

def low_pass_filter(image_array, cutoff):
    f_transform = fft2(image_array)
    f_transform_shifted = fftshift(f_transform)
    
    rows, cols = image_array.shape
    crow, ccol = rows // 2 , cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 1
    
    f_transform_shifted_filtered = f_transform_shifted * mask
    f_transform_filtered = ifftshift(f_transform_shifted_filtered)
    filtered_image = ifft2(f_transform_filtered)
    return np.abs(filtered_image), f_transform_shifted, f_transform_shifted_filtered

def high_pass_filter(image_array, cutoff):
    f_transform = fft2(image_array)
    f_transform_shifted = fftshift(f_transform)
    
    rows, cols = image_array.shape
    crow, ccol = rows // 2 , cols // 2
    mask = np.ones((rows, cols), np.uint8)
    mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 0
    
    f_transform_shifted_filtered = f_transform_shifted * mask
    f_transform_filtered = ifftshift(f_transform_shifted_filtered)
    filtered_image = ifft2(f_transform_filtered)
    return np.abs(filtered_image), f_transform_shifted, f_transform_shifted_filtered

# 이미지 읽기 및 회색조 변환
image_path = 'moon.jpg'  # 분석할 이미지 파일 경로
image = Image.open(image_path).convert('L')  # 회색조 변환
image_array = np.array(image)

# 필터링 수행
cutoff_frequency = 30
low_passed_image, original_f_transform, low_passed_f_transform = low_pass_filter(image_array, cutoff_frequency)
high_passed_image, _, high_passed_f_transform = high_pass_filter(image_array, cutoff_frequency)

# 주파수 스펙트럼 계산
def compute_log_magnitude_spectrum(f_transform):
    magnitude_spectrum = np.abs(f_transform)
    log_magnitude_spectrum = np.log(1 + magnitude_spectrum)
    return log_magnitude_spectrum

original_spectrum = compute_log_magnitude_spectrum(original_f_transform)
low_passed_spectrum = compute_log_magnitude_spectrum(low_passed_f_transform)
high_passed_spectrum = compute_log_magnitude_spectrum(high_passed_f_transform)

# 원본 이미지, 필터링된 이미지 및 주파수 스펙트럼 시각화
plt.figure(figsize=(18, 12))

plt.subplot(3, 3, 1)
plt.title('Original Image')
plt.imshow(image_array, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.title('Low Pass Filtered Image')
plt.imshow(low_passed_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.title('High Pass Filtered Image')
plt.imshow(high_passed_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.title('Original Spectrum')
plt.imshow(original_spectrum, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.title('Low Pass Spectrum')
plt.imshow(low_passed_spectrum, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.title('High Pass Spectrum')
plt.imshow(high_passed_spectrum, cmap='gray')
plt.axis('off')

plt.show()
