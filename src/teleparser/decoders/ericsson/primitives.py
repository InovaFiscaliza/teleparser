class OctetString:
    def __init__(self, octets, size: int = None):
        if size and size > len(octets):
            raise ValueError("size parameter is bigger than octets length")
        self.string = octets.hex().upper()
