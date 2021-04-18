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
    # im = Image.fromarray(np.uint8(slice))
    slice = (slice.astype(np.float64)-slice.min())*255.0 / (slice.max()-slice.min())
    im = Image.fromarray(slice)
    im.show()
    im.save("slice_" + str(i).zfill(3)+ ".jpg", quality=95, subsampling=0)
    print(type(im))



# datashape = fileheader{}





# data = np.linspace(1, 50, 50)
# nrrd.write('output.nrrd', data)

# data2, header = nrrd.read('output.nrrd')
# print(np.all(data == data2))