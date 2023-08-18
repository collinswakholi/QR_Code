import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# QR code decoder (weChat), get artefacts from https://github.com/WeChatCV/opencv_3rdparty/tree/wechat_qrcode
from . import artefacts

class ReadQR:
    """
    Reads QR codes from image returns list of strings of data encoded
    """
    
    def __init__(self):
        # self.qrDecoder = qrDetector
        self.qrDetector = cv2.wechat_qrcode_WeChatQRCode(
            artefacts.model_detect_prototxt, 
            artefacts.model_detect_caffemodel,
            artefacts.model_sr_prototxt,
            artefacts.model_sr_caffemodel
            )
        
    def decode(self, img, show=None): # show = None, "single", "continuous"
        """
        Decodes QR codes from image
        
        Args:
            img: image with QR codes to be decoded, must be BGR cv2 image (ndarray)
            show: default is None: no image is shown, "single": image is shown and waits for key press, "continuous": image is shown and waits for 1 ms (for video)
        """
        # Detect and decode the qrcode
        data,bbox = self.qrDetector.detectAndDecode(img)
        
        if len(data)>0:
            if show is not None:
                window_size = 800
                h, w = img.shape[:2]
                resized_dims = [window_size, window_size]
                min_val, min_pos = min(h,w), np.argmin([h,w])
                max_val, max_pos = max(h,w), np.argmax([h,w])
                ratio = max_val/min_val
                if h!=w:
                    new_window_size = np.int32(window_size*ratio)
                    resized_dims[max_pos] = new_window_size
                
                # print(resized_dims)
                thickness = max(1,round(min_val/200))
                color = (0,255,0)
                is_closed = True
                
                thickness_txt = max(1,round(min_val/1000))
                font_size = max(1,round(min_val/2000))
                color_txt = (255,0,0)
                
                # print(thickness_txt, font_size)
                n = len(bbox)
                
                for j in range(0,n):
                    img = cv2.polylines(img, np.int32([bbox[j]]), 
                                    is_closed, color, thickness)
                    text = data[j]
                    img = cv2.putText(img, text, 
                                    (np.int32(bbox[j][0][0]), np.int32(bbox[j][0][1])), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                    font_size, 
                                    color_txt, 
                                    thickness_txt, 
                                    cv2.LINE_AA)  
                try: # try to show image using cv2
                    cv2.namedWindow("Detected QR", cv2.WINDOW_NORMAL)
                    cv2.resizeWindow("Detected QR", resized_dims[1], resized_dims[0])
                    cv2.imshow("Detected QR", img)
                    if show == "single":
                        cv2.waitKey(0)
                    else:
                        cv2.waitKey(1)
                except: # preview image using matplotlib
                    plt.figure(figsize=(resized_dims[0]/100, resized_dims[1]/100))
                    plt.imshow(img[:,:,::-1]) # convert BGR to RGB
                    plt.title("Detected QR")
                    if show == "single":
                        plt.waitforbuttonpress()
                    else:
                        plt.pause(0.001)
                    plt.close()
            
        else:
            # print("Could NOT QR code in the image!!!") # print this in red bold color
            print("%sCould NOT find QR code in the image!!!%s" % ("\033[1;31m", "\033[0m"))
        return data
    

# Example usage

# import cv2
# from readQR_weChat import readQR
# if __name__ == "__main__":
#     im = cv2.imread("images/single_qr.jpeg")
#     qr = ReadQR()
#     data = qr.decode(im, show="single")
#     [print(data[i]) for i in range(len(data))]