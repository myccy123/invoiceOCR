from paddleocr import PaddleOCR, draw_ocr


ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = r'C:\Users\myccy\Desktop\ttt\5.jpg'
result = ocr.ocr(img_path, cls=True)
for r in result:
    print(r)

