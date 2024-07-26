def add_gaussian_noise_color(image, mean=0, std_dev=20):
    noise = np.random.normal(mean, std_dev, image.shape)
    noisy_image = np.zeros_like(image, dtype=np.float64)
    for channel in range(image.shape[2]):
        noisy_image[:,:,channel] = image[:,:,channel] + noise[:,:,channel]
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)
