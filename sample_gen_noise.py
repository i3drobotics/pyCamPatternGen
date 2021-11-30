import matplotlib.pyplot as plt
from patterngen.noise import Noise

noise = Noise(shape=(420, 594), bw=True)
noise.save_raw('noise_px.png')
plt.imshow(noise.data, cmap='gray')
plt.axis('off')
plt.show()
