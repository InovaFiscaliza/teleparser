
from .string.digit import ServiceKey
from .boolean import Bool
from .enums import TriggerDetectionPoint
from .string.octet import (
    GlobalTitle,
    GlobalTitleAndSubSystemNumber,
    PointCodeAndSubSystemNumber,
)


# class TriggerData(UserDict):
#     """Trigger Data

#     The Trigger data parameter stores data for each SCF
#     invocation.

#     The trigger data is sent to Charging Data Output when
#     a dialogue towards an SCF has been opened as a result
#     of processing an armed Trigger Detection Point (TDP).
#     The first data will be stored in TriggerData 0. In the
#     case of several dialogues resulting from processing of
#     armed TDPs in the same call then each will produce
#     trigger data to Call Data Output by using the first
#     free number of Trigger Data.

#     Note that if criteria for invoking a dialogue towards
#     the SCF is not met during the call then no Trigger Data
#     will be sent to Call Data Output. Trigger Data applies
#     to CAMEL calls, extended CAMEL calls and to IN calls.

#      The Trigger data are built up of the following:

#      - Trigger Detection Point

#        This parameter indicates at what point in the
#        call the SCF invocation took place.

#      - Service Key

#        The Service key is sent to the SCF in the Initial
#        Detection Point Operation. It is used as a
#        reference by the SCF.

#      - SCP Address

#        The SCP address includes the full network address of
#        the SCF/gsmSCF used for sending the Initial Detection
#        Point operation.
#     """

#     def __init__(self):
#         super().__init__(
#             {
#                 0: {"name": "triggerDetectionPoint", "type": TriggerDetectionPoint},
#                 1: {"name": "serviceKey", "type": ServiceKey},
#                 2: {"name": "sCPAddress.co-located", "type": Bool},
#                 3: {
#                     "name": "sCPAddress.pointCodeAndSubSystemNumber",
#                     "type": PointCodeAndSubSystemNumber,
#                 },
#                 4: {"name": "sCPAddress.globalTitle", "type": GlobalTitle},
#                 5: {
#                     "name": "sCPAddress.globalTitleAndSubSystemNumber",
#                     "type": GlobalTitleAndSubSystemNumber,
#                 },
#             }
#         )


TriggerData = {
    0: {"name": "triggerDetectionPoint", "type": TriggerDetectionPoint},
    1: {"name": "serviceKey", "type": ServiceKey},
    2: {"name": "sCPAddress.co-located", "type": Bool},
    3: {
        "name": "sCPAddress.pointCodeAndSubSystemNumber",
        "type": PointCodeAndSubSystemNumber,
    },
    4: {"name": "sCPAddress.globalTitle", "type": GlobalTitle},
    5: {
        "name": "sCPAddress.globalTitleAndSubSystemNumber",
        "type": GlobalTitleAndSubSystemNumber,
    },
}
