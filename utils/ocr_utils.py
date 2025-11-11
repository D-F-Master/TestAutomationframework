import base64
import time

import ddddocr
from PIL import Image
import base64
from io import BytesIO


def dddd_ocr_text(image):
    """
    使用ddddocr库对base64编码的图像进行OCR文字识别

    参数:
        image (str): base64编码的图像数据，格式为 'data:image/jpeg;base64,...'

    返回:
        str: 识别出的文字内容
    """
    # 提取base64编码部分（去除data:image/jpeg;base64,前缀）
    encode_data = image.split(',')[1]

    # 将base64编码数据解码为二进制数据
    decode_data = base64.b64decode(encode_data)

    # 创建OCR识别对象
    ocr = ddddocr.DdddOcr()

    # 对图像数据进行文字识别
    text = ocr.classification(decode_data)

    # 返回识别结果
    return text


if __name__ == '__main__':
    str = '{"_t":time.time()}'
    print(eval(str))