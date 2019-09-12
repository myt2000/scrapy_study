import pytesseract
from PIL import Image


def ocr_image():
    tessract_env = '--tessdata-dir "/usr/local/share/Tesseract/"'
    image = Image.open('test.jpg')
    # image = Image.open('./tesseract/排序算法.png')
    # image = Image.open('./tesseract/7code.png')
    print(image)
    txt = pytesseract.image_to_string(image=image)
    # txt = pytesseract.image_to_string(image=image, lang='chi_sim', config='--tessdata-dir "/usr/local/share/Tesseract/"')

    print(txt)
if __name__ == '__main__':
    ocr_image()