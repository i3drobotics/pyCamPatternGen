import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Noise:
    """
    Noise generation.
    Includes addition functions for saving the data.

    ...

    Attributes
    ----------
    data : np.ndarray
        numpy array containing the noise data

    Methods
    -------
    save(filepath)
        Save noise to image file

    """

    def __init__(self, shape: tuple, bw: bool = False):
        """
        Noise construction

        Parameters
        ----------
        shape : tuple
            Shape of the noise pattern (height, width).
            (e.g. (100, 100))
        """
        self.height, self.width = shape
        self.bw = bw
        if bw:
            shape = (shape[0], shape[1], 1)
        else:
            shape = (shape[0], shape[1], 3)
        self.data = self._generate(shape)

    def _generate(self, shape: list) -> np.ndarray:
        """
        Generate noise

        Parameters
        ----------
        shape : tuple
            Shape of the noise (e.g. (10, 10))

        Returns
        -------
        np.ndarray
            image data of noise
        """
        mean = 0
        var = 0.1
        sigma = var**0.5
        shape = (shape[0], shape[1], shape[2])
        gauss = np.random.normal(mean, sigma, shape)
        data = (gauss * 255).astype(np.uint8)
        if self.bw:
            data = np.reshape(data, (shape[0], shape[1]))
        return data

    def save_raw(self, filepath: str) -> None:
        """
        Save noise to file

        Parameters
        ----------
        filepath : str
            File path to save image to (e.g. './noise.png')
        """
        if self.bw:
            mpimg.imsave(filepath, self.data, cmap=plt.cm.gray)
        else:
            mpimg.imsave(filepath, self.data)


if __name__ == '__main__':
    noise = Noise(shape=(420, 594), bw=True)

    noise.save_raw('noise_px_bw.png')
    # noise.save_mm('checkerboard_mm.png', square_size_mm=36, ppi=300)
    # plt.imshow(noise.data, cmap='gray')
    # plt.axis('off')
    # plt.show()
