# ppocr-tool
## Intruduction
ppocr-tool是一个款基于PaddlePaddleOCR的命令行工具,使PaddlePalldeOCR的命令更加易用
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
## 安装到本地
```
pip install .
```
## 识别
图片
windows
```
ppocrtool -ot=text -src doc\imgs\11.jpg --lang ch
```
unix
```
ppocrtool -ot=text -src doc/imgs/11.jpg --lang ch
```

识别PDF
windows
```
ppocrtool -ot=text -src doc\pdfs\lab_1.pdf --lang ch
```
unix
```
ppocrtool -ot=text -src doc/pdfs/lab_1.pdf --lang ch
```
- ch, Chinese
- en, English
- fr, French
- german
- korean
- japan`

##识别目录所有文件并将识别结果写入新的文件
```
ppocrtool --image_dir doc/pdfs --output output_dir
```

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
仅仅在windows上编译和运行成功
编译成二进制文件
```
python build.yml
```
测试运行
```
测试1
```
dist\ppocr -ot=text -src doc\imgs\11.jpg --lang ch

## 查看帮助
2.支持的参数
```
ppocrtool --h
```

```
usage: ppocrtool.exe [-h] [--use_gpu USE_GPU] [--use_xpu USE_XPU] [--use_npu USE_NPU] [--ir_optim IR_OPTIM] [--use_tensorrt USE_TENSORRT] [--min_subgraph_size MIN_SUBGRAPH_SIZE] [--precision PRECISION]
                 [--gpu_mem GPU_MEM] [--gpu_id GPU_ID] [--image_dir IMAGE_DIR] [--page_num PAGE_NUM] [--det_algorithm DET_ALGORITHM] [--det_model_dir DET_MODEL_DIR] [--det_limit_side_len DET_LIMIT_SIDE_LEN]
                 [--det_limit_type DET_LIMIT_TYPE] [--det_box_type DET_BOX_TYPE] [--det_db_thresh DET_DB_THRESH] [--det_db_box_thresh DET_DB_BOX_THRESH] [--det_db_unclip_ratio DET_DB_UNCLIP_RATIO]
                 [--max_batch_size MAX_BATCH_SIZE] [--use_dilation USE_DILATION] [--det_db_score_mode DET_DB_SCORE_MODE] [--det_east_score_thresh DET_EAST_SCORE_THRESH]
                 [--det_east_cover_thresh DET_EAST_COVER_THRESH] [--det_east_nms_thresh DET_EAST_NMS_THRESH] [--det_sast_score_thresh DET_SAST_SCORE_THRESH] [--det_sast_nms_thresh DET_SAST_NMS_THRESH]
                 [--det_pse_thresh DET_PSE_THRESH] [--det_pse_box_thresh DET_PSE_BOX_THRESH] [--det_pse_min_area DET_PSE_MIN_AREA] [--det_pse_scale DET_PSE_SCALE] [--scales SCALES] [--alpha ALPHA]
                 [--beta BETA] [--fourier_degree FOURIER_DEGREE] [--rec_algorithm REC_ALGORITHM] [--rec_model_dir REC_MODEL_DIR] [--rec_image_inverse REC_IMAGE_INVERSE] [--rec_image_shape REC_IMAGE_SHAPE]
                 [--rec_batch_num REC_BATCH_NUM] [--max_text_length MAX_TEXT_LENGTH] [--rec_char_dict_path REC_CHAR_DICT_PATH] [--use_space_char USE_SPACE_CHAR] [--vis_font_path VIS_FONT_PATH]
                 [--drop_score DROP_SCORE] [--e2e_algorithm E2E_ALGORITHM] [--e2e_model_dir E2E_MODEL_DIR] [--e2e_limit_side_len E2E_LIMIT_SIDE_LEN] [--e2e_limit_type E2E_LIMIT_TYPE]
                 [--e2e_pgnet_score_thresh E2E_PGNET_SCORE_THRESH] [--e2e_char_dict_path E2E_CHAR_DICT_PATH] [--e2e_pgnet_valid_set E2E_PGNET_VALID_SET] [--e2e_pgnet_mode E2E_PGNET_MODE]
                 [--use_angle_cls USE_ANGLE_CLS] [--cls_model_dir CLS_MODEL_DIR] [--cls_image_shape CLS_IMAGE_SHAPE] [--label_list LABEL_LIST] [--cls_batch_num CLS_BATCH_NUM] [--cls_thresh CLS_THRESH]
                 [--enable_mkldnn ENABLE_MKLDNN] [--cpu_threads CPU_THREADS] [--use_pdserving USE_PDSERVING] [--warmup WARMUP] [--sr_model_dir SR_MODEL_DIR] [--sr_image_shape SR_IMAGE_SHAPE]
                 [--sr_batch_num SR_BATCH_NUM] [--draw_img_save_dir DRAW_IMG_SAVE_DIR] [--save_crop_res SAVE_CROP_RES] [--crop_res_save_dir CROP_RES_SAVE_DIR] [--use_mp USE_MP]
                 [--total_process_num TOTAL_PROCESS_NUM] [--process_id PROCESS_ID] [--benchmark BENCHMARK] [--save_log_path SAVE_LOG_PATH] [--show_log SHOW_LOG] [--use_onnx USE_ONNX] [--output OUTPUT]
                 [--table_max_len TABLE_MAX_LEN] [--table_algorithm TABLE_ALGORITHM] [--table_model_dir TABLE_MODEL_DIR] [--merge_no_span_structure MERGE_NO_SPAN_STRUCTURE]
                 [--table_char_dict_path TABLE_CHAR_DICT_PATH] [--layout_model_dir LAYOUT_MODEL_DIR] [--layout_dict_path LAYOUT_DICT_PATH] [--layout_score_threshold LAYOUT_SCORE_THRESHOLD]
                 [--layout_nms_threshold LAYOUT_NMS_THRESHOLD] [--kie_algorithm KIE_ALGORITHM] [--ser_model_dir SER_MODEL_DIR] [--re_model_dir RE_MODEL_DIR] [--use_visual_backbone USE_VISUAL_BACKBONE]
                 [--ser_dict_path SER_DICT_PATH] [--ocr_order_method OCR_ORDER_METHOD] [--mode {structure,kie}] [--image_orientation IMAGE_ORIENTATION] [--layout LAYOUT] [--table TABLE] [--ocr OCR]
                 [--recovery RECOVERY] [--use_pdf2docx_api USE_PDF2DOCX_API] [--invert INVERT] [--binarize BINARIZE] [--alphacolor ALPHACOLOR] [--lang LANG] [--det DET] [--rec REC] [--type TYPE]
                 [--ocr_version {PP-OCR,PP-OCRv2,PP-OCRv3,PP-OCRv4}] [--structure_version {PP-Structure,PP-StructureV2}]

optional arguments:
  -h, --help            show this help message and exit
  --use_gpu USE_GPU
  --use_xpu USE_XPU
  --use_npu USE_NPU
  --ir_optim IR_OPTIM
  --use_tensorrt USE_TENSORRT
  --min_subgraph_size MIN_SUBGRAPH_SIZE
  --precision PRECISION
  --gpu_mem GPU_MEM
  --gpu_id GPU_ID
  --image_dir IMAGE_DIR
  --page_num PAGE_NUM
  --det_algorithm DET_ALGORITHM
  --det_model_dir DET_MODEL_DIR
  --det_limit_side_len DET_LIMIT_SIDE_LEN
  --det_limit_type DET_LIMIT_TYPE
  --det_box_type DET_BOX_TYPE
  --det_db_thresh DET_DB_THRESH
  --det_db_box_thresh DET_DB_BOX_THRESH
  --det_db_unclip_ratio DET_DB_UNCLIP_RATIO
  --max_batch_size MAX_BATCH_SIZE
  --use_dilation USE_DILATION
  --det_db_score_mode DET_DB_SCORE_MODE
  --det_east_score_thresh DET_EAST_SCORE_THRESH
  --det_east_cover_thresh DET_EAST_COVER_THRESH
  --det_east_nms_thresh DET_EAST_NMS_THRESH
  --det_sast_score_thresh DET_SAST_SCORE_THRESH
  --det_sast_nms_thresh DET_SAST_NMS_THRESH
  --det_pse_thresh DET_PSE_THRESH
  --det_pse_box_thresh DET_PSE_BOX_THRESH
  --det_pse_min_area DET_PSE_MIN_AREA
  --det_pse_scale DET_PSE_SCALE
  --scales SCALES
  --alpha ALPHA
  --beta BETA
  --fourier_degree FOURIER_DEGREE
  --rec_algorithm REC_ALGORITHM
  --rec_model_dir REC_MODEL_DIR
  --rec_image_inverse REC_IMAGE_INVERSE
  --rec_image_shape REC_IMAGE_SHAPE
  --rec_batch_num REC_BATCH_NUM
  --max_text_length MAX_TEXT_LENGTH
  --rec_char_dict_path REC_CHAR_DICT_PATH
  --use_space_char USE_SPACE_CHAR
  --vis_font_path VIS_FONT_PATH
  --drop_score DROP_SCORE
  --e2e_algorithm E2E_ALGORITHM
  --e2e_model_dir E2E_MODEL_DIR
  --e2e_limit_side_len E2E_LIMIT_SIDE_LEN
  --e2e_limit_type E2E_LIMIT_TYPE
  --e2e_pgnet_score_thresh E2E_PGNET_SCORE_THRESH
  --e2e_char_dict_path E2E_CHAR_DICT_PATH
  --e2e_pgnet_valid_set E2E_PGNET_VALID_SET
  --e2e_pgnet_mode E2E_PGNET_MODE
  --use_angle_cls USE_ANGLE_CLS
  --cls_model_dir CLS_MODEL_DIR
  --cls_image_shape CLS_IMAGE_SHAPE
  --label_list LABEL_LIST
  --cls_batch_num CLS_BATCH_NUM
  --cls_thresh CLS_THRESH
  --enable_mkldnn ENABLE_MKLDNN
  --cpu_threads CPU_THREADS
  --use_pdserving USE_PDSERVING
  --warmup WARMUP
  --sr_model_dir SR_MODEL_DIR
  --sr_image_shape SR_IMAGE_SHAPE
  --sr_batch_num SR_BATCH_NUM
  --draw_img_save_dir DRAW_IMG_SAVE_DIR
  --save_crop_res SAVE_CROP_RES
  --crop_res_save_dir CROP_RES_SAVE_DIR
  --use_mp USE_MP
  --total_process_num TOTAL_PROCESS_NUM
  --process_id PROCESS_ID
  --benchmark BENCHMARK
  --save_log_path SAVE_LOG_PATH
  --show_log SHOW_LOG
  --use_onnx USE_ONNX
  --output OUTPUT
  --table_max_len TABLE_MAX_LEN
  --table_algorithm TABLE_ALGORITHM
  --table_model_dir TABLE_MODEL_DIR
  --merge_no_span_structure MERGE_NO_SPAN_STRUCTURE
  --table_char_dict_path TABLE_CHAR_DICT_PATH
  --layout_model_dir LAYOUT_MODEL_DIR
  --layout_dict_path LAYOUT_DICT_PATH
  --layout_score_threshold LAYOUT_SCORE_THRESHOLD
                        Threshold of score.
  --layout_nms_threshold LAYOUT_NMS_THRESHOLD
                        Threshold of nms.
  --kie_algorithm KIE_ALGORITHM
  --ser_model_dir SER_MODEL_DIR
  --re_model_dir RE_MODEL_DIR
  --use_visual_backbone USE_VISUAL_BACKBONE
  --ser_dict_path SER_DICT_PATH
  --ocr_order_method OCR_ORDER_METHOD
  --mode {structure,kie}
                        structure and kie is supported
  --image_orientation IMAGE_ORIENTATION
                        Whether to enable image orientation recognition
  --layout LAYOUT       Whether to enable layout analysis
  --table TABLE         In the forward, whether the table area uses table recognition
  --ocr OCR             In the forward, whether the non-table area is recognition by ocr
  --recovery RECOVERY   Whether to enable layout of recovery
  --use_pdf2docx_api USE_PDF2DOCX_API
                        Whether to use pdf2docx api
  --invert INVERT       Whether to invert image before processing
  --binarize BINARIZE   Whether to threshold binarize image before processing
  --alphacolor ALPHACOLOR
                        Replacement color for the alpha channel, if the latter is present; R,G,B integers
  --lang LANG
  --det DET
  --rec REC
  --type TYPE
  --ocr_version {PP-OCR,PP-OCRv2,PP-OCRv3,PP-OCRv4}
                        OCR Model version, the current model support list is as follows: 1. PP-OCRv4/v3 Support Chinese and English detection and recognition model, and direction classifier model2. PP-OCRv2
                        Support Chinese detection and recognition model. 3. PP-OCR support Chinese detection, recognition and direction classifier and multilingual recognition model.
  --structure_version {PP-Structure,PP-StructureV2}
                        Model version, the current model support list is as follows: 1. PP-Structure Support en table structure model. 2. PP-StructureV2 Support ch and en table structure model. 
```