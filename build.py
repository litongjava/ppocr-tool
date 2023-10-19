import os
from distutils.sysconfig import get_python_lib
import sys
import shutil

def get_packages_path():
    packages_path = get_python_lib()
    print(packages_path);
    return packages_path;

def get_paddle_libs_path():
    # 获取 Python 安装路径
    packages_path = get_packages_path()

    # 构造 lib 路径
    paddle_libs_path = os.path.join(packages_path, "paddle", "libs")
    print(paddle_libs_path)
    return paddle_libs_path

def build_on_windows():
    # PyInstaller 构建命令 for Windows
    packages_path = get_packages_path()
    paddle_libs_path = get_paddle_libs_path()
    cmd = (f'pyinstaller -F main-ocr-text.py --name ppocr '
           f'--add-data "{packages_path}\paddleocr\\tools;./paddleocr/tools" '
           f'--add-data "{packages_path}\paddleocr\ppocr;./paddleocr/ppocr" '
           f'--add-data "{packages_path}\paddleocr\ppstructure;./paddleocr/ppstructure" '
           '--hidden-import=Pillow --hidden-import=PIL.ImageDraw --hidden-import=shapely --hidden-import=pyclipper '
           '--hidden-import=scikit-image --hidden-import=imgaug --hidden-import=lmdb --hidden-import=tqdm '
           '--hidden-import=numpy --hidden-import=visualdl --hidden-import=rapidfuzz --hidden-import=opencv-python '
           '--hidden-import=opencv-contrib-python --hidden-import=cython --hidden-import=lxml --hidden-import=premailer '
           '--hidden-import=openpyxl --hidden-import=attrdict --hidden-import=PyMuPDF --hidden-import=pyyaml '
           '--hidden-import=imghdr --hidden-import=scipy.io '
           f'--add-binary="{paddle_libs_path};."') 
    return cmd


def build_on_unix():
    # PyInstaller 构建命令 for Linux & MacOS
    packages_path = get_packages_path()
    paddle_libs_path = get_paddle_libs_path()
    cmd = (f'pyinstaller -F demo.py --name ppocr '
           f'--add-data "{packages_path}/paddleocr/tools:./paddleocr/tools" '
           f'--add-data "{packages_path}/paddleocr/ppocr:./paddleocr/ppocr" '
           f'--add-data "{packages_path}/paddleocr/ppstructure:./paddleocr/ppstructure" '
           '--hidden-import=Pillow --hidden-import=PIL.ImageDraw --hidden-import=shapely --hidden-import=pyclipper '
           '--hidden-import=scikit-image --hidden-import=imgaug --hidden-import=lmdb --hidden-import=tqdm '
           '--hidden-import=numpy --hidden-import=visualdl --hidden-import=rapidfuzz --hidden-import=opencv-python '
           '--hidden-import=opencv-contrib-python --hidden-import=cython --hidden-import=lxml --hidden-import=premailer '
           '--hidden-import=openpyxl --hidden-import=attrdict --hidden-import=PyMuPDF --hidden-import=pyyaml '
           '--hidden-import=imghdr --hidden-import=scipy.io '
           f'--add-binary="{paddle_libs_path}:."') 
    return cmd


def main():
    if os.name == 'nt':
        cmd = build_on_windows()
    else:
        cmd = build_on_unix()

    # 执行 PyInstaller 构建命令
    print(cmd)
    os.system(cmd)

    # 复制 libs 文件夹的内容到 dist 文件夹
    # lib_path = get_paddle_libs_path()
    # dest_path = os.path.join("dist")
    # for item in os.listdir(lib_path):
    #     s = os.path.join(lib_path, item)
    #     d = os.path.join(dest_path, item)
    #     if os.path.isdir(s):
    #         shutil.copytree(s, d, dirs_exist_ok=True)
    #     else:
    #         print("copy {} to {}".format(s, d))
    #         shutil.copy2(s, d)


if __name__ == "__main__":
    main()
