import argparse
import sys
import paddle
import paddleocr
from paddleocr import PaddleOCR, draw_ocr


def version():
    print(f"Python Version: {sys.version}")
    print(f"Paddle Version: {paddle.__version__}")
    print(f"PaddleOCR Version: {paddleocr.__version__}")


def ocr(source, language):
    # 检测+方向分类器+识别全流程
    from paddleocr import PaddleOCR, draw_ocr

    ocr = PaddleOCR(use_angle_cls=True, lang=language)  # need to run only once to download and load model into memory

    result = ocr.ocr(source, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            coordinates, content_info = line  # 解包line
            text, confidence = content_info  # 解包content_info
            print(text)


def main():
    parser = argparse.ArgumentParser(description='PaddleOCR Utility')

    # 添加参数
    parser.add_argument('-v', '--version', action='store_true', help='输出版本')
    parser.add_argument('-src', '--source', type=str, help='图像文件路径')
    parser.add_argument('-lang', '--language', type=str, help='语言')

    args = parser.parse_args()

    # 根据参数执行相应的操作
    if args.version:
        return version()

    if args.source:
        ocr(args.source, args.language);


if __name__ == '__main__':
    main()
