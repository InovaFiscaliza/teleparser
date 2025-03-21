from ..primitives import Ia5String


class ExchangeIdentity(Ia5String):
    """Exchange Identity

      This parameter contains the identity (name) of the
      exchange where the output is initiated.

    ASN.1 Formal Description
        ExchangeIdentity ::= IA5STRING (SIZE(1..15))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |  1st character                        | octet 1
        /---------------------------------------/
        .
        .
        .
        /---------------------------------------/
        |  14th character                       | octet 14
        +---------------------------------------+
        |  15th character                       | octet 15
        /---------------------------------------/
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=1, upper=15)


class Route(Ia5String):
    """ASN.1 Formal Description
    Route ::= IA5STRING (SIZE(1..7))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |            1st character              | octet 1
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |            6th character              | octet 6
    +---------------------------------------+
    |            7th character              | octet 7
    /---------------------------------------/
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=1, upper=7)
