# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\ProgramData\\Anaconda3\\envs\\paddle_ocr_cpu_env\\Lib\\site-packages\\paddleocr\\tools', './paddleocr/tools'), ('D:\\ProgramData\\Anaconda3\\envs\\paddle_ocr_cpu_env\\Lib\\site-packages\\paddleocr\\ppocr', './paddleocr/ppocr'), ('D:\\ProgramData\\Anaconda3\\envs\\paddle_ocr_cpu_env\\Lib\\site-packages\\paddleocr\\ppstructure', './paddleocr/ppstructure')],
    hiddenimports=['Pillow', 'PIL.ImageDraw', 'shapely', 'pyclipper', 'scikit-image', 'imgaug', 'lmdb', 'tqdm', 'numpy', 'visualdl', 'rapidfuzz', 'opencv-python', 'opencv-contrib-python', 'cython', 'lxml', 'premailer', 'openpyxl', 'attrdict', 'PyMuPDF', 'pyyaml', 'imghdr', 'scipy.io'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
