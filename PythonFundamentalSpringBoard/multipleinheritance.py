class MobilePhone:
    def __init__(self, memory):
        self.memory = memory
class Camera:
    def take_picture(self):
        print('say cheesy!')
class CameraPhone(MobilePhone, Camera):
    pass
android = CameraPhone('64GB')
print(android.memory)
android.take_picture()