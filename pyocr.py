import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
import os


def ocrtest(img,lang:str='en'):
    # rcParams['figure.figsize'] = 8, 16
    reader = easyocr.Reader([lang])
    #Image(self)
    output = reader.readtext(f'media/{img}')
    # print(output)
    result = []
    for x in range(len(output)):
        text = output[:][x][-2]
        if text.isdigit():
            text=''
        result.append(text)

    return result

# def ocrtest1(img,user):
#     if os.makedirs(f'AI/{user}/{img}', exist_ok = True):
#         rcParams['figure.figsize'] = 8, 16
#         reader = easyocr.Reader(['en'])
#         #Image(self)
#         result = []
#         output = reader.readtext(f'media/{img}')
#         for x in range(len(output)):
#             cord = output[x][-2]
#             # if text.isdigit():
#             #     text=''

#             # result.append(text)
#             x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
#             x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
#             image = cv2.imread(f'media/{img}')
#             cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
#             plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
#             try:
#                 os.makedirs(f'AI/{user}/{img}', exist_ok = True)
#                 result.append(plt.savefig(f'AI/{user}/{img}/{x}'))
#             except OSError as error:
#                 result.append(plt.savefig(f'AI/{user}/{img}/{x}')) 
            

