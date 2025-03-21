"""This module implement simple datatypes inherited from the primitives
It's organized here because it's just the boilerplate of the type name and its description
"""

from . import primitives


@primitives.fixed_size_unsigned_int(1)
class ChargingOrigin(primitives.UnsignedInt):
    """ASN.1 Formal Description
    ChargingOrigin ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned integer.
    Values vary according to operator's definition.
    Value range: H'1 - H'7F
    """


@primitives.fixed_size_unsigned_int(2)
class CUGIndex(primitives.UnsignedInt):
    """CUG Index

    The Closed User Group (CUG) Index contains the code that
    indicates a closed user group for the subscriber. The CUG
    Index has significance only between the subscriber and
    network. The value of the parameter corresponds to the
    same CUG as parameter CUG Interlock Code.

    ASN.1 Formal Description
      CUGIndex ::= OCTET STRING (SIZE(2))
      |    |    |    |    |    |    |    |    |
      |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
      |    |    |    |    |    |    |    |    |
      /---------------------------------------/
      | MSB                                   |  octet 1
      +---------------------------------------+
      |                                    LSB|  octet 2
      /---------------------------------------/
      Note: The OCTET STRING is coded as an unsigned integer.
      Value range:  H'0 - H'7FFF
    """


@primitives.fixed_size_ia5_string(15)
class ExchangeIdentity(primitives.Ia5String):
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


@primitives.fixed_size_unsigned_int(2)
class FaultCode(primitives.UnsignedInt):
    """Fault Code

      This parameter contains the internal End-of-Selection
      code (EOS), which defines the event that lead to
      disconnection of the call component.

      Fault codes are also present for successful calls. It
      can be determined from the EOS code if a fault occurred
      or not.

    ASN.1 Formal Description
        FaultCode ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |MSB                                    |  octet 1
        +---------------------------------------+
        |                                    LSB|  octet 2
        /---------------------------------------/
        Note: OCTET STRING is coded as an unsigned integer.
        Note: Detailed information on fault code values is
        available in the Application Information "List
        Of End-Of-Selection Codes".
    """


@primitives.fixed_size_unsigned_int(1)
class PartialOutputRecNum(primitives.UnsignedInt):
    """Partial Output Record Number

      This parameter contains a consecutive number which is
      incremented at every partial output for a call.

      It appears only if partial output has taken place.
    ASN.1 Formal Description
        PartialOutputRecNum ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                              LSB  |
        /---------------------------------------/
        Note: OCTET STRING is coded as an unsigned integer.
        Value range: H'1 - H'FF
    """


@primitives.fixed_size_unsigned_int(3)
class RecordSequenceNumber(primitives.UnsignedInt):
    r"""Record Sequence Number  (M)

    This parameter contains a consecutive number for each
    Call Data Record generated and output.
    ASN.1 Formal Description

    RecordSequenceNumber ::= OCTET STRING (SIZE(3))

    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------\
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                       | octet 2
    +---------------------------------------+
    |                                  LSB  | octet 3
    \---------------------------------------/

    Note: OCTET STRING is coded as an unsigned integer.

    Value range: H'0 - H'FFFFFF"""


@primitives.fixed_size_unsigned_int(1)
class RedirectionCounter(primitives.UnsignedInt):
    """ASN.1 Formal Description
    RedirectionCounter ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                              LSB  |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Values     Meaning
    0 - 10     Number of redirections
    Note: The maximum value is set by an
    Exchange Parameter.
    """


class RerountingIndicator(primitives.Bool):
    """Rerouting Indicator

    This parameter indicates if the call has been rerouted
    (for example a new B-number analysis has been performed)
    by the exchange where the charging data is output. This
    field is output only for ISOCODE or PACKED postprocessing
    purposes.
    """


@primitives.fixed_size_ia5_string(7)
class Route(primitives.Ia5String):
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


@primitives.fixed_size_unsigned_int(1)
class SubscriptionType(primitives.UnsignedInt):
    """Subscription Type

      This parameter indicates the subscription type used for
      mobile subscriber. This parameter enables grouping
      of mobile subscribers independent of their numbers.

      The parameter values are defined by operator. The value
      '0' is output if the feature 'Support for Subscription
      Type Dependent Analysis' is not active in the (G)MSC.

    ASN.1 Formal Description
        SubscriptionType ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |                                       |
        /---------------------------------------/
        Value range: H'0 - H'7F
        Value H'0 : No subscription type
        Value H'1 - H'7F : Subscription type 1 - 127
    """


@primitives.fixed_size_unsigned_int(2)
class SwitchIdentity(primitives.UnsignedInt):
    """Switch Identity

      This parameter contains the identification
      number of the exchange where the output originated.

      This parameter is part of the Network Call Reference
      (NCR). Switch Identity in NCR identifies the exchange
      where the NCR has been generated. Thus, this parameter
      can be used to determine whether the own exchange
      generated the NCR or the NCR was received from the
      incoming network.

    ASN.1 Formal Description
        SwitchIdentity ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                                   |   octet 1
        +---------------------------------------|
        |                                   LSB |   octet 2
        /---------------------------------------/
        Note: OCTET STRING is coded internally as
        an unsigned integer.
        Value range: H'1 - H'FFFF
    """


@primitives.fixed_size_unsigned_int(1)
class TypeOfCallingSubscriber(primitives.UnsignedInt):
    """Type of Calling Subscriber

    This parameter indicates that the type of subscriber is
    registered, for example, normal subscriber, subscriber
    with priority, or coin box.

    In case of a network-initiated USSD service request,
    this parameter contains the type of served subscriber in
    the Subscriber Service Procedure Call Module.

    When a call is routed from the SSF/gsmSSF, the parameter
    may be modified by SCF/gsmSCF.
    """
