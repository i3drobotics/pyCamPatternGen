import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from patterngen.util import PaperSize


class Checkerboard:
    """
    Checkerboard generation.
    Includes addition functions for saving the data.

    ...

    Attributes
    ----------
    data : np.ndarray
        numpy array containing the checkerboard data

    Methods
    -------
    save(filepath)
        Save checkerboard to image file

    """

    def __init__(self, shape: tuple):
        """
        Checkerboard construction

        Parameters
        ----------
        shape : tuple
            Shape of the checkerboard (height, width).
            (e.g. (10, 10))
        """
        self.height, self.width = shape
        self.data = self._generate(shape)

    def _generate(self, shape: list) -> np.ndarray:
        """
        Generate checkerboard

        Parameters
        ----------
        shape : tuple
            Shape of the checkerboard (e.g. (10, 10))

        Returns
        -------
        np.ndarray
            image data of checkerboard
        """
        data = np.indices(shape).sum(axis=0) % 2
        return data

    def _scale_squares(self, data, square_size_px: int):
        """
        Scale checkerboard to mm

        Parameters
        ----------
        square_size_px : int
            Pixel width of each square in the checkerboard.
            Default is 1. MUST be bigger than 0.
        """
        if square_size_px < 1:
            raise ValueError("Square size must be greater than 0")
        if square_size_px == 1:
            return data

        # scale image by pixel square size
        data = data.repeat(
            square_size_px, axis=0).repeat(square_size_px, axis=1)
        return data

    def save_raw(self, filepath: str, square_size_px: int = 1) -> None:
        """
        Save checkerboard to file

        Parameters
        ----------
        filepath : str
            File path to save image to (e.g. './checkerboard.png')
        square_size_px : int
            Pixel width of each square in the checkerboard.
            Default is 1. MUST be bigger than 0.
        """
        data = self._scale_squares(self.data, square_size_px)
        mpimg.imsave(filepath, data, cmap=plt.cm.gray)

    def save_mm(self, filepath: str,
                square_size_mm: int = 36, ppi: int = 300) -> None:
        """
        Save checkerboard to file

        Parameters
        ----------
        square_size_mm : int
            Width of each square in mm. Default is 36mm
        filepath : str
            File path to save image to (e.g. './checkerboard_a4.png')
        """
        # convert pixels per inch (ppi) to pixels per mm
        pixels_per_mm = ppi / 25.4
        # calculate pixel size from mm and pixels per mm
        square_size_px = int(square_size_mm * pixels_per_mm)
        # scale checkerboard to fit chosen size
        data = self._scale_squares(self.data, square_size_px)
        # save page image to file
        mpimg.imsave(filepath, data, cmap=plt.cm.gray)

    def save_page(self, filepath: str, paper_size: PaperSize,
                  square_size_mm: int = 36, margin: int = 5) -> None:
        """
        Save checkerboard to file

        Parameters
        ----------
        square_size_mm : int
            Width of each square in mm. Default is 36mm
        filepath : str
            File path to save image to (e.g. './checkerboard_a4.png')
        """

        raise Exception("Not implemented")
        # board_width_mm = square_size_mm * self.width
        # board_height_mm = square_size_mm * self.height

        # calculate pixels per mm from pixels per inch (ppi)
        # pixels_per_mm = ppi / 25.4
        # square_size_px = int(square_size_mm * pixels_per_mm)

        # check if checkerboard is landscape or portrait
        if self.width > self.height:
            landscape = True
        else:
            landscape = False

        if landscape:
            pass


if __name__ == '__main__':
    checkerboard = Checkerboard(shape=(7, 11))

    checkerboard.save_raw('checkerboard_px.png', square_size_px=200)
    # checkerboard.save_mm('checkerboard_mm.png', square_size_mm=36, ppi=300)
    # checkerboard.save_page(
    #     'checkerboard_a4.png', paper_size=PaperSize.A4, square_size_mm=36)
    # plt.imshow(checkerboard.data, cmap='gray')
    # plt.axis('off')
    # plt.show()
