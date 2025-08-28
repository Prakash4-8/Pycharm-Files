class Mobile:
    def __init__(self, model, ram, memory):
        self._model = model  # protected member
        self.__ram = ram  # private member
        self._memory = memory
    def get_model(self):
        return self._model

    def get_ram(self):
        return self.__ram

    def get_memory(self):
        return self._memory
    def set_ram(self, new_ram):
        self.__ram = new_ram

samsung = Mobile('M30s', '4GB', '64GB')
print(samsung.get_ram())
samsung.set_ram('6GB')
print(samsung.get_ram())
