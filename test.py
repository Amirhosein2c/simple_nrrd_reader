import numpy as np
import nrrd
# from PIL import Image
import cv2

filename = "./Guenette_FN_CISS_Subject_09.nrrd"
filedata, fileheader = nrrd.read(filename)
print("fileheader", fileheader)
print("filedata", filedata.shape)

for i in range(filedata.shape[2]):
    _slice = filedata[:,:,i]
    print(type(_slice))
    print(_slice.shape)
    slice = (_slice.astype(np.float64)-_slice.min()) / (_slice.max()-_slice.min())
    slice = slice.astype('float32')
    cv2.imshow("raw image", slice)
    cv2.waitKey(30)
    cv2.imwrite("slice_" + str(i).zfill(3)+ ".jpg", slice*255, [cv2.IMWRITE_JPEG_QUALITY, 100])
    # cv2.imwrite("slice_" + str(i).zfill(3)+ ".png", slice*255)
cv2.destroyAllWindows
