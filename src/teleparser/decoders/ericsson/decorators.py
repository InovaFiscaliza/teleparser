from functools import wraps
from .datatypes.primitives import UnsignedInt


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
