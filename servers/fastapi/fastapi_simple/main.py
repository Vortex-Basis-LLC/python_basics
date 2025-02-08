import os

from simple_app import simple_app_setup

static_img_file_path = os.path.abspath("../../../assets/images")
print("STATIC IMG PATH: ", static_img_file_path)

app = simple_app_setup.setup_app(static_img_file_path = static_img_file_path)