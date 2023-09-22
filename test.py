import cv2
from rapidocr_onnxruntime import RapidOCR, VisRes

engine = RapidOCR()
vis = VisRes(font_path="font\\Roboto-Light.ttf")

img_path = 'images\\01.png'
result, elapse_list = engine(img_path)
boxes, txts, scores = list(zip(*result))
res = vis(img_path, boxes, txts, scores)
cv2.imwrite("vis_det_rec.png", res)
