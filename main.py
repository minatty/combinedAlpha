#!/user/bin/env python

import numpy as np
from PIL import Image

def main():
	img_alpha = np.array(Image.open('./Body_tex_alpha.png'))
	img_source = np.array(Image.open('./Body_tex_noalpha.png'))
	img_dest = img_source.copy()
	img_dest[:,:,3] = img_alpha[:,:,3]
	Image.fromarray(img_dest).save('./combined_alpha.png')

if __name__ == '__main__':
	main()