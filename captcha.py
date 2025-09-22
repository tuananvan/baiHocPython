import random
from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height=90)

def generate_random_captcha_text(length=6):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text

captcha_text = generate_random_captcha_text()

data = image.generate(captcha_text)
image.write(captcha_text, 'captcha.png')

from PIL import Image
Image.open('captcha.png').show()