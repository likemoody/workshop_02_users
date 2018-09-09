class Validator:
    EXPECTED_TYPE_ERROR = "Expected type is {} but got {}"
    NUMBER_SMALLER_THEN_ZERO = "Value {} is smaller then 0"

    def __get_message(self, expected_type, current_type):
        return self.EXPECTED_TYPE_ERROR.format(expected_type, current_type)

    @staticmethod
    def validate_is_str(self, value):
        if not isinstance(value, str):
            raise TypeError(self.__get_message(str, type(value)))
        return value

    @staticmethod
    def validate_is_float(self, value):
        if not isinstance(value, float):
            raise TypeError(self.__get_message(float, type(value)))
        return value

    @staticmethod
    def validate_is_int(self, value):
        if not isinstance(value, int):
            raise TypeError(self.__get_message(int, type(value)))
        return value

    @staticmethod
    def validate_is_positive_number(self, value):
        if value < 0:
            raise ValueError(self.NUMBER_SMALLER_THEN_ZERO.format(value.__doc__))
        return value
