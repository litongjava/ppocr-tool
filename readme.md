# ppocr-tool
## 准备环境
```
conda create --name paddle_ocr_cpu_env python=3.8 -y
activate paddle_ocr_cpu_env 
or
conda activate paddle_ocr_cpu_env 
```
```
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install "paddleocr>=2.0.1" -i https://mirror.baidu.com/pypi/simple
```
## 识别图片
```
python main-ocr-text.py -ot=text -src E:\code\python\project-github\PaddleOCR\doc\imgs\11.jpg -lang ch
```

识别PDF

```
-src "F:\document\subject-docs\11_Music\Mus 107\week 4\Hawaiian Music Reading-1.pdf" -lang en
```

- ch, Chinese
- en, English
- fr, French
- german
- korean
- japan`

## 模型 
首次运行会自动下载模型
中文模型
- https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_det_infer.tar
- https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_rec_infer.tar
- https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar


英文模型
- https://paddleocr.bj.bcebos.com/PP-OCRv4/english/en_PP-OCRv4_rec_infer.tar

模型保存位置
- windows C:\Users\Administrator\.paddleocr\whl
- macos /Users/ping/.paddleocr/whl

## 编译成二进制文件
### Windows
``` 
pyinstaller -F main-ocr-text.py --name ppocr --add-data "D:\ProgramData\Anaconda3\envs\paddle_ocr_cpu_env\Lib\site-packages\paddleocr\tools;./paddleocr/tools" --add-data "D:\ProgramData\Anaconda3\envs\paddle_ocr_cpu_env\Lib\site-packages\paddleocr\ppocr;./paddleocr/ppocr" --add-data "D:\ProgramData\Anaconda3\envs\paddle_ocr_cpu_env\Lib\site-packages\paddleocr\ppstructure;./paddleocr/ppstructure" --hidden-import=Pillow --hidden-import=PIL.ImageDraw --hidden-import=shapely --hidden-import=pyclipper --hidden-import=scikit-image --hidden-import=imgaug --hidden-import=lmdb --hidden-import=tqdm --hidden-import=numpy --hidden-import=visualdl --hidden-import=rapidfuzz --hidden-import=opencv-python --hidden-import=opencv-contrib-python --hidden-import=cython --hidden-import=lxml --hidden-import=premailer --hidden-import=openpyxl --hidden-import=attrdict --hidden-import=PyMuPDF --hidden-import=pyyaml --hidden-import=imghdr --hidden-import=scipy.io
```
构建完成后复制libs到指定生成的程序的同级目录
```
D:\ProgramData\Anaconda3\envs\paddle_ocr_cpu_env\Lib\site-packages\paddle\libs
```
测试1
```
dist\ppocr -ot=text -src doc\imgs\11.jpg --lang ch
```
测试2
```
dist\ppocr --image_dir doc\imgs\11.jpg --use_angle_cls true --use_gpu false
```