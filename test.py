from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

img_path = '01.png'
result, elapse = engine(img_path)
# print(result)
print(elapse)
