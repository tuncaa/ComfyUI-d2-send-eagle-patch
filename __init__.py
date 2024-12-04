"""
@author: da2el
@title: D2 Send Eagle
@description: Send images to Eagle, an image management application
"""

# from .send_eagle import SendEagle
from .D2_SendEagle import D2_SendEagle

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "D2 Send Eagle patch": D2_SendEagle_patch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "D2 Send Eagle patch": "D2 Send Eagle patch",
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
