import numpy as np
from skimage import data, util, io
import matplotlib.pyplot as plt

astro = data.astronaut()
blocks = util.view_as_blocks(astro, (8, 8, 3))

img_data = io.imread()
print(astro.shape)
print(blocks.shape)

mean_color = np.mean(blocks, axis=(2, 3, 4))

fig, ax = plt.subplots()
ax.imshow(mean_color.astype(np.uint8))