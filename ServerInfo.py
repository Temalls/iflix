#ServerInfo.py

class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'vipserver'
        if self.get.lower() == 'about':
            return 'linux version'
        if self.get.lower() == 'ver':
            return 'Vip01'
        if self.get.lower() == 'date':
            return '06-10-2019'
        if self.get.lower() == 'by':
            return 'Temalls'
        if self.get.lower() == 'mail':
            return 'slametjuliyanto4@gmail.com'