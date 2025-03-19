from functools import wraps
from .primitives import UnsignedInt, DigitString, Ia5String


def fixed_size_unsigned_int(size):
    """Factory function to create UnsignedInt classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            UnsignedInt.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != UnsignedInt.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator


def fixed_size_digit_string(size):
    """Factory function to create DigitString classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            DigitString.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != DigitString.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator


def fixed_size_ia5_string(size):
    """Factory function to create DigitString classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            Ia5String.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != Ia5String.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator
