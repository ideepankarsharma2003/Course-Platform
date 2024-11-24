import cloudinary
from decouple import config # quite similar to os.environ.get ---> but not quite same

CLOUDINARY_CLOUD_NAME= config("CLOUDINARY_CLOUD_NAME", default="")
CLOUDINARY_API_KEY= config("CLOUDINARY_API_KEY", default="828288495573486")
CLOUDINARY_API_SECRET= config("CLOUDINARY_API_SECRET", default="")



def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_API_KEY, 
        api_secret = CLOUDINARY_API_SECRET, # Click 'View API Keys' above to copy your API secret
        secure=True
    )
