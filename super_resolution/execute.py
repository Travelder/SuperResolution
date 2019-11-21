import os
import matplotlib.pyplot as plt


from .data import DIV2K
from .model.srgan import generator, discriminator
from .train import SrganTrainer, SrganGeneratorTrainer

from .model import resolve_single
from .utils import load_image
dirname = os.path.dirname(__file__)
weights_dir = os.path.join(dirname,'weights/srgan')
weights_file = lambda filename: os.path.join(weights_dir, filename)
os.makedirs(weights_dir, exist_ok=True)
pre_generator = generator()
gan_generator = generator()
pre_generator.load_weights(weights_file('pre_generator.h5'))
gan_generator.load_weights(weights_file('gan_generator.h5'))

def resolve(lr_image_path):
    lr = load_image(lr_image_path)
    
    pre_sr = resolve_single(pre_generator, lr)
    gan_sr = resolve_single(gan_generator, lr)
    
    images = [lr, pre_sr, gan_sr]
    titles = ['LR', 'SR (PRE)', 'SR (GAN)']
    positions = [1, 3, 4]
    
    plt.axis('off')
    plt.imshow(gan_sr)
    fname = '.'.join(lr_image_path.split('.')[:-1])
    image_name =  fname + '_out' + '.png'
    
    plt.savefig(image_name, transparent=True, bbox_inches='tight', pad_inches=0)
    
    return image_name