# IOS Resizer
This is a simple python app to resize a logo for all the required sizes by xcode when building an ios / ipad app

## How to use it?

### Run it:
* pip3 install tk ttkthemes pillow
* python3 ResizerIOS.py

### Turn it into a MacOS app:
* pip3 install -U py2app
* py2app --make-setup ResizerIOS.py
* python3 setup.py py2app

* Navigate to the "dist" folder
* Click on "ResizerIOS"
