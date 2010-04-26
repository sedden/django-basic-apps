from imagekit.specs import ImageSpec 
from imagekit import processors 

# first we define our thumbnail resize processor 
class ResizeThumb(processors.Resize): 
    width = 120 
    height = 120 
    crop = True

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 1024

# now lets create an adjustment processor to enhance the image at small sizes 
class EnchanceThumb(processors.Adjustment): 
    contrast = 1.2 
    sharpness = 1.1 

# now we can define our thumbnail spec 
class Thumbnail(ImageSpec): 
    pre_cache = True 
    processors = [ResizeThumb, EnchanceThumb] 

# and our display spec
class Display(ImageSpec):
    processors = [ResizeDisplay]
