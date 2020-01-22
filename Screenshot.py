from PIL import Image

class Screenshot:
    def __init__(self, driver):
        self.driver = driver

    def capture(self, element, filelocation):
        location = element.location
        size = element.size
        self.driver.save_screenshot(filelocation)
        x = location['x']
        y = location['y']
        width = location['x'] + size['width']
        height = location['y'] + size['height']
        im = Image.open(filelocation)
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save(filelocation)