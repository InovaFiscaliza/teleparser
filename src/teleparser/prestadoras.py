from collections import namedtuple

Prestadora = namedtuple(
    "Prestadora", ["nome", "cnpj", "mnc", "mcc"], defaults=(None, None, None, "724")
)
PRESTADORAS = {
    0: Prestadora(nome="CLARO S.A.", cnpj="40432544000147", mnc="00"),
    1: Prestadora(
        nome="Sisteer Do Brasil Telecomunicações Ltda", cnpj="13420027000185", mnc="01"
    ),
    2: Prestadora(nome="TIM S/A", cnpj="02421421000111", mnc="02"),
    3: Prestadora(nome="TIM S/A", cnpj="02421421000111", mnc="03"),
    4: Prestadora(nome="TIM S/A", cnpj="02421421000111", mnc="04"),
    5: Prestadora(nome="CLARO S.A.", cnpj="40432544000147", mnc="05"),
    6: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="06"),
    7: Prestadora(
        nome="TERAPAR TELECOMUNICAÇÕES LTDA", cnpj="14840419000166", mnc="07"
    ),
    8: Prestadora(nome="Transatel Brasil Ltda.", cnpj="51042993000103", mnc="08"),
    9: Prestadora(
        nome="Virgin Mobile Telecomunicaçoes Ltda", cnpj="13892589000121", mnc="09"
    ),
    10: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="10"),
    11: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="11"),
    12: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="12"),
    13: Prestadora(nome="NEXT LEVEL TELECOM LTDA.", cnpj="20877748000184", mnc="13"),
    14: Prestadora(nome="CLARO S.A.", cnpj="40432544000147", mnc="14"),
    15: Prestadora(nome="SERCOMTEL CELULAR S.A.", cnpj="02494988000118", mnc="15"),
    16: Prestadora(
        nome="OI MÓVEL S.A. - EM RECUPERAÇÃO JUDICIAL", cnpj="05423963000111", mnc="16"
    ),
    17: Prestadora(nome="SURF TELECOM SA", cnpj="10455746000143", mnc="17"),
    18: Prestadora(
        nome="DATORA MOBILE TELECOMUNICACOES S.A", cnpj="18384930000151", mnc="18"
    ),
    19: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="19"),
    21: Prestadora(nome="LIGUE TELECOMUNICAÇÕES LTDA", cnpj="10442435000140", mnc="21"),
    23: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="23"),
    26: Prestadora(nome="AMERICA NET LTDA", cnpj="01778972000174", mnc="26"),
    27: Prestadora(
        nome="VMNO COMUNICAÇÕES DO BRASIL S.A.", cnpj="13481715000155", mnc="27"
    ),
    28: Prestadora(nome="CLARO S.A.", cnpj="40432544000147", mnc="28"),
    29: Prestadora(
        nome="UNIFIQUE TELECOMUNICACOES S/A", cnpj="02255187000108", mnc="29"
    ),
    30: Prestadora(
        nome="OI MÓVEL S.A. - EM RECUPERAÇÃO JUDICIAL", cnpj="05423963000111", mnc="30"
    ),
    31: Prestadora(nome="TIM S/A", cnpj="02421421000111", mnc="31"),
    32: Prestadora(nome="ALGAR TELECOM S/A", cnpj="71208516000174", mnc="32"),
    33: Prestadora(nome="ALGAR TELECOM S/A", cnpj="71208516000174", mnc="33"),
    34: Prestadora(nome="ALGAR TELECOM S/A", cnpj="71208516000174", mnc="34"),
    36: Prestadora(nome="Options Comp & Elet Ltda", cnpj="00063329000100", mnc="36"),
    38: Prestadora(nome="CLARO S.A.", cnpj="40432544000147", mnc="38"),
    39: Prestadora(
        nome="Claro NXT Telecomunicações LTDA", cnpj="66970229000167", mnc="39"
    ),
    40: Prestadora(
        nome="TELEXPERTS TELECOMUNICAÇÕES LTDA", cnpj="07625852000113", mnc="40"
    ),
    41: Prestadora(nome="Digaa Telecom Ltda", cnpj="24331791000109", mnc="41"),
    42: Prestadora(nome="TELEFONICA BRASIL S.A.", cnpj="02558157000162", mnc="42"),
    46: Prestadora(nome="CUBIC TELECOM BRASIL LTDA", cnpj="31904804000149", mnc="46"),
    51: Prestadora(nome="EMNIFY BRASIL LTDA", cnpj="45953596000182", mnc="51"),
    54: Prestadora(nome="TIM S/A", cnpj="02421421000111", mnc="54"),
    70: Prestadora(nome="IEZ! TELECOM LTDA.", cnpj="37278419000110", mnc="70"),
    72: Prestadora(
        nome="AIRNITY BRASIL TELECOMUNICAÇÕES LTDA", cnpj="50667694000193", mnc="72"
    ),
    77: Prestadora(
        nome="Brisanet Serviços de Telecomunicações SA", cnpj="04601397000128", mnc="77"
    ),
    88: Prestadora(nome="CONNECT IOT SOLUTIONS LTDA", cnpj="52842561000131", mnc="88"),
}
