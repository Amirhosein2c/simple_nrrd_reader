import numpy as np
import nrrd
from PIL import Image

filename = "./Guenette_FN_CISS_Subject_09.nrrd"
filedata, fileheader = nrrd.read(filename)
print("fileheader", fileheader)
print("filedata", filedata.shape)

for i in range(filedata.shape[2]):
    slice = filedata[:,:,i]
    print(type(slice))
    print(slice.shape)
    slice = (slice.astype(np.float64)-slice.min())*255.0 / (slice.max()-slice.min())
    im = Image.fromarray(slice)
    im.show()
    im = im.convert("L")
    # im.save("./slice_" + str(i).zfill(3)+ ".png")
    im.save("slice_" + str(i).zfill(3)+ ".jpg", quality=95, subsampling=0)
    print(type(im))
