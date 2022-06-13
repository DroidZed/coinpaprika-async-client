class ResponseObject:

    __slots__ = {"_status_code", "_data"}

    def __init__(self, status_code: int = None, data: dict = None):
        self._status_code = status_code
        self._data = data

    def __str__(self):
        return f"data: \n{self._data}\nstatus_code: {self._status_code}"

    def __repr__(self):
        return f"data: \n{self._data}\nstatus_code: {self._status_code}"

    @property
    def status_code(self):
        return self._status_code

    @property
    def data(self):
        return self._data

    @status_code.setter
    def status_code(self, code: int):
        self._status_code = code

    @data.setter
    def data(self, data: dict):
        self._data = data
