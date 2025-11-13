class Tour:
    def __init__(self, __id__, price, _days):
        self.__id__ = __id__
        self._price = price
        self._days = _days
        self. _is_booked =True/False
        self. _client = None
        
    @property
    def id(self):
        return self.__id__
