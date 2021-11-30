import matplotlib.pyplot as plt
from patterngen.checker import Checkerboard

checkerboard = Checkerboard(shape=(7, 11))
checkerboard.save_raw('checkerboard_px.png', square_size_px=200)
plt.imshow(checkerboard.data, cmap='gray')
plt.show()
