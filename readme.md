# ppocr-tool
## 安装环境
CPU
```
conda create --name paddle_ocr_cpu_env python=3.8
activate paddle_ocr_cpu_env 
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install "paddleocr>=2.0.1" -i https://mirror.baidu.com/pypi/simple
```
## 识别

识别图片
```
-src E:\code\python\project-github\PaddleOCR\doc\imgs\11.jpg -lang ch
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
- japan

## 错误记录
在windows上编译成exe运行,运行出现错误