class MobilePhone:
    def __init__(self, displaysize, ram, os):
        self.display_size = displaysize
        self.ram = ram
        self.os = os


motrolla = MobilePhone(5.5, '4GB', 'Android 11')
samsung = MobilePhone(6.5, '4GB', "Android 12")
print(
    'The new motrolla phone has a {} inch display. {} of RAM and runs on the latest version of {}. It\'s biggest '
    'competitor is the Samsung Phone `which supports a similar AMOLED {} inch display, {} of RAM and runs {}.'.format(
        motrolla.display_size, motrolla.ram, motrolla.os, samsung.display_size, samsung.ram, samsung.os))
