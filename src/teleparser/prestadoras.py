from collections import namedtuple

Prestadora = namedtuple(
    "Prestadora",
    ["nome", "cnpj", "mnc", "mcc", "pais"],
    defaults=(None, None, None, "724", "Brazil"),
)
PRESTADORAS: dict[tuple[str, str], Prestadora] = {
    ("00", "724"): Prestadora(
        nome="CLARO S.A.", cnpj="40432544000147", mnc="00", mcc="724", pais="Brazil"
    ),
    ("01", "724"): Prestadora(
        nome="Sisteer Do Brasil Telecomunicações Ltda",
        cnpj="13420027000185",
        mnc="01",
        mcc="724",
        pais="Brazil",
    ),
    ("02", "724"): Prestadora(
        nome="TIM S/A", cnpj="02421421000111", mnc="02", mcc="724", pais="Brazil"
    ),
    ("03", "724"): Prestadora(
        nome="TIM S/A", cnpj="02421421000111", mnc="03", mcc="724", pais="Brazil"
    ),
    ("04", "724"): Prestadora(
        nome="TIM S/A", cnpj="02421421000111", mnc="04", mcc="724", pais="Brazil"
    ),
    ("05", "724"): Prestadora(
        nome="CLARO S.A.", cnpj="40432544000147", mnc="05", mcc="724", pais="Brazil"
    ),
    ("06", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="06",
        mcc="724",
        pais="Brazil",
    ),
    ("07", "724"): Prestadora(
        nome="TERAPAR TELECOMUNICAÇÕES LTDA",
        cnpj="14840419000166",
        mnc="07",
        mcc="724",
        pais="Brazil",
    ),
    ("08", "724"): Prestadora(
        nome="Transatel Brasil Ltda.",
        cnpj="51042993000103",
        mnc="08",
        mcc="724",
        pais="Brazil",
    ),
    ("09", "724"): Prestadora(
        nome="Virgin Mobile Telecomunicaçoes Ltda",
        cnpj="13892589000121",
        mnc="09",
        mcc="724",
        pais="Brazil",
    ),
    ("10", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="10",
        mcc="724",
        pais="Brazil",
    ),
    ("11", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="11",
        mcc="724",
        pais="Brazil",
    ),
    ("12", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="12",
        mcc="724",
        pais="Brazil",
    ),
    ("13", "724"): Prestadora(
        nome="NEXT LEVEL TELECOM LTDA.",
        cnpj="20877748000184",
        mnc="13",
        mcc="724",
        pais="Brazil",
    ),
    ("14", "724"): Prestadora(
        nome="CLARO S.A.", cnpj="40432544000147", mnc="14", mcc="724", pais="Brazil"
    ),
    ("15", "724"): Prestadora(
        nome="SERCOMTEL CELULAR S.A.",
        cnpj="02494988000118",
        mnc="15",
        mcc="724",
        pais="Brazil",
    ),
    ("16", "724"): Prestadora(
        nome="OI MÓVEL S.A. - EM RECUPERAÇÃO JUDICIAL",
        cnpj="05423963000111",
        mnc="16",
        mcc="724",
        pais="Brazil",
    ),
    ("17", "724"): Prestadora(
        nome="SURF TELECOM SA",
        cnpj="10455746000143",
        mnc="17",
        mcc="724",
        pais="Brazil",
    ),
    ("18", "724"): Prestadora(
        nome="DATORA MOBILE TELECOMUNICACOES S.A",
        cnpj="18384930000151",
        mnc="18",
        mcc="724",
        pais="Brazil",
    ),
    ("19", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="19",
        mcc="724",
        pais="Brazil",
    ),
    ("21", "724"): Prestadora(
        nome="LIGUE TELECOMUNICAÇÕES LTDA",
        cnpj="10442435000140",
        mnc="21",
        mcc="724",
        pais="Brazil",
    ),
    ("23", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="23",
        mcc="724",
        pais="Brazil",
    ),
    ("26", "724"): Prestadora(
        nome="AMERICA NET LTDA",
        cnpj="01778972000174",
        mnc="26",
        mcc="724",
        pais="Brazil",
    ),
    ("27", "724"): Prestadora(
        nome="VMNO COMUNICAÇÕES DO BRASIL S.A.",
        cnpj="13481715000155",
        mnc="27",
        mcc="724",
        pais="Brazil",
    ),
    ("28", "724"): Prestadora(
        nome="CLARO S.A.", cnpj="40432544000147", mnc="28", mcc="724", pais="Brazil"
    ),
    ("29", "724"): Prestadora(
        nome="UNIFIQUE TELECOMUNICACOES S/A",
        cnpj="02255187000108",
        mnc="29",
        mcc="724",
        pais="Brazil",
    ),
    ("30", "724"): Prestadora(
        nome="OI MÓVEL S.A. - EM RECUPERAÇÃO JUDICIAL",
        cnpj="05423963000111",
        mnc="30",
        mcc="724",
        pais="Brazil",
    ),
    ("31", "724"): Prestadora(
        nome="TIM S/A", cnpj="02421421000111", mnc="31", mcc="724", pais="Brazil"
    ),
    ("32", "724"): Prestadora(
        nome="ALGAR TELECOM S/A",
        cnpj="71208516000174",
        mnc="32",
        mcc="724",
        pais="Brazil",
    ),
    ("33", "724"): Prestadora(
        nome="ALGAR TELECOM S/A",
        cnpj="71208516000174",
        mnc="33",
        mcc="724",
        pais="Brazil",
    ),
    ("34", "724"): Prestadora(
        nome="ALGAR TELECOM S/A",
        cnpj="71208516000174",
        mnc="34",
        mcc="724",
        pais="Brazil",
    ),
    ("36", "724"): Prestadora(
        nome="Options Comp & Elet Ltda",
        cnpj="00063329000100",
        mnc="36",
        mcc="724",
        pais="Brazil",
    ),
    ("38", "724"): Prestadora(
        nome="CLARO S.A.", cnpj="40432544000147", mnc="38", mcc="724", pais="Brazil"
    ),
    ("39", "724"): Prestadora(
        nome="Claro NXT Telecomunicações LTDA",
        cnpj="66970229000167",
        mnc="39",
        mcc="724",
        pais="Brazil",
    ),
    ("40", "724"): Prestadora(
        nome="TELEXPERTS TELECOMUNICAÇÕES LTDA",
        cnpj="07625852000113",
        mnc="40",
        mcc="724",
        pais="Brazil",
    ),
    ("41", "724"): Prestadora(
        nome="Digaa Telecom Ltda",
        cnpj="24331791000109",
        mnc="41",
        mcc="724",
        pais="Brazil",
    ),
    ("42", "724"): Prestadora(
        nome="TELEFONICA BRASIL S.A.",
        cnpj="02558157000162",
        mnc="42",
        mcc="724",
        pais="Brazil",
    ),
    ("46", "724"): Prestadora(
        nome="CUBIC TELECOM BRASIL LTDA",
        cnpj="31904804000149",
        mnc="46",
        mcc="724",
        pais="Brazil",
    ),
    ("51", "724"): Prestadora(
        nome="EMNIFY BRASIL LTDA",
        cnpj="45953596000182",
        mnc="51",
        mcc="724",
        pais="Brazil",
    ),
    ("54", "724"): Prestadora(
        nome="TIM S/A", cnpj="02421421000111", mnc="54", mcc="724", pais="Brazil"
    ),
    ("70", "724"): Prestadora(
        nome="IEZ! TELECOM LTDA.",
        cnpj="37278419000110",
        mnc="70",
        mcc="724",
        pais="Brazil",
    ),
    ("72", "724"): Prestadora(
        nome="AIRNITY BRASIL TELECOMUNICAÇÕES LTDA",
        cnpj="50667694000193",
        mnc="72",
        mcc="724",
        pais="Brazil",
    ),
    ("77", "724"): Prestadora(
        nome="Brisanet Serviços de Telecomunicações SA",
        cnpj="04601397000128",
        mnc="77",
        mcc="724",
        pais="Brazil",
    ),
    ("88", "724"): Prestadora(
        nome="CONNECT IOT SOLUTIONS LTDA",
        cnpj="52842561000131",
        mnc="88",
        mcc="724",
        pais="Brazil",
    ),
    ("01", "412"): Prestadora(nome="AWCC", mnc="01", mcc="412", pais="Afghanistan"),
    ("20", "412"): Prestadora(nome="Roshan", mnc="20", mcc="412", pais="Afghanistan"),
    ("40", "412"): Prestadora(
        nome="Areeba Afghanistan", mnc="40", mcc="412", pais="Afghanistan"
    ),
    ("50", "412"): Prestadora(nome="Etisalat", mnc="50", mcc="412", pais="Afghanistan"),
    ("80", "412"): Prestadora(
        nome="Afghan Telecom", mnc="80", mcc="412", pais="Afghanistan"
    ),
    ("88", "412"): Prestadora(
        nome="Afghan Telecom", mnc="88", mcc="412", pais="Afghanistan"
    ),
    ("01", "276"): Prestadora(
        nome="ONE TELECOMMUNICATIONS  sh.a",
        mnc="01",
        mcc="276",
        pais="Albania",
    ),
    ("02", "276"): Prestadora(
        nome="Vodafone Albania", mnc="02", mcc="276", pais="Albania"
    ),
    ("03", "276"): Prestadora(
        nome="ALBTELECOM sh.a.", mnc="03", mcc="276", pais="Albania"
    ),
    ("01", "603"): Prestadora(
        nome="Algérie Télécom Mobile « ATM » / GSM/public",
        mnc="01",
        mcc="603",
        pais="Algeria",
    ),
    ("02", "603"): Prestadora(
        nome="Optimum Télécom Algérie « OTA » / GSM/public",
        mnc="02",
        mcc="603",
        pais="Algeria",
    ),
    ("03", "603"): Prestadora(
        nome="Wataniya Télécom Algérie « WTA » / GSM/public",
        mnc="03",
        mcc="603",
        pais="Algeria",
    ),
    ("07", "603"): Prestadora(
        nome="Algérie Télécom « AT » / WLL / public",
        mnc="07",
        mcc="603",
        pais="Algeria",
    ),
    ("09", "603"): Prestadora(
        nome="Algérie Télécom « AT » / LTE Fixe / public",
        mnc="09",
        mcc="603",
        pais="Algeria",
    ),
    ("03", "213"): Prestadora(nome="Mobiland", mnc="03", mcc="213", pais="Andorra"),
    ("02", "631"): Prestadora(nome="Unitel", mnc="02", mcc="631", pais="Angola"),
    ("04", "631"): Prestadora(nome="Movicel", mnc="04", mcc="631", pais="Angola"),
    ("05", "631"): Prestadora(nome="AFRICELL", mnc="05", mcc="631", pais="Angola"),
    ("010", "365"): Prestadora(
        nome="Weblinks Limited", mnc="010", mcc="365", pais="Anguilla"
    ),
    ("840", "365"): Prestadora(
        nome="Cable and Wireless (Anguilla) Ltd trading as Lime",
        mnc="840",
        mcc="365",
        pais="Anguilla",
    ),
    ("030", "344"): Prestadora(
        nome="APUA PCS", mnc="030", mcc="344", pais="Antigua and Barbuda"
    ),
    ("920", "344"): Prestadora(
        nome="Cable & Wireless (Antigua) trading as Lime",
        mnc="920",
        mcc="344",
        pais="Antigua and Barbuda",
    ),
    ("930", "344"): Prestadora(
        nome="AT&T Wireless (Antigua)",
        mnc="930",
        mcc="344",
        pais="Antigua and Barbuda",
    ),
    ("010", "722"): Prestadora(
        nome="Compañia de Radiocomunicaciones Moviles S.A.",
        mnc="010",
        mcc="722",
        pais="Argentina",
    ),
    ("020", "722"): Prestadora(
        nome="Nextel Argentina srl", mnc="020", mcc="722", pais="Argentina"
    ),
    ("070", "722"): Prestadora(
        nome="Telefónica Comunicaciones Personales S.A.",
        mnc="070",
        mcc="722",
        pais="Argentina",
    ),
    ("310", "722"): Prestadora(
        nome="CTI PCS S.A.", mnc="310", mcc="722", pais="Argentina"
    ),
    ("320", "722"): Prestadora(
        nome="Compañia de Telefonos del Interior Norte S.A.",
        mnc="320",
        mcc="722",
        pais="Argentina",
    ),
    ("330", "722"): Prestadora(
        nome="Compañia de Telefonos del Interior S.A.",
        mnc="330",
        mcc="722",
        pais="Argentina",
    ),
    ("341", "722"): Prestadora(
        nome="Telecom Personal S.A.", mnc="341", mcc="722", pais="Argentina"
    ),
    ("01", "363"): Prestadora(nome="SETAR N.V.", mnc="01", mcc="363", pais="Aruba"),
    ("02", "363"): Prestadora(nome="DIGICEL ARUBA", mnc="02", mcc="363", pais="Aruba"),
    ("01", "505"): Prestadora(
        nome="Telstra Corporation Ltd.",
        mnc="01",
        mcc="505",
        pais="Australia",
    ),
    ("02", "505"): Prestadora(
        nome="Optus Mobile Pty. Ltd.", mnc="02", mcc="505", pais="Australia"
    ),
    ("03", "505"): Prestadora(
        nome="Vodafone Network Pty. Ltd.",
        mnc="03",
        mcc="505",
        pais="Australia",
    ),
    ("04", "505"): Prestadora(
        nome="Department of Defence", mnc="04", mcc="505", pais="Australia"
    ),
    ("05", "505"): Prestadora(
        nome="The Ozitel Network Pty. Ltd.",
        mnc="05",
        mcc="505",
        pais="Australia",
    ),
    ("06", "505"): Prestadora(
        nome="Hutchison 3G Australia Pty. Ltd.",
        mnc="06",
        mcc="505",
        pais="Australia",
    ),
    ("07", "505"): Prestadora(
        nome="Vodafone Network Pty. Ltd.",
        mnc="07",
        mcc="505",
        pais="Australia",
    ),
    ("08", "505"): Prestadora(
        nome="One.Tel GSM 1800 Pty. Ltd.",
        mnc="08",
        mcc="505",
        pais="Australia",
    ),
    ("09", "505"): Prestadora(
        nome="Airnet Commercial Australia Ltd.",
        mnc="09",
        mcc="505",
        pais="Australia",
    ),
    ("10", "505"): Prestadora(
        nome="Norfolk Telecom", mnc="10", mcc="505", pais="Australia"
    ),
    ("11", "505"): Prestadora(
        nome="Telstra Corporation Ltd.",
        mnc="11",
        mcc="505",
        pais="Australia",
    ),
    ("12", "505"): Prestadora(
        nome="Vodafone Hutchison Australia Pty Ltd",
        mnc="12",
        mcc="505",
        pais="Australia",
    ),
    ("13", "505"): Prestadora(nome="Railcorp", mnc="13", mcc="505", pais="Australia"),
    ("14", "505"): Prestadora(nome="AAPT Ltd", mnc="14", mcc="505", pais="Australia"),
    ("15", "505"): Prestadora(
        nome="3GIS Pty Ltd. (Telstra & Hutchison 3G)",
        mnc="15",
        mcc="505",
        pais="Australia",
    ),
    ("16", "505"): Prestadora(
        nome="Victorian Rail Track", mnc="16", mcc="505", pais="Australia"
    ),
    ("17", "505"): Prestadora(
        nome="Vivid Wireless Pty Ltd", mnc="17", mcc="505", pais="Australia"
    ),
    ("19", "505"): Prestadora(
        nome="Lycamobile Pty Ltd", mnc="19", mcc="505", pais="Australia"
    ),
    ("20", "505"): Prestadora(
        nome="Ausgrid Corporation", mnc="20", mcc="505", pais="Australia"
    ),
    ("21", "505"): Prestadora(
        nome="Queensland Rail Limited", mnc="21", mcc="505", pais="Australia"
    ),
    ("22", "505"): Prestadora(nome="iiNet Ltd", mnc="22", mcc="505", pais="Australia"),
    ("23", "505"): Prestadora(
        nome="Challenge Networks Pty Ltd",
        mnc="23",
        mcc="505",
        pais="Australia",
    ),
    ("24", "505"): Prestadora(
        nome="Advanced Communications Technologies Pty. Ltd.",
        mnc="24",
        mcc="505",
        pais="Australia",
    ),
    ("25", "505"): Prestadora(
        nome="Pilbara Iron Company Services Pty Ltd",
        mnc="25",
        mcc="505",
        pais="Australia",
    ),
    ("26", "505"): Prestadora(
        nome="Dialogue Communications Pty Ltd",
        mnc="26",
        mcc="505",
        pais="Australia",
    ),
    ("27", "505"): Prestadora(
        nome="Nexium Telecommunications",
        mnc="27",
        mcc="505",
        pais="Australia",
    ),
    ("28", "505"): Prestadora(
        nome="RCOM International Pty Ltd",
        mnc="28",
        mcc="505",
        pais="Australia",
    ),
    ("30", "505"): Prestadora(
        nome="Compatel Limited", mnc="30", mcc="505", pais="Australia"
    ),
    ("31", "505"): Prestadora(
        nome="BHP Billiton", mnc="31", mcc="505", pais="Australia"
    ),
    ("32", "505"): Prestadora(
        nome="Thales Australia", mnc="32", mcc="505", pais="Australia"
    ),
    ("33", "505"): Prestadora(
        nome="CLX Networks Pty Ltd", mnc="33", mcc="505", pais="Australia"
    ),
    ("34", "505"): Prestadora(nome="Santos Ltd", mnc="34", mcc="505", pais="Australia"),
    ("35", "505"): Prestadora(
        nome="MessageBird Pty Ltd", mnc="35", mcc="505", pais="Australia"
    ),
    ("36", "505"): Prestadora(
        nome="Optus Mobile Pty. Ltd.", mnc="36", mcc="505", pais="Australia"
    ),
    ("37", "505"): Prestadora(
        nome="Yancoal Australia Ltd", mnc="37", mcc="505", pais="Australia"
    ),
    ("38", "505"): Prestadora(
        nome="Truphone Pty Ltd", mnc="38", mcc="505", pais="Australia"
    ),
    ("39", "505"): Prestadora(
        nome="Telstra Corporation Ltd.",
        mnc="39",
        mcc="505",
        pais="Australia",
    ),
    ("40", "505"): Prestadora(
        nome="CITIC PACIFIC MINING", mnc="40", mcc="505", pais="Australia"
    ),
    ("41", "505"): Prestadora(
        nome="Aqura Technologies Pty", mnc="41", mcc="505", pais="Australia"
    ),
    ("42", "505"): Prestadora(
        nome="Groote Eylandt Mining Company Pty Ltd",
        mnc="42",
        mcc="505",
        pais="Australia",
    ),
    ("43", "505"): Prestadora(
        nome="Arrow Energy Pty Ltd", mnc="43", mcc="505", pais="Australia"
    ),
    ("44", "505"): Prestadora(
        nome="ROY HILL IRON ORE PTY LTD",
        mnc="44",
        mcc="505",
        pais="Australia",
    ),
    ("45", "505"): Prestadora(
        nome="CLERMONT COAL OPERATIONS PTY Limited",
        mnc="45",
        mcc="505",
        pais="Australia",
    ),
    ("46", "505"): Prestadora(
        nome="ANGLOGOLD ASHANTI AUSTRALIA LTD",
        mnc="46",
        mcc="505",
        pais="Australia",
    ),
    ("47", "505"): Prestadora(
        nome="Woodside Energy Limited", mnc="47", mcc="505", pais="Australia"
    ),
    ("48", "505"): Prestadora(
        nome="Titan ICT Pty Ltd", mnc="48", mcc="505", pais="Australia"
    ),
    ("49", "505"): Prestadora(
        nome="Field Solutions Group Pty Ltd",
        mnc="49",
        mcc="505",
        pais="Australia",
    ),
    ("50", "505"): Prestadora(
        nome="Pivotel Group Pty Limited",
        mnc="50",
        mcc="505",
        pais="Australia",
    ),
    ("51", "505"): Prestadora(
        nome="Fortescue Metals Group Ltd",
        mnc="51",
        mcc="505",
        pais="Australia",
    ),
    ("52", "505"): Prestadora(
        nome="Optitel Pty Ltd", mnc="52", mcc="505", pais="Australia"
    ),
    ("53", "505"): Prestadora(
        nome="Shell Australia Pty Ltd", mnc="53", mcc="505", pais="Australia"
    ),
    ("55", "505"): Prestadora(
        nome="New South Wales Government Telecommunications Authority",
        mnc="55",
        mcc="505",
        pais="Australia",
    ),
    ("56", "505"): Prestadora(
        nome="Nokia Solutions and Networks Pty Ltd",
        mnc="56",
        mcc="505",
        pais="Australia",
    ),
    ("57", "505"): Prestadora(
        nome="CiFi Pty Ltd", mnc="57", mcc="505", pais="Australia"
    ),
    ("61", "505"): Prestadora(
        nome="Commtel Network Solutions Pty Ltd",
        mnc="61",
        mcc="505",
        pais="Australia",
    ),
    ("62", "505"): Prestadora(
        nome="NBNCo Limited", mnc="62", mcc="505", pais="Australia"
    ),
    ("68", "505"): Prestadora(
        nome="NBNCo Limited", mnc="68", mcc="505", pais="Australia"
    ),
    ("71", "505"): Prestadora(
        nome="Telstra Corporation Ltd.",
        mnc="71",
        mcc="505",
        pais="Australia",
    ),
    ("72", "505"): Prestadora(
        nome="Telstra Corporation Ltd.",
        mnc="72",
        mcc="505",
        pais="Australia",
    ),
    ("88", "505"): Prestadora(
        nome="Pivotel Group Pty Limited",
        mnc="88",
        mcc="505",
        pais="Australia",
    ),
    ("90", "505"): Prestadora(
        nome="UE Access Pty Ltd", mnc="90", mcc="505", pais="Australia"
    ),
    ("99", "505"): Prestadora(
        nome="One.Tel GSM 1800 Pty. Ltd.",
        mnc="99",
        mcc="505",
        pais="Australia",
    ),
    ("01", "232"): Prestadora(
        nome="A1 Telekom Austria AG", mnc="01", mcc="232", pais="Austria"
    ),
    ("02", "232"): Prestadora(
        nome="A1 Telekom Austria AG", mnc="02", mcc="232", pais="Austria"
    ),
    ("03", "232"): Prestadora(
        nome="T-Mobile Austria GmbH", mnc="03", mcc="232", pais="Austria"
    ),
    ("04", "232"): Prestadora(
        nome="T-Mobile Austria GmbH", mnc="04", mcc="232", pais="Austria"
    ),
    ("05", "232"): Prestadora(
        nome="Hutchison Drei Austria GmbH",
        mnc="05",
        mcc="232",
        pais="Austria",
    ),
    ("07", "232"): Prestadora(
        nome="T-Mobile Austria GmbH", mnc="07", mcc="232", pais="Austria"
    ),
    ("08", "232"): Prestadora(
        nome="Lycamobile Austria Ltd", mnc="08", mcc="232", pais="Austria"
    ),
    ("09", "232"): Prestadora(
        nome="A1 Telekom Austria AG", mnc="09", mcc="232", pais="Austria"
    ),
    ("10", "232"): Prestadora(
        nome="Hutchison Drei Austria GmbH",
        mnc="10",
        mcc="232",
        pais="Austria",
    ),
    ("11", "232"): Prestadora(
        nome="A1 Telekom Austria AG", mnc="11", mcc="232", pais="Austria"
    ),
    ("12", "232"): Prestadora(
        nome="A1 Telekom Austria AG", mnc="12", mcc="232", pais="Austria"
    ),
    ("13", "232"): Prestadora(
        nome="UPC Austria Services GmbH", mnc="13", mcc="232", pais="Austria"
    ),
    ("14", "232"): Prestadora(
        nome="Hutchison Drei Austria GmbH",
        mnc="14",
        mcc="232",
        pais="Austria",
    ),
    ("15", "232"): Prestadora(
        nome="Mundio Mobile (Austria) Ltd",
        mnc="15",
        mcc="232",
        pais="Austria",
    ),
    ("16", "232"): Prestadora(
        nome="Hutchison Drei Austria GmbH",
        mnc="16",
        mcc="232",
        pais="Austria",
    ),
    ("17", "232"): Prestadora(
        nome="MASS Response Service GmbH",
        mnc="17",
        mcc="232",
        pais="Austria",
    ),
    ("18", "232"): Prestadora(
        nome="smartspace GmbH", mnc="18", mcc="232", pais="Austria"
    ),
    ("19", "232"): Prestadora(
        nome="Tele2 Telecommunication GmbH",
        mnc="19",
        mcc="232",
        pais="Austria",
    ),
    ("20", "232"): Prestadora(
        nome="Mtel Austrija GmbH", mnc="20", mcc="232", pais="Austria"
    ),
    ("91", "232"): Prestadora(
        nome="ÖBB - Infrastruktur AG", mnc="91", mcc="232", pais="Austria"
    ),
    ("01", "400"): Prestadora(
        nome='Azercell Telecom" LLC"', mnc="01", mcc="400", pais="Azerbaijan"
    ),
    ("02", "400"): Prestadora(
        nome='Bakcell" LLC"', mnc="02", mcc="400", pais="Azerbaijan"
    ),
    ("03", "400"): Prestadora(
        nome='Catel" LLC"', mnc="03", mcc="400", pais="Azerbaijan"
    ),
    ("04", "400"): Prestadora(
        nome='Azerfon" LLC"', mnc="04", mcc="400", pais="Azerbaijan"
    ),
    ("05", "400"): Prestadora(
        nome="Special State Protection Service of the Republic of Azerbaijan",
        mnc="05",
        mcc="400",
        pais="Azerbaijan",
    ),
    ("06", "400"): Prestadora(
        nome='Nakhtel" LLC"', mnc="06", mcc="400", pais="Azerbaijan"
    ),
    ("39", "364"): Prestadora(
        nome="Bahamas Telecommunications Company Limited",
        mnc="39",
        mcc="364",
        pais="Bahamas",
    ),
    ("49", "364"): Prestadora(
        nome="NewCo2015 Limited", mnc="49", mcc="364", pais="Bahamas"
    ),
    ("01", "426"): Prestadora(
        nome="Bahrain Telecommunications Company (BATELCO)",
        mnc="01",
        mcc="426",
        pais="Bahrain",
    ),
    ("02", "426"): Prestadora(nome="Zain Bahrain", mnc="02", mcc="426", pais="Bahrain"),
    ("03", "426"): Prestadora(
        nome="Civil Aviation Authority", mnc="03", mcc="426", pais="Bahrain"
    ),
    ("04", "426"): Prestadora(nome="STC Bahrain", mnc="04", mcc="426", pais="Bahrain"),
    ("05", "426"): Prestadora(nome="Royal Court", mnc="05", mcc="426", pais="Bahrain"),
    ("06", "426"): Prestadora(nome="STC Bahrain", mnc="06", mcc="426", pais="Bahrain"),
    ("07", "426"): Prestadora(nome="TAIF", mnc="07", mcc="426", pais="Bahrain"),
    ("01", "470"): Prestadora(
        nome="GramenPhone", mnc="01", mcc="470", pais="Bangladesh"
    ),
    ("02", "470"): Prestadora(nome="Aktel", mnc="02", mcc="470", pais="Bangladesh"),
    ("03", "470"): Prestadora(
        nome="Mobile 2000", mnc="03", mcc="470", pais="Bangladesh"
    ),
    ("600", "342"): Prestadora(
        nome="Cable & Wireless", mnc="600", mcc="342", pais="Barbados"
    ),
    ("646", "342"): Prestadora(
        nome="KW Telecommunications Inc.",
        mnc="646",
        mcc="342",
        pais="Barbados",
    ),
    ("800", "342"): Prestadora(nome="Ozone", mnc="800", mcc="342", pais="Barbados"),
    ("820", "342"): Prestadora(
        nome="Neptune Communications Inc.",
        mnc="820",
        mcc="342",
        pais="Barbados",
    ),
    ("01", "257"): Prestadora(nome="MDC Velcom", mnc="01", mcc="257", pais="Belarus"),
    ("02", "257"): Prestadora(nome="MTS", mnc="02", mcc="257", pais="Belarus"),
    ("03", "257"): Prestadora(
        nome="BelCel Joint Venture (JV)", mnc="03", mcc="257", pais="Belarus"
    ),
    ("04", "257"): Prestadora(
        nome='Closed joint-stock company Belarusian telecommunication network""',
        mnc="04",
        mcc="257",
        pais="Belarus",
    ),
    ("05", "257"): Prestadora(
        nome="Republican Unitary Telecommunication Enterprise (RUE) Beltelecom (National Telecommunications Operator of the Republic of Belarus)",
        mnc="05",
        mcc="257",
        pais="Belarus",
    ),
    ("06", "257"): Prestadora(
        nome="Belorussian Cloud Technologies",
        mnc="06",
        mcc="257",
        pais="Belarus",
    ),
    ("01", "206"): Prestadora(nome="Proximus", mnc="01", mcc="206", pais="Belgium"),
    ("02", "206"): Prestadora(nome="N.M.B.S", mnc="02", mcc="206", pais="Belgium"),
    ("03", "206"): Prestadora(nome="Citymesh", mnc="03", mcc="206", pais="Belgium"),
    ("04", "206"): Prestadora(
        nome="MWINGZ (Proximus/Orange Belgium)",
        mnc="04",
        mcc="206",
        pais="Belgium",
    ),
    ("05", "206"): Prestadora(nome="Telenet", mnc="05", mcc="206", pais="Belgium"),
    ("06", "206"): Prestadora(
        nome="Lycamobile sprl", mnc="06", mcc="206", pais="Belgium"
    ),
    ("07", "206"): Prestadora(
        nome="Mundio Mobile Belgium nv", mnc="07", mcc="206", pais="Belgium"
    ),
    ("08", "206"): Prestadora(nome="Nethys", mnc="08", mcc="206", pais="Belgium"),
    ("10", "206"): Prestadora(
        nome="Orange Belgium", mnc="10", mcc="206", pais="Belgium"
    ),
    ("11", "206"): Prestadora(
        nome="L-Mobi Mobile", mnc="11", mcc="206", pais="Belgium"
    ),
    ("20", "206"): Prestadora(
        nome="Telenet Group", mnc="20", mcc="206", pais="Belgium"
    ),
    ("22", "206"): Prestadora(nome="FEBO Telecom", mnc="22", mcc="206", pais="Belgium"),
    ("25", "206"): Prestadora(nome="Voyacom", mnc="25", mcc="206", pais="Belgium"),
    ("28", "206"): Prestadora(nome="BICS SA", mnc="28", mcc="206", pais="Belgium"),
    ("29", "206"): Prestadora(nome="TISMI", mnc="29", mcc="206", pais="Belgium"),
    ("30", "206"): Prestadora(nome="Unleashed", mnc="30", mcc="206", pais="Belgium"),
    ("33", "206"): Prestadora(
        nome="Ericsson *test use only*", mnc="33", mcc="206", pais="Belgium"
    ),
    ("34", "206"): Prestadora(nome="ONOFFAPP", mnc="34", mcc="206", pais="Belgium"),
    ("50", "206"): Prestadora(nome="IP Nexia", mnc="50", mcc="206", pais="Belgium"),
    ("77", "270"): Prestadora(
        nome="Proximus Luxembourg S.A.", mnc="77", mcc="270", pais="Belgium"
    ),
    ("99", "206"): Prestadora(
        nome="e-BO Enterprises", mnc="99", mcc="206", pais="Belgium"
    ),
    ("99", "270"): Prestadora(
        nome="Orange Communications Luxembourg S.A.",
        mnc="99",
        mcc="270",
        pais="Belgium",
    ),
    ("67", "702"): Prestadora(
        nome="Belize Telecommunications Ltd., GSM 1900",
        mnc="67",
        mcc="702",
        pais="Belize",
    ),
    ("69", "702"): Prestadora(
        nome="SMART/Speednet Communications Ltd.",
        mnc="69",
        mcc="702",
        pais="Belize",
    ),
    ("01", "616"): Prestadora(nome="Libercom", mnc="01", mcc="616", pais="Benin"),
    ("02", "616"): Prestadora(nome="Telecel", mnc="02", mcc="616", pais="Benin"),
    ("03", "616"): Prestadora(nome="Spacetel Benin", mnc="03", mcc="616", pais="Benin"),
    ("000", "350"): Prestadora(
        nome="Bermuda Digital Communications Ltd (CellOne)",
        mnc="000",
        mcc="350",
        pais="Bermuda",
    ),
    ("05", "350"): Prestadora(
        nome="Telecom Networks", mnc="05", mcc="350", pais="Bermuda"
    ),
    ("007", "350"): Prestadora(
        nome="Paradise Mobile", mnc="007", mcc="350", pais="Bermuda"
    ),
    ("11", "350"): Prestadora(nome="Deltronics", mnc="11", mcc="350", pais="Bermuda"),
    ("15", "350"): Prestadora(nome="FKB Net Ltd.", mnc="15", mcc="350", pais="Bermuda"),
    ("11", "402"): Prestadora(
        nome="Bhutan Telecom Limited (Bmobile)",
        mnc="11",
        mcc="402",
        pais="Bhutan",
    ),
    ("17", "402"): Prestadora(
        nome="Bhutan Telecom Limited (Bmobile)",
        mnc="17",
        mcc="402",
        pais="Bhutan",
    ),
    ("77", "402"): Prestadora(
        nome="Tashi InfoComm Limited (Tashi Cell)",
        mnc="77",
        mcc="402",
        pais="Bhutan",
    ),
    ("01", "736"): Prestadora(
        nome="Nuevatel S.A.",
        mnc="01",
        mcc="736",
        pais="Bolivia (Plurinational State of)",
    ),
    ("02", "736"): Prestadora(
        nome="ENTEL S.A.",
        mnc="02",
        mcc="736",
        pais="Bolivia (Plurinational State of)",
    ),
    ("03", "736"): Prestadora(
        nome="Telecel S.A.",
        mnc="03",
        mcc="736",
        pais="Bolivia (Plurinational State of)",
    ),
    ("03", "218"): Prestadora(
        nome="Eronet Mobile Communications Ltd.",
        mnc="03",
        mcc="218",
        pais="Bosnia and Herzegovina",
    ),
    ("05", "218"): Prestadora(
        nome="MOBI'S (Mobilina Srpske)",
        mnc="05",
        mcc="218",
        pais="Bosnia and Herzegovina",
    ),
    ("90", "218"): Prestadora(
        nome="GSMBIH", mnc="90", mcc="218", pais="Bosnia and Herzegovina"
    ),
    ("01", "652"): Prestadora(
        nome="Mascom Wireless (Pty) Ltd",
        mnc="01",
        mcc="652",
        pais="Botswana",
    ),
    ("02", "652"): Prestadora(
        nome="Orange Botswana (Pty) Ltd",
        mnc="02",
        mcc="652",
        pais="Botswana",
    ),
    ("04", "652"): Prestadora(
        nome="Botswana Telecommunications Corporation (BTC)",
        mnc="04",
        mcc="652",
        pais="Botswana",
    ),
    ("24", "724"): Prestadora(
        nome="AMAZONIA CELULAR", mnc="24", mcc="724", pais="Brazil"
    ),
    ("35", "724"): Prestadora(nome="TELCOM", mnc="35", mcc="724", pais="Brazil"),
    ("37", "724"): Prestadora(nome="UNICEL", mnc="37", mcc="724", pais="Brazil"),
    ("99", "724"): Prestadora(nome="LOCAL (STFC)", mnc="99", mcc="724", pais="Brazil"),
    ("170", "348"): Prestadora(
        nome="Cable & Wireless (BVI) Ltd trading as lime",
        mnc="170",
        mcc="348",
        pais="British Virgin Islands",
    ),
    ("370", "348"): Prestadora(
        nome="BVI Cable TV Ltd",
        mnc="370",
        mcc="348",
        pais="British Virgin Islands",
    ),
    ("570", "348"): Prestadora(
        nome="Caribbean Cellular Telephone Ltd.",
        mnc="570",
        mcc="348",
        pais="British Virgin Islands",
    ),
    ("770", "348"): Prestadora(
        nome="Digicel (BVI) Ltd",
        mnc="770",
        mcc="348",
        pais="British Virgin Islands",
    ),
    ("01", "528"): Prestadora(
        nome="Telekom Brunei Berhad (TelBru)",
        mnc="01",
        mcc="528",
        pais="Brunei Darussalam",
    ),
    ("02", "528"): Prestadora(
        nome="Progresif Cellular Sdn Bhd (PCSB)",
        mnc="02",
        mcc="528",
        pais="Brunei Darussalam",
    ),
    ("03", "528"): Prestadora(
        nome="Unified National Networks Sdn Bhd (UNN)",
        mnc="03",
        mcc="528",
        pais="Brunei Darussalam",
    ),
    ("11", "528"): Prestadora(
        nome="DST Com", mnc="11", mcc="528", pais="Brunei Darussalam"
    ),
    ("01", "284"): Prestadora(
        nome="Mobiltel EAD", mnc="01", mcc="284", pais="Bulgaria"
    ),
    ("05", "284"): Prestadora(nome="Globul", mnc="05", mcc="284", pais="Bulgaria"),
    ("02", "613"): Prestadora(nome="Celtel", mnc="02", mcc="613", pais="Burkina Faso"),
    ("03", "613"): Prestadora(nome="Telecel", mnc="03", mcc="613", pais="Burkina Faso"),
    ("01", "642"): Prestadora(nome="Econet", mnc="01", mcc="642", pais="Burundi"),
    ("02", "642"): Prestadora(nome="Africell", mnc="02", mcc="642", pais="Burundi"),
    ("03", "642"): Prestadora(nome="ONAMOB", mnc="03", mcc="642", pais="Burundi"),
    ("07", "642"): Prestadora(nome="LACELL", mnc="07", mcc="642", pais="Burundi"),
    ("82", "642"): Prestadora(nome="U.COM", mnc="82", mcc="642", pais="Burundi"),
    ("01", "625"): Prestadora(
        nome="Cabo Verde Telecom", mnc="01", mcc="625", pais="Cabo Verde"
    ),
    ("02", "625"): Prestadora(
        nome="T+Telecomunicações", mnc="02", mcc="625", pais="Cabo Verde"
    ),
    ("01", "456"): Prestadora(
        nome="Mobitel (Cam GSM)", mnc="01", mcc="456", pais="Cambodia"
    ),
    ("02", "456"): Prestadora(nome="Hello", mnc="02", mcc="456", pais="Cambodia"),
    ("03", "456"): Prestadora(
        nome="S Telecom (CDMA)", mnc="03", mcc="456", pais="Cambodia"
    ),
    ("04", "456"): Prestadora(nome="Cadcomms", mnc="04", mcc="456", pais="Cambodia"),
    ("05", "456"): Prestadora(nome="Starcell", mnc="05", mcc="456", pais="Cambodia"),
    ("06", "456"): Prestadora(nome="Smart", mnc="06", mcc="456", pais="Cambodia"),
    ("08", "456"): Prestadora(nome="Viettel", mnc="08", mcc="456", pais="Cambodia"),
    ("18", "456"): Prestadora(nome="Mfone", mnc="18", mcc="456", pais="Cambodia"),
    ("01", "624"): Prestadora(
        nome="Mobile Telephone Networks Cameroon",
        mnc="01",
        mcc="624",
        pais="Cameroon",
    ),
    ("02", "624"): Prestadora(
        nome="Orange Cameroun", mnc="02", mcc="624", pais="Cameroon"
    ),
    ("04", "624"): Prestadora(
        nome="NEXTTEL (ex VIETTEL CAMEROON)",
        mnc="04",
        mcc="624",
        pais="Cameroon",
    ),
    ("100", "302"): Prestadora(
        nome="Data on Tap Inc.", mnc="100", mcc="302", pais="Canada"
    ),
    ("130", "302"): Prestadora(
        nome="Xplornet Communications", mnc="130", mcc="302", pais="Canada"
    ),
    ("131", "302"): Prestadora(
        nome="Xplornet Communications", mnc="131", mcc="302", pais="Canada"
    ),
    ("140", "302"): Prestadora(
        nome="Fibernetics Corporation", mnc="140", mcc="302", pais="Canada"
    ),
    ("150", "302"): Prestadora(
        nome="Cogeco Connexion Inc.", mnc="150", mcc="302", pais="Canada"
    ),
    ("151", "302"): Prestadora(
        nome="Cogeco Connexion Inc.", mnc="151", mcc="302", pais="Canada"
    ),
    ("152", "302"): Prestadora(
        nome="Cogeco Connexion Inc.", mnc="152", mcc="302", pais="Canada"
    ),
    ("220", "302"): Prestadora(
        nome="Telus Mobility", mnc="220", mcc="302", pais="Canada"
    ),
    ("221", "302"): Prestadora(
        nome="Telus Mobility", mnc="221", mcc="302", pais="Canada"
    ),
    ("222", "302"): Prestadora(
        nome="Telus Mobility", mnc="222", mcc="302", pais="Canada"
    ),
    ("230", "302"): Prestadora(nome="ISP Telecom", mnc="230", mcc="302", pais="Canada"),
    ("250", "302"): Prestadora(
        nome="Bell Mobility", mnc="250", mcc="302", pais="Canada"
    ),
    ("270", "302"): Prestadora(
        nome="Bragg Communications", mnc="270", mcc="302", pais="Canada"
    ),
    ("300", "302"): Prestadora(nome="ECOTEL inc.", mnc="300", mcc="302", pais="Canada"),
    ("320", "302"): Prestadora(
        nome="Dave Wireless", mnc="320", mcc="302", pais="Canada"
    ),
    ("340", "302"): Prestadora(nome="Execulink", mnc="340", mcc="302", pais="Canada"),
    ("350", "302"): Prestadora(
        nome="Naskapi Imuun Inc.", mnc="350", mcc="302", pais="Canada"
    ),
    ("360", "302"): Prestadora(
        nome="Telus Mobility", mnc="360", mcc="302", pais="Canada"
    ),
    ("370", "302"): Prestadora(nome="Microcell", mnc="370", mcc="302", pais="Canada"),
    ("380", "302"): Prestadora(
        nome="Dryden Mobility", mnc="380", mcc="302", pais="Canada"
    ),
    ("390", "302"): Prestadora(
        nome="Dryden Mobility", mnc="390", mcc="302", pais="Canada"
    ),
    ("420", "302"): Prestadora(
        nome="A.B.C. Allen Business Communications Ltd.",
        mnc="420",
        mcc="302",
        pais="Canada",
    ),
    ("490", "302"): Prestadora(
        nome="Globalive Wireless", mnc="490", mcc="302", pais="Canada"
    ),
    ("491", "302"): Prestadora(
        nome="Freedom Mobile Inc.", mnc="491", mcc="302", pais="Canada"
    ),
    ("500", "302"): Prestadora(
        nome="Videotron Ltd", mnc="500", mcc="302", pais="Canada"
    ),
    ("510", "302"): Prestadora(
        nome="Videotron Ltd", mnc="510", mcc="302", pais="Canada"
    ),
    ("530", "302"): Prestadora(
        nome="Keewatinook Okimacinac", mnc="530", mcc="302", pais="Canada"
    ),
    ("550", "302"): Prestadora(
        nome="Star Solutions International Inc.",
        mnc="550",
        mcc="302",
        pais="Canada",
    ),
    ("560", "302"): Prestadora(
        nome="Lynx Mobility", mnc="560", mcc="302", pais="Canada"
    ),
    ("570", "302"): Prestadora(
        nome="Ligado Networks Corp.", mnc="570", mcc="302", pais="Canada"
    ),
    ("590", "302"): Prestadora(
        nome="Quadro Communication", mnc="590", mcc="302", pais="Canada"
    ),
    ("600", "302"): Prestadora(
        nome="Iristel Inc.", mnc="600", mcc="302", pais="Canada"
    ),
    ("610", "302"): Prestadora(
        nome="Bell Mobility", mnc="610", mcc="302", pais="Canada"
    ),
    ("620", "302"): Prestadora(
        nome="Ice Wireless", mnc="620", mcc="302", pais="Canada"
    ),
    ("630", "302"): Prestadora(
        nome="Aliant Mobility", mnc="630", mcc="302", pais="Canada"
    ),
    ("640", "302"): Prestadora(
        nome="Bell Mobility", mnc="640", mcc="302", pais="Canada"
    ),
    ("650", "302"): Prestadora(nome="Tbaytel", mnc="650", mcc="302", pais="Canada"),
    ("660", "302"): Prestadora(
        nome="MTS Mobility", mnc="660", mcc="302", pais="Canada"
    ),
    ("670", "302"): Prestadora(
        nome="CityTel Mobility", mnc="670", mcc="302", pais="Canada"
    ),
    ("680", "302"): Prestadora(
        nome="Sask Tel Mobility", mnc="680", mcc="302", pais="Canada"
    ),
    ("681", "302"): Prestadora(
        nome="SaskTel Mobility", mnc="681", mcc="302", pais="Canada"
    ),
    ("690", "302"): Prestadora(
        nome="Bell Mobility", mnc="690", mcc="302", pais="Canada"
    ),
    ("710", "302"): Prestadora(nome="Globalstar", mnc="710", mcc="302", pais="Canada"),
    ("720", "302"): Prestadora(
        nome="Rogers Wireless", mnc="720", mcc="302", pais="Canada"
    ),
    ("721", "302"): Prestadora(
        nome="Rogers Communications Canada Inc. (Wireless)",
        mnc="721",
        mcc="302",
        pais="Canada",
    ),
    ("730", "302"): Prestadora(
        nome="TerreStar Solutions", mnc="730", mcc="302", pais="Canada"
    ),
    ("740", "302"): Prestadora(
        nome="Rogers Communications Canada Inc.",
        mnc="740",
        mcc="302",
        pais="Canada",
    ),
    ("741", "302"): Prestadora(
        nome="Rogers Communications Canada Inc.",
        mnc="741",
        mcc="302",
        pais="Canada",
    ),
    ("760", "302"): Prestadora(
        nome="Public Mobile Inc", mnc="760", mcc="302", pais="Canada"
    ),
    ("770", "302"): Prestadora(
        nome="TNW Wireless Inc.", mnc="770", mcc="302", pais="Canada"
    ),
    ("780", "302"): Prestadora(
        nome="Sask Tel Mobility", mnc="780", mcc="302", pais="Canada"
    ),
    ("781", "302"): Prestadora(
        nome="SaskTel Mobility", mnc="781", mcc="302", pais="Canada"
    ),
    ("848", "302"): Prestadora(
        nome="Vocom International Telecommunications, Inc",
        mnc="848",
        mcc="302",
        pais="Canada",
    ),
    ("860", "302"): Prestadora(
        nome="Telus Mobility", mnc="860", mcc="302", pais="Canada"
    ),
    ("880", "302"): Prestadora(
        nome="Telus/Bell shared", mnc="880", mcc="302", pais="Canada"
    ),
    ("910", "302"): Prestadora(
        nome="Halton Regional Police", mnc="910", mcc="302", pais="Canada"
    ),
    ("940", "302"): Prestadora(
        nome="Wightman Telecom", mnc="940", mcc="302", pais="Canada"
    ),
    ("990", "302"): Prestadora(nome="Test", mnc="990", mcc="302", pais="Canada"),
    ("996", "302"): Prestadora(
        nome="Powertech Labs (experimental)",
        mnc="996",
        mcc="302",
        pais="Canada",
    ),
    ("998", "302"): Prestadora(
        nome="Institut de Recherche d’Hydro-Québec (experimental)",
        mnc="998",
        mcc="302",
        pais="Canada",
    ),
    ("001", "346"): Prestadora(
        nome="WestTel Ltd., trading as Logic",
        mnc="001",
        mcc="346",
        pais="Cayman Islands",
    ),
    ("140", "346"): Prestadora(
        nome="Cable & Wireless (Cayman) trading as Lime",
        mnc="140",
        mcc="346",
        pais="Cayman Islands",
    ),
    ("01", "623"): Prestadora(
        nome="Centrafrique Telecom Plus (CTP)",
        mnc="01",
        mcc="623",
        pais="Central African Rep.",
    ),
    ("02", "623"): Prestadora(
        nome="Telecel Centrafrique (TC)",
        mnc="02",
        mcc="623",
        pais="Central African Rep.",
    ),
    ("03", "623"): Prestadora(
        nome="Celca (Socatel)",
        mnc="03",
        mcc="623",
        pais="Central African Rep.",
    ),
    ("01", "622"): Prestadora(nome="Celtel", mnc="01", mcc="622", pais="Chad"),
    ("02", "622"): Prestadora(nome="Tchad Mobile", mnc="02", mcc="622", pais="Chad"),
    ("01", "730"): Prestadora(
        nome="Entel Telefónica Móvil", mnc="01", mcc="730", pais="Chile"
    ),
    ("02", "730"): Prestadora(
        nome="Telefónica Móvil", mnc="02", mcc="730", pais="Chile"
    ),
    ("03", "730"): Prestadora(nome="Smartcom", mnc="03", mcc="730", pais="Chile"),
    ("04", "730"): Prestadora(
        nome="Centennial Cayman Corp. Chile S.A.",
        mnc="04",
        mcc="730",
        pais="Chile",
    ),
    ("05", "730"): Prestadora(nome="Multikom S.A.", mnc="05", mcc="730", pais="Chile"),
    ("06", "730"): Prestadora(
        nome="Blue Two Chile SA", mnc="06", mcc="730", pais="Chile"
    ),
    ("07", "730"): Prestadora(
        nome="Telefónica Móviles Chile S.A.",
        mnc="07",
        mcc="730",
        pais="Chile",
    ),
    ("08", "730"): Prestadora(nome="VTR Móvil S.A.", mnc="08", mcc="730", pais="Chile"),
    ("09", "730"): Prestadora(
        nome="Centennial Cayman Corp. Chile S.A.",
        mnc="09",
        mcc="730",
        pais="Chile",
    ),
    ("10", "730"): Prestadora(nome="Entel", mnc="10", mcc="730", pais="Chile"),
    ("11", "730"): Prestadora(nome="Celupago S.A.", mnc="11", mcc="730", pais="Chile"),
    ("12", "730"): Prestadora(
        nome="Telestar Móvil S.A.", mnc="12", mcc="730", pais="Chile"
    ),
    ("13", "730"): Prestadora(
        nome="TRIBE Mobile Chile SPA", mnc="13", mcc="730", pais="Chile"
    ),
    ("14", "730"): Prestadora(
        nome="Netline Telefónica Móvil Ltda",
        mnc="14",
        mcc="730",
        pais="Chile",
    ),
    ("15", "730"): Prestadora(
        nome="CIBELES TELECOM S.A.", mnc="15", mcc="730", pais="Chile"
    ),
    ("16", "730"): Prestadora(
        nome="Nomade Telecomunicaciones S.A.",
        mnc="16",
        mcc="730",
        pais="Chile",
    ),
    ("17", "730"): Prestadora(
        nome="COMPATEL Chile Limitada", mnc="17", mcc="730", pais="Chile"
    ),
    ("18", "730"): Prestadora(
        nome="Empresas Bunker S.A.", mnc="18", mcc="730", pais="Chile"
    ),
    ("19", "730"): Prestadora(
        nome="Sociedad Falabella Móvil SPA",
        mnc="19",
        mcc="730",
        pais="Chile",
    ),
    ("20", "730"): Prestadora(
        nome="Inversiones Santa Fe Limitada",
        mnc="20",
        mcc="730",
        pais="Chile",
    ),
    ("21", "730"): Prestadora(nome="WILL S.A.", mnc="21", mcc="730", pais="Chile"),
    ("22", "730"): Prestadora(nome="CELLPLUS SPA", mnc="22", mcc="730", pais="Chile"),
    ("23", "730"): Prestadora(
        nome="CLARO SERVICIOS EMPRESARIALES S.A.",
        mnc="23",
        mcc="730",
        pais="Chile",
    ),
    ("26", "730"): Prestadora(nome="WILL S.A.", mnc="26", mcc="730", pais="Chile"),
    ("27", "730"): Prestadora(
        nome="Cibeles Telecom S.A.", mnc="27", mcc="730", pais="Chile"
    ),
    ("00", "460"): Prestadora(nome="China Mobile", mnc="00", mcc="460", pais="China"),
    ("01", "460"): Prestadora(nome="China Unicom", mnc="01", mcc="460", pais="China"),
    ("03", "460"): Prestadora(
        nome="China Unicom CDMA", mnc="03", mcc="460", pais="China"
    ),
    ("04", "460"): Prestadora(
        nome="China Satellite Global Star Network",
        mnc="04",
        mcc="460",
        pais="China",
    ),
    ("001", "732"): Prestadora(
        nome="Colombia Telecomunicaciones S.A. - Telecom",
        mnc="001",
        mcc="732",
        pais="Colombia",
    ),
    ("002", "732"): Prestadora(
        nome="Edatel S.A.", mnc="002", mcc="732", pais="Colombia"
    ),
    ("020", "732"): Prestadora(nome="Emtelsa", mnc="020", mcc="732", pais="Colombia"),
    ("099", "732"): Prestadora(nome="Emcali", mnc="099", mcc="732", pais="Colombia"),
    ("101", "732"): Prestadora(
        nome="Comcel S.A. Occel S.A./Celcaribe",
        mnc="101",
        mcc="732",
        pais="Colombia",
    ),
    ("102", "732"): Prestadora(
        nome="Bellsouth Colombia S.A.", mnc="102", mcc="732", pais="Colombia"
    ),
    ("103", "732"): Prestadora(
        nome="Colombia Móvil S.A.", mnc="103", mcc="732", pais="Colombia"
    ),
    ("111", "732"): Prestadora(
        nome="Colombia Móvil S.A.", mnc="111", mcc="732", pais="Colombia"
    ),
    ("123", "732"): Prestadora(
        nome="Telefónica Móviles Colombia S.A.",
        mnc="123",
        mcc="732",
        pais="Colombia",
    ),
    ("130", "732"): Prestadora(nome="Avantel", mnc="130", mcc="732", pais="Colombia"),
    ("01", "654"): Prestadora(
        nome="HURI / Comores Telecom", mnc="01", mcc="654", pais="Comoros"
    ),
    ("02", "654"): Prestadora(
        nome="TELMA / TELCO SA", mnc="02", mcc="654", pais="Comoros"
    ),
    ("01", "629"): Prestadora(nome="Celtel", mnc="01", mcc="629", pais="Congo"),
    ("10", "629"): Prestadora(
        nome="Libertis Telecom", mnc="10", mcc="629", pais="Congo"
    ),
    ("01", "548"): Prestadora(
        nome="Telecom Cook", mnc="01", mcc="548", pais="Cook Islands"
    ),
    ("01", "712"): Prestadora(
        nome="Instituto Costarricense de Electricidad - ICE",
        mnc="01",
        mcc="712",
        pais="Costa Rica",
    ),
    ("02", "712"): Prestadora(
        nome="Instituto Costarricense de Electricidad - ICE",
        mnc="02",
        mcc="712",
        pais="Costa Rica",
    ),
    ("03", "712"): Prestadora(
        nome="CLARO CR Telecomunicaciones S.A.",
        mnc="03",
        mcc="712",
        pais="Costa Rica",
    ),
    ("04", "712"): Prestadora(
        nome="Telefónica de Costa Rica TC, S.A.",
        mnc="04",
        mcc="712",
        pais="Costa Rica",
    ),
    ("20", "712"): Prestadora(nome="Virtualis", mnc="20", mcc="712", pais="Costa Rica"),
    ("02", "612"): Prestadora(
        nome="Atlantique Cellulaire",
        mnc="02",
        mcc="612",
        pais="Côte d'Ivoire",
    ),
    ("03", "612"): Prestadora(
        nome="Orange Côte d'Ivoire",
        mnc="03",
        mcc="612",
        pais="Côte d'Ivoire",
    ),
    ("04", "612"): Prestadora(
        nome="Comium Côte d'Ivoire",
        mnc="04",
        mcc="612",
        pais="Côte d'Ivoire",
    ),
    ("05", "612"): Prestadora(
        nome="Loteny Telecom", mnc="05", mcc="612", pais="Côte d'Ivoire"
    ),
    ("06", "612"): Prestadora(
        nome="Oricel Côte d'Ivoire",
        mnc="06",
        mcc="612",
        pais="Côte d'Ivoire",
    ),
    ("07", "612"): Prestadora(
        nome="Aircomm Côte d'Ivoire",
        mnc="07",
        mcc="612",
        pais="Côte d'Ivoire",
    ),
    ("01", "219"): Prestadora(
        nome="T-Mobile Hrvatska d.o.o./T-Mobile Croatia LLC",
        mnc="01",
        mcc="219",
        pais="Croatia",
    ),
    ("02", "219"): Prestadora(
        nome="Tele2/Tele2 d.o.o.", mnc="02", mcc="219", pais="Croatia"
    ),
    ("10", "219"): Prestadora(
        nome="VIPnet/VIPnet d.o.o.", mnc="10", mcc="219", pais="Croatia"
    ),
    ("01", "368"): Prestadora(nome="ETECSA", mnc="01", mcc="368", pais="Cuba"),
    ("51", "362"): Prestadora(nome="TELCELL GSM", mnc="51", mcc="362", pais="Curaçao"),
    ("69", "362"): Prestadora(nome="CT GSM", mnc="69", mcc="362", pais="Curaçao"),
    ("91", "362"): Prestadora(nome="SETEL GSM", mnc="91", mcc="362", pais="Curaçao"),
    ("01", "280"): Prestadora(nome="CYTA", mnc="01", mcc="280", pais="Cyprus"),
    ("02", "280"): Prestadora(nome="CYTA", mnc="02", mcc="280", pais="Cyprus"),
    ("10", "280"): Prestadora(
        nome="Scancom (Cyprus) Ltd.", mnc="10", mcc="280", pais="Cyprus"
    ),
    ("20", "280"): Prestadora(nome="PrimeTel PLC", mnc="20", mcc="280", pais="Cyprus"),
    ("22", "280"): Prestadora(nome="Lemontel Ltd", mnc="22", mcc="280", pais="Cyprus"),
    ("01", "230"): Prestadora(
        nome="T-Mobile Czech Republic a.s.",
        mnc="01",
        mcc="230",
        pais="Czech Rep.",
    ),
    ("02", "230"): Prestadora(
        nome="O2 Czech Republic a.s.", mnc="02", mcc="230", pais="Czech Rep."
    ),
    ("03", "230"): Prestadora(
        nome="Vodafone Czech Republic a.s.",
        mnc="03",
        mcc="230",
        pais="Czech Rep.",
    ),
    ("04", "230"): Prestadora(
        nome="Nordic Telecom Regional s.r.o.",
        mnc="04",
        mcc="230",
        pais="Czech Rep.",
    ),
    ("05", "230"): Prestadora(nome="PODA a.s.", mnc="05", mcc="230", pais="Czech Rep."),
    ("06", "230"): Prestadora(
        nome="Nordic Telecom 5G a.s.", mnc="06", mcc="230", pais="Czech Rep."
    ),
    ("07", "230"): Prestadora(
        nome="T-Mobile Czech Republic a.s.",
        mnc="07",
        mcc="230",
        pais="Czech Rep.",
    ),
    ("08", "230"): Prestadora(
        nome="Compatel s.r.o", mnc="08", mcc="230", pais="Czech Rep."
    ),
    ("09", "230"): Prestadora(
        nome="Uniphone, s.r.o.", mnc="09", mcc="230", pais="Czech Rep."
    ),
    ("11", "230"): Prestadora(
        nome="incrate s.r.o.", mnc="11", mcc="230", pais="Czech Rep."
    ),
    ("98", "230"): Prestadora(
        nome="Sprava zeleznic, statni organizace",
        mnc="98",
        mcc="230",
        pais="Czech Rep.",
    ),
    ("01", "630"): Prestadora(
        nome="Vodacom Congo RDC sprl",
        mnc="01",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("02", "630"): Prestadora(
        nome="AIRTEL sprl",
        mnc="02",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("05", "630"): Prestadora(
        nome="Supercell Sprl",
        mnc="05",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("86", "630"): Prestadora(
        nome="Congo-Chine Telecom s.a.r.l.",
        mnc="86",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("88", "630"): Prestadora(
        nome="YOZMA TIMETURNS sprl",
        mnc="88",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("89", "630"): Prestadora(
        nome="OASIS sprl", mnc="89", mcc="630", pais="Dem. Rep. of the Congo"
    ),
    ("90", "630"): Prestadora(
        nome="Africell RDC",
        mnc="90",
        mcc="630",
        pais="Dem. Rep. of the Congo",
    ),
    ("01", "238"): Prestadora(nome="TDC A/S", mnc="01", mcc="238", pais="Denmark"),
    ("02", "238"): Prestadora(nome="Telenor", mnc="02", mcc="238", pais="Denmark"),
    ("03", "238"): Prestadora(
        nome="Syniverse Technologies", mnc="03", mcc="238", pais="Denmark"
    ),
    ("05", "238"): Prestadora(
        nome="Dansk Beredskabskommunikation",
        mnc="05",
        mcc="238",
        pais="Denmark",
    ),
    ("06", "238"): Prestadora(nome="Hi3G", mnc="06", mcc="238", pais="Denmark"),
    ("08", "238"): Prestadora(nome="Voxbone", mnc="08", mcc="238", pais="Denmark"),
    ("09", "238"): Prestadora(
        nome="Dansk Beredskabskommunikation",
        mnc="09",
        mcc="238",
        pais="Denmark",
    ),
    ("10", "238"): Prestadora(nome="TDC A/S", mnc="10", mcc="238", pais="Denmark"),
    ("11", "238"): Prestadora(
        nome="Dansk Beredskabskommunikation",
        mnc="11",
        mcc="238",
        pais="Denmark",
    ),
    ("12", "238"): Prestadora(
        nome="Lycamobile Denmark Ltd.", mnc="12", mcc="238", pais="Denmark"
    ),
    ("13", "238"): Prestadora(
        nome="Compatel Limited", mnc="13", mcc="238", pais="Denmark"
    ),
    ("14", "238"): Prestadora(
        nome="Monty UK Global Limited", mnc="14", mcc="238", pais="Denmark"
    ),
    ("15", "238"): Prestadora(
        nome="Ice Danmark ApS", mnc="15", mcc="238", pais="Denmark"
    ),
    ("16", "238"): Prestadora(nome="Tismi B.V.", mnc="16", mcc="238", pais="Denmark"),
    ("17", "238"): Prestadora(nome="Gotanet AB", mnc="17", mcc="238", pais="Denmark"),
    ("18", "238"): Prestadora(
        nome="Cubic Telecom", mnc="18", mcc="238", pais="Denmark"
    ),
    ("20", "238"): Prestadora(nome="Telia", mnc="20", mcc="238", pais="Denmark"),
    ("23", "238"): Prestadora(nome="Banedanmark", mnc="23", mcc="238", pais="Denmark"),
    ("25", "238"): Prestadora(
        nome="Viahub (SMS Provider Corp.)",
        mnc="25",
        mcc="238",
        pais="Denmark",
    ),
    ("28", "238"): Prestadora(
        nome="LINK Mobility A/S", mnc="28", mcc="238", pais="Denmark"
    ),
    ("30", "238"): Prestadora(
        nome="Interactive Digital Media GmbH",
        mnc="30",
        mcc="238",
        pais="Denmark",
    ),
    ("42", "238"): Prestadora(
        nome="Greenwave Mobile IoT ApS", mnc="42", mcc="238", pais="Denmark"
    ),
    ("66", "238"): Prestadora(
        nome="TT-Netvaerket P/S", mnc="66", mcc="238", pais="Denmark"
    ),
    ("73", "238"): Prestadora(nome="Onomondo ApS", mnc="73", mcc="238", pais="Denmark"),
    ("88", "238"): Prestadora(nome="Cobira ApS", mnc="88", mcc="238", pais="Denmark"),
    ("96", "238"): Prestadora(
        nome="Telia Danmark", mnc="96", mcc="238", pais="Denmark"
    ),
    ("01", "638"): Prestadora(nome="Evatis", mnc="01", mcc="638", pais="Djibouti"),
    ("110", "366"): Prestadora(
        nome="Cable & Wireless Dominica Ltd trading as Lime",
        mnc="110",
        mcc="366",
        pais="Dominica",
    ),
    ("01", "370"): Prestadora(
        nome="Orange Dominicana, S.A.",
        mnc="01",
        mcc="370",
        pais="Dominican Rep.",
    ),
    ("02", "370"): Prestadora(
        nome="Verizon Dominicana S.A.",
        mnc="02",
        mcc="370",
        pais="Dominican Rep.",
    ),
    ("03", "370"): Prestadora(
        nome="Tricom S.A.", mnc="03", mcc="370", pais="Dominican Rep."
    ),
    ("04", "370"): Prestadora(
        nome="CentennialDominicana",
        mnc="04",
        mcc="370",
        pais="Dominican Rep.",
    ),
    ("00", "740"): Prestadora(
        nome="Otecel S.A. - Bellsouth", mnc="00", mcc="740", pais="Ecuador"
    ),
    ("01", "740"): Prestadora(nome="Porta GSM", mnc="01", mcc="740", pais="Ecuador"),
    ("02", "740"): Prestadora(nome="Telecsa S.A.", mnc="02", mcc="740", pais="Ecuador"),
    ("01", "602"): Prestadora(nome="Mobinil", mnc="01", mcc="602", pais="Egypt"),
    ("02", "602"): Prestadora(nome="Vodafone", mnc="02", mcc="602", pais="Egypt"),
    ("03", "602"): Prestadora(nome="Etisalat", mnc="03", mcc="602", pais="Egypt"),
    ("01", "706"): Prestadora(
        nome="CTE Telecom Personal, S.A. de C.V.",
        mnc="01",
        mcc="706",
        pais="El Salvador",
    ),
    ("02", "706"): Prestadora(
        nome="Digicel, S.A. de C.V.", mnc="02", mcc="706", pais="El Salvador"
    ),
    ("03", "706"): Prestadora(
        nome="Telemóvil El Salvador, S.A.",
        mnc="03",
        mcc="706",
        pais="El Salvador",
    ),
    ("01", "627"): Prestadora(
        nome="Guinea Ecuatorial de Telecomunicaciones Sociedad Anónima (GETESA)",
        mnc="01",
        mcc="627",
        pais="Equatorial Guinea",
    ),
    ("01", "248"): Prestadora(
        nome="AS Eesti Telekom", mnc="01", mcc="248", pais="Estonia"
    ),
    ("02", "248"): Prestadora(nome="RLE", mnc="02", mcc="248", pais="Estonia"),
    ("03", "248"): Prestadora(nome="Tele2", mnc="03", mcc="248", pais="Estonia"),
    ("04", "248"): Prestadora(
        nome="OY Top Connect", mnc="04", mcc="248", pais="Estonia"
    ),
    ("05", "248"): Prestadora(
        nome="CSC Telecom Estonia OÜ", mnc="05", mcc="248", pais="Estonia"
    ),
    ("07", "248"): Prestadora(nome="Televõrgu AS", mnc="07", mcc="248", pais="Estonia"),
    ("11", "248"): Prestadora(
        nome="UAB Raystorm Eesti filiaal",
        mnc="11",
        mcc="248",
        pais="Estonia",
    ),
    ("12", "248"): Prestadora(
        nome="Ntel Solutions OÜ", mnc="12", mcc="248", pais="Estonia"
    ),
    ("13", "248"): Prestadora(
        nome="Telia Eesti AS", mnc="13", mcc="248", pais="Estonia"
    ),
    ("14", "248"): Prestadora(
        nome="Estonian Crafts OÜ", mnc="14", mcc="248", pais="Estonia"
    ),
    ("16", "248"): Prestadora(
        nome="SmartTel Plus OÜ", mnc="16", mcc="248", pais="Estonia"
    ),
    ("18", "248"): Prestadora(
        nome="CLOUD COMMUNICATIONS OÜ", mnc="18", mcc="248", pais="Estonia"
    ),
    ("19", "248"): Prestadora(nome="OkTelecom OÜ", mnc="19", mcc="248", pais="Estonia"),
    ("20", "248"): Prestadora(
        nome="DOTT Telecom OÜ", mnc="20", mcc="248", pais="Estonia"
    ),
    ("21", "248"): Prestadora(nome="Tismi B.V.", mnc="21", mcc="248", pais="Estonia"),
    ("22", "248"): Prestadora(
        nome="M2MConnect OÜ", mnc="22", mcc="248", pais="Estonia"
    ),
    ("24", "248"): Prestadora(nome="Novametro OÜ", mnc="24", mcc="248", pais="Estonia"),
    ("26", "248"): Prestadora(
        nome="IT-Decision Telecom OÜ", mnc="26", mcc="248", pais="Estonia"
    ),
    ("28", "248"): Prestadora(
        nome="Nord Connect OÜ", mnc="28", mcc="248", pais="Estonia"
    ),
    ("29", "248"): Prestadora(nome="SkyTel OÜ", mnc="29", mcc="248", pais="Estonia"),
    ("30", "248"): Prestadora(
        nome="Mediafon Carrier Services OÜ",
        mnc="30",
        mcc="248",
        pais="Estonia",
    ),
    ("31", "248"): Prestadora(nome="YATECO OÜ", mnc="31", mcc="248", pais="Estonia"),
    ("32", "248"): Prestadora(nome="Narayana OÜ", mnc="32", mcc="248", pais="Estonia"),
    ("71", "248"): Prestadora(
        nome="Siseministeerium (Ministry of Interior)",
        mnc="71",
        mcc="248",
        pais="Estonia",
    ),
    ("01", "653"): Prestadora(nome="SPTC", mnc="01", mcc="653", pais="Eswatini"),
    ("02", "653"): Prestadora(
        nome="Swazi Mobile Limited", mnc="02", mcc="653", pais="Eswatini"
    ),
    ("10", "653"): Prestadora(nome="Swazi MTN", mnc="10", mcc="653", pais="Eswatini"),
    ("01", "636"): Prestadora(nome="ETH MTN", mnc="01", mcc="636", pais="Ethiopia"),
    ("001", "750"): Prestadora(
        nome="Touch",
        mnc="001",
        mcc="750",
        pais="Falkland Islands (Malvinas)",
    ),
    ("01", "288"): Prestadora(
        nome="Faroese Telecom - GSM",
        mnc="01",
        mcc="288",
        pais="Faroe Islands",
    ),
    ("02", "274"): Prestadora(
        nome="P/F Kall, reg. No 2868 (Vodafone FO)",
        mnc="02",
        mcc="274",
        pais="Faroe Islands",
    ),
    ("02", "288"): Prestadora(
        nome="Kall GSM", mnc="02", mcc="288", pais="Faroe Islands"
    ),
    ("10", "288"): Prestadora(
        nome="Faroese Telecom", mnc="10", mcc="288", pais="Faroe Islands"
    ),
    ("01", "542"): Prestadora(
        nome="Vodafone (Fiji) Ltd", mnc="01", mcc="542", pais="Fiji"
    ),
    ("02", "542"): Prestadora(
        nome="Digicel (Fiji) Ltd", mnc="02", mcc="542", pais="Fiji"
    ),
    ("03", "542"): Prestadora(
        nome="Telecom Fiji Ltd (CDMA)", mnc="03", mcc="542", pais="Fiji"
    ),
    ("03", "244"): Prestadora(nome="DNA Oy", mnc="03", mcc="244", pais="Finland"),
    ("04", "244"): Prestadora(nome="DNA Oy", mnc="04", mcc="244", pais="Finland"),
    ("05", "244"): Prestadora(nome="Elisa Oyj", mnc="05", mcc="244", pais="Finland"),
    ("06", "244"): Prestadora(nome="Elisa Oyj", mnc="06", mcc="244", pais="Finland"),
    ("07", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="07",
        mcc="244",
        pais="Finland",
    ),
    ("08", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="08",
        mcc="244",
        pais="Finland",
    ),
    ("09", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="09",
        mcc="244",
        pais="Finland",
    ),
    ("10", "244"): Prestadora(
        nome="Viestintävirasto", mnc="10", mcc="244", pais="Finland"
    ),
    ("11", "244"): Prestadora(
        nome="Viestintävirasto", mnc="11", mcc="244", pais="Finland"
    ),
    ("12", "244"): Prestadora(nome="DNA Oy", mnc="12", mcc="244", pais="Finland"),
    ("13", "244"): Prestadora(nome="DNA Oy", mnc="13", mcc="244", pais="Finland"),
    ("14", "244"): Prestadora(
        nome="Ålands Telekommunikation Ab",
        mnc="14",
        mcc="244",
        pais="Finland",
    ),
    ("15", "244"): Prestadora(
        nome="Satakunnan ammattikorkeakoulu Oy",
        mnc="15",
        mcc="244",
        pais="Finland",
    ),
    ("17", "244"): Prestadora(
        nome="Liikennevirasto", mnc="17", mcc="244", pais="Finland"
    ),
    ("21", "244"): Prestadora(nome="Elisa Oyj", mnc="21", mcc="244", pais="Finland"),
    ("22", "244"): Prestadora(nome="EXFO Oy", mnc="22", mcc="244", pais="Finland"),
    ("23", "244"): Prestadora(nome="EXFO Oy", mnc="23", mcc="244", pais="Finland"),
    ("24", "244"): Prestadora(nome="TTY-säätiö", mnc="24", mcc="244", pais="Finland"),
    ("26", "244"): Prestadora(
        nome="Compatel Limited", mnc="26", mcc="244", pais="Finland"
    ),
    ("27", "244"): Prestadora(
        nome="Teknologian tutkimuskeskus VTT Oy",
        mnc="27",
        mcc="244",
        pais="Finland",
    ),
    ("31", "244"): Prestadora(
        nome="Kuiri Mobile Oy", mnc="31", mcc="244", pais="Finland"
    ),
    ("32", "244"): Prestadora(nome="Voxbone S.A.", mnc="32", mcc="244", pais="Finland"),
    ("33", "244"): Prestadora(
        nome="Virve Tuotteet ja Palvelut Oy",
        mnc="33",
        mcc="244",
        pais="Finland",
    ),
    ("34", "244"): Prestadora(
        nome="Bittium Wireless Oy", mnc="34", mcc="244", pais="Finland"
    ),
    ("35", "244"): Prestadora(
        nome="Ukkoverkot Oy", mnc="35", mcc="244", pais="Finland"
    ),
    ("36", "244"): Prestadora(
        nome="TeliaSonera Finland Oyj", mnc="36", mcc="244", pais="Finland"
    ),
    ("37", "244"): Prestadora(nome="Tismi BV", mnc="37", mcc="244", pais="Finland"),
    ("38", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="38",
        mcc="244",
        pais="Finland",
    ),
    ("39", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="39",
        mcc="244",
        pais="Finland",
    ),
    ("40", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="40",
        mcc="244",
        pais="Finland",
    ),
    ("41", "244"): Prestadora(
        nome="Nokia Solutions and Networks Oy",
        mnc="41",
        mcc="244",
        pais="Finland",
    ),
    ("91", "244"): Prestadora(
        nome="TeliaSonera Finland Oyj", mnc="91", mcc="244", pais="Finland"
    ),
    ("92", "244"): Prestadora(
        nome="TeliaSonera Finland Oyj", mnc="92", mcc="244", pais="Finland"
    ),
    ("01", "208"): Prestadora(nome="Orange", mnc="01", mcc="208", pais="France"),
    ("02", "208"): Prestadora(nome="Orange", mnc="02", mcc="208", pais="France"),
    ("03", "208"): Prestadora(nome="MobiquiThings", mnc="03", mcc="208", pais="France"),
    ("04", "208"): Prestadora(nome="Sisteer", mnc="04", mcc="208", pais="France"),
    ("05", "208"): Prestadora(
        nome="Globalstar Europe", mnc="05", mcc="208", pais="France"
    ),
    ("06", "208"): Prestadora(
        nome="Globalstar Europe", mnc="06", mcc="208", pais="France"
    ),
    ("07", "208"): Prestadora(
        nome="Globalstar Europe", mnc="07", mcc="208", pais="France"
    ),
    ("08", "208"): Prestadora(
        nome="Société Française du Radiotéléphone",
        mnc="08",
        mcc="208",
        pais="France",
    ),
    ("09", "208"): Prestadora(
        nome="Société Française du Radiotéléphone",
        mnc="09",
        mcc="208",
        pais="France",
    ),
    ("10", "208"): Prestadora(
        nome="Société Française du Radiotéléphone",
        mnc="10",
        mcc="208",
        pais="France",
    ),
    ("11", "208"): Prestadora(
        nome="Société Française du Radiotéléphone",
        mnc="11",
        mcc="208",
        pais="France",
    ),
    ("12", "208"): Prestadora(
        nome="Truphone France", mnc="12", mcc="208", pais="France"
    ),
    ("13", "208"): Prestadora(
        nome="Société Française du Radiotéléphone",
        mnc="13",
        mcc="208",
        pais="France",
    ),
    ("14", "208"): Prestadora(nome="RFF", mnc="14", mcc="208", pais="France"),
    ("15", "208"): Prestadora(nome="Free Mobile", mnc="15", mcc="208", pais="France"),
    ("16", "208"): Prestadora(nome="Free Mobile", mnc="16", mcc="208", pais="France"),
    ("17", "208"): Prestadora(nome="Legos", mnc="17", mcc="208", pais="France"),
    ("19", "208"): Prestadora(
        nome="Haute-Garonne numérique", mnc="19", mcc="208", pais="France"
    ),
    ("20", "208"): Prestadora(
        nome="Bouygues Telecom", mnc="20", mcc="208", pais="France"
    ),
    ("21", "208"): Prestadora(
        nome="Bouygues Telecom", mnc="21", mcc="208", pais="France"
    ),
    ("22", "208"): Prestadora(nome="Transatel", mnc="22", mcc="208", pais="France"),
    ("23", "208"): Prestadora(
        nome="Syndicat mixte ouvert Charente Numérique",
        mnc="23",
        mcc="208",
        pais="France",
    ),
    ("24", "208"): Prestadora(nome="MobiquiThings", mnc="24", mcc="208", pais="France"),
    ("25", "208"): Prestadora(nome="Lycamobile", mnc="25", mcc="208", pais="France"),
    ("26", "208"): Prestadora(
        nome="Bouygues Telecom Business - Distribution",
        mnc="26",
        mcc="208",
        pais="France",
    ),
    ("27", "208"): Prestadora(
        nome="Coriolis Telecom", mnc="27", mcc="208", pais="France"
    ),
    ("28", "208"): Prestadora(
        nome="Airmob Infra Full", mnc="28", mcc="208", pais="France"
    ),
    ("29", "208"): Prestadora(
        nome="Cubic télécom France", mnc="29", mcc="208", pais="France"
    ),
    ("30", "208"): Prestadora(nome="Syma", mnc="30", mcc="208", pais="France"),
    ("31", "208"): Prestadora(
        nome="Vectone Mobile", mnc="31", mcc="208", pais="France"
    ),
    ("32", "208"): Prestadora(nome="Orange", mnc="32", mcc="208", pais="France"),
    ("33", "208"): Prestadora(
        nome="Syndicat mixte La Fibre64", mnc="33", mcc="208", pais="France"
    ),
    ("34", "208"): Prestadora(
        nome="Cellhire (France)", mnc="34", mcc="208", pais="France"
    ),
    ("35", "208"): Prestadora(nome="Free mobile", mnc="35", mcc="208", pais="France"),
    ("36", "208"): Prestadora(nome="Free mobile", mnc="36", mcc="208", pais="France"),
    ("37", "208"): Prestadora(nome="IP Directions", mnc="37", mcc="208", pais="France"),
    ("38", "208"): Prestadora(
        nome="Lebara France Limited", mnc="38", mcc="208", pais="France"
    ),
    ("39", "208"): Prestadora(nome="Netwo", mnc="39", mcc="208", pais="France"),
    ("86", "208"): Prestadora(nome="SEM@FOR77", mnc="86", mcc="208", pais="France"),
    ("87", "208"): Prestadora(
        nome="AIRBUS DEFENCE AND SPACE SAS",
        mnc="87",
        mcc="208",
        pais="France",
    ),
    ("88", "208"): Prestadora(
        nome="Bouygues Telecom", mnc="88", mcc="208", pais="France"
    ),
    ("89", "208"): Prestadora(nome="Hub One", mnc="89", mcc="208", pais="France"),
    ("91", "208"): Prestadora(nome="Orange", mnc="91", mcc="208", pais="France"),
    ("94", "208"): Prestadora(nome="Halys", mnc="94", mcc="208", pais="France"),
    ("96", "208"): Prestadora(
        nome="Région Bourgogne-Franche-Comté",
        mnc="96",
        mcc="208",
        pais="France",
    ),
    ("97", "208"): Prestadora(
        nome="Thales communications & Security",
        mnc="97",
        mcc="208",
        pais="France",
    ),
    ("500", "208"): Prestadora(nome="EDF", mnc="500", mcc="208", pais="France"),
    ("501", "208"): Prestadora(nome="Butachimie", mnc="501", mcc="208", pais="France"),
    ("502", "208"): Prestadora(nome="EDF", mnc="502", mcc="208", pais="France"),
    ("700", "208"): Prestadora(
        nome="Weaccess group", mnc="700", mcc="208", pais="France"
    ),
    ("701", "208"): Prestadora(
        nome="GIP Vendée numérique", mnc="701", mcc="208", pais="France"
    ),
    ("702", "208"): Prestadora(
        nome="17-Numerique", mnc="702", mcc="208", pais="France"
    ),
    ("703", "208"): Prestadora(nome="Nivertel", mnc="703", mcc="208", pais="France"),
    ("704", "208"): Prestadora(
        nome="Axione Limousin", mnc="704", mcc="208", pais="France"
    ),
    ("705", "208"): Prestadora(
        nome="Hautes-Pyrénées Numérique", mnc="705", mcc="208", pais="France"
    ),
    ("706", "208"): Prestadora(
        nome="Tours Métropole Numérique", mnc="706", mcc="208", pais="France"
    ),
    ("707", "208"): Prestadora(nome="Sartel THD", mnc="707", mcc="208", pais="France"),
    ("708", "208"): Prestadora(
        nome="Melis@ territoires ruraux", mnc="708", mcc="208", pais="France"
    ),
    ("709", "208"): Prestadora(
        nome="Quimper communauté télécom",
        mnc="709",
        mcc="208",
        pais="France",
    ),
    ("710", "208"): Prestadora(nome="Losange", mnc="710", mcc="208", pais="France"),
    ("711", "208"): Prestadora(nome="Nomotech", mnc="711", mcc="208", pais="France"),
    ("712", "208"): Prestadora(
        nome="Syndicat Audois d'énergies et du Numérique",
        mnc="712",
        mcc="208",
        pais="France",
    ),
    ("713", "208"): Prestadora(nome="SD NUM SAS", mnc="713", mcc="208", pais="France"),
    ("714", "208"): Prestadora(
        nome="Département de l'Isère", mnc="714", mcc="208", pais="France"
    ),
    ("00", "647"): Prestadora(
        nome="Orange",
        mnc="00",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("01", "647"): Prestadora(
        nome="BJT Partners",
        mnc="01",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("02", "647"): Prestadora(
        nome="Telco OI",
        mnc="02",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("03", "647"): Prestadora(
        nome="Telco OI",
        mnc="03",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("04", "647"): Prestadora(
        nome="ZEOP Mobile",
        mnc="04",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("10", "647"): Prestadora(
        nome="Société Réunionnaise du Radiotéléphone",
        mnc="10",
        mcc="647",
        pais="French Departments and Territories in the Indian Ocean",
    ),
    ("04", "742"): Prestadora(
        nome="Free Caraïbe", mnc="04", mcc="742", pais="French Guiana"
    ),
    ("05", "547"): Prestadora(
        nome="VITI", mnc="05", mcc="547", pais="French Polynesia"
    ),
    ("10", "547"): Prestadora(
        nome="Mara Telecom", mnc="10", mcc="547", pais="French Polynesia"
    ),
    ("15", "547"): Prestadora(
        nome="Pacific Mobile Telecom",
        mnc="15",
        mcc="547",
        pais="French Polynesia",
    ),
    ("20", "547"): Prestadora(
        nome="Tikiphone", mnc="20", mcc="547", pais="French Polynesia"
    ),
    ("01", "628"): Prestadora(nome="LIBERTIS", mnc="01", mcc="628", pais="Gabon"),
    ("02", "628"): Prestadora(nome="MOOV", mnc="02", mcc="628", pais="Gabon"),
    ("03", "628"): Prestadora(nome="CELTEL", mnc="03", mcc="628", pais="Gabon"),
    ("04", "628"): Prestadora(nome="USAN GABON", mnc="04", mcc="628", pais="Gabon"),
    ("05", "628"): Prestadora(
        nome="Réseau de l’Administration Gabonaise (RAG)",
        mnc="05",
        mcc="628",
        pais="Gabon",
    ),
    ("01", "607"): Prestadora(nome="Gamcel", mnc="01", mcc="607", pais="Gambia"),
    ("02", "607"): Prestadora(nome="Africell", mnc="02", mcc="607", pais="Gambia"),
    ("03", "607"): Prestadora(nome="COMIUM", mnc="03", mcc="607", pais="Gambia"),
    ("04", "607"): Prestadora(nome="Qcell", mnc="04", mcc="607", pais="Gambia"),
    ("05", "607"): Prestadora(nome="GAMTEL-Ecowan", mnc="05", mcc="607", pais="Gambia"),
    ("06", "607"): Prestadora(nome="NETPAGE", mnc="06", mcc="607", pais="Gambia"),
    ("01", "282"): Prestadora(nome="Geocell Ltd.", mnc="01", mcc="282", pais="Georgia"),
    ("02", "282"): Prestadora(
        nome="Magti GSM Ltd.", mnc="02", mcc="282", pais="Georgia"
    ),
    ("03", "282"): Prestadora(
        nome="Iberiatel Ltd.", mnc="03", mcc="282", pais="Georgia"
    ),
    ("04", "282"): Prestadora(nome="Mobitel Ltd.", mnc="04", mcc="282", pais="Georgia"),
    ("05", "282"): Prestadora(nome="Silknet JSC", mnc="05", mcc="282", pais="Georgia"),
    ("06", "282"): Prestadora(nome="JSC Compatel", mnc="06", mcc="282", pais="Georgia"),
    ("07", "282"): Prestadora(
        nome="GLOBALCELL  LTD", mnc="07", mcc="282", pais="Georgia"
    ),
    ("08", "282"): Prestadora(nome="Silknet GSC", mnc="08", mcc="282", pais="Georgia"),
    ("09", "282"): Prestadora(nome="Gmobile LTD", mnc="09", mcc="282", pais="Georgia"),
    ("10", "282"): Prestadora(
        nome="Premium Net International SRL LTD",
        mnc="10",
        mcc="282",
        pais="Georgia",
    ),
    ("11", "282"): Prestadora(nome="Mobilive LTD", mnc="11", mcc="282", pais="Georgia"),
    ("12", "282"): Prestadora(
        nome='Telecom1" LTD"', mnc="12", mcc="282", pais="Georgia"
    ),
    ("13", "282"): Prestadora(nome='Asanet" LTD"', mnc="13", mcc="282", pais="Georgia"),
    ("14", "282"): Prestadora(
        nome='Datahouseglobal” LTD"', mnc="14", mcc="282", pais="Georgia"
    ),
    ("15", "282"): Prestadora(
        nome='Servicebox" LTD"', mnc="15", mcc="282", pais="Georgia"
    ),
    ("22", "282"): Prestadora(
        nome='Myphone" LTD"', mnc="22", mcc="282", pais="Georgia"
    ),
    ("01", "262"): Prestadora(
        nome="Telekom Deutschland GmbH", mnc="01", mcc="262", pais="Germany"
    ),
    ("02", "262"): Prestadora(
        nome="Vodafone GmbH", mnc="02", mcc="262", pais="Germany"
    ),
    ("03", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="03",
        mcc="262",
        pais="Germany",
    ),
    ("04", "262"): Prestadora(
        nome="Vodafone GmbH", mnc="04", mcc="262", pais="Germany"
    ),
    ("05", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="05",
        mcc="262",
        pais="Germany",
    ),
    ("06", "262"): Prestadora(
        nome="Telekom Deutschland GmbH", mnc="06", mcc="262", pais="Germany"
    ),
    ("07", "262"): Prestadora(
        nome="Telefónica Germany GmbH & Co. OHG",
        mnc="07",
        mcc="262",
        pais="Germany",
    ),
    ("08", "262"): Prestadora(
        nome="Telefónica Germany GmbH & Co. OHG",
        mnc="08",
        mcc="262",
        pais="Germany",
    ),
    ("09", "262"): Prestadora(
        nome="Vodafone GmbH", mnc="09", mcc="262", pais="Germany"
    ),
    ("10", "262"): Prestadora(nome="DB Netz AG", mnc="10", mcc="262", pais="Germany"),
    ("11", "262"): Prestadora(
        nome="Telefónica Germany GmbH & Co. OHG",
        mnc="11",
        mcc="262",
        pais="Germany",
    ),
    ("12", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="12",
        mcc="262",
        pais="Germany",
    ),
    ("15", "262"): Prestadora(nome="AirData AG", mnc="15", mcc="262", pais="Germany"),
    ("16", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="16",
        mcc="262",
        pais="Germany",
    ),
    ("17", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="17",
        mcc="262",
        pais="Germany",
    ),
    ("18", "262"): Prestadora(
        nome="NetCologne Gesellschaft für Telekommunikation mbH",
        mnc="18",
        mcc="262",
        pais="Germany",
    ),
    ("19", "262"): Prestadora(
        nome="Inquam Deutschland GmbH", mnc="19", mcc="262", pais="Germany"
    ),
    ("20", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="20",
        mcc="262",
        pais="Germany",
    ),
    ("21", "262"): Prestadora(
        nome="Multiconnect GmbH", mnc="21", mcc="262", pais="Germany"
    ),
    ("22", "262"): Prestadora(
        nome="Sipgate Wireless GmbH", mnc="22", mcc="262", pais="Germany"
    ),
    ("23", "262"): Prestadora(
        nome="Drillisch Online AG", mnc="23", mcc="262", pais="Germany"
    ),
    ("42", "262"): Prestadora(
        nome="Vodafone GmbH", mnc="42", mcc="262", pais="Germany"
    ),
    ("43", "262"): Prestadora(
        nome="Vodafone GmbH", mnc="43", mcc="262", pais="Germany"
    ),
    ("72", "262"): Prestadora(
        nome="Ericsson GmbH", mnc="72", mcc="262", pais="Germany"
    ),
    ("73", "262"): Prestadora(
        nome="Xantaro Deutschland GmbH", mnc="73", mcc="262", pais="Germany"
    ),
    ("74", "262"): Prestadora(
        nome="Qualcomm CDMA Technologies GmbH",
        mnc="74",
        mcc="262",
        pais="Germany",
    ),
    ("75", "262"): Prestadora(
        nome="Core Network Dynamics GmbH",
        mnc="75",
        mcc="262",
        pais="Germany",
    ),
    ("77", "262"): Prestadora(
        nome="E-Plus Mobilfunk GmbH & Co. KG",
        mnc="77",
        mcc="262",
        pais="Germany",
    ),
    ("78", "262"): Prestadora(
        nome="Telekom Deutschland GmbH", mnc="78", mcc="262", pais="Germany"
    ),
    ("01", "620"): Prestadora(nome="Spacefon", mnc="01", mcc="620", pais="Ghana"),
    ("02", "620"): Prestadora(
        nome="Ghana Telecom Mobile", mnc="02", mcc="620", pais="Ghana"
    ),
    ("03", "620"): Prestadora(nome="Mobitel", mnc="03", mcc="620", pais="Ghana"),
    ("04", "620"): Prestadora(
        nome="Kasapa Telecom Ltd.", mnc="04", mcc="620", pais="Ghana"
    ),
    ("11", "620"): Prestadora(
        nome="Netafriques Dot Com Ltd", mnc="11", mcc="620", pais="Ghana"
    ),
    ("01", "266"): Prestadora(nome="Gibtel", mnc="01", mcc="266", pais="Gibraltar"),
    ("03", "266"): Prestadora(
        nome="GibFibre Ltd (trading as “Gibfibrespeed”)",
        mnc="03",
        mcc="266",
        pais="Gibraltar",
    ),
    ("09", "266"): Prestadora(
        nome="Eazi Telecom Ltd (trading as “Limba”)",
        mnc="09",
        mcc="266",
        pais="Gibraltar",
    ),
    ("01", "202"): Prestadora(nome="Cosmote AE", mnc="01", mcc="202", pais="Greece"),
    ("02", "202"): Prestadora(nome="Cosmote AE", mnc="02", mcc="202", pais="Greece"),
    ("03", "202"): Prestadora(nome="OTE AE", mnc="03", mcc="202", pais="Greece"),
    ("04", "202"): Prestadora(nome="OTE AE", mnc="04", mcc="202", pais="Greece"),
    ("05", "202"): Prestadora(
        nome="Vodafone - Panafon", mnc="05", mcc="202", pais="Greece"
    ),
    ("07", "202"): Prestadora(
        nome="AMD TELECOM AE", mnc="07", mcc="202", pais="Greece"
    ),
    ("09", "202"): Prestadora(
        nome="WIND HELLAS TELECOMMUNICATIONS",
        mnc="09",
        mcc="202",
        pais="Greece",
    ),
    ("10", "202"): Prestadora(
        nome="WIND HELLAS TELECOMMUNICATIONS",
        mnc="10",
        mcc="202",
        pais="Greece",
    ),
    ("11", "202"): Prestadora(nome="INTERCONNECT", mnc="11", mcc="202", pais="Greece"),
    ("12", "202"): Prestadora(nome="YUBOTO", mnc="12", mcc="202", pais="Greece"),
    ("13", "202"): Prestadora(
        nome="COMPATEL LIMITED", mnc="13", mcc="202", pais="Greece"
    ),
    ("14", "202"): Prestadora(nome="CYTA (HELLAS)", mnc="14", mcc="202", pais="Greece"),
    ("15", "202"): Prestadora(nome="BWS", mnc="15", mcc="202", pais="Greece"),
    ("16", "202"): Prestadora(nome="INTER TELECOM", mnc="16", mcc="202", pais="Greece"),
    ("01", "290"): Prestadora(
        nome="Tele Greenland", mnc="01", mcc="290", pais="Greenland"
    ),
    ("02", "290"): Prestadora(nome="inu:it a/s", mnc="02", mcc="290", pais="Greenland"),
    ("03", "290"): Prestadora(nome="GTV", mnc="03", mcc="290", pais="Greenland"),
    ("110", "352"): Prestadora(
        nome="Cable & Wireless Grenada ltd trading as lime",
        mnc="110",
        mcc="352",
        pais="Grenada",
    ),
    ("01", "340"): Prestadora(
        nome="Orange Caraïbe", mnc="01", mcc="340", pais="Guadeloupe"
    ),
    ("02", "340"): Prestadora(
        nome="Outremer Telecom", mnc="02", mcc="340", pais="Guadeloupe"
    ),
    ("03", "340"): Prestadora(
        nome="United telecommunications services Caraïbe",
        mnc="03",
        mcc="340",
        pais="Guadeloupe",
    ),
    ("08", "340"): Prestadora(
        nome="Dauphin Telecom", mnc="08", mcc="340", pais="Guadeloupe"
    ),
    ("09", "340"): Prestadora(
        nome="Free Caraïbe", mnc="09", mcc="340", pais="Guadeloupe"
    ),
    ("10", "340"): Prestadora(
        nome="Guadeloupe Téléphone Mobile",
        mnc="10",
        mcc="340",
        pais="Guadeloupe",
    ),
    ("20", "340"): Prestadora(
        nome="Digicel Antilles Françaises Guyane",
        mnc="20",
        mcc="340",
        pais="Guadeloupe",
    ),
    ("01", "704"): Prestadora(
        nome="Servicios de Comunicaciones Personales Inalámbricas, S.A. (SERCOM, S.A",
        mnc="01",
        mcc="704",
        pais="Guatemala",
    ),
    ("02", "704"): Prestadora(
        nome="Comunicaciones Celulares S.A.",
        mnc="02",
        mcc="704",
        pais="Guatemala",
    ),
    ("03", "704"): Prestadora(
        nome="Telefónica Centroamérica Guatemala S.A.",
        mnc="03",
        mcc="704",
        pais="Guatemala",
    ),
    ("01", "611"): Prestadora(nome="Orange Guinée", mnc="01", mcc="611", pais="Guinea"),
    ("02", "611"): Prestadora(nome="Sotelgui", mnc="02", mcc="611", pais="Guinea"),
    ("05", "611"): Prestadora(
        nome="Cellcom Guinée SA", mnc="05", mcc="611", pais="Guinea"
    ),
    ("01", "632"): Prestadora(
        nome="Guinétel S.A.", mnc="01", mcc="632", pais="Guinea-Bissau"
    ),
    ("02", "632"): Prestadora(
        nome="Spacetel Guinea-Bissau S.A.",
        mnc="02",
        mcc="632",
        pais="Guinea-Bissau",
    ),
    ("00", "738"): Prestadora(
        nome="E-Networks Inc.", mnc="00", mcc="738", pais="Guyana"
    ),
    ("01", "738"): Prestadora(
        nome="U-Mobile (Cellular) Inc.", mnc="01", mcc="738", pais="Guyana"
    ),
    ("002", "738"): Prestadora(
        nome="Guyana Telephone & Telegraph Company Limited (Cellink)",
        mnc="002",
        mcc="738",
        pais="Guyana",
    ),
    ("003", "738"): Prestadora(
        nome="Quark Communications Inc.", mnc="003", mcc="738", pais="Guyana"
    ),
    ("05", "738"): Prestadora(
        nome="eGovernment Unit, Ministry of the Presidency",
        mnc="05",
        mcc="738",
        pais="Guyana",
    ),
    ("040", "738"): Prestadora(
        nome="E-Networks Inc.", mnc="040", mcc="738", pais="Guyana"
    ),
    ("01", "372"): Prestadora(nome="Comcel", mnc="01", mcc="372", pais="Haiti"),
    ("02", "372"): Prestadora(nome="Digicel", mnc="02", mcc="372", pais="Haiti"),
    ("03", "372"): Prestadora(nome="Rectel", mnc="03", mcc="372", pais="Haiti"),
    ("001", "708"): Prestadora(nome="Megatel", mnc="001", mcc="708", pais="Honduras"),
    ("002", "708"): Prestadora(nome="Celtel", mnc="002", mcc="708", pais="Honduras"),
    ("040", "708"): Prestadora(
        nome="Digicel Honduras", mnc="040", mcc="708", pais="Honduras"
    ),
    ("00", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="00",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("01", "454"): Prestadora(
        nome="CITIC Telecom International Limited",
        mnc="01",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("02", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="02",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("03", "454"): Prestadora(
        nome="Hutchison Telephone Company Limited",
        mnc="03",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("04", "454"): Prestadora(
        nome="Hutchison Telephone Company Limited",
        mnc="04",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("05", "454"): Prestadora(
        nome="Hutchison Telephone Company Limited",
        mnc="05",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("06", "454"): Prestadora(
        nome="SmarTone Mobile Communications Limited",
        mnc="06",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("07", "454"): Prestadora(
        nome="China Unicom (Hong Kong) Operations Limited",
        mnc="07",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("08", "454"): Prestadora(
        nome="Truphone (Hong Kong) Ltd",
        mnc="08",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("10", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="10",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("11", "454"): Prestadora(
        nome="China-Hongkong Telecom Limited",
        mnc="11",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("12", "454"): Prestadora(
        nome="China Mobile Hong Kong Company Limited",
        mnc="12",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("13", "454"): Prestadora(
        nome="China Mobile Hong Kong Company Limited",
        mnc="13",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("14", "454"): Prestadora(
        nome="Hutchison Telephone Company Limited",
        mnc="14",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("15", "454"): Prestadora(
        nome="SmarTone Mobile Communications Limited",
        mnc="15",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("16", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="16",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("17", "454"): Prestadora(
        nome="SmarTone Mobile Communications Limited",
        mnc="17",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("18", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="18",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("19", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="19",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("20", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="20",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("21", "454"): Prestadora(
        nome="21 ViaNet Group Limited",
        mnc="21",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("22", "454"): Prestadora(
        nome="263 Mobile Communications (HongKong) Limited",
        mnc="22",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("24", "454"): Prestadora(
        nome="Multibyte Info Technology Limited",
        mnc="24",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("25", "454"): Prestadora(
        nome="Government use", mnc="25", mcc="454", pais="Hong Kong, China"
    ),
    ("26", "454"): Prestadora(
        nome="Government use", mnc="26", mcc="454", pais="Hong Kong, China"
    ),
    ("27", "454"): Prestadora(
        nome="Government use", mnc="27", mcc="454", pais="Hong Kong, China"
    ),
    ("28", "454"): Prestadora(
        nome="Government use", mnc="28", mcc="454", pais="Hong Kong, China"
    ),
    ("29", "454"): Prestadora(
        nome="Hong Kong Telecommunications (HKT) Limited",
        mnc="29",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("30", "454"): Prestadora(
        nome="China Mobile Hong Kong Company Limited",
        mnc="30",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("31", "454"): Prestadora(
        nome="China Telecom Global Limited",
        mnc="31",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("32", "454"): Prestadora(
        nome="Hong Kong Broadband Network Ltd",
        mnc="32",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("35", "454"): Prestadora(
        nome="Webbing Hong Kong Limited",
        mnc="35",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("36", "454"): Prestadora(
        nome="Easco Telecommunications Limited",
        mnc="36",
        mcc="454",
        pais="Hong Kong, China",
    ),
    ("01", "216"): Prestadora(
        nome="Yettel Hungary Ltd.", mnc="01", mcc="216", pais="Hungary"
    ),
    ("02", "216"): Prestadora(nome="MVM NET Ltd.", mnc="02", mcc="216", pais="Hungary"),
    ("03", "216"): Prestadora(
        nome="DIGI Telecommunication Ltd.",
        mnc="03",
        mcc="216",
        pais="Hungary",
    ),
    ("04", "216"): Prestadora(
        nome="Pro-M PrCo. Ltd.", mnc="04", mcc="216", pais="Hungary"
    ),
    ("20", "216"): Prestadora(
        nome="Yettel Hungary Ltd.", mnc="20", mcc="216", pais="Hungary"
    ),
    ("30", "216"): Prestadora(
        nome="Magyar Telecom Plc", mnc="30", mcc="216", pais="Hungary"
    ),
    ("70", "216"): Prestadora(nome="Vodafone", mnc="70", mcc="216", pais="Hungary"),
    ("71", "216"): Prestadora(
        nome="Vodafone Hungary Ltd", mnc="71", mcc="216", pais="Hungary"
    ),
    ("99", "216"): Prestadora(nome="MÁV Co.", mnc="99", mcc="216", pais="Hungary"),
    ("01", "274"): Prestadora(
        nome="Iceland Telecom Ltd.", mnc="01", mcc="274", pais="Iceland"
    ),
    ("03", "274"): Prestadora(
        nome="Og fjarskipti hf (Vodafone Iceland)",
        mnc="03",
        mcc="274",
        pais="Iceland",
    ),
    ("04", "274"): Prestadora(
        nome="IMC Islande ehf", mnc="04", mcc="274", pais="Iceland"
    ),
    ("07", "274"): Prestadora(nome="IceCell ehf", mnc="07", mcc="274", pais="Iceland"),
    ("00", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Madhya Pradesh",
        mnc="00",
        mcc="404",
        pais="India",
    ),
    ("000", "405"): Prestadora(
        nome="Shyam Telelink Ltd, Rajasthan",
        mnc="000",
        mcc="405",
        pais="India",
    ),
    ("01", "404"): Prestadora(
        nome="Aircell Digilink India Ltd., Haryana",
        mnc="01",
        mcc="404",
        pais="India",
    ),
    ("02", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Punjab", mnc="02", mcc="404", pais="India"
    ),
    ("03", "404"): Prestadora(
        nome="Bharti Airtel Ltd., H.P.", mnc="03", mcc="404", pais="India"
    ),
    ("04", "404"): Prestadora(
        nome="Idea Cellular Ltd., Delhi", mnc="04", mcc="404", pais="India"
    ),
    ("05", "404"): Prestadora(
        nome="Fascel Ltd., Gujarat", mnc="05", mcc="404", pais="India"
    ),
    ("005", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Delhi",
        mnc="005",
        mcc="405",
        pais="India",
    ),
    ("06", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Karnataka",
        mnc="06",
        mcc="404",
        pais="India",
    ),
    ("006", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Gujarat",
        mnc="006",
        mcc="405",
        pais="India",
    ),
    ("07", "404"): Prestadora(
        nome="Idea Cellular Ltd., Andhra Pradesh",
        mnc="07",
        mcc="404",
        pais="India",
    ),
    ("007", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Haryana",
        mnc="007",
        mcc="405",
        pais="India",
    ),
    ("08", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Himachal Pradesh",
        mnc="08",
        mcc="405",
        pais="India",
    ),
    ("09", "404"): Prestadora(
        nome="Reliance Telecom Ltd., Assam",
        mnc="09",
        mcc="404",
        pais="India",
    ),
    ("009", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, J&K",
        mnc="009",
        mcc="405",
        pais="India",
    ),
    ("10", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Delhi", mnc="10", mcc="404", pais="India"
    ),
    ("010", "405"): Prestadora(
        nome="Reliance Communications Ltd,/GSM Karnataka",
        mnc="010",
        mcc="405",
        pais="India",
    ),
    ("11", "404"): Prestadora(
        nome="Hutchison Essar Mobile Services Ltd, Delhi",
        mnc="11",
        mcc="404",
        pais="India",
    ),
    ("011", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Kerala",
        mnc="011",
        mcc="405",
        pais="India",
    ),
    ("12", "404"): Prestadora(
        nome="Idea Mobile Communications Ltd., Haryana",
        mnc="12",
        mcc="404",
        pais="India",
    ),
    ("012", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Andhra Pradesh",
        mnc="012",
        mcc="405",
        pais="India",
    ),
    ("12", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Kolkata",
        mnc="12",
        mcc="405",
        pais="India",
    ),
    ("13", "404"): Prestadora(
        nome="Hutchison Essar South Ltd., Andhra Pradesh",
        mnc="13",
        mcc="404",
        pais="India",
    ),
    ("013", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Maharashtra",
        mnc="013",
        mcc="405",
        pais="India",
    ),
    ("14", "404"): Prestadora(
        nome="Spice Communications PVT Ltd., Punjab",
        mnc="14",
        mcc="404",
        pais="India",
    ),
    ("014", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Madhya Pradesh",
        mnc="014",
        mcc="405",
        pais="India",
    ),
    ("15", "404"): Prestadora(
        nome="Aircell Digilink India Ltd., UP (East)",
        mnc="15",
        mcc="404",
        pais="India",
    ),
    ("15", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Mumbai",
        mnc="15",
        mcc="405",
        pais="India",
    ),
    ("16", "404"): Prestadora(
        nome="Bharti Airtel Ltd, North East",
        mnc="16",
        mcc="404",
        pais="India",
    ),
    ("17", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, West Bengal",
        mnc="17",
        mcc="404",
        pais="India",
    ),
    ("17", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Orissa",
        mnc="17",
        mcc="405",
        pais="India",
    ),
    ("18", "404"): Prestadora(
        nome="Reliance Telecom Ltd., H.P.", mnc="18", mcc="404", pais="India"
    ),
    ("018", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Punjab",
        mnc="018",
        mcc="405",
        pais="India",
    ),
    ("19", "404"): Prestadora(
        nome="Idea Mobile Communications Ltd., Kerala",
        mnc="19",
        mcc="404",
        pais="India",
    ),
    ("20", "404"): Prestadora(
        nome="Hutchison Essar Ltd, Mumbai", mnc="20", mcc="404", pais="India"
    ),
    ("020", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, Tamilnadu",
        mnc="020",
        mcc="405",
        pais="India",
    ),
    ("21", "404"): Prestadora(
        nome="BPL Mobile Communications Ltd., Mumbai",
        mnc="21",
        mcc="404",
        pais="India",
    ),
    ("021", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, UP (East)",
        mnc="021",
        mcc="405",
        pais="India",
    ),
    ("22", "404"): Prestadora(
        nome="Idea Cellular Ltd., Maharashtra",
        mnc="22",
        mcc="404",
        pais="India",
    ),
    ("022", "405"): Prestadora(
        nome="Reliance Communications Ltd/GSM, UP (West)",
        mnc="022",
        mcc="405",
        pais="India",
    ),
    ("23", "404"): Prestadora(
        nome="Idea Cellular Ltd, Maharashtra",
        mnc="23",
        mcc="404",
        pais="India",
    ),
    ("23", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, West bengal",
        mnc="23",
        mcc="405",
        pais="India",
    ),
    ("24", "404"): Prestadora(
        nome="Idea Cellular Ltd., Gujarat", mnc="24", mcc="404", pais="India"
    ),
    ("25", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Bihar", mnc="25", mcc="404", pais="India"
    ),
    ("025", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Andhra Pradesh",
        mnc="025",
        mcc="405",
        pais="India",
    ),
    ("27", "404"): Prestadora(
        nome="Hutchison Essar Cellular Ltd., Maharashtra",
        mnc="27",
        mcc="404",
        pais="India",
    ),
    ("027", "405"): Prestadora(
        nome="Tata Teleservices Ltd,/GSM Bihar",
        mnc="027",
        mcc="405",
        pais="India",
    ),
    ("28", "405"): Prestadora(
        nome="Tata Teleservices Ltd, Chennai",
        mnc="28",
        mcc="405",
        pais="India",
    ),
    ("29", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Assam", mnc="29", mcc="404", pais="India"
    ),
    ("029", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Delhi",
        mnc="029",
        mcc="405",
        pais="India",
    ),
    ("30", "404"): Prestadora(
        nome="Hutchison Telecom East Ltd, Kolkata",
        mnc="30",
        mcc="404",
        pais="India",
    ),
    ("030", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Gujarat",
        mnc="030",
        mcc="405",
        pais="India",
    ),
    ("31", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Kolkata", mnc="31", mcc="404", pais="India"
    ),
    ("031", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Haryana",
        mnc="031",
        mcc="405",
        pais="India",
    ),
    ("032", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Himachal Pradesh",
        mnc="032",
        mcc="405",
        pais="India",
    ),
    ("33", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, North East",
        mnc="33",
        mcc="404",
        pais="India",
    ),
    ("033", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Bihar",
        mnc="033",
        mcc="405",
        pais="India",
    ),
    ("34", "404"): Prestadora(nome="BSNL, Haryana", mnc="34", mcc="404", pais="India"),
    ("034", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Kamataka",
        mnc="034",
        mcc="405",
        pais="India",
    ),
    ("35", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Himachal Pradesh",
        mnc="35",
        mcc="404",
        pais="India",
    ),
    ("035", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Kerala",
        mnc="035",
        mcc="405",
        pais="India",
    ),
    ("36", "404"): Prestadora(
        nome="Reliance Telecom Ltd., Bihar",
        mnc="36",
        mcc="404",
        pais="India",
    ),
    ("036", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Kolkata",
        mnc="036",
        mcc="405",
        pais="India",
    ),
    ("37", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, J&K", mnc="37", mcc="404", pais="India"
    ),
    ("037", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Maharashtra",
        mnc="037",
        mcc="405",
        pais="India",
    ),
    ("38", "404"): Prestadora(nome="BSNL, Assam", mnc="38", mcc="404", pais="India"),
    ("038", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Madhya Pradesh",
        mnc="038",
        mcc="405",
        pais="India",
    ),
    ("039", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Mumbai",
        mnc="039",
        mcc="405",
        pais="India",
    ),
    ("40", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Chennai", mnc="40", mcc="404", pais="India"
    ),
    ("040", "405"): Prestadora(
        nome="Reliance Infocomm Ltd, Chennai",
        mnc="040",
        mcc="405",
        pais="India",
    ),
    ("41", "404"): Prestadora(
        nome="Aircell Cellular Ltd, Chennai",
        mnc="41",
        mcc="404",
        pais="India",
    ),
    ("041", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Orissa",
        mnc="041",
        mcc="405",
        pais="India",
    ),
    ("42", "404"): Prestadora(
        nome="Aircel Ltd., Tamil Nadu", mnc="42", mcc="404", pais="India"
    ),
    ("042", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Punjab",
        mnc="042",
        mcc="405",
        pais="India",
    ),
    ("43", "404"): Prestadora(
        nome="Hutchison Essar Cellular Ltd., Tamil Nadu",
        mnc="43",
        mcc="404",
        pais="India",
    ),
    ("043", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Rajasthan",
        mnc="043",
        mcc="405",
        pais="India",
    ),
    ("44", "404"): Prestadora(
        nome="Spice Communications PVT Ltd., Karnataka",
        mnc="44",
        mcc="404",
        pais="India",
    ),
    ("044", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, Tamilnadu",
        mnc="044",
        mcc="405",
        pais="India",
    ),
    ("045", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, UP (East)",
        mnc="045",
        mcc="405",
        pais="India",
    ),
    ("46", "404"): Prestadora(
        nome="Hutchison Essar Cellular Ltd., Kerala",
        mnc="46",
        mcc="404",
        pais="India",
    ),
    ("046", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, UP (West)",
        mnc="046",
        mcc="405",
        pais="India",
    ),
    ("047", "405"): Prestadora(
        nome="Tata Teleservices Ltd/GSM, West Bengal",
        mnc="047",
        mcc="405",
        pais="India",
    ),
    ("48", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, UP (West)",
        mnc="48",
        mcc="404",
        pais="India",
    ),
    ("49", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Andra Pradesh",
        mnc="49",
        mcc="404",
        pais="India",
    ),
    ("50", "404"): Prestadora(
        nome="Reliance Telecom Ltd., North East",
        mnc="50",
        mcc="404",
        pais="India",
    ),
    ("51", "404"): Prestadora(nome="BSNL, H.P.", mnc="51", mcc="404", pais="India"),
    ("52", "404"): Prestadora(
        nome="Reliance Telecom Ltd., Orissa",
        mnc="52",
        mcc="404",
        pais="India",
    ),
    ("52", "405"): Prestadora(
        nome="Bharti Airtel Ltd, Bihar", mnc="52", mcc="405", pais="India"
    ),
    ("53", "404"): Prestadora(nome="BSNL, Punjab", mnc="53", mcc="404", pais="India"),
    ("53", "405"): Prestadora(
        nome="Bharti Airtel Ltd, Orissa", mnc="53", mcc="405", pais="India"
    ),
    ("54", "404"): Prestadora(
        nome="BSNL, UP (West)", mnc="54", mcc="404", pais="India"
    ),
    ("54", "405"): Prestadora(
        nome="Bharti Airtel Ltd, UP (East)",
        mnc="54",
        mcc="405",
        pais="India",
    ),
    ("55", "404"): Prestadora(
        nome="BSNL, UP (East)", mnc="55", mcc="404", pais="India"
    ),
    ("55", "405"): Prestadora(
        nome="Bharti Airtel Ltd, J&K", mnc="55", mcc="405", pais="India"
    ),
    ("56", "404"): Prestadora(
        nome="Idea Mobile Communications Ltd., UP (West)",
        mnc="56",
        mcc="404",
        pais="India",
    ),
    ("56", "405"): Prestadora(
        nome="Bharti Airtel Ltd, Assam", mnc="56", mcc="405", pais="India"
    ),
    ("57", "404"): Prestadora(nome="BSNL, Gujarat", mnc="57", mcc="404", pais="India"),
    ("58", "404"): Prestadora(
        nome="BSNL, Madhya Pradesh", mnc="58", mcc="404", pais="India"
    ),
    ("59", "404"): Prestadora(
        nome="BSNL, Rajasthan", mnc="59", mcc="404", pais="India"
    ),
    ("60", "404"): Prestadora(
        nome="Aircell Digilink India Ltd., Rajasthan",
        mnc="60",
        mcc="404",
        pais="India",
    ),
    ("61", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Punjab",
        mnc="61",
        mcc="404",
        pais="India",
    ),
    ("62", "404"): Prestadora(nome="BSNL, J&K", mnc="62", mcc="404", pais="India"),
    ("63", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Haryana",
        mnc="63",
        mcc="404",
        pais="India",
    ),
    ("64", "404"): Prestadora(nome="BSNL, Chennai", mnc="64", mcc="404", pais="India"),
    ("65", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, UP (East)",
        mnc="65",
        mcc="404",
        pais="India",
    ),
    ("66", "404"): Prestadora(
        nome="BSNL, Maharashtra", mnc="66", mcc="404", pais="India"
    ),
    ("66", "405"): Prestadora(
        nome="Hutchison Essar South Ltd, UP (West)",
        mnc="66",
        mcc="405",
        pais="India",
    ),
    ("67", "404"): Prestadora(
        nome="Reliance Telecom Ltd., Madhya Pradesh",
        mnc="67",
        mcc="404",
        pais="India",
    ),
    ("67", "405"): Prestadora(
        nome="Hutchison Essar South Ltd, Orissa",
        mnc="67",
        mcc="405",
        pais="India",
    ),
    ("68", "404"): Prestadora(nome="MTNL, Delhi", mnc="68", mcc="404", pais="India"),
    ("68", "405"): Prestadora(
        nome="Vodaphone/Hutchison, Madhya Pradesh",
        mnc="68",
        mcc="405",
        pais="India",
    ),
    ("69", "404"): Prestadora(nome="MTNL, Mumbai", mnc="69", mcc="404", pais="India"),
    ("70", "404"): Prestadora(
        nome="Bharti Hexacom Ltd, Rajasthan",
        mnc="70",
        mcc="404",
        pais="India",
    ),
    ("70", "405"): Prestadora(
        nome="Aditya Birla Telecom Ltd, Bihar",
        mnc="70",
        mcc="405",
        pais="India",
    ),
    ("71", "404"): Prestadora(
        nome="BSNL, Karnataka", mnc="71", mcc="404", pais="India"
    ),
    ("71", "405"): Prestadora(
        nome="Essar Spacetel Ltd, Himachal Pradesh",
        mnc="71",
        mcc="405",
        pais="India",
    ),
    ("72", "404"): Prestadora(nome="BSNL, Kerala", mnc="72", mcc="404", pais="India"),
    ("72", "405"): Prestadora(
        nome="Essar Spacetel Ltd, North East",
        mnc="72",
        mcc="405",
        pais="India",
    ),
    ("73", "404"): Prestadora(
        nome="BSNL, Andhra Pradesh", mnc="73", mcc="404", pais="India"
    ),
    ("73", "405"): Prestadora(
        nome="Essar Spacetel Ltd, Assam", mnc="73", mcc="405", pais="India"
    ),
    ("74", "404"): Prestadora(
        nome="BSNL, West Bengal", mnc="74", mcc="404", pais="India"
    ),
    ("74", "405"): Prestadora(
        nome="Essar Spacetel Ltd, J&K", mnc="74", mcc="405", pais="India"
    ),
    ("75", "404"): Prestadora(nome="BSNL, Bihar", mnc="75", mcc="404", pais="India"),
    ("76", "404"): Prestadora(nome="BSNL, Orissa", mnc="76", mcc="404", pais="India"),
    ("76", "405"): Prestadora(
        nome="Essar Spacetel Ltd, Orissa", mnc="76", mcc="405", pais="India"
    ),
    ("77", "404"): Prestadora(
        nome="BSNL, North East", mnc="77", mcc="404", pais="India"
    ),
    ("77", "405"): Prestadora(
        nome="Essar Spacetel Ltd, Maharashtra",
        mnc="77",
        mcc="405",
        pais="India",
    ),
    ("78", "404"): Prestadora(
        nome="BTA Cellcom Ltd., Madhya Pradesh",
        mnc="78",
        mcc="404",
        pais="India",
    ),
    ("79", "404"): Prestadora(
        nome="BSNL, Andaman & Nicobar", mnc="79", mcc="404", pais="India"
    ),
    ("80", "404"): Prestadora(
        nome="BSNL, Tamil Nadu", mnc="80", mcc="404", pais="India"
    ),
    ("81", "404"): Prestadora(nome="BSNL, Kolkata", mnc="81", mcc="404", pais="India"),
    ("81", "405"): Prestadora(
        nome="Aircell Ltd, Delhi", mnc="81", mcc="405", pais="India"
    ),
    ("82", "404"): Prestadora(
        nome="Idea Telecommunications Ltd, H.P.",
        mnc="82",
        mcc="404",
        pais="India",
    ),
    ("82", "405"): Prestadora(
        nome="Aircell Ltd, Andhra Pradesh", mnc="82", mcc="405", pais="India"
    ),
    ("83", "404"): Prestadora(
        nome="Reliable Internet Services Ltd., Kolkata",
        mnc="83",
        mcc="404",
        pais="India",
    ),
    ("83", "405"): Prestadora(
        nome="Aircell Ltd, Gujarat", mnc="83", mcc="405", pais="India"
    ),
    ("84", "404"): Prestadora(
        nome="Hutchison Essar South Ltd., Chennai",
        mnc="84",
        mcc="404",
        pais="India",
    ),
    ("84", "405"): Prestadora(
        nome="Aircell Ltd, Maharashtra", mnc="84", mcc="405", pais="India"
    ),
    ("85", "404"): Prestadora(
        nome="Reliance Telecom Ltd., W.B. & A.N.",
        mnc="85",
        mcc="404",
        pais="India",
    ),
    ("85", "405"): Prestadora(
        nome="Aircell Ltd, Mumbai", mnc="85", mcc="405", pais="India"
    ),
    ("86", "404"): Prestadora(
        nome="Hutchison Essar South Ltd., Karnataka",
        mnc="86",
        mcc="404",
        pais="India",
    ),
    ("86", "405"): Prestadora(
        nome="Aircell Ltd, Rajasthan", mnc="86", mcc="405", pais="India"
    ),
    ("87", "404"): Prestadora(
        nome="Idea Telecommunications Ltd, Rajasthan",
        mnc="87",
        mcc="404",
        pais="India",
    ),
    ("88", "404"): Prestadora(
        nome="Hutchison Essar South Ltd, Punjab",
        mnc="88",
        mcc="404",
        pais="India",
    ),
    ("89", "404"): Prestadora(
        nome="Idea Telecommunications Ltd, UP (East)",
        mnc="89",
        mcc="404",
        pais="India",
    ),
    ("90", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Maharashtra",
        mnc="90",
        mcc="404",
        pais="India",
    ),
    ("91", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Kolkata",
        mnc="91",
        mcc="404",
        pais="India",
    ),
    ("92", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Mumbai", mnc="92", mcc="404", pais="India"
    ),
    ("93", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Madhya Pradesh",
        mnc="93",
        mcc="404",
        pais="India",
    ),
    ("94", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Tamil Nadu",
        mnc="94",
        mcc="404",
        pais="India",
    ),
    ("95", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Kerala", mnc="95", mcc="404", pais="India"
    ),
    ("96", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Haryana", mnc="96", mcc="404", pais="India"
    ),
    ("97", "404"): Prestadora(
        nome="Bharti Airtel Ltd., UP (West)",
        mnc="97",
        mcc="404",
        pais="India",
    ),
    ("98", "404"): Prestadora(
        nome="Bharti Airtel Ltd., Gujarat", mnc="98", mcc="404", pais="India"
    ),
    ("99", "404"): Prestadora(
        nome="Dishnet Wireless Ltd, Kerala",
        mnc="99",
        mcc="404",
        pais="India",
    ),
    ("750", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, J&K",
        mnc="750",
        mcc="405",
        pais="India",
    ),
    ("751", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, Assam",
        mnc="751",
        mcc="405",
        pais="India",
    ),
    ("752", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, Bihar",
        mnc="752",
        mcc="405",
        pais="India",
    ),
    ("753", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, Orissa",
        mnc="753",
        mcc="405",
        pais="India",
    ),
    ("754", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, Himachal Pradesh",
        mnc="754",
        mcc="405",
        pais="India",
    ),
    ("755", "405"): Prestadora(
        nome="Vodafone Essar Spacetel Ltd, North East",
        mnc="755",
        mcc="405",
        pais="India",
    ),
    ("799", "405"): Prestadora(
        nome="Idea Cellular Ltd, MUMBAI", mnc="799", mcc="405", pais="India"
    ),
    ("800", "405"): Prestadora(
        nome="Aircell Ltd, Delhi", mnc="800", mcc="405", pais="India"
    ),
    ("801", "405"): Prestadora(
        nome="Aircell Ltd, Andhra Pradesh",
        mnc="801",
        mcc="405",
        pais="India",
    ),
    ("802", "405"): Prestadora(
        nome="Aircell Ltd, Gujarat", mnc="802", mcc="405", pais="India"
    ),
    ("803", "405"): Prestadora(
        nome="Aircell Ltd, Kamataka", mnc="803", mcc="405", pais="India"
    ),
    ("804", "405"): Prestadora(
        nome="Aircell Ltd, Maharashtra", mnc="804", mcc="405", pais="India"
    ),
    ("805", "405"): Prestadora(
        nome="Aircell Ltd, Mumbai", mnc="805", mcc="405", pais="India"
    ),
    ("806", "405"): Prestadora(
        nome="Aircell Ltd, Rajasthan", mnc="806", mcc="405", pais="India"
    ),
    ("807", "405"): Prestadora(
        nome="Dishnet Wireless Ltd, Haryana",
        mnc="807",
        mcc="405",
        pais="India",
    ),
    ("808", "405"): Prestadora(
        nome="Dishnet Wireless Ltd, Madhya Pradesh",
        mnc="808",
        mcc="405",
        pais="India",
    ),
    ("809", "405"): Prestadora(
        nome="Dishnet Wireless Ltd, Kerala",
        mnc="809",
        mcc="405",
        pais="India",
    ),
    ("00", "510"): Prestadora(nome="PSN", mnc="00", mcc="510", pais="Indonesia"),
    ("01", "510"): Prestadora(nome="Satelindo", mnc="01", mcc="510", pais="Indonesia"),
    ("08", "510"): Prestadora(
        nome="Natrindo (Lippo Telecom)",
        mnc="08",
        mcc="510",
        pais="Indonesia",
    ),
    ("10", "510"): Prestadora(nome="Telkomsel", mnc="10", mcc="510", pais="Indonesia"),
    ("11", "510"): Prestadora(
        nome="Excelcomindo", mnc="11", mcc="510", pais="Indonesia"
    ),
    ("21", "510"): Prestadora(
        nome="Indosat - M3", mnc="21", mcc="510", pais="Indonesia"
    ),
    ("28", "510"): Prestadora(nome="Komselindo", mnc="28", mcc="510", pais="Indonesia"),
    ("01", "432"): Prestadora(
        nome="KISH CELL PARS",
        mnc="01",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("02", "432"): Prestadora(
        nome="NEGIN ERTEBATAT AVA",
        mnc="02",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("03", "432"): Prestadora(
        nome="PARSIAN HAMRAH LOTUS",
        mnc="03",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("04", "432"): Prestadora(
        nome="TOSE E FANAVARI ERTEBATAT NOVIN HAMRAH",
        mnc="04",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("05", "432"): Prestadora(
        nome="HAMRAH HOSHMAND AYANDEH",
        mnc="05",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("06", "432"): Prestadora(
        nome="ERTEBATAT ARYANTEL",
        mnc="06",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("07", "432"): Prestadora(
        nome="HOOSHMAND AMIN MOBILE",
        mnc="07",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("08", "432"): Prestadora(
        nome="TOSE-E ERTEBATAT HAMRAH SHATEL",
        mnc="08",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("09", "432"): Prestadora(
        nome="HIWEB", mnc="09", mcc="432", pais="Iran (Islamic Republic of)"
    ),
    ("11", "432"): Prestadora(
        nome="MCI (Mobile Communications of Iran)",
        mnc="11",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("12", "432"): Prestadora(
        nome="HIWEB", mnc="12", mcc="432", pais="Iran (Islamic Republic of)"
    ),
    ("13", "432"): Prestadora(
        nome="HIWEB", mnc="13", mcc="432", pais="Iran (Islamic Republic of)"
    ),
    ("14", "432"): Prestadora(
        nome="Kish Free Zone Organization",
        mnc="14",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("20", "432"): Prestadora(
        nome="RIGHTEL",
        mnc="20",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("32", "432"): Prestadora(
        nome="TCI (Telecommunication Company of Iran)",
        mnc="32",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("35", "432"): Prestadora(
        nome="IRANCELL",
        mnc="35",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("44", "432"): Prestadora(
        nome="ERTEBATAT MOBIN NET",
        mnc="44",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("45", "432"): Prestadora(
        nome="FARABORD DADEHAYE IRANIAN",
        mnc="45",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("46", "432"): Prestadora(
        nome="HIWEB", mnc="46", mcc="432", pais="Iran (Islamic Republic of)"
    ),
    ("49", "432"): Prestadora(
        nome="GOSTARESH ERTEBATAT MABNA",
        mnc="49",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("50", "432"): Prestadora(
        nome="SHATEL", mnc="50", mcc="432", pais="Iran (Islamic Republic of)"
    ),
    ("51", "432"): Prestadora(
        nome="PISHGAMAN TOSE-E ERTEBATAT",
        mnc="51",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("52", "432"): Prestadora(
        nome="ASIATECH",
        mnc="52",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("70", "432"): Prestadora(
        nome="TCI (Telecommunication Company of Iran)",
        mnc="70",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("71", "432"): Prestadora(
        nome="ERTEBATAT KOOHE NOOR",
        mnc="71",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("93", "432"): Prestadora(
        nome="ERTEBATAT FARZANEGAN PARS",
        mnc="93",
        mcc="432",
        pais="Iran (Islamic Republic of)",
    ),
    ("05", "418"): Prestadora(nome="Asia Cell", mnc="05", mcc="418", pais="Iraq"),
    ("20", "418"): Prestadora(
        nome="Zain Iraq (previously Atheer)",
        mnc="20",
        mcc="418",
        pais="Iraq",
    ),
    ("30", "418"): Prestadora(
        nome="Zain Iraq (previously Iraqna)",
        mnc="30",
        mcc="418",
        pais="Iraq",
    ),
    ("40", "418"): Prestadora(nome="Korek Telecom", mnc="40", mcc="418", pais="Iraq"),
    ("47", "418"): Prestadora(
        nome="Iraq Central Cooperative Association for Communication and Transportation",
        mnc="47",
        mcc="418",
        pais="Iraq",
    ),
    ("48", "418"): Prestadora(nome="ITC Fanoos", mnc="48", mcc="418", pais="Iraq"),
    ("49", "418"): Prestadora(nome="Iraqtel", mnc="49", mcc="418", pais="Iraq"),
    ("62", "418"): Prestadora(nome="Itisaluna", mnc="62", mcc="418", pais="Iraq"),
    ("70", "418"): Prestadora(nome="Kalimat", mnc="70", mcc="418", pais="Iraq"),
    ("80", "418"): Prestadora(
        nome="Iraqi Telecommunications & Post Company (ITPC)",
        mnc="80",
        mcc="418",
        pais="Iraq",
    ),
    ("81", "418"): Prestadora(
        nome="ITPC (Al-Mazaya)", mnc="81", mcc="418", pais="Iraq"
    ),
    ("83", "418"): Prestadora(
        nome="ITPC (Sader Al-Iraq)", mnc="83", mcc="418", pais="Iraq"
    ),
    ("84", "418"): Prestadora(
        nome="ITPC (Eaamar Albasrah)", mnc="84", mcc="418", pais="Iraq"
    ),
    ("85", "418"): Prestadora(
        nome="ITPC (Anwar Yagotat Alkhalee)",
        mnc="85",
        mcc="418",
        pais="Iraq",
    ),
    ("86", "418"): Prestadora(
        nome="ITPC (Furatfone)", mnc="86", mcc="418", pais="Iraq"
    ),
    ("87", "418"): Prestadora(nome="ITPC (Al-Seraj)", mnc="87", mcc="418", pais="Iraq"),
    ("88", "418"): Prestadora(
        nome="ITPC (High Link)", mnc="88", mcc="418", pais="Iraq"
    ),
    ("89", "418"): Prestadora(nome="ITPC (Al-Shams)", mnc="89", mcc="418", pais="Iraq"),
    ("91", "418"): Prestadora(
        nome="ITPC (Belad Babel)", mnc="91", mcc="418", pais="Iraq"
    ),
    ("92", "418"): Prestadora(
        nome="ITPC (Al Nakheel)", mnc="92", mcc="418", pais="Iraq"
    ),
    ("93", "418"): Prestadora(nome="ITPC (Iraqcell)", mnc="93", mcc="418", pais="Iraq"),
    ("94", "418"): Prestadora(nome="ITPC (Shaly)", mnc="94", mcc="418", pais="Iraq"),
    ("01", "272"): Prestadora(
        nome="Vodafone Ireland Plc", mnc="01", mcc="272", pais="Ireland"
    ),
    ("02", "272"): Prestadora(
        nome="Three Ireland Services (Hutchison) Ltd",
        mnc="02",
        mcc="272",
        pais="Ireland",
    ),
    ("03", "272"): Prestadora(nome="Eircom Ltd", mnc="03", mcc="272", pais="Ireland"),
    ("05", "272"): Prestadora(
        nome="Three Ireland (Hutchison) Ltd",
        mnc="05",
        mcc="272",
        pais="Ireland",
    ),
    ("07", "272"): Prestadora(nome="Eircom Ltd", mnc="07", mcc="272", pais="Ireland"),
    ("08", "272"): Prestadora(nome="Eircom Ltd", mnc="08", mcc="272", pais="Ireland"),
    ("11", "272"): Prestadora(
        nome="Liffey Telecom Ltd", mnc="11", mcc="272", pais="Ireland"
    ),
    ("13", "272"): Prestadora(
        nome="Lycamobile Ireland Ltd", mnc="13", mcc="272", pais="Ireland"
    ),
    ("15", "272"): Prestadora(
        nome="Virgin Media Ireland Ltd", mnc="15", mcc="272", pais="Ireland"
    ),
    ("16", "272"): Prestadora(
        nome="Carphone Warehouse Ireland Mobile Ltd",
        mnc="16",
        mcc="272",
        pais="Ireland",
    ),
    ("17", "272"): Prestadora(
        nome="Three Ireland (Hutchison) Ltd",
        mnc="17",
        mcc="272",
        pais="Ireland",
    ),
    ("18", "272"): Prestadora(
        nome="Cubic Telecom Limited", mnc="18", mcc="272", pais="Ireland"
    ),
    ("21", "272"): Prestadora(
        nome="Net Feasa Limited", mnc="21", mcc="272", pais="Ireland"
    ),
    ("68", "272"): Prestadora(
        nome="Office of the Government Chief Information Officer",
        mnc="68",
        mcc="272",
        pais="Ireland",
    ),
    ("01", "425"): Prestadora(
        nome="Partner Communications Co. Ltd.",
        mnc="01",
        mcc="425",
        pais="Israel",
    ),
    ("02", "425"): Prestadora(
        nome="Cellcom Israel Ltd", mnc="02", mcc="425", pais="Israel"
    ),
    ("03", "425"): Prestadora(
        nome="Pelephone Communications Ltd",
        mnc="03",
        mcc="425",
        pais="Israel",
    ),
    ("04", "425"): Prestadora(nome="Globalsim Ltd", mnc="04", mcc="425", pais="Israel"),
    ("06", "425"): Prestadora(nome="Wataniya", mnc="06", mcc="425", pais="Israel"),
    ("07", "425"): Prestadora(nome="Mirs Ltd", mnc="07", mcc="425", pais="Israel"),
    ("08", "425"): Prestadora(
        nome="Golan Telecom Ltd", mnc="08", mcc="425", pais="Israel"
    ),
    ("09", "425"): Prestadora(
        nome="Marathon 018 Xphone Ltd.", mnc="09", mcc="425", pais="Israel"
    ),
    ("11", "425"): Prestadora(
        nome="365 Telecom (MVNO)", mnc="11", mcc="425", pais="Israel"
    ),
    ("12", "425"): Prestadora(
        nome="Free Telecom (MVNO)", mnc="12", mcc="425", pais="Israel"
    ),
    ("13", "425"): Prestadora(
        nome="Ituran Cellular Communications",
        mnc="13",
        mcc="425",
        pais="Israel",
    ),
    ("14", "425"): Prestadora(
        nome="Alon Cellular Ltd.", mnc="14", mcc="425", pais="Israel"
    ),
    ("15", "425"): Prestadora(
        nome="Home Cellular (MVNO)", mnc="15", mcc="425", pais="Israel"
    ),
    ("16", "425"): Prestadora(
        nome="Rami Levi (MVNO)", mnc="16", mcc="425", pais="Israel"
    ),
    ("17", "425"): Prestadora(
        nome="Gale Phone (MVNO)", mnc="17", mcc="425", pais="Israel"
    ),
    ("18", "425"): Prestadora(
        nome="Cellact Communications Ltd (MVNO)",
        mnc="18",
        mcc="425",
        pais="Israel",
    ),
    ("19", "425"): Prestadora(
        nome="Azi Communications Ltd", mnc="19", mcc="425", pais="Israel"
    ),
    ("20", "425"): Prestadora(nome="Bezeq Ltd", mnc="20", mcc="425", pais="Israel"),
    ("21", "425"): Prestadora(
        nome="B.I.P Communications Ltd.", mnc="21", mcc="425", pais="Israel"
    ),
    ("22", "425"): Prestadora(
        nome="Maskyoo Telephonia Ltd.", mnc="22", mcc="425", pais="Israel"
    ),
    ("23", "425"): Prestadora(
        nome="Beezz Communication Solutions Ltd.",
        mnc="23",
        mcc="425",
        pais="Israel",
    ),
    ("24", "425"): Prestadora(
        nome="012 Telecom Ltd.", mnc="24", mcc="425", pais="Israel"
    ),
    ("25", "425"): Prestadora(nome="IMOD", mnc="25", mcc="425", pais="Israel"),
    ("26", "425"): Prestadora(
        nome="LB Annatel Ltd.", mnc="26", mcc="425", pais="Israel"
    ),
    ("27", "425"): Prestadora(nome="BITIT Ltd.", mnc="27", mcc="425", pais="Israel"),
    ("28", "425"): Prestadora(nome="PHI Networks", mnc="28", mcc="425", pais="Israel"),
    ("29", "425"): Prestadora(nome="CG Networks", mnc="29", mcc="425", pais="Israel"),
    ("01", "222"): Prestadora(
        nome="Telecom Italia Mobile (TIM)", mnc="01", mcc="222", pais="Italy"
    ),
    ("02", "222"): Prestadora(nome="Elsacom", mnc="02", mcc="222", pais="Italy"),
    ("10", "222"): Prestadora(
        nome="Omnitel Pronto Italia (OPI)", mnc="10", mcc="222", pais="Italy"
    ),
    ("77", "222"): Prestadora(nome="IPSE 2000", mnc="77", mcc="222", pais="Italy"),
    ("88", "222"): Prestadora(nome="Wind", mnc="88", mcc="222", pais="Italy"),
    ("98", "222"): Prestadora(nome="Blu", mnc="98", mcc="222", pais="Italy"),
    ("99", "222"): Prestadora(nome="H3G", mnc="99", mcc="222", pais="Italy"),
    ("050", "338"): Prestadora(
        nome="Digicel (Jamaica) Ltd", mnc="050", mcc="338", pais="Jamaica"
    ),
    ("080", "338"): Prestadora(
        nome="Rock Mobile Limited", mnc="080", mcc="338", pais="Jamaica"
    ),
    ("110", "338"): Prestadora(
        nome="Cable and Wireless Jamaica Ltd",
        mnc="110",
        mcc="338",
        pais="Jamaica",
    ),
    ("00", "440"): Prestadora(nome="SoftBank Corp.", mnc="00", mcc="440", pais="Japan"),
    ("00", "441"): Prestadora(
        nome="Wireless City Planning Inc.", mnc="00", mcc="441", pais="Japan"
    ),
    ("01", "440"): Prestadora(
        nome="KDDI Corporation", mnc="01", mcc="440", pais="Japan"
    ),
    ("01", "441"): Prestadora(nome="SoftBank Corp.", mnc="01", mcc="441", pais="Japan"),
    ("02", "440"): Prestadora(
        nome="Hanshin Cable Engineering Co. Ltd.",
        mnc="02",
        mcc="440",
        pais="Japan",
    ),
    ("03", "440"): Prestadora(
        nome="Internet Initiative Japan Inc.",
        mnc="03",
        mcc="440",
        pais="Japan",
    ),
    ("04", "440"): Prestadora(
        nome="Japan Radio Co., Ltd.", mnc="04", mcc="440", pais="Japan"
    ),
    ("05", "440"): Prestadora(
        nome="Wireless City Planning Inc.", mnc="05", mcc="440", pais="Japan"
    ),
    ("06", "440"): Prestadora(
        nome="SAKURA Internet Inc.", mnc="06", mcc="440", pais="Japan"
    ),
    ("07", "440"): Prestadora(nome="closip, Inc.", mnc="07", mcc="440", pais="Japan"),
    ("08", "440"): Prestadora(
        nome="Panasonic Connect Co., Ltd", mnc="08", mcc="440", pais="Japan"
    ),
    ("09", "440"): Prestadora(
        nome="Marubeni Network Solutions Inc.",
        mnc="09",
        mcc="440",
        pais="Japan",
    ),
    ("10", "440"): Prestadora(
        nome="NTT DOCOMO, INC.", mnc="10", mcc="440", pais="Japan"
    ),
    ("11", "440"): Prestadora(
        nome="Rakuten Mobile Network, Inc.",
        mnc="11",
        mcc="440",
        pais="Japan",
    ),
    ("12", "440"): Prestadora(
        nome="CABLE MEDIA WAIWAI CORPORATION",
        mnc="12",
        mcc="440",
        pais="Japan",
    ),
    ("13", "440"): Prestadora(
        nome="NTT Communications Corporation",
        mnc="13",
        mcc="440",
        pais="Japan",
    ),
    ("14", "440"): Prestadora(nome="GRAPE ONE LTD.", mnc="14", mcc="440", pais="Japan"),
    ("15", "440"): Prestadora(
        nome="BB Backbone Corp.", mnc="15", mcc="440", pais="Japan"
    ),
    ("16", "440"): Prestadora(
        nome="Nokia Innovations Japan G.K.",
        mnc="16",
        mcc="440",
        pais="Japan",
    ),
    ("17", "440"): Prestadora(
        nome="OSAKA GAS BUSINESS CREATE CORPORATION",
        mnc="17",
        mcc="440",
        pais="Japan",
    ),
    ("18", "440"): Prestadora(
        nome="Kintetsu Cable Network, Ltd", mnc="18", mcc="440", pais="Japan"
    ),
    ("19", "440"): Prestadora(
        nome="NEC Networks & System Integration Corporation",
        mnc="19",
        mcc="440",
        pais="Japan",
    ),
    ("20", "440"): Prestadora(nome="SoftBank Corp.", mnc="20", mcc="440", pais="Japan"),
    ("21", "440"): Prestadora(nome="SoftBank Corp.", mnc="21", mcc="440", pais="Japan"),
    ("22", "440"): Prestadora(nome="JTOWER Inc.", mnc="22", mcc="440", pais="Japan"),
    ("23", "440"): Prestadora(
        nome="FUJITSU LIMITED", mnc="23", mcc="440", pais="Japan"
    ),
    ("50", "440"): Prestadora(
        nome="KDDI Corporation", mnc="50", mcc="440", pais="Japan"
    ),
    ("51", "440"): Prestadora(
        nome="KDDI Corporation", mnc="51", mcc="440", pais="Japan"
    ),
    ("52", "440"): Prestadora(
        nome="KDDI Corporation", mnc="52", mcc="440", pais="Japan"
    ),
    ("53", "440"): Prestadora(
        nome="KDDI Corporation", mnc="53", mcc="440", pais="Japan"
    ),
    ("54", "440"): Prestadora(
        nome="KDDI Corporation", mnc="54", mcc="440", pais="Japan"
    ),
    ("200", "441"): Prestadora(
        nome="SORACOM, Inc.", mnc="200", mcc="441", pais="Japan"
    ),
    ("201", "441"): Prestadora(
        nome="Aurens Co.,Ltd.", mnc="201", mcc="441", pais="Japan"
    ),
    ("202", "441"): Prestadora(
        nome="Sony Wireless Communications Inc.",
        mnc="202",
        mcc="441",
        pais="Japan",
    ),
    ("203", "441"): Prestadora(nome="GujoCity", mnc="203", mcc="441", pais="Japan"),
    ("204", "441"): Prestadora(nome="Wicom Inc.", mnc="204", mcc="441", pais="Japan"),
    ("205", "441"): Prestadora(
        nome="KATCH NETWORK INC.", mnc="205", mcc="441", pais="Japan"
    ),
    ("206", "441"): Prestadora(
        nome="MITSUBISHI ELECTRIC CORPORATION",
        mnc="206",
        mcc="441",
        pais="Japan",
    ),
    ("207", "441"): Prestadora(
        nome="Mitsui Knowledge Industry Co., Ltd.",
        mnc="207",
        mcc="441",
        pais="Japan",
    ),
    ("208", "441"): Prestadora(
        nome="CHUDENKO CORPORATION", mnc="208", mcc="441", pais="Japan"
    ),
    ("209", "441"): Prestadora(
        nome="Cable Television TOYAMA Inc.",
        mnc="209",
        mcc="441",
        pais="Japan",
    ),
    ("210", "441"): Prestadora(
        nome="NIPPON TELEGRAPH AND TELEPHONE EAST CORPORATION",
        mnc="210",
        mcc="441",
        pais="Japan",
    ),
    ("211", "441"): Prestadora(
        nome="STARCAT CABLE NETWORK Co., LTD.",
        mnc="211",
        mcc="441",
        pais="Japan",
    ),
    ("212", "441"): Prestadora(
        nome="I-TEC Solutions Co., Ltd.", mnc="212", mcc="441", pais="Japan"
    ),
    ("213", "441"): Prestadora(
        nome="Hokkaido Telecommunication Network Co., Inc.",
        mnc="213",
        mcc="441",
        pais="Japan",
    ),
    ("01", "416"): Prestadora(nome="Fastlink", mnc="01", mcc="416", pais="Jordan"),
    ("02", "416"): Prestadora(nome="Xpress", mnc="02", mcc="416", pais="Jordan"),
    ("03", "416"): Prestadora(nome="Umniah", mnc="03", mcc="416", pais="Jordan"),
    ("77", "416"): Prestadora(nome="MobileCom", mnc="77", mcc="416", pais="Jordan"),
    ("01", "401"): Prestadora(
        nome="Kar-Tel llc", mnc="01", mcc="401", pais="Kazakhstan"
    ),
    ("02", "401"): Prestadora(
        nome="TSC Kazak Telecom", mnc="02", mcc="401", pais="Kazakhstan"
    ),
    ("01", "639"): Prestadora(nome="Safaricom PLC", mnc="01", mcc="639", pais="Kenya"),
    ("02", "639"): Prestadora(nome="Safaricom PLC", mnc="02", mcc="639", pais="Kenya"),
    ("03", "639"): Prestadora(
        nome="Airtel Networks Kenya Limited",
        mnc="03",
        mcc="639",
        pais="Kenya",
    ),
    ("04", "639"): Prestadora(
        nome="Mobile Pay Kenya Limited", mnc="04", mcc="639", pais="Kenya"
    ),
    ("05", "639"): Prestadora(
        nome="Airtel Networks Kenya Limited",
        mnc="05",
        mcc="639",
        pais="Kenya",
    ),
    ("06", "639"): Prestadora(
        nome="Finserve Africa Limited", mnc="06", mcc="639", pais="Kenya"
    ),
    ("07", "639"): Prestadora(
        nome="Telkom Kenya Limited", mnc="07", mcc="639", pais="Kenya"
    ),
    ("09", "639"): Prestadora(
        nome="Homeland Media Group Limited",
        mnc="09",
        mcc="639",
        pais="Kenya",
    ),
    ("10", "639"): Prestadora(
        nome="Jamii Telecommunications Limited",
        mnc="10",
        mcc="639",
        pais="Kenya",
    ),
    ("11", "639"): Prestadora(
        nome="Jambo Telcoms Limited", mnc="11", mcc="639", pais="Kenya"
    ),
    ("12", "639"): Prestadora(nome="Infura Limited", mnc="12", mcc="639", pais="Kenya"),
    ("01", "545"): Prestadora(nome="ATHKL", mnc="01", mcc="545", pais="Kiribati"),
    ("02", "545"): Prestadora(nome="OceanLink", mnc="02", mcc="545", pais="Kiribati"),
    ("01", "450"): Prestadora(
        nome="Globalstar Asia Pacific / Satellite network",
        mnc="01",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("02", "450"): Prestadora(
        nome="KT / 5G test bed", mnc="02", mcc="450", pais="Korea (Rep. of)"
    ),
    ("04", "450"): Prestadora(
        nome="KT / IoT network", mnc="04", mcc="450", pais="Korea (Rep. of)"
    ),
    ("05", "450"): Prestadora(
        nome="SK Telecom / 3G, 4G network",
        mnc="05",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("06", "450"): Prestadora(
        nome="LGU+ / 3G, 4G network",
        mnc="06",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("07", "450"): Prestadora(
        nome="KT Powertel / 3G network",
        mnc="07",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("08", "450"): Prestadora(
        nome="KT / 3G, 4G network",
        mnc="08",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("11", "450"): Prestadora(
        nome="SK Telecom / 3G, 4G  network",
        mnc="11",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("12", "450"): Prestadora(
        nome="SK Telecom / IoT network",
        mnc="12",
        mcc="450",
        pais="Korea (Rep. of)",
    ),
    ("01", "221"): Prestadora(
        nome="Telecom of Kosovo J.S.C.", mnc="01", mcc="221", pais="Kosovo*"
    ),
    ("02", "221"): Prestadora(
        nome="IPKO Telecommunications LLC",
        mnc="02",
        mcc="221",
        pais="Kosovo*",
    ),
    ("07", "221"): Prestadora(
        nome="Dukagjini Telecommunications LLC",
        mnc="07",
        mcc="221",
        pais="Kosovo*",
    ),
    ("02", "419"): Prestadora(nome="ZAIN", mnc="02", mcc="419", pais="Kuwait"),
    ("03", "419"): Prestadora(
        nome="Wataniya Telecom", mnc="03", mcc="419", pais="Kuwait"
    ),
    ("04", "419"): Prestadora(nome="Viva", mnc="04", mcc="419", pais="Kuwait"),
    ("01", "437"): Prestadora(
        nome="Sky Mobile", mnc="01", mcc="437", pais="Kyrgyzstan"
    ),
    ("03", "437"): Prestadora(nome="7 Mobile", mnc="03", mcc="437", pais="Kyrgyzstan"),
    ("05", "437"): Prestadora(
        nome="Alfa Telecom", mnc="05", mcc="437", pais="Kyrgyzstan"
    ),
    ("06", "437"): Prestadora(
        nome="Kyrgyztelecom", mnc="06", mcc="437", pais="Kyrgyzstan"
    ),
    ("09", "437"): Prestadora(
        nome="Nur Telecom", mnc="09", mcc="437", pais="Kyrgyzstan"
    ),
    ("10", "437"): Prestadora(
        nome="Saima Telecom", mnc="10", mcc="437", pais="Kyrgyzstan"
    ),
    ("11", "437"): Prestadora(nome="iTel", mnc="11", mcc="437", pais="Kyrgyzstan"),
    ("01", "457"): Prestadora(
        nome="Lao Telecommunication Public Company",
        mnc="01",
        mcc="457",
        pais="Lao P.D.R.",
    ),
    ("02", "457"): Prestadora(
        nome="ETL Company Limited", mnc="02", mcc="457", pais="Lao P.D.R."
    ),
    ("03", "457"): Prestadora(
        nome="Star Telecom Co., Ltd", mnc="03", mcc="457", pais="Lao P.D.R."
    ),
    ("07", "457"): Prestadora(
        nome="Best Telecom Co., Ltd", mnc="07", mcc="457", pais="Lao P.D.R."
    ),
    ("08", "457"): Prestadora(
        nome="TPLUS Digital Sole Company Limited",
        mnc="08",
        mcc="457",
        pais="Lao P.D.R.",
    ),
    ("01", "247"): Prestadora(
        nome="Latvijas Mobilais Telefons SIA",
        mnc="01",
        mcc="247",
        pais="Latvia",
    ),
    ("02", "247"): Prestadora(nome="Tele2", mnc="02", mcc="247", pais="Latvia"),
    ("03", "247"): Prestadora(
        nome="Telekom Baltija", mnc="03", mcc="247", pais="Latvia"
    ),
    ("04", "247"): Prestadora(nome="Beta Telecom", mnc="04", mcc="247", pais="Latvia"),
    ("05", "247"): Prestadora(nome="Bite Mobile", mnc="05", mcc="247", pais="Latvia"),
    ("06", "247"): Prestadora(nome="Rigatta", mnc="06", mcc="247", pais="Latvia"),
    ("07", "247"): Prestadora(
        nome="Master Telecom", mnc="07", mcc="247", pais="Latvia"
    ),
    ("08", "247"): Prestadora(nome="IZZI", mnc="08", mcc="247", pais="Latvia"),
    ("09", "247"): Prestadora(
        nome='SIA Camel Mobile""', mnc="09", mcc="247", pais="Latvia"
    ),
    ("05", "415"): Prestadora(
        nome="Ogero Telecom", mnc="05", mcc="415", pais="Lebanon"
    ),
    ("32", "415"): Prestadora(nome="Cellis", mnc="32", mcc="415", pais="Lebanon"),
    ("33", "415"): Prestadora(nome="Cellis", mnc="33", mcc="415", pais="Lebanon"),
    ("34", "415"): Prestadora(nome="Cellis", mnc="34", mcc="415", pais="Lebanon"),
    ("35", "415"): Prestadora(nome="Cellis", mnc="35", mcc="415", pais="Lebanon"),
    ("36", "415"): Prestadora(nome="Libancell", mnc="36", mcc="415", pais="Lebanon"),
    ("37", "415"): Prestadora(nome="Libancell", mnc="37", mcc="415", pais="Lebanon"),
    ("38", "415"): Prestadora(nome="Libancell", mnc="38", mcc="415", pais="Lebanon"),
    ("39", "415"): Prestadora(nome="Libancell", mnc="39", mcc="415", pais="Lebanon"),
    ("01", "651"): Prestadora(
        nome="Vodacom Lesotho (pty) Ltd.",
        mnc="01",
        mcc="651",
        pais="Lesotho",
    ),
    ("02", "651"): Prestadora(
        nome="Econet Ezin-cel", mnc="02", mcc="651", pais="Lesotho"
    ),
    ("10", "651"): Prestadora(
        nome="VODACOM LESOTHO", mnc="10", mcc="651", pais="Lesotho"
    ),
    ("04", "618"): Prestadora(
        nome="Comium Liberia", mnc="04", mcc="618", pais="Liberia"
    ),
    ("01", "228"): Prestadora(
        nome="Swisscom Schweiz AG", mnc="01", mcc="228", pais="Liechtenstein"
    ),
    ("01", "295"): Prestadora(
        nome="Swisscom Schweiz AG", mnc="01", mcc="295", pais="Liechtenstein"
    ),
    ("02", "295"): Prestadora(
        nome="Salt (Liechtenstein) AG",
        mnc="02",
        mcc="295",
        pais="Liechtenstein",
    ),
    ("05", "295"): Prestadora(
        nome="Telecom Liechtenstein AG",
        mnc="05",
        mcc="295",
        pais="Liechtenstein",
    ),
    ("06", "295"): Prestadora(
        nome="Cubic AG", mnc="06", mcc="295", pais="Liechtenstein"
    ),
    ("09", "295"): Prestadora(
        nome="Emnify GmbH", mnc="09", mcc="295", pais="Liechtenstein"
    ),
    ("10", "295"): Prestadora(
        nome="SORACOM CORPORATION, LTD.",
        mnc="10",
        mcc="295",
        pais="Liechtenstein",
    ),
    ("11", "295"): Prestadora(
        nome="DIMOCO Messaging AG", mnc="11", mcc="295", pais="Liechtenstein"
    ),
    ("01", "246"): Prestadora(nome="Omnitel", mnc="01", mcc="246", pais="Lithuania"),
    ("02", "246"): Prestadora(nome="Bité GSM", mnc="02", mcc="246", pais="Lithuania"),
    ("03", "246"): Prestadora(nome="Tele2", mnc="03", mcc="246", pais="Lithuania"),
    ("01", "270"): Prestadora(
        nome="POST Luxembourg", mnc="01", mcc="270", pais="Luxembourg"
    ),
    ("02", "270"): Prestadora(
        nome="MTX Connect S.à r.l.", mnc="02", mcc="270", pais="Luxembourg"
    ),
    ("05", "270"): Prestadora(
        nome="Luxembourg Online S.A.", mnc="05", mcc="270", pais="Luxembourg"
    ),
    ("07", "270"): Prestadora(
        nome="Bouygues Telecom S.A.", mnc="07", mcc="270", pais="Luxembourg"
    ),
    ("10", "270"): Prestadora(
        nome="Join Experience S.A.", mnc="10", mcc="270", pais="Luxembourg"
    ),
    ("78", "270"): Prestadora(
        nome="Interactive Digital Media GmbH",
        mnc="78",
        mcc="270",
        pais="Luxembourg",
    ),
    ("79", "270"): Prestadora(
        nome="Mitto A.G.", mnc="79", mcc="270", pais="Luxembourg"
    ),
    ("80", "270"): Prestadora(
        nome="Syniverse Technologies S.à r.l.",
        mnc="80",
        mcc="270",
        pais="Luxembourg",
    ),
    ("81", "270"): Prestadora(
        nome="E-Lux Mobile Telecommunication S.A.",
        mnc="81",
        mcc="270",
        pais="Luxembourg",
    ),
    ("00", "455"): Prestadora(
        nome="SmarTone – Comunicações Móveis, S.A.",
        mnc="00",
        mcc="455",
        pais="Macao, China",
    ),
    ("01", "455"): Prestadora(
        nome="Companhia de Telecomunicações de Macau, S.A.R.L.",
        mnc="01",
        mcc="455",
        pais="Macao, China",
    ),
    ("02", "455"): Prestadora(
        nome="China Telecom (Macau) Limitada",
        mnc="02",
        mcc="455",
        pais="Macao, China",
    ),
    ("03", "455"): Prestadora(
        nome="Hutchison – Telefone (Macau), Limitada",
        mnc="03",
        mcc="455",
        pais="Macao, China",
    ),
    ("04", "455"): Prestadora(
        nome="Companhia de Telecomunicações de Macau, S.A.R.L.",
        mnc="04",
        mcc="455",
        pais="Macao, China",
    ),
    ("05", "455"): Prestadora(
        nome="Hutchison – Telefone (Macau), Limitada",
        mnc="05",
        mcc="455",
        pais="Macao, China",
    ),
    ("06", "455"): Prestadora(
        nome="SmarTone – Comunicações Móveis, S.A.",
        mnc="06",
        mcc="455",
        pais="Macao, China",
    ),
    ("07", "455"): Prestadora(
        nome="China Telecom (Macau) Limitada",
        mnc="07",
        mcc="455",
        pais="Macao, China",
    ),
    ("01", "646"): Prestadora(
        nome="Celtel Madagascar (Zain), GSM",
        mnc="01",
        mcc="646",
        pais="Madagascar",
    ),
    ("02", "646"): Prestadora(
        nome="Orange Madagascar, GSM", mnc="02", mcc="646", pais="Madagascar"
    ),
    ("04", "646"): Prestadora(
        nome="Telecom Malagasy Mobile, GSM",
        mnc="04",
        mcc="646",
        pais="Madagascar",
    ),
    ("01", "650"): Prestadora(
        nome="Telekom Network Ltd.", mnc="01", mcc="650", pais="Malawi"
    ),
    ("10", "650"): Prestadora(nome="Celtel ltd.", mnc="10", mcc="650", pais="Malawi"),
    ("10", "502"): Prestadora(
        nome="DIGI Telecommunications", mnc="10", mcc="502", pais="Malaysia"
    ),
    ("12", "502"): Prestadora(
        nome="Malaysian Mobile Services Sdn Bhd",
        mnc="12",
        mcc="502",
        pais="Malaysia",
    ),
    ("13", "502"): Prestadora(
        nome="Celcom (Malaysia) Berhad", mnc="13", mcc="502", pais="Malaysia"
    ),
    ("14", "502"): Prestadora(
        nome="Telekom Malaysia Berhad", mnc="14", mcc="502", pais="Malaysia"
    ),
    ("16", "502"): Prestadora(
        nome="DIGI Telecommunications", mnc="16", mcc="502", pais="Malaysia"
    ),
    ("17", "502"): Prestadora(
        nome="Malaysian Mobile Services Sdn Bhd",
        mnc="17",
        mcc="502",
        pais="Malaysia",
    ),
    ("18", "502"): Prestadora(
        nome="U Mobile Sdn. Bhd.", mnc="18", mcc="502", pais="Malaysia"
    ),
    ("19", "502"): Prestadora(
        nome="Celcom (Malaysia) Berhad", mnc="19", mcc="502", pais="Malaysia"
    ),
    ("20", "502"): Prestadora(
        nome="Electcoms Wireless Sdn Bhd",
        mnc="20",
        mcc="502",
        pais="Malaysia",
    ),
    ("01", "472"): Prestadora(nome="DhiMobile", mnc="01", mcc="472", pais="Maldives"),
    ("01", "610"): Prestadora(nome="Malitel", mnc="01", mcc="610", pais="Mali"),
    ("02", "610"): Prestadora(nome="Orange Mali Sa", mnc="02", mcc="610", pais="Mali"),
    ("03", "610"): Prestadora(nome="ATEL-SA", mnc="03", mcc="610", pais="Mali"),
    ("01", "278"): Prestadora(
        nome="Epic Communications Ltd", mnc="01", mcc="278", pais="Malta"
    ),
    ("21", "278"): Prestadora(nome="GO Mobile", mnc="21", mcc="278", pais="Malta"),
    ("30", "278"): Prestadora(nome="GO Mobile", mnc="30", mcc="278", pais="Malta"),
    ("77", "278"): Prestadora(nome="Melita Ltd", mnc="77", mcc="278", pais="Malta"),
    ("01", "609"): Prestadora(
        nome="Mattel S.A.", mnc="01", mcc="609", pais="Mauritania"
    ),
    ("02", "609"): Prestadora(
        nome="Chinguitel S.A.", mnc="02", mcc="609", pais="Mauritania"
    ),
    ("10", "609"): Prestadora(
        nome="Mauritel Mobiles", mnc="10", mcc="609", pais="Mauritania"
    ),
    ("01", "617"): Prestadora(nome="Cellplus", mnc="01", mcc="617", pais="Mauritius"),
    ("02", "617"): Prestadora(
        nome="Mahanagar Telephone (Mauritius) Ltd",
        mnc="02",
        mcc="617",
        pais="Mauritius",
    ),
    ("03", "617"): Prestadora(
        nome="Mahanagar Telephone (Mauritius) Ltd",
        mnc="03",
        mcc="617",
        pais="Mauritius",
    ),
    ("10", "617"): Prestadora(nome="Emtel", mnc="10", mcc="617", pais="Mauritius"),
    ("001", "334"): Prestadora(
        nome="COMUNICACIONES DIGITALES DEL NORTE, S.A. DE C.V.",
        mnc="001",
        mcc="334",
        pais="Mexico",
    ),
    ("010", "334"): Prestadora(
        nome="AT&T COMUNICACIONES DIGITALES, S. DE R.L. DE C.V.",
        mnc="010",
        mcc="334",
        pais="Mexico",
    ),
    ("020", "334"): Prestadora(
        nome="RADIOMÓVIL DIPSA, S.A. DE C.V.",
        mnc="020",
        mcc="334",
        pais="Mexico",
    ),
    ("030", "334"): Prestadora(
        nome="PEGASO PCS, S.A. DE C.V.", mnc="030", mcc="334", pais="Mexico"
    ),
    ("040", "334"): Prestadora(
        nome="AT&T NORTE, S. DE R.L. DE C.V. Y AT&T DESARROLLO EN COMUNICACIONES DE MÉXICO, S. DE R.L. DE C.V.",
        mnc="040",
        mcc="334",
        pais="Mexico",
    ),
    ("050", "334"): Prestadora(
        nome="GRUPO AT&T CELULLAR, S. DE R.L. DE C.V.",
        mnc="050",
        mcc="334",
        pais="Mexico",
    ),
    ("060", "334"): Prestadora(
        nome="SERVICIOS DE ACCESO INALÁMBRICO, S.A DE C.V.",
        mnc="060",
        mcc="334",
        pais="Mexico",
    ),
    ("066", "334"): Prestadora(
        nome="TELÉFONOS DE MÉXICO, S.A.B. DE C.V.",
        mnc="066",
        mcc="334",
        pais="Mexico",
    ),
    ("070", "334"): Prestadora(
        nome="AT&T COMERCIALIZACIÓN MÓVIL, S. DE R.L. DE C.V.",
        mnc="070",
        mcc="334",
        pais="Mexico",
    ),
    ("080", "334"): Prestadora(
        nome="AT&T COMERCIALIZACIÓN MÓVIL, S. DE R.L. DE C.V.",
        mnc="080",
        mcc="334",
        pais="Mexico",
    ),
    ("090", "334"): Prestadora(
        nome="AT&T COMUNICACIONES DIGITALES, S. DE R.L. DE C.V.",
        mnc="090",
        mcc="334",
        pais="Mexico",
    ),
    ("100", "334"): Prestadora(
        nome="TELECOMUNICACIONES DE MÉXICO",
        mnc="100",
        mcc="334",
        pais="Mexico",
    ),
    ("110", "334"): Prestadora(
        nome="MAXCOM TELECOMUNICACIONES, S.A.B. DE C.V.",
        mnc="110",
        mcc="334",
        pais="Mexico",
    ),
    ("120", "334"): Prestadora(
        nome="QUICKLY PHONE, S.A. DE C.V.",
        mnc="120",
        mcc="334",
        pais="Mexico",
    ),
    ("130", "334"): Prestadora(
        nome="AXTEL, S.A.B. DE C.V.", mnc="130", mcc="334", pais="Mexico"
    ),
    ("140", "334"): Prestadora(
        nome="ALTÁN REDES, S.A.P.I. DE C.V.",
        mnc="140",
        mcc="334",
        pais="Mexico",
    ),
    ("150", "334"): Prestadora(
        nome="ULTRAVISIÓN, S.A. DE C.V.", mnc="150", mcc="334", pais="Mexico"
    ),
    ("160", "334"): Prestadora(
        nome="CABLEVISIÓN RED, S.A. DE C.V.",
        mnc="160",
        mcc="334",
        pais="Mexico",
    ),
    ("170", "334"): Prestadora(
        nome="OXIO MOBILE, S.A. DE C.V.", mnc="170", mcc="334", pais="Mexico"
    ),
    ("180", "334"): Prestadora(
        nome="FREEDOMPOP MÉXICO, S.A. DE C.V.",
        mnc="180",
        mcc="334",
        pais="Mexico",
    ),
    ("190", "334"): Prestadora(
        nome="VIASAT TECNOLOGÍA, S.A. DE C.V.",
        mnc="190",
        mcc="334",
        pais="Mexico",
    ),
    ("01", "550"): Prestadora(
        nome="FSM Telecom", mnc="01", mcc="550", pais="Micronesia"
    ),
    ("01", "259"): Prestadora(
        nome="Orange Moldova GSM",
        mnc="01",
        mcc="259",
        pais="Moldova (Republic of)",
    ),
    ("02", "259"): Prestadora(
        nome="Moldcell GSM",
        mnc="02",
        mcc="259",
        pais="Moldova (Republic of)",
    ),
    ("05", "259"): Prestadora(
        nome="J.S.C. Moldtelecom/3G UMTS (W-CDMA)",
        mnc="05",
        mcc="259",
        pais="Moldova (Republic of)",
    ),
    ("99", "259"): Prestadora(
        nome="J.S.C. Moldtelecom",
        mnc="99",
        mcc="259",
        pais="Moldova (Republic of)",
    ),
    ("10", "212"): Prestadora(
        nome="Monaco Telecom", mnc="10", mcc="212", pais="Monaco"
    ),
    ("99", "428"): Prestadora(nome="Mobicom", mnc="99", mcc="428", pais="Mongolia"),
    ("01", "297"): Prestadora(
        nome="Telenor Montenegro", mnc="01", mcc="297", pais="Montenegro"
    ),
    ("02", "297"): Prestadora(
        nome="Crnogorski Telekom", mnc="02", mcc="297", pais="Montenegro"
    ),
    ("03", "297"): Prestadora(
        nome="Mtel Montenegro", mnc="03", mcc="297", pais="Montenegro"
    ),
    ("860", "354"): Prestadora(
        nome="Cable & Wireless (West Indies) Ltd trading as Lime",
        mnc="860",
        mcc="354",
        pais="Montserrat",
    ),
    ("00", "604"): Prestadora(nome="Médi Télécom", mnc="00", mcc="604", pais="Morocco"),
    ("01", "604"): Prestadora(
        nome="Itissalat Al-Maghrib", mnc="01", mcc="604", pais="Morocco"
    ),
    ("02", "604"): Prestadora(
        nome="Wana Corporate", mnc="02", mcc="604", pais="Morocco"
    ),
    ("04", "604"): Prestadora(
        nome="Al Houria Telecom", mnc="04", mcc="604", pais="Morocco"
    ),
    ("05", "604"): Prestadora(
        nome="Wana Corporate", mnc="05", mcc="604", pais="Morocco"
    ),
    ("06", "604"): Prestadora(
        nome="Itissalat Al-Maghrib", mnc="06", mcc="604", pais="Morocco"
    ),
    ("99", "604"): Prestadora(
        nome="Al Houria Telecom", mnc="99", mcc="604", pais="Morocco"
    ),
    ("01", "643"): Prestadora(
        nome="T.D.M. GSM", mnc="01", mcc="643", pais="Mozambique"
    ),
    ("03", "643"): Prestadora(nome="Movitel", mnc="03", mcc="643", pais="Mozambique"),
    ("04", "643"): Prestadora(nome="VM Sarl", mnc="04", mcc="643", pais="Mozambique"),
    ("00", "414"): Prestadora(
        nome="Myanmar Posts and Telecommunications",
        mnc="00",
        mcc="414",
        pais="Myanmar",
    ),
    ("01", "414"): Prestadora(
        nome="Myanmar Posts and Telecommunications",
        mnc="01",
        mcc="414",
        pais="Myanmar",
    ),
    ("02", "414"): Prestadora(
        nome="Myanmar Posts and Telecommunications",
        mnc="02",
        mcc="414",
        pais="Myanmar",
    ),
    ("03", "414"): Prestadora(
        nome="Myanmar Economic Corporation",
        mnc="03",
        mcc="414",
        pais="Myanmar",
    ),
    ("04", "414"): Prestadora(
        nome="Myanmar Posts and Telecommunications",
        mnc="04",
        mcc="414",
        pais="Myanmar",
    ),
    ("05", "414"): Prestadora(
        nome="Ooredoo Myanmar Limited", mnc="05", mcc="414", pais="Myanmar"
    ),
    ("06", "414"): Prestadora(
        nome="Telenor Myanmar Limited", mnc="06", mcc="414", pais="Myanmar"
    ),
    ("09", "414"): Prestadora(
        nome="Myanmar National Tele & Communication Co.,Ltd",
        mnc="09",
        mcc="414",
        pais="Myanmar",
    ),
    ("20", "414"): Prestadora(
        nome="Amara Communication Co.,Ltd",
        mnc="20",
        mcc="414",
        pais="Myanmar",
    ),
    ("21", "414"): Prestadora(
        nome="Amara Communication Co.,Ltd",
        mnc="21",
        mcc="414",
        pais="Myanmar",
    ),
    ("22", "414"): Prestadora(
        nome="Fortune Telecom Co., Ltd", mnc="22", mcc="414", pais="Myanmar"
    ),
    ("23", "414"): Prestadora(
        nome="Global Technology Co., Ltd",
        mnc="23",
        mcc="414",
        pais="Myanmar",
    ),
    ("01", "649"): Prestadora(
        nome="Mobile Telecommunications Ltd.",
        mnc="01",
        mcc="649",
        pais="Namibia",
    ),
    ("02", "649"): Prestadora(
        nome="Telecom Namibia", mnc="02", mcc="649", pais="Namibia"
    ),
    ("03", "649"): Prestadora(
        nome="Powercom Pty Ltd (leo)", mnc="03", mcc="649", pais="Namibia"
    ),
    ("04", "649"): Prestadora(
        nome="Paratus Telecommunications (Pty)",
        mnc="04",
        mcc="649",
        pais="Namibia",
    ),
    ("05", "649"): Prestadora(
        nome="Demshi Investments CC", mnc="05", mcc="649", pais="Namibia"
    ),
    ("06", "649"): Prestadora(nome="MTN Namibia", mnc="06", mcc="649", pais="Namibia"),
    ("07", "649"): Prestadora(
        nome="Capricorn Connect", mnc="07", mcc="649", pais="Namibia"
    ),
    ("01", "429"): Prestadora(
        nome="Nepal Telecommunications", mnc="01", mcc="429", pais="Nepal"
    ),
    ("00", "204"): Prestadora(
        nome="Intovoice B.V.", mnc="00", mcc="204", pais="Netherlands"
    ),
    ("02", "204"): Prestadora(
        nome="T-Mobile Netherlands B.V.",
        mnc="02",
        mcc="204",
        pais="Netherlands",
    ),
    ("03", "204"): Prestadora(
        nome="Voiceworks B.V.", mnc="03", mcc="204", pais="Netherlands"
    ),
    ("04", "204"): Prestadora(
        nome="Vodafone Libertel B.V.",
        mnc="04",
        mcc="204",
        pais="Netherlands",
    ),
    ("06", "204"): Prestadora(
        nome="Private Mobility Nederland B.V.",
        mnc="06",
        mcc="204",
        pais="Netherlands",
    ),
    ("07", "204"): Prestadora(
        nome="Tata Communications MOVE B.V.",
        mnc="07",
        mcc="204",
        pais="Netherlands",
    ),
    ("08", "204"): Prestadora(nome="KPN B.V.", mnc="08", mcc="204", pais="Netherlands"),
    ("09", "204"): Prestadora(
        nome="Lycamobile Netherlands Limited",
        mnc="09",
        mcc="204",
        pais="Netherlands",
    ),
    ("10", "204"): Prestadora(nome="KPN B.V.", mnc="10", mcc="204", pais="Netherlands"),
    ("11", "204"): Prestadora(
        nome="Greenet Netwerk B.V.", mnc="11", mcc="204", pais="Netherlands"
    ),
    ("12", "204"): Prestadora(nome="KPN B.V.", mnc="12", mcc="204", pais="Netherlands"),
    ("13", "204"): Prestadora(
        nome="Unica Installatietechniek B.V.",
        mnc="13",
        mcc="204",
        pais="Netherlands",
    ),
    ("14", "204"): Prestadora(
        nome="Venus & Mercury Telecom",
        mnc="14",
        mcc="204",
        pais="Netherlands",
    ),
    ("15", "204"): Prestadora(
        nome="Ziggo B.V.", mnc="15", mcc="204", pais="Netherlands"
    ),
    ("16", "204"): Prestadora(
        nome="T-Mobile Netherlands B.V.",
        mnc="16",
        mcc="204",
        pais="Netherlands",
    ),
    ("17", "204"): Prestadora(
        nome="Lebara Ltd", mnc="17", mcc="204", pais="Netherlands"
    ),
    ("18", "204"): Prestadora(
        nome="Ziggo Services  B.V.", mnc="18", mcc="204", pais="Netherlands"
    ),
    ("19", "204"): Prestadora(
        nome="Mixe Communication Solutions B.V.",
        mnc="19",
        mcc="204",
        pais="Netherlands",
    ),
    ("20", "204"): Prestadora(
        nome="T-Mobile Netherlands B.V.",
        mnc="20",
        mcc="204",
        pais="Netherlands",
    ),
    ("21", "204"): Prestadora(
        nome="ProRail B.V.", mnc="21", mcc="204", pais="Netherlands"
    ),
    ("22", "204"): Prestadora(
        nome="Ministerie van Defensie",
        mnc="22",
        mcc="204",
        pais="Netherlands",
    ),
    ("23", "204"): Prestadora(
        nome="KORE Wireless Nederland B.V.",
        mnc="23",
        mcc="204",
        pais="Netherlands",
    ),
    ("24", "204"): Prestadora(
        nome="PM Factory B.V.", mnc="24", mcc="204", pais="Netherlands"
    ),
    ("25", "204"): Prestadora(
        nome="CapX Nederland", mnc="25", mcc="204", pais="Netherlands"
    ),
    ("26", "204"): Prestadora(
        nome="SpeakUp B.V.", mnc="26", mcc="204", pais="Netherlands"
    ),
    ("27", "204"): Prestadora(
        nome="L-Mobi Mobile B.V.", mnc="27", mcc="204", pais="Netherlands"
    ),
    ("28", "204"): Prestadora(
        nome="Lancelot B.V.", mnc="28", mcc="204", pais="Netherlands"
    ),
    ("29", "204"): Prestadora(
        nome="Tismi B.V.", mnc="29", mcc="204", pais="Netherlands"
    ),
    ("30", "204"): Prestadora(
        nome="ASpider Solutions Nederland B.V.",
        mnc="30",
        mcc="204",
        pais="Netherlands",
    ),
    ("32", "204"): Prestadora(
        nome="Cubic Telecom Limited", mnc="32", mcc="204", pais="Netherlands"
    ),
    ("33", "204"): Prestadora(
        nome="Truphone B.V.", mnc="33", mcc="204", pais="Netherlands"
    ),
    ("61", "204"): Prestadora(
        nome="Alcadis B.V.", mnc="61", mcc="204", pais="Netherlands"
    ),
    ("62", "204"): Prestadora(
        nome="RGTN Wholesale Netherlands B.V.",
        mnc="62",
        mcc="204",
        pais="Netherlands",
    ),
    ("63", "204"): Prestadora(
        nome="Messagebird BV", mnc="63", mcc="204", pais="Netherlands"
    ),
    ("64", "204"): Prestadora(
        nome="Zetacom B.V.", mnc="64", mcc="204", pais="Netherlands"
    ),
    ("66", "204"): Prestadora(
        nome="Utility Connect B.V.", mnc="66", mcc="204", pais="Netherlands"
    ),
    ("69", "204"): Prestadora(nome="KPN B.V.", mnc="69", mcc="204", pais="Netherlands"),
    ("91", "204"): Prestadora(
        nome="Enexis Netbeheer B.V.", mnc="91", mcc="204", pais="Netherlands"
    ),
    ("01", "546"): Prestadora(
        nome="OPT Mobilis", mnc="01", mcc="546", pais="New Caledonia"
    ),
    ("00", "530"): Prestadora(
        nome="Reserved for AMPS MIN based IMSI's",
        mnc="00",
        mcc="530",
        pais="New Zealand",
    ),
    ("01", "530"): Prestadora(
        nome="One New Zealand Group Limited",
        mnc="01",
        mcc="530",
        pais="New Zealand",
    ),
    ("02", "530"): Prestadora(
        nome="Teleom New Zealand CDMA Network",
        mnc="02",
        mcc="530",
        pais="New Zealand",
    ),
    ("03", "530"): Prestadora(
        nome="Woosh Wireless - CDMA Network",
        mnc="03",
        mcc="530",
        pais="New Zealand",
    ),
    ("04", "530"): Prestadora(
        nome="One New Zealand Group Limited",
        mnc="04",
        mcc="530",
        pais="New Zealand",
    ),
    ("05", "530"): Prestadora(
        nome="Telecom New Zealand - UMTS Ntework",
        mnc="05",
        mcc="530",
        pais="New Zealand",
    ),
    ("06", "530"): Prestadora(
        nome="FX Networks Ltd", mnc="06", mcc="530", pais="New Zealand"
    ),
    ("07", "530"): Prestadora(
        nome="Dense Air New Zealand Ltd",
        mnc="07",
        mcc="530",
        pais="New Zealand",
    ),
    ("11", "530"): Prestadora(
        nome="Interim Māori Spectrum Commission",
        mnc="11",
        mcc="530",
        pais="New Zealand",
    ),
    ("24", "530"): Prestadora(
        nome="NZ Communications - UMTS Network",
        mnc="24",
        mcc="530",
        pais="New Zealand",
    ),
    ("21", "710"): Prestadora(
        nome="Empresa Nicaragüense de Telecomunicaciones, S.A. (ENITEL)",
        mnc="21",
        mcc="710",
        pais="Nicaragua",
    ),
    ("73", "710"): Prestadora(
        nome="Servicios de Comunicaciones, S.A. (SERCOM)",
        mnc="73",
        mcc="710",
        pais="Nicaragua",
    ),
    ("01", "614"): Prestadora(nome="Sahel.Com", mnc="01", mcc="614", pais="Niger"),
    ("02", "614"): Prestadora(nome="Celtel", mnc="02", mcc="614", pais="Niger"),
    ("03", "614"): Prestadora(nome="Telecel", mnc="03", mcc="614", pais="Niger"),
    ("20", "621"): Prestadora(
        nome="Econet Wireless Nigeria Ltd.",
        mnc="20",
        mcc="621",
        pais="Nigeria",
    ),
    ("30", "621"): Prestadora(
        nome="MTN Nigeria Communications",
        mnc="30",
        mcc="621",
        pais="Nigeria",
    ),
    ("40", "621"): Prestadora(nome="MTEL", mnc="40", mcc="621", pais="Nigeria"),
    ("50", "621"): Prestadora(nome="Globacom", mnc="50", mcc="621", pais="Nigeria"),
    ("60", "621"): Prestadora(nome="EMTS", mnc="60", mcc="621", pais="Nigeria"),
    ("01", "555"): Prestadora(nome="Telecom Niue", mnc="01", mcc="555", pais="Niue"),
    ("01", "294"): Prestadora(
        nome="T-Mobile", mnc="01", mcc="294", pais="North Macedonia"
    ),
    ("02", "294"): Prestadora(
        nome="Cosmofon", mnc="02", mcc="294", pais="North Macedonia"
    ),
    ("03", "294"): Prestadora(
        nome="Nov Operator", mnc="03", mcc="294", pais="North Macedonia"
    ),
    ("04", "294"): Prestadora(
        nome="Company for telecommunications LYCAMOBILE LLC-Skopje",
        mnc="04",
        mcc="294",
        pais="North Macedonia",
    ),
    ("10", "294"): Prestadora(
        nome="WTI Macedonia", mnc="10", mcc="294", pais="North Macedonia"
    ),
    ("11", "294"): Prestadora(
        nome="MOBIK TELEKOMUNIKACII DOOEL- Skopje",
        mnc="11",
        mcc="294",
        pais="North Macedonia",
    ),
    ("12", "294"): Prestadora(
        nome="MTEL DOOEL Skopje", mnc="12", mcc="294", pais="North Macedonia"
    ),
    ("01", "242"): Prestadora(
        nome="Telenor Norge AS", mnc="01", mcc="242", pais="Norway"
    ),
    ("02", "242"): Prestadora(
        nome="Telia Norge AS", mnc="02", mcc="242", pais="Norway"
    ),
    ("03", "242"): Prestadora(
        nome="Teletopia Gruppen AS", mnc="03", mcc="242", pais="Norway"
    ),
    ("05", "242"): Prestadora(
        nome="Telia Norge AS", mnc="05", mcc="242", pais="Norway"
    ),
    ("06", "242"): Prestadora(nome="ICE Norge AS", mnc="06", mcc="242", pais="Norway"),
    ("07", "242"): Prestadora(nome="Phonero AS", mnc="07", mcc="242", pais="Norway"),
    ("08", "242"): Prestadora(nome="TDC AS", mnc="08", mcc="242", pais="Norway"),
    ("09", "242"): Prestadora(nome="Com4 AS", mnc="09", mcc="242", pais="Norway"),
    ("10", "242"): Prestadora(
        nome="Norwegian Communications Authority",
        mnc="10",
        mcc="242",
        pais="Norway",
    ),
    ("11", "242"): Prestadora(nome="Systemnet AS", mnc="11", mcc="242", pais="Norway"),
    ("12", "242"): Prestadora(
        nome="Telenor Norge AS", mnc="12", mcc="242", pais="Norway"
    ),
    ("14", "242"): Prestadora(
        nome="ICE Communication Norge AS", mnc="14", mcc="242", pais="Norway"
    ),
    ("20", "242"): Prestadora(
        nome="Jernbaneverket", mnc="20", mcc="242", pais="Norway"
    ),
    ("21", "242"): Prestadora(
        nome="Jernbaneverket", mnc="21", mcc="242", pais="Norway"
    ),
    ("23", "242"): Prestadora(
        nome="Lycamobile Norway Ltd", mnc="23", mcc="242", pais="Norway"
    ),
    ("99", "242"): Prestadora(nome="Tampnet AS", mnc="99", mcc="242", pais="Norway"),
    ("02", "422"): Prestadora(
        nome="Oman Mobile Telecommunications Company (Oman Mobile)",
        mnc="02",
        mcc="422",
        pais="Oman",
    ),
    ("03", "422"): Prestadora(
        nome="Oman Qatari Telecommunications Company (Nawras)",
        mnc="03",
        mcc="422",
        pais="Oman",
    ),
    ("04", "422"): Prestadora(
        nome="Oman Telecommunications Company (Omantel)",
        mnc="04",
        mcc="422",
        pais="Oman",
    ),
    ("06", "422"): Prestadora(nome="Vodafone Oman", mnc="06", mcc="422", pais="Oman"),
    ("01", "410"): Prestadora(nome="Mobilink", mnc="01", mcc="410", pais="Pakistan"),
    ("03", "410"): Prestadora(
        nome="PAK Telecom Mobile Ltd. (UFONE)",
        mnc="03",
        mcc="410",
        pais="Pakistan",
    ),
    ("04", "410"): Prestadora(nome="CMPak", mnc="04", mcc="410", pais="Pakistan"),
    ("06", "410"): Prestadora(
        nome="Telenor Pakistan", mnc="06", mcc="410", pais="Pakistan"
    ),
    ("07", "410"): Prestadora(
        nome="Warid Telecom", mnc="07", mcc="410", pais="Pakistan"
    ),
    ("01", "552"): Prestadora(
        nome="Palau National Communications Corp. (a.k.a. PNCC)",
        mnc="01",
        mcc="552",
        pais="Palau",
    ),
    ("02", "552"): Prestadora(
        nome="PECI / PalauTel", mnc="02", mcc="552", pais="Palau"
    ),
    ("99", "552"): Prestadora(
        nome="Palau Mobile Communications Inc. (PMCI)",
        mnc="99",
        mcc="552",
        pais="Palau",
    ),
    ("01", "714"): Prestadora(
        nome="Cable & Wireless Panama S.A.",
        mnc="01",
        mcc="714",
        pais="Panama",
    ),
    ("02", "714"): Prestadora(
        nome="Grupo de Comunicaciones Digitales, S.A. (TIGO)",
        mnc="02",
        mcc="714",
        pais="Panama",
    ),
    ("03", "714"): Prestadora(
        nome="Claro Panamá, S.A.", mnc="03", mcc="714", pais="Panama"
    ),
    ("04", "714"): Prestadora(
        nome="Digicel (Panamá), S.A.", mnc="04", mcc="714", pais="Panama"
    ),
    ("05", "714"): Prestadora(
        nome="Cable & Wireless Panamá, S.A.",
        mnc="05",
        mcc="714",
        pais="Panama",
    ),
    ("020", "714"): Prestadora(
        nome="Grupo de Comunicaciones Digitales, S.A. (TIGO)",
        mnc="020",
        mcc="714",
        pais="Panama",
    ),
    ("01", "537"): Prestadora(
        nome="Bmobile", mnc="01", mcc="537", pais="Papua New Guinea"
    ),
    ("02", "537"): Prestadora(
        nome="Telikom PNG Ltd", mnc="02", mcc="537", pais="Papua New Guinea"
    ),
    ("03", "537"): Prestadora(
        nome="Digicel Ltd", mnc="03", mcc="537", pais="Papua New Guinea"
    ),
    ("04", "537"): Prestadora(
        nome="Digitec Communication Limited",
        mnc="04",
        mcc="537",
        pais="Papua New Guinea",
    ),
    ("01", "744"): Prestadora(
        nome="Hóla Paraguay S.A.", mnc="01", mcc="744", pais="Paraguay"
    ),
    ("02", "744"): Prestadora(
        nome="Hutchison Telecom S.A.", mnc="02", mcc="744", pais="Paraguay"
    ),
    ("03", "744"): Prestadora(
        nome="Compañia Privada de Comunicaciones S.A.",
        mnc="03",
        mcc="744",
        pais="Paraguay",
    ),
    ("10", "716"): Prestadora(nome="TIM Peru", mnc="10", mcc="716", pais="Peru"),
    ("01", "515"): Prestadora(nome="Islacom", mnc="01", mcc="515", pais="Philippines"),
    ("02", "515"): Prestadora(
        nome="Globe Telecom", mnc="02", mcc="515", pais="Philippines"
    ),
    ("03", "515"): Prestadora(
        nome="Smart Communications", mnc="03", mcc="515", pais="Philippines"
    ),
    ("05", "515"): Prestadora(nome="Digitel", mnc="05", mcc="515", pais="Philippines"),
    ("01", "260"): Prestadora(
        nome="Plus / Polkomtel S.A.", mnc="01", mcc="260", pais="Poland"
    ),
    ("02", "260"): Prestadora(
        nome="T-Mobile / PTC S.A.", mnc="02", mcc="260", pais="Poland"
    ),
    ("03", "260"): Prestadora(
        nome="Orange / PTK Centertel Sp. z o.o.",
        mnc="03",
        mcc="260",
        pais="Poland",
    ),
    ("04", "260"): Prestadora(
        nome="LTE / CenterNet S.A.", mnc="04", mcc="260", pais="Poland"
    ),
    ("05", "260"): Prestadora(
        nome="Orange(UMTS) / PTK Centertel Sp. z o.o.",
        mnc="05",
        mcc="260",
        pais="Poland",
    ),
    ("06", "260"): Prestadora(
        nome="Play / P4 Sp. z o.o.", mnc="06", mcc="260", pais="Poland"
    ),
    ("07", "260"): Prestadora(
        nome="Netia / Netia S.A.", mnc="07", mcc="260", pais="Poland"
    ),
    ("08", "260"): Prestadora(
        nome="E-Telko / E-Telko Sp. z o.o.",
        mnc="08",
        mcc="260",
        pais="Poland",
    ),
    ("09", "260"): Prestadora(
        nome="Lycamobile / Lycamobile Sp. z o.o.",
        mnc="09",
        mcc="260",
        pais="Poland",
    ),
    ("10", "260"): Prestadora(
        nome="Sferia / Sferia S.A.", mnc="10", mcc="260", pais="Poland"
    ),
    ("11", "260"): Prestadora(
        nome="Nordisk Polska / Nordisk Polska Sp. z o.o.",
        mnc="11",
        mcc="260",
        pais="Poland",
    ),
    ("12", "260"): Prestadora(
        nome="Cyfrowy Polsat / Cyfrowy Polsat S.A.",
        mnc="12",
        mcc="260",
        pais="Poland",
    ),
    ("13", "260"): Prestadora(
        nome="Sferia / Sferia S.A.", mnc="13", mcc="260", pais="Poland"
    ),
    ("14", "260"): Prestadora(
        nome="Sferia / Sferia S.A.", mnc="14", mcc="260", pais="Poland"
    ),
    ("15", "260"): Prestadora(
        nome="CenterNet / CenterNet S.A.", mnc="15", mcc="260", pais="Poland"
    ),
    ("16", "260"): Prestadora(
        nome="Mobyland / Mobyland Sp. z o.o.",
        mnc="16",
        mcc="260",
        pais="Poland",
    ),
    ("17", "260"): Prestadora(
        nome="Aero 2 / Aero 2 Sp. z o.o.", mnc="17", mcc="260", pais="Poland"
    ),
    ("18", "260"): Prestadora(
        nome="AMD Telecom / AMD Telecom S.A.",
        mnc="18",
        mcc="260",
        pais="Poland",
    ),
    ("19", "260"): Prestadora(
        nome="Teleena / Teleena Holding BV",
        mnc="19",
        mcc="260",
        pais="Poland",
    ),
    ("20", "260"): Prestadora(
        nome="Mobile.Net / Mobile.Net Sp. z o.o.",
        mnc="20",
        mcc="260",
        pais="Poland",
    ),
    ("21", "260"): Prestadora(
        nome="Exteri / Exteri Sp. z o.o.", mnc="21", mcc="260", pais="Poland"
    ),
    ("22", "260"): Prestadora(
        nome="Arcomm / Arcomm Sp. z o.o.", mnc="22", mcc="260", pais="Poland"
    ),
    ("23", "260"): Prestadora(
        nome="Amicomm / Amicomm Sp. z o.o.",
        mnc="23",
        mcc="260",
        pais="Poland",
    ),
    ("24", "260"): Prestadora(
        nome="WideNet / WideNet Sp. z o.o.",
        mnc="24",
        mcc="260",
        pais="Poland",
    ),
    ("25", "260"): Prestadora(
        nome="BS&T / Best Solutions & Technology Sp. z o.o.",
        mnc="25",
        mcc="260",
        pais="Poland",
    ),
    ("26", "260"): Prestadora(
        nome="ATE / ATE-Advanced Technology & Experience Sp. z o.o.",
        mnc="26",
        mcc="260",
        pais="Poland",
    ),
    ("27", "260"): Prestadora(
        nome="Intertelcom / Intertelcom Sp. z o.o.",
        mnc="27",
        mcc="260",
        pais="Poland",
    ),
    ("28", "260"): Prestadora(
        nome="PhoneNet / PhoneNet Sp. z o.o.",
        mnc="28",
        mcc="260",
        pais="Poland",
    ),
    ("29", "260"): Prestadora(
        nome="Interfonica / Interfonica Sp. z o.o.",
        mnc="29",
        mcc="260",
        pais="Poland",
    ),
    ("30", "260"): Prestadora(
        nome="GrandTel / GrandTel Sp. z o.o.",
        mnc="30",
        mcc="260",
        pais="Poland",
    ),
    ("31", "260"): Prestadora(
        nome="Phone IT / Phone IT Sp. z o.o.",
        mnc="31",
        mcc="260",
        pais="Poland",
    ),
    ("32", "260"): Prestadora(
        nome="Compatel Ltd / COMPATEL LIMITED",
        mnc="32",
        mcc="260",
        pais="Poland",
    ),
    ("33", "260"): Prestadora(
        nome="Truphone Poland / Truphone Poland Sp. Z o.o.",
        mnc="33",
        mcc="260",
        pais="Poland",
    ),
    ("34", "260"): Prestadora(
        nome="T-Mobile / PTC S.A.", mnc="34", mcc="260", pais="Poland"
    ),
    ("98", "260"): Prestadora(
        nome="Play (testowy) / P4 Sp. z o.o.",
        mnc="98",
        mcc="260",
        pais="Poland",
    ),
    ("01", "268"): Prestadora(
        nome="Vodafone Portugal - Comunicações Pessoais, S.A.",
        mnc="01",
        mcc="268",
        pais="Portugal",
    ),
    ("03", "268"): Prestadora(
        nome="NOS Comunicações, S.A.", mnc="03", mcc="268", pais="Portugal"
    ),
    ("04", "268"): Prestadora(
        nome="Lycamobile Portugal, Lda", mnc="04", mcc="268", pais="Portugal"
    ),
    ("06", "268"): Prestadora(
        nome="MEO - Serviços de Comunicações e Multimédia, S.A.",
        mnc="06",
        mcc="268",
        pais="Portugal",
    ),
    ("11", "268"): Prestadora(
        nome="Compatel, Limited", mnc="11", mcc="268", pais="Portugal"
    ),
    ("12", "268"): Prestadora(
        nome="Infraestruturas de Portugal, S.A.",
        mnc="12",
        mcc="268",
        pais="Portugal",
    ),
    ("13", "268"): Prestadora(
        nome="G9Telecom, S.A.", mnc="13", mcc="268", pais="Portugal"
    ),
    ("80", "268"): Prestadora(
        nome="MEO - Serviços de Comunicações e Multimédia, S.A.",
        mnc="80",
        mcc="268",
        pais="Portugal",
    ),
    ("01", "427"): Prestadora(nome="QATARNET", mnc="01", mcc="427", pais="Qatar"),
    ("06", "427"): Prestadora(
        nome="Ooredoo Q.S.C./MOI LTE", mnc="06", mcc="427", pais="Qatar"
    ),
    ("01", "226"): Prestadora(nome="Vodafone", mnc="01", mcc="226", pais="Romania"),
    ("02", "226"): Prestadora(nome="Romtelecom", mnc="02", mcc="226", pais="Romania"),
    ("03", "226"): Prestadora(nome="Cosmote", mnc="03", mcc="226", pais="Romania"),
    ("04", "226"): Prestadora(nome="Cosmote", mnc="04", mcc="226", pais="Romania"),
    ("05", "226"): Prestadora(nome="Digi.Mobil", mnc="05", mcc="226", pais="Romania"),
    ("06", "226"): Prestadora(nome="Cosmote", mnc="06", mcc="226", pais="Romania"),
    ("10", "226"): Prestadora(nome="Orange", mnc="10", mcc="226", pais="Romania"),
    ("11", "226"): Prestadora(
        nome="Enigma-System", mnc="11", mcc="226", pais="Romania"
    ),
    ("01", "250"): Prestadora(
        nome="Mobile Telesystems",
        mnc="01",
        mcc="250",
        pais="Russian Federation",
    ),
    ("02", "250"): Prestadora(
        nome="Megafon", mnc="02", mcc="250", pais="Russian Federation"
    ),
    ("03", "250"): Prestadora(
        nome="Nizhegorodskaya Cellular Communications",
        mnc="03",
        mcc="250",
        pais="Russian Federation",
    ),
    ("04", "250"): Prestadora(
        nome="Sibchallenge", mnc="04", mcc="250", pais="Russian Federation"
    ),
    ("05", "250"): Prestadora(
        nome="Mobile Comms System",
        mnc="05",
        mcc="250",
        pais="Russian Federation",
    ),
    ("07", "250"): Prestadora(
        nome="BM Telecom", mnc="07", mcc="250", pais="Russian Federation"
    ),
    ("10", "250"): Prestadora(
        nome="Don Telecom", mnc="10", mcc="250", pais="Russian Federation"
    ),
    ("11", "250"): Prestadora(
        nome="Orensot", mnc="11", mcc="250", pais="Russian Federation"
    ),
    ("12", "250"): Prestadora(
        nome="Baykal Westcom", mnc="12", mcc="250", pais="Russian Federation"
    ),
    ("13", "250"): Prestadora(
        nome="Kuban GSM", mnc="13", mcc="250", pais="Russian Federation"
    ),
    ("16", "250"): Prestadora(
        nome="New Telephone Company",
        mnc="16",
        mcc="250",
        pais="Russian Federation",
    ),
    ("17", "250"): Prestadora(
        nome="Ermak RMS", mnc="17", mcc="250", pais="Russian Federation"
    ),
    ("19", "250"): Prestadora(
        nome="Volgograd Mobile",
        mnc="19",
        mcc="250",
        pais="Russian Federation",
    ),
    ("20", "250"): Prestadora(
        nome="ECC", mnc="20", mcc="250", pais="Russian Federation"
    ),
    ("28", "250"): Prestadora(
        nome="Extel", mnc="28", mcc="250", pais="Russian Federation"
    ),
    ("39", "250"): Prestadora(
        nome="Uralsvyazinform",
        mnc="39",
        mcc="250",
        pais="Russian Federation",
    ),
    ("44", "250"): Prestadora(
        nome="Stuvtelesot", mnc="44", mcc="250", pais="Russian Federation"
    ),
    ("92", "250"): Prestadora(
        nome="Printelefone", mnc="92", mcc="250", pais="Russian Federation"
    ),
    ("93", "250"): Prestadora(
        nome="Telecom XXI", mnc="93", mcc="250", pais="Russian Federation"
    ),
    ("99", "250"): Prestadora(
        nome="Beeline", mnc="99", mcc="250", pais="Russian Federation"
    ),
    ("10", "635"): Prestadora(
        nome="MTN Rwandacell", mnc="10", mcc="635", pais="Rwanda"
    ),
    ("13", "635"): Prestadora(
        nome="AIRTEL RWANDA Ltd", mnc="13", mcc="635", pais="Rwanda"
    ),
    ("17", "635"): Prestadora(
        nome="Olleh Rwanda Networks (ORN)",
        mnc="17",
        mcc="635",
        pais="Rwanda",
    ),
    ("01", "658"): Prestadora(
        nome="Sure South Atlantic Ltd. (Ascension)",
        mnc="01",
        mcc="658",
        pais="Saint Helena, Ascension and Tristan da Cunha",
    ),
    ("110", "356"): Prestadora(
        nome="Cable & Wireless St Kitts & Nevis Ltd trading as Lime",
        mnc="110",
        mcc="356",
        pais="Saint Kitts and Nevis",
    ),
    ("110", "358"): Prestadora(
        nome="Cable & Wireless (St Lucia) Ltd trading as Lime",
        mnc="110",
        mcc="358",
        pais="Saint Lucia",
    ),
    ("01", "308"): Prestadora(
        nome="SAS SPM Telecom",
        mnc="01",
        mcc="308",
        pais="Saint Pierre and Miquelon",
    ),
    ("02", "308"): Prestadora(
        nome="Globaltel",
        mnc="02",
        mcc="308",
        pais="Saint Pierre and Miquelon",
    ),
    ("03", "308"): Prestadora(
        nome="SAS SPM Telecom",
        mnc="03",
        mcc="308",
        pais="Saint Pierre and Miquelon",
    ),
    ("110", "360"): Prestadora(
        nome="Cable & Wireless St Vincent and the Grenadines Ltd trading as lime",
        mnc="110",
        mcc="360",
        pais="Saint Vincent and the Grenadines",
    ),
    ("01", "549"): Prestadora(
        nome="Telecom Samoa Cellular Ltd.", mnc="01", mcc="549", pais="Samoa"
    ),
    ("27", "549"): Prestadora(
        nome="GoMobile SamoaTel Ltd", mnc="27", mcc="549", pais="Samoa"
    ),
    ("01", "292"): Prestadora(
        nome="Prima San Marino / San Marino Telecom",
        mnc="01",
        mcc="292",
        pais="San Marino",
    ),
    ("01", "626"): Prestadora(
        nome="Companhia Santomese de Telecomunicações",
        mnc="01",
        mcc="626",
        pais="Sao Tome and Principe",
    ),
    ("01", "420"): Prestadora(
        nome="Saudi Telecom", mnc="01", mcc="420", pais="Saudi Arabia"
    ),
    ("03", "420"): Prestadora(
        nome="Etihad Etisalat Company (Mobily)",
        mnc="03",
        mcc="420",
        pais="Saudi Arabia",
    ),
    ("01", "608"): Prestadora(
        nome="Sonatel (Orange)", mnc="01", mcc="608", pais="Senegal"
    ),
    ("02", "608"): Prestadora(
        nome="Sentel GSM (Tigo)", mnc="02", mcc="608", pais="Senegal"
    ),
    ("03", "608"): Prestadora(
        nome="Expresso Sénégal", mnc="03", mcc="608", pais="Senegal"
    ),
    ("04", "608"): Prestadora(nome="CSU", mnc="04", mcc="608", pais="Senegal"),
    ("01", "220"): Prestadora(
        nome="Telenor d.o.o.", mnc="01", mcc="220", pais="Serbia"
    ),
    ("03", "220"): Prestadora(
        nome="Telekom Srbija a.d.", mnc="03", mcc="220", pais="Serbia"
    ),
    ("05", "220"): Prestadora(
        nome="Vip mobile d.o.o.", mnc="05", mcc="220", pais="Serbia"
    ),
    ("07", "220"): Prestadora(
        nome="Orion telekom d.o.o.", mnc="07", mcc="220", pais="Serbia"
    ),
    ("09", "220"): Prestadora(
        nome="MUNDIO MOBILE d.o.o.", mnc="09", mcc="220", pais="Serbia"
    ),
    ("11", "220"): Prestadora(
        nome="GLOBALTEL d.o.o.", mnc="11", mcc="220", pais="Serbia"
    ),
    ("01", "633"): Prestadora(
        nome="Cable and wireless (Seychelles) Ltd",
        mnc="01",
        mcc="633",
        pais="Seychelles",
    ),
    ("05", "633"): Prestadora(
        nome="Intelvision Ltd", mnc="05", mcc="633", pais="Seychelles"
    ),
    ("10", "633"): Prestadora(
        nome="Airtel (Seychelles) Ltd",
        mnc="10",
        mcc="633",
        pais="Seychelles",
    ),
    ("01", "619"): Prestadora(nome="Celtel", mnc="01", mcc="619", pais="Sierra Leone"),
    ("02", "619"): Prestadora(
        nome="Millicom", mnc="02", mcc="619", pais="Sierra Leone"
    ),
    ("03", "619"): Prestadora(
        nome="Africell", mnc="03", mcc="619", pais="Sierra Leone"
    ),
    ("04", "619"): Prestadora(
        nome="Comium (Sierra Leone) Ltd",
        mnc="04",
        mcc="619",
        pais="Sierra Leone",
    ),
    ("05", "619"): Prestadora(
        nome="Lintel (Sierra Leone) Ltd.",
        mnc="05",
        mcc="619",
        pais="Sierra Leone",
    ),
    ("07", "619"): Prestadora(
        nome="QCELL SIERRA LEONE", mnc="07", mcc="619", pais="Sierra Leone"
    ),
    ("09", "619"): Prestadora(
        nome="INTERGROUP TELECOM", mnc="09", mcc="619", pais="Sierra Leone"
    ),
    ("25", "619"): Prestadora(nome="Mobitel", mnc="25", mcc="619", pais="Sierra Leone"),
    ("40", "619"): Prestadora(
        nome="Datatel (SL) Ltd GSM", mnc="40", mcc="619", pais="Sierra Leone"
    ),
    ("50", "619"): Prestadora(
        nome="Datatel (SL) Ltd CDMA",
        mnc="50",
        mcc="619",
        pais="Sierra Leone",
    ),
    ("01", "525"): Prestadora(
        nome="Singtel ST GSM900", mnc="01", mcc="525", pais="Singapore"
    ),
    ("02", "525"): Prestadora(
        nome="Singtel ST GSM1800", mnc="02", mcc="525", pais="Singapore"
    ),
    ("03", "525"): Prestadora(nome="M1", mnc="03", mcc="525", pais="Singapore"),
    ("05", "525"): Prestadora(nome="StarHub", mnc="05", mcc="525", pais="Singapore"),
    ("08", "525"): Prestadora(nome="StarHub", mnc="08", mcc="525", pais="Singapore"),
    ("09", "525"): Prestadora(
        nome="Liberty Wireless Pte Ltd",
        mnc="09",
        mcc="525",
        pais="Singapore",
    ),
    ("10", "525"): Prestadora(
        nome="TPG Telecom Pte Ltd", mnc="10", mcc="525", pais="Singapore"
    ),
    ("12", "525"): Prestadora(
        nome="Digital Trunked Radio Network",
        mnc="12",
        mcc="525",
        pais="Singapore",
    ),
    ("01", "231"): Prestadora(nome="Orange, GSM", mnc="01", mcc="231", pais="Slovakia"),
    ("02", "231"): Prestadora(
        nome="Eurotel, GSM & NMT", mnc="02", mcc="231", pais="Slovakia"
    ),
    ("04", "231"): Prestadora(
        nome="Eurotel, UMTS", mnc="04", mcc="231", pais="Slovakia"
    ),
    ("05", "231"): Prestadora(
        nome="Orange, UMTS", mnc="05", mcc="231", pais="Slovakia"
    ),
    ("10", "293"): Prestadora(
        nome="Slovenske železnice – Infrastruktura d.o.o.",
        mnc="10",
        mcc="293",
        pais="Slovenia",
    ),
    ("11", "293"): Prestadora(
        nome="BeeIN d.o.o.", mnc="11", mcc="293", pais="Slovenia"
    ),
    ("20", "293"): Prestadora(
        nome="Compatel Limited", mnc="20", mcc="293", pais="Slovenia"
    ),
    ("21", "293"): Prestadora(
        nome="Novatel d.o.o.", mnc="21", mcc="293", pais="Slovenia"
    ),
    ("40", "293"): Prestadora(
        nome="A1 Slovenija d.d.", mnc="40", mcc="293", pais="Slovenia"
    ),
    ("41", "293"): Prestadora(
        nome="Telekom Slovenije d.d.", mnc="41", mcc="293", pais="Slovenia"
    ),
    ("64", "293"): Prestadora(nome="T-2 d.o.o.", mnc="64", mcc="293", pais="Slovenia"),
    ("70", "293"): Prestadora(
        nome="Telemach d.o.o.", mnc="70", mcc="293", pais="Slovenia"
    ),
    ("02", "540"): Prestadora(
        nome="Bemobile (BMobile (SI) Ltd)",
        mnc="02",
        mcc="540",
        pais="Solomon Islands",
    ),
    ("01", "655"): Prestadora(
        nome="Vodacom (Pty) Ltd.", mnc="01", mcc="655", pais="South Africa"
    ),
    ("02", "655"): Prestadora(
        nome="Telkom SA Ltd", mnc="02", mcc="655", pais="South Africa"
    ),
    ("03", "655"): Prestadora(
        nome="Telkom SA SOC Ltd", mnc="03", mcc="655", pais="South Africa"
    ),
    ("05", "655"): Prestadora(
        nome="Telkom SA Ltd", mnc="05", mcc="655", pais="South Africa"
    ),
    ("06", "655"): Prestadora(
        nome="Sentech (Pty) Ltd.", mnc="06", mcc="655", pais="South Africa"
    ),
    ("07", "655"): Prestadora(
        nome="Cell C (Pty) Ltd.", mnc="07", mcc="655", pais="South Africa"
    ),
    ("10", "655"): Prestadora(
        nome="Mobile Telephone Networks (MTN) Pty Ltd",
        mnc="10",
        mcc="655",
        pais="South Africa",
    ),
    ("12", "655"): Prestadora(
        nome="Mobile Telephone Networks (MTN) Pty Ltd",
        mnc="12",
        mcc="655",
        pais="South Africa",
    ),
    ("13", "655"): Prestadora(
        nome="Neotel Pty Ltd", mnc="13", mcc="655", pais="South Africa"
    ),
    ("14", "655"): Prestadora(
        nome="Neotel Pty Ltd", mnc="14", mcc="655", pais="South Africa"
    ),
    ("19", "655"): Prestadora(
        nome="Wireless Business Solutions (iBurst)",
        mnc="19",
        mcc="655",
        pais="South Africa",
    ),
    ("24", "655"): Prestadora(
        nome="SMS Portal (Pty) Ltd", mnc="24", mcc="655", pais="South Africa"
    ),
    ("25", "655"): Prestadora(
        nome="Wirels Connect", mnc="25", mcc="655", pais="South Africa"
    ),
    ("27", "655"): Prestadora(
        nome="A to Z Vaal Industrial Supplies Pty Ltd",
        mnc="27",
        mcc="655",
        pais="South Africa",
    ),
    ("28", "655"): Prestadora(
        nome="Hymax Talking Solutions (Pty) Ltd",
        mnc="28",
        mcc="655",
        pais="South Africa",
    ),
    ("30", "655"): Prestadora(
        nome="Bokamoso Consortium Pty Ltd",
        mnc="30",
        mcc="655",
        pais="South Africa",
    ),
    ("31", "655"): Prestadora(
        nome="Karabo Telecoms (Pty) Ltd.",
        mnc="31",
        mcc="655",
        pais="South Africa",
    ),
    ("32", "655"): Prestadora(
        nome="Ilizwi Telecommunications Pty Ltd",
        mnc="32",
        mcc="655",
        pais="South Africa",
    ),
    ("33", "655"): Prestadora(
        nome="Thinta Thinta Telecommunications Pty Ltd",
        mnc="33",
        mcc="655",
        pais="South Africa",
    ),
    ("34", "655"): Prestadora(
        nome="Bokone Telecoms Pty Ltd",
        mnc="34",
        mcc="655",
        pais="South Africa",
    ),
    ("35", "655"): Prestadora(
        nome="Kingdom Communications Pty Ltd",
        mnc="35",
        mcc="655",
        pais="South Africa",
    ),
    ("36", "655"): Prestadora(
        nome="Amatole Telecommunication Pty Ltd",
        mnc="36",
        mcc="655",
        pais="South Africa",
    ),
    ("38", "655"): Prestadora(
        nome="Wireless Business Solutions (Pty) Ltd",
        mnc="38",
        mcc="655",
        pais="South Africa",
    ),
    ("46", "655"): Prestadora(
        nome="SMS Cellular Services (Pty) Ltd",
        mnc="46",
        mcc="655",
        pais="South Africa",
    ),
    ("50", "655"): Prestadora(
        nome="Ericsson South Africa (Pty) Ltd",
        mnc="50",
        mcc="655",
        pais="South Africa",
    ),
    ("51", "655"): Prestadora(
        nome="Integrat (Pty) Ltd", mnc="51", mcc="655", pais="South Africa"
    ),
    ("53", "655"): Prestadora(
        nome="Lycamobile (Pty) Ltd", mnc="53", mcc="655", pais="South Africa"
    ),
    ("65", "655"): Prestadora(
        nome="Vodacom Pty Ltd", mnc="65", mcc="655", pais="South Africa"
    ),
    ("73", "655"): Prestadora(
        nome="Wireless Business Solutions (Pty) Ltd",
        mnc="73",
        mcc="655",
        pais="South Africa",
    ),
    ("74", "655"): Prestadora(
        nome="Wireless Business Solutions (Pty) Ltd",
        mnc="74",
        mcc="655",
        pais="South Africa",
    ),
    ("76", "655"): Prestadora(
        nome="Comsol Networks (Pty) Ltd",
        mnc="76",
        mcc="655",
        pais="South Africa",
    ),
    ("77", "655"): Prestadora(
        nome="K2015315513 (Pty) Ltd t\\a One Telecom (Pty) Ltd",
        mnc="77",
        mcc="655",
        pais="South Africa",
    ),
    ("12", "659"): Prestadora(
        nome="Sudani/Sudatel", mnc="12", mcc="659", pais="South Sudan"
    ),
    ("91", "659"): Prestadora(
        nome="Zain-South Sudan", mnc="91", mcc="659", pais="South Sudan"
    ),
    ("92", "659"): Prestadora(
        nome="MTN-South Sudan", mnc="92", mcc="659", pais="South Sudan"
    ),
    ("95", "659"): Prestadora(
        nome="Vivacel/NOW", mnc="95", mcc="659", pais="South Sudan"
    ),
    ("97", "659"): Prestadora(nome="Gemtel", mnc="97", mcc="659", pais="South Sudan"),
    ("01", "214"): Prestadora(
        nome="Vodafone España, SAU", mnc="01", mcc="214", pais="Spain"
    ),
    ("02", "214"): Prestadora(
        nome="Alta Tecnologia en Comunicacions, S.L.",
        mnc="02",
        mcc="214",
        pais="Spain",
    ),
    ("03", "214"): Prestadora(
        nome="France Telecom España, SA", mnc="03", mcc="214", pais="Spain"
    ),
    ("04", "214"): Prestadora(
        nome="Xfera Móviles, S.A.", mnc="04", mcc="214", pais="Spain"
    ),
    ("05", "214"): Prestadora(
        nome="Telefónica Móviles España, SAU",
        mnc="05",
        mcc="214",
        pais="Spain",
    ),
    ("06", "214"): Prestadora(
        nome="Vodafone España, SAU", mnc="06", mcc="214", pais="Spain"
    ),
    ("07", "214"): Prestadora(
        nome="Telefónica Móviles España, SAU",
        mnc="07",
        mcc="214",
        pais="Spain",
    ),
    ("08", "214"): Prestadora(nome="Euskaltel, SA", mnc="08", mcc="214", pais="Spain"),
    ("09", "214"): Prestadora(
        nome="France Telecom España, SA", mnc="09", mcc="214", pais="Spain"
    ),
    ("10", "214"): Prestadora(
        nome="ZINNIA TELECOMUNICACIONES, S.L.U.",
        mnc="10",
        mcc="214",
        pais="Spain",
    ),
    ("11", "214"): Prestadora(
        nome="TELECOM CASTILLA-LA MANCHA, S.A.",
        mnc="11",
        mcc="214",
        pais="Spain",
    ),
    ("12", "214"): Prestadora(
        nome="VENUS MOVIL, S.L. UNIPERSONAL",
        mnc="12",
        mcc="214",
        pais="Spain",
    ),
    ("14", "214"): Prestadora(
        nome="AVATEL MÓVIL, S.L.U.", mnc="14", mcc="214", pais="Spain"
    ),
    ("16", "214"): Prestadora(
        nome="R CABLE Y TELECOMUNICACIONES GALICIA, S.A.",
        mnc="16",
        mcc="214",
        pais="Spain",
    ),
    ("17", "214"): Prestadora(
        nome="R Cable y Telecomunicaciones Galicia, SA",
        mnc="17",
        mcc="214",
        pais="Spain",
    ),
    ("19", "214"): Prestadora(
        nome="E-Plus Móviles, SL", mnc="19", mcc="214", pais="Spain"
    ),
    ("22", "214"): Prestadora(
        nome="Best Spain Telecom, SL", mnc="22", mcc="214", pais="Spain"
    ),
    ("23", "214"): Prestadora(
        nome="Xfera Móviles, S.A.U.", mnc="23", mcc="214", pais="Spain"
    ),
    ("24", "214"): Prestadora(
        nome="VODAFONE ESPAÑA, S.A.U.", mnc="24", mcc="214", pais="Spain"
    ),
    ("25", "214"): Prestadora(
        nome="XFERA MÓVILES, S.A. UNIPERSONAL",
        mnc="25",
        mcc="214",
        pais="Spain",
    ),
    ("26", "214"): Prestadora(
        nome="Lleida Networks Serveis Telemátics, SL",
        mnc="26",
        mcc="214",
        pais="Spain",
    ),
    ("27", "214"): Prestadora(
        nome="SCN Truphone SL", mnc="27", mcc="214", pais="Spain"
    ),
    ("28", "214"): Prestadora(
        nome="Consorcio de Telecomunicaciones Avanzadas, S.A.",
        mnc="28",
        mcc="214",
        pais="Spain",
    ),
    ("29", "214"): Prestadora(
        nome="XFERA MÓVILES, S.A.U.", mnc="29", mcc="214", pais="Spain"
    ),
    ("31", "214"): Prestadora(
        nome="Red Digital De Telecomunicaciones de las Islas Baleares, S.L.",
        mnc="31",
        mcc="214",
        pais="Spain",
    ),
    ("34", "214"): Prestadora(
        nome="AIRE NETWORKS DEL MEDITERRÁNEO, S.L. UNIPERSONAL",
        mnc="34",
        mcc="214",
        pais="Spain",
    ),
    ("35", "214"): Prestadora(
        nome="INGENIUM OUTSOURCING SERVICES, S.L.",
        mnc="35",
        mcc="214",
        pais="Spain",
    ),
    ("36", "214"): Prestadora(
        nome="ALAI OPERADOR DE TELECOMUNICACIONES, S.L.",
        mnc="36",
        mcc="214",
        pais="Spain",
    ),
    ("37", "214"): Prestadora(
        nome="VODAFONE ESPAÑA, S.A.U.", mnc="37", mcc="214", pais="Spain"
    ),
    ("38", "214"): Prestadora(
        nome="Telefónica Móviles España, SAU",
        mnc="38",
        mcc="214",
        pais="Spain",
    ),
    ("51", "214"): Prestadora(
        nome="ENTIDAD PÚBLICA EMPRESARIAL ADMINISTRADOR DE INFRAESTRUCTURAS FERROVIARIAS",
        mnc="51",
        mcc="214",
        pais="Spain",
    ),
    ("700", "214"): Prestadora(
        nome="IBERDROLA ESPAÑA, S.A.UNIPERSONAL",
        mnc="700",
        mcc="214",
        pais="Spain",
    ),
    ("701", "214"): Prestadora(
        nome="ENDESA DISTRIBUCIÓN ELÉCTRICA, S.L.",
        mnc="701",
        mcc="214",
        pais="Spain",
    ),
    ("02", "413"): Prestadora(
        nome="MTN Network Ltd.", mnc="02", mcc="413", pais="Sri Lanka"
    ),
    ("01", "634"): Prestadora(nome="SD Mobitel", mnc="01", mcc="634", pais="Sudan"),
    ("02", "634"): Prestadora(nome="Areeba-Sudan", mnc="02", mcc="634", pais="Sudan"),
    ("03", "634"): Prestadora(nome="MTN Sudan", mnc="03", mcc="634", pais="Sudan"),
    ("05", "634"): Prestadora(
        nome="Network of the World Ltd (NOW)",
        mnc="05",
        mcc="634",
        pais="Sudan",
    ),
    ("06", "634"): Prestadora(nome="Zain Sudan", mnc="06", mcc="634", pais="Sudan"),
    ("07", "634"): Prestadora(
        nome="Sudanese Telecommunication Co. LTD (SUDATEL)",
        mnc="07",
        mcc="634",
        pais="Sudan",
    ),
    ("99", "634"): Prestadora(nome="MTN Sudan", mnc="99", mcc="634", pais="Sudan"),
    ("02", "746"): Prestadora(nome="Telesur", mnc="02", mcc="746", pais="Suriname"),
    ("03", "746"): Prestadora(nome="Digicel", mnc="03", mcc="746", pais="Suriname"),
    ("05", "746"): Prestadora(
        nome="Telesur (CDMA)", mnc="05", mcc="746", pais="Suriname"
    ),
    ("01", "240"): Prestadora(
        nome="Telia Sverige AB", mnc="01", mcc="240", pais="Sweden"
    ),
    ("02", "240"): Prestadora(
        nome="Hi3G Access AB", mnc="02", mcc="240", pais="Sweden"
    ),
    ("03", "240"): Prestadora(nome="Teracom AB", mnc="03", mcc="240", pais="Sweden"),
    ("04", "240"): Prestadora(
        nome="3G Infrastructure Services AB",
        mnc="04",
        mcc="240",
        pais="Sweden",
    ),
    ("05", "240"): Prestadora(
        nome="Svenska UMTS-Nät AB", mnc="05", mcc="240", pais="Sweden"
    ),
    ("06", "240"): Prestadora(
        nome="Telenor Sverige AB", mnc="06", mcc="240", pais="Sweden"
    ),
    ("07", "240"): Prestadora(
        nome="Tele2 Sverige AB", mnc="07", mcc="240", pais="Sweden"
    ),
    ("08", "240"): Prestadora(
        nome="Telenor Sverige AB", mnc="08", mcc="240", pais="Sweden"
    ),
    ("09", "240"): Prestadora(
        nome="Com4 Sweden AB", mnc="09", mcc="240", pais="Sweden"
    ),
    ("10", "240"): Prestadora(
        nome="Tele2 Sverige AB", mnc="10", mcc="240", pais="Sweden"
    ),
    ("12", "240"): Prestadora(
        nome="Lycamobile Sweden Limited", mnc="12", mcc="240", pais="Sweden"
    ),
    ("13", "240"): Prestadora(
        nome="Bredband2 Allmänna IT AB", mnc="13", mcc="240", pais="Sweden"
    ),
    ("14", "240"): Prestadora(
        nome="Tele2 Sverige AB", mnc="14", mcc="240", pais="Sweden"
    ),
    ("15", "240"): Prestadora(
        nome="Sierra Wireless Sweden AB", mnc="15", mcc="240", pais="Sweden"
    ),
    ("16", "240"): Prestadora(nome="42 Telecom AB", mnc="16", mcc="240", pais="Sweden"),
    ("17", "240"): Prestadora(
        nome="Götalandsnätet AB", mnc="17", mcc="240", pais="Sweden"
    ),
    ("18", "240"): Prestadora(
        nome="Generic Mobile Systems Sweden AB",
        mnc="18",
        mcc="240",
        pais="Sweden",
    ),
    ("19", "240"): Prestadora(
        nome="Vecton Mobile (Sweden) Ltd", mnc="19", mcc="240", pais="Sweden"
    ),
    ("20", "240"): Prestadora(
        nome="Sierra Wireless Messaging AB",
        mnc="20",
        mcc="240",
        pais="Sweden",
    ),
    ("21", "240"): Prestadora(
        nome="Trafikverket centralfunktion IT",
        mnc="21",
        mcc="240",
        pais="Sweden",
    ),
    ("23", "240"): Prestadora(
        nome="Infobip LTD (UK)", mnc="23", mcc="240", pais="Sweden"
    ),
    ("24", "240"): Prestadora(
        nome="Net4Mobility HB", mnc="24", mcc="240", pais="Sweden"
    ),
    ("25", "240"): Prestadora(
        nome="Monty UK Global Limited", mnc="25", mcc="240", pais="Sweden"
    ),
    ("26", "240"): Prestadora(
        nome="Twilio Ireland Ltd.", mnc="26", mcc="240", pais="Sweden"
    ),
    ("27", "240"): Prestadora(nome="GlobeTouch AB", mnc="27", mcc="240", pais="Sweden"),
    ("29", "240"): Prestadora(
        nome="MI Carrier Services AB", mnc="29", mcc="240", pais="Sweden"
    ),
    ("30", "240"): Prestadora(nome="Teracom AB", mnc="30", mcc="240", pais="Sweden"),
    ("32", "240"): Prestadora(
        nome="Compatel Limited", mnc="32", mcc="240", pais="Sweden"
    ),
    ("33", "240"): Prestadora(
        nome="Mobile Arts AB", mnc="33", mcc="240", pais="Sweden"
    ),
    ("34", "240"): Prestadora(
        nome="Trafikverket centralfunktion IT",
        mnc="34",
        mcc="240",
        pais="Sweden",
    ),
    ("35", "240"): Prestadora(
        nome="42 Telecom LTD", mnc="35", mcc="240", pais="Sweden"
    ),
    ("36", "240"): Prestadora(
        nome="interactive digital media GmbH",
        mnc="36",
        mcc="240",
        pais="Sweden",
    ),
    ("37", "240"): Prestadora(
        nome="Sinch Sweden AB", mnc="37", mcc="240", pais="Sweden"
    ),
    ("38", "240"): Prestadora(nome="Voxbone SA", mnc="38", mcc="240", pais="Sweden"),
    ("39", "240"): Prestadora(nome="Primlight AB", mnc="39", mcc="240", pais="Sweden"),
    ("40", "240"): Prestadora(
        nome="Netmore Group AB", mnc="40", mcc="240", pais="Sweden"
    ),
    ("41", "240"): Prestadora(
        nome="Telenor Sverige AB", mnc="41", mcc="240", pais="Sweden"
    ),
    ("42", "240"): Prestadora(
        nome="Telenor Connexion AB", mnc="42", mcc="240", pais="Sweden"
    ),
    ("43", "240"): Prestadora(nome="MobiWeb Ltd.", mnc="43", mcc="240", pais="Sweden"),
    ("44", "240"): Prestadora(nome="Telenabler AB", mnc="44", mcc="240", pais="Sweden"),
    ("45", "240"): Prestadora(nome="Spirius AB", mnc="45", mcc="240", pais="Sweden"),
    ("46", "240"): Prestadora(
        nome="SMS Provider Corp.", mnc="46", mcc="240", pais="Sweden"
    ),
    ("47", "240"): Prestadora(
        nome="Viatel Sweden AB", mnc="47", mcc="240", pais="Sweden"
    ),
    ("48", "240"): Prestadora(nome="Tismi BV", mnc="48", mcc="240", pais="Sweden"),
    ("49", "240"): Prestadora(
        nome="Telia Sverige AB", mnc="49", mcc="240", pais="Sweden"
    ),
    ("60", "240"): Prestadora(
        nome="Västra Götalandsregionen (temporary assigned until 2026-12-31)",
        mnc="60",
        mcc="240",
        pais="Sweden",
    ),
    ("63", "240"): Prestadora(
        nome="Fink Telecom Services", mnc="63", mcc="240", pais="Sweden"
    ),
    ("65", "240"): Prestadora(
        nome="shared use for closed networks",
        mnc="65",
        mcc="240",
        pais="Sweden",
    ),
    ("66", "240"): Prestadora(
        nome="shared use for closed networks",
        mnc="66",
        mcc="240",
        pais="Sweden",
    ),
    ("67", "240"): Prestadora(
        nome="shared use for test purpose",
        mnc="67",
        mcc="240",
        pais="Sweden",
    ),
    ("68", "240"): Prestadora(
        nome="shared use for test purpose",
        mnc="68",
        mcc="240",
        pais="Sweden",
    ),
    ("69", "240"): Prestadora(
        nome="crisis management after determination by the Swedish Post- and Telecom Authority",
        mnc="69",
        mcc="240",
        pais="Sweden",
    ),
    ("02", "228"): Prestadora(
        nome="Sunrise Communications AG",
        mnc="02",
        mcc="228",
        pais="Switzerland",
    ),
    ("03", "228"): Prestadora(
        nome="Salt Mobile SA", mnc="03", mcc="228", pais="Switzerland"
    ),
    ("05", "228"): Prestadora(
        nome="Comfone AG", mnc="05", mcc="228", pais="Switzerland"
    ),
    ("06", "228"): Prestadora(nome="SBB AG", mnc="06", mcc="228", pais="Switzerland"),
    ("08", "228"): Prestadora(
        nome="Sunrise Communications AG",
        mnc="08",
        mcc="228",
        pais="Switzerland",
    ),
    ("09", "228"): Prestadora(
        nome="Comfone AG", mnc="09", mcc="228", pais="Switzerland"
    ),
    ("11", "228"): Prestadora(
        nome="Swisscom Broadcast AG", mnc="11", mcc="228", pais="Switzerland"
    ),
    ("12", "228"): Prestadora(
        nome="Sunrise Communications AG",
        mnc="12",
        mcc="228",
        pais="Switzerland",
    ),
    ("51", "228"): Prestadora(
        nome="Bebbicell AG", mnc="51", mcc="228", pais="Switzerland"
    ),
    ("53", "228"): Prestadora(
        nome="upc Cablecom GmbH", mnc="53", mcc="228", pais="Switzerland"
    ),
    ("54", "228"): Prestadora(
        nome="Lycamobile AG", mnc="54", mcc="228", pais="Switzerland"
    ),
    ("55", "228"): Prestadora(
        nome="WeMobile SA", mnc="55", mcc="228", pais="Switzerland"
    ),
    ("57", "228"): Prestadora(nome="Mitto AG", mnc="57", mcc="228", pais="Switzerland"),
    ("58", "228"): Prestadora(
        nome="Beeone Communications SA",
        mnc="58",
        mcc="228",
        pais="Switzerland",
    ),
    ("59", "228"): Prestadora(
        nome="Vectone Mobile Limited, London",
        mnc="59",
        mcc="228",
        pais="Switzerland",
    ),
    ("60", "228"): Prestadora(
        nome="Sunrise Communications AG",
        mnc="60",
        mcc="228",
        pais="Switzerland",
    ),
    ("62", "228"): Prestadora(
        nome="Telecom26 AG", mnc="62", mcc="228", pais="Switzerland"
    ),
    ("63", "228"): Prestadora(
        nome="Fink Telecom Services", mnc="63", mcc="228", pais="Switzerland"
    ),
    ("64", "228"): Prestadora(nome="NTH AG", mnc="64", mcc="228", pais="Switzerland"),
    ("66", "228"): Prestadora(
        nome="Inovia Services SA", mnc="66", mcc="228", pais="Switzerland"
    ),
    ("67", "228"): Prestadora(
        nome="Datatrade Managed AG", mnc="67", mcc="228", pais="Switzerland"
    ),
    ("68", "228"): Prestadora(
        nome="Intellico AG", mnc="68", mcc="228", pais="Switzerland"
    ),
    ("69", "228"): Prestadora(
        nome="MTEL Schweiz GmbH", mnc="69", mcc="228", pais="Switzerland"
    ),
    ("70", "228"): Prestadora(nome="Tismi BV", mnc="70", mcc="228", pais="Switzerland"),
    ("71", "228"): Prestadora(nome="Spusu AG", mnc="71", mcc="228", pais="Switzerland"),
    ("01", "417"): Prestadora(
        nome="Syriatel", mnc="01", mcc="417", pais="Syrian Arab Republic"
    ),
    ("02", "417"): Prestadora(
        nome="MTN Syria", mnc="02", mcc="417", pais="Syrian Arab Republic"
    ),
    ("03", "417"): Prestadora(
        nome="WAFA Telecom", mnc="03", mcc="417", pais="Syrian Arab Republic"
    ),
    ("09", "417"): Prestadora(
        nome="Syrian Telecom",
        mnc="09",
        mcc="417",
        pais="Syrian Arab Republic",
    ),
    ("01", "436"): Prestadora(
        nome="JC Somoncom", mnc="01", mcc="436", pais="Tajikistan"
    ),
    ("02", "436"): Prestadora(
        nome="CJSC Indigo Tajikistan", mnc="02", mcc="436", pais="Tajikistan"
    ),
    ("03", "436"): Prestadora(nome="TT mobile", mnc="03", mcc="436", pais="Tajikistan"),
    ("04", "436"): Prestadora(
        nome="Josa Babilon-T", mnc="04", mcc="436", pais="Tajikistan"
    ),
    ("05", "436"): Prestadora(
        nome="CTJTHSC Tajik-tel", mnc="05", mcc="436", pais="Tajikistan"
    ),
    ("02", "640"): Prestadora(
        nome="MIC Tanzania Limited (Tigo)",
        mnc="02",
        mcc="640",
        pais="Tanzania",
    ),
    ("03", "640"): Prestadora(
        nome="Zanzibar Telecom Limited (Zantel)",
        mnc="03",
        mcc="640",
        pais="Tanzania",
    ),
    ("04", "640"): Prestadora(
        nome="Vodacom Tanzania Limited", mnc="04", mcc="640", pais="Tanzania"
    ),
    ("05", "640"): Prestadora(
        nome="Airtel Tanzania Limited", mnc="05", mcc="640", pais="Tanzania"
    ),
    ("06", "640"): Prestadora(
        nome="WIA Company Limited", mnc="06", mcc="640", pais="Tanzania"
    ),
    ("07", "640"): Prestadora(
        nome="Tanzania Telecommunications Company Limited",
        mnc="07",
        mcc="640",
        pais="Tanzania",
    ),
    ("09", "640"): Prestadora(
        nome="Viettel Tanzania Limited (Halotel)",
        mnc="09",
        mcc="640",
        pais="Tanzania",
    ),
    ("11", "640"): Prestadora(
        nome="Smile Communications Tanzania Ltd",
        mnc="11",
        mcc="640",
        pais="Tanzania",
    ),
    ("00", "520"): Prestadora(nome="CAT CDMA", mnc="00", mcc="520", pais="Thailand"),
    ("01", "520"): Prestadora(nome="AIS GSM", mnc="01", mcc="520", pais="Thailand"),
    ("02", "520"): Prestadora(nome="CAT CDMA", mnc="02", mcc="520", pais="Thailand"),
    ("03", "520"): Prestadora(
        nome="Advanced Wireless Network Company Limited",
        mnc="03",
        mcc="520",
        pais="Thailand",
    ),
    ("04", "520"): Prestadora(
        nome="Real Future Company Limited",
        mnc="04",
        mcc="520",
        pais="Thailand",
    ),
    ("05", "520"): Prestadora(
        nome="DTAC Network Company Limite",
        mnc="05",
        mcc="520",
        pais="Thailand",
    ),
    ("15", "520"): Prestadora(
        nome="TOT Public Company Limited",
        mnc="15",
        mcc="520",
        pais="Thailand",
    ),
    ("18", "520"): Prestadora(
        nome="Total Access Communications Public  Company Limited",
        mnc="18",
        mcc="520",
        pais="Thailand",
    ),
    ("20", "520"): Prestadora(
        nome="ACes Regional Services Company Limited",
        mnc="20",
        mcc="520",
        pais="Thailand",
    ),
    ("23", "520"): Prestadora(
        nome="Digital Phone Company Limited",
        mnc="23",
        mcc="520",
        pais="Thailand",
    ),
    ("47", "520"): Prestadora(
        nome="TOT Public Company Limited",
        mnc="47",
        mcc="520",
        pais="Thailand",
    ),
    ("99", "520"): Prestadora(
        nome="True Move Company Limited",
        mnc="99",
        mcc="520",
        pais="Thailand",
    ),
    ("01", "514"): Prestadora(
        nome="Telin Timor-Leste", mnc="01", mcc="514", pais="Timor-Leste"
    ),
    ("02", "514"): Prestadora(
        nome="Timor Telecom", mnc="02", mcc="514", pais="Timor-Leste"
    ),
    ("03", "514"): Prestadora(
        nome="Viettel Timor-Leste", mnc="03", mcc="514", pais="Timor-Leste"
    ),
    ("01", "615"): Prestadora(nome="Togo Telecom", mnc="01", mcc="615", pais="Togo"),
    ("01", "554"): Prestadora(
        nome="Teletok/LTE 4G", mnc="01", mcc="554", pais="Tokelau"
    ),
    ("01", "539"): Prestadora(
        nome="Tonga Communications Corporation",
        mnc="01",
        mcc="539",
        pais="Tonga",
    ),
    ("43", "539"): Prestadora(nome="Digicel", mnc="43", mcc="539", pais="Tonga"),
    ("88", "539"): Prestadora(
        nome="Digicel (Tonga) Ltd", mnc="88", mcc="539", pais="Tonga"
    ),
    ("12", "374"): Prestadora(
        nome="TSTT Mobile", mnc="12", mcc="374", pais="Trinidad and Tobago"
    ),
    ("130", "374"): Prestadora(
        nome="Digicel Trinidad and Tobago Ltd.",
        mnc="130",
        mcc="374",
        pais="Trinidad and Tobago",
    ),
    ("140", "374"): Prestadora(
        nome="LaqTel Ltd.", mnc="140", mcc="374", pais="Trinidad and Tobago"
    ),
    ("02", "605"): Prestadora(
        nome="Tunisie Telecom", mnc="02", mcc="605", pais="Tunisia"
    ),
    ("03", "605"): Prestadora(
        nome="Orascom Telecom", mnc="03", mcc="605", pais="Tunisia"
    ),
    ("01", "286"): Prestadora(nome="Turkcell", mnc="01", mcc="286", pais="Türkiye"),
    ("02", "286"): Prestadora(nome="Telsim GSM", mnc="02", mcc="286", pais="Türkiye"),
    ("03", "286"): Prestadora(nome="Aria", mnc="03", mcc="286", pais="Türkiye"),
    ("04", "286"): Prestadora(nome="Aycell", mnc="04", mcc="286", pais="Türkiye"),
    ("01", "438"): Prestadora(
        nome="Barash Communication Technologies (BCTI)",
        mnc="01",
        mcc="438",
        pais="Turkmenistan",
    ),
    ("02", "438"): Prestadora(nome="TM-Cell", mnc="02", mcc="438", pais="Turkmenistan"),
    ("350", "376"): Prestadora(
        nome="Cable & Wireless (TCI) Ltd trading asLime",
        mnc="350",
        mcc="376",
        pais="Turks and Caicos Islands",
    ),
    ("360", "376"): Prestadora(
        nome="Digicel", mnc="360", mcc="376", pais="Turks and Caicos Islands"
    ),
    ("01", "553"): Prestadora(
        nome="Tuvalu Telecommunications Corporation",
        mnc="01",
        mcc="553",
        pais="Tuvalu",
    ),
    ("01", "641"): Prestadora(
        nome="Airtel Uganda Limited", mnc="01", mcc="641", pais="Uganda"
    ),
    ("04", "641"): Prestadora(
        nome="Tangerine Uganda Limited", mnc="04", mcc="641", pais="Uganda"
    ),
    ("08", "641"): Prestadora(
        nome="Talkio Mobile Limited", mnc="08", mcc="641", pais="Uganda"
    ),
    ("10", "641"): Prestadora(
        nome="MTN Uganda Limited", mnc="10", mcc="641", pais="Uganda"
    ),
    ("11", "641"): Prestadora(
        nome="Uganda Telecom Limited", mnc="11", mcc="641", pais="Uganda"
    ),
    ("16", "641"): Prestadora(
        nome="SimbaNET Uganda Limited", mnc="16", mcc="641", pais="Uganda"
    ),
    ("22", "641"): Prestadora(
        nome="Airtel Uganda Limited", mnc="22", mcc="641", pais="Uganda"
    ),
    ("33", "641"): Prestadora(
        nome="Smile Communications Uganda Limited",
        mnc="33",
        mcc="641",
        pais="Uganda",
    ),
    ("40", "641"): Prestadora(
        nome="Civil Aviation Authority (CAA)",
        mnc="40",
        mcc="641",
        pais="Uganda",
    ),
    ("44", "641"): Prestadora(
        nome="K2 Telecom Limited", mnc="44", mcc="641", pais="Uganda"
    ),
    ("01", "255"): Prestadora(
        nome='VF UKRAINE" PrJSC"', mnc="01", mcc="255", pais="Ukraine"
    ),
    ("02", "255"): Prestadora(
        nome='Kyivstar" PrJSC"', mnc="02", mcc="255", pais="Ukraine"
    ),
    ("03", "255"): Prestadora(
        nome='Kyivstar" PrJSC"', mnc="03", mcc="255", pais="Ukraine"
    ),
    ("04", "255"): Prestadora(
        nome='Intertelecom" LLC"', mnc="04", mcc="255", pais="Ukraine"
    ),
    ("06", "255"): Prestadora(
        nome='lifecell" LLC"', mnc="06", mcc="255", pais="Ukraine"
    ),
    ("07", "255"): Prestadora(nome='TriMob" LLC"', mnc="07", mcc="255", pais="Ukraine"),
    ("08", "255"): Prestadora(
        nome='Ukrtelecom" JSC"', mnc="08", mcc="255", pais="Ukraine"
    ),
    ("09", "255"): Prestadora(
        nome='Farlep-Invest", PrJSC"', mnc="09", mcc="255", pais="Ukraine"
    ),
    ("10", "255"): Prestadora(
        nome='Atlantis Telecom", LLC"', mnc="10", mcc="255", pais="Ukraine"
    ),
    ("21", "255"): Prestadora(
        nome='Telesystems of Ukraine" PrJSC"',
        mnc="21",
        mcc="255",
        pais="Ukraine",
    ),
    ("02", "424"): Prestadora(
        nome="Etisalat", mnc="02", mcc="424", pais="United Arab Emirates"
    ),
    ("00", "234"): Prestadora(
        nome="British Telecom", mnc="00", mcc="234", pais="United Kingdom"
    ),
    ("00", "235"): Prestadora(
        nome="Vectone Mobile Limited",
        mnc="00",
        mcc="235",
        pais="United Kingdom",
    ),
    ("01", "234"): Prestadora(
        nome="Vectone Mobile Limited",
        mnc="01",
        mcc="234",
        pais="United Kingdom",
    ),
    ("01", "235"): Prestadora(
        nome="EE Limited ( TM)", mnc="01", mcc="235", pais="United Kingdom"
    ),
    ("02", "234"): Prestadora(
        nome="Telefonica UK Limited",
        mnc="02",
        mcc="234",
        pais="United Kingdom",
    ),
    ("02", "235"): Prestadora(
        nome="EE Limited ( TM)", mnc="02", mcc="235", pais="United Kingdom"
    ),
    ("03", "234"): Prestadora(
        nome="Jersey Airtel Limited",
        mnc="03",
        mcc="234",
        pais="United Kingdom",
    ),
    ("03", "235"): Prestadora(
        nome="UK Broadband Limited",
        mnc="03",
        mcc="235",
        pais="United Kingdom",
    ),
    ("04", "234"): Prestadora(
        nome="FMS Solutions Limited",
        mnc="04",
        mcc="234",
        pais="United Kingdom",
    ),
    ("04", "235"): Prestadora(
        nome="University Of Strathclyde",
        mnc="04",
        mcc="235",
        pais="United Kingdom",
    ),
    ("06", "235"): Prestadora(
        nome="University Of Strathclyde",
        mnc="06",
        mcc="235",
        pais="United Kingdom",
    ),
    ("07", "235"): Prestadora(
        nome="University Of Strathclyde",
        mnc="07",
        mcc="235",
        pais="United Kingdom",
    ),
    ("08", "234"): Prestadora(
        nome="BT OnePhone Limited",
        mnc="08",
        mcc="234",
        pais="United Kingdom",
    ),
    ("08", "235"): Prestadora(
        nome="Spitfire Network Services Limited",
        mnc="08",
        mcc="235",
        pais="United Kingdom",
    ),
    ("09", "234"): Prestadora(
        nome="Tismi BV", mnc="09", mcc="234", pais="United Kingdom"
    ),
    ("10", "234"): Prestadora(
        nome="Telefonica UK Limited",
        mnc="10",
        mcc="234",
        pais="United Kingdom",
    ),
    ("11", "234"): Prestadora(
        nome="Telefonica UK Limited",
        mnc="11",
        mcc="234",
        pais="United Kingdom",
    ),
    ("12", "234"): Prestadora(
        nome="Network Rail Infrastructure Limited",
        mnc="12",
        mcc="234",
        pais="United Kingdom",
    ),
    ("13", "234"): Prestadora(
        nome="Network Rail Infrastructure Limited",
        mnc="13",
        mcc="234",
        pais="United Kingdom",
    ),
    ("14", "234"): Prestadora(
        nome="LINK MOBILITY UK LTD",
        mnc="14",
        mcc="234",
        pais="United Kingdom",
    ),
    ("15", "234"): Prestadora(
        nome="Vodafone Limited", mnc="15", mcc="234", pais="United Kingdom"
    ),
    ("16", "234"): Prestadora(
        nome="TalkTalk Communications Limited",
        mnc="16",
        mcc="234",
        pais="United Kingdom",
    ),
    ("18", "234"): Prestadora(
        nome="Cloud9 Communications Limited",
        mnc="18",
        mcc="234",
        pais="United Kingdom",
    ),
    ("19", "234"): Prestadora(
        nome="TeleWare Group PLC", mnc="19", mcc="234", pais="United Kingdom"
    ),
    ("20", "234"): Prestadora(
        nome="Hutchison 3G UK Limited",
        mnc="20",
        mcc="234",
        pais="United Kingdom",
    ),
    ("22", "234"): Prestadora(
        nome="Telesign Mobile Limited",
        mnc="22",
        mcc="234",
        pais="United Kingdom",
    ),
    ("23", "234"): Prestadora(
        nome="Icron Network Limited",
        mnc="23",
        mcc="234",
        pais="United Kingdom",
    ),
    ("24", "234"): Prestadora(
        nome="Stour Marine Limited",
        mnc="24",
        mcc="234",
        pais="United Kingdom",
    ),
    ("25", "234"): Prestadora(
        nome="Truphone Limited", mnc="25", mcc="234", pais="United Kingdom"
    ),
    ("26", "234"): Prestadora(
        nome="Lycamobile UK Limited",
        mnc="26",
        mcc="234",
        pais="United Kingdom",
    ),
    ("27", "234"): Prestadora(
        nome="Tata Communications Move UK Ltd",
        mnc="27",
        mcc="234",
        pais="United Kingdom",
    ),
    ("28", "234"): Prestadora(
        nome="Marathon Telecom Limited",
        mnc="28",
        mcc="234",
        pais="United Kingdom",
    ),
    ("29", "234"): Prestadora(
        nome="(AQ) LIMITED", mnc="29", mcc="234", pais="United Kingdom"
    ),
    ("30", "234"): Prestadora(
        nome="EE Limited ( TM)", mnc="30", mcc="234", pais="United Kingdom"
    ),
    ("31", "234"): Prestadora(
        nome="EE Limited ( TM)", mnc="31", mcc="234", pais="United Kingdom"
    ),
    ("32", "234"): Prestadora(
        nome="EE Limited ( TM)", mnc="32", mcc="234", pais="United Kingdom"
    ),
    ("33", "234"): Prestadora(
        nome="EE Limited (Orange)",
        mnc="33",
        mcc="234",
        pais="United Kingdom",
    ),
    ("34", "234"): Prestadora(
        nome="EE Limited (Orange)",
        mnc="34",
        mcc="234",
        pais="United Kingdom",
    ),
    ("36", "234"): Prestadora(
        nome="Sure (Isle of Man) Limited",
        mnc="36",
        mcc="234",
        pais="United Kingdom",
    ),
    ("37", "234"): Prestadora(
        nome="Synectiv Ltd", mnc="37", mcc="234", pais="United Kingdom"
    ),
    ("38", "234"): Prestadora(
        nome="Virgin Mobile Telecoms Limited",
        mnc="38",
        mcc="234",
        pais="United Kingdom",
    ),
    ("39", "234"): Prestadora(
        nome="Gamma Telecom Holdings Ltd",
        mnc="39",
        mcc="234",
        pais="United Kingdom",
    ),
    ("40", "234"): Prestadora(
        nome="Mass Response Service GmbH",
        mnc="40",
        mcc="234",
        pais="United Kingdom",
    ),
    ("50", "234"): Prestadora(
        nome="JT (Jersey) Limited",
        mnc="50",
        mcc="234",
        pais="United Kingdom",
    ),
    ("51", "234"): Prestadora(
        nome="UK Broadband Limited",
        mnc="51",
        mcc="234",
        pais="United Kingdom",
    ),
    ("52", "234"): Prestadora(
        nome="Shyam Telecom UK Ltd",
        mnc="52",
        mcc="234",
        pais="United Kingdom",
    ),
    ("53", "234"): Prestadora(
        nome="Tango Networks UK Ltd",
        mnc="53",
        mcc="234",
        pais="United Kingdom",
    ),
    ("54", "234"): Prestadora(
        nome="The Carphone Warehouse Limited",
        mnc="54",
        mcc="234",
        pais="United Kingdom",
    ),
    ("55", "234"): Prestadora(
        nome="Sure (Guernsey) Limited",
        mnc="55",
        mcc="234",
        pais="United Kingdom",
    ),
    ("56", "234"): Prestadora(
        nome="The National Cyber Security Centre",
        mnc="56",
        mcc="234",
        pais="United Kingdom",
    ),
    ("57", "234"): Prestadora(
        nome="Sky UK Limited", mnc="57", mcc="234", pais="United Kingdom"
    ),
    ("58", "234"): Prestadora(
        nome="MANX TELECOM TRADING LIMITED",
        mnc="58",
        mcc="234",
        pais="United Kingdom",
    ),
    ("71", "234"): Prestadora(
        nome="Home Office", mnc="71", mcc="234", pais="United Kingdom"
    ),
    ("72", "234"): Prestadora(
        nome="Hanhaa Limited", mnc="72", mcc="234", pais="United Kingdom"
    ),
    ("73", "234"): Prestadora(
        nome="BlueWave Communications",
        mnc="73",
        mcc="234",
        pais="United Kingdom",
    ),
    ("74", "234"): Prestadora(
        nome="Pareteum Europe B.V.",
        mnc="74",
        mcc="234",
        pais="United Kingdom",
    ),
    ("76", "234"): Prestadora(
        nome="British Telecom", mnc="76", mcc="234", pais="United Kingdom"
    ),
    ("77", "234"): Prestadora(
        nome="Vodafone Limited", mnc="77", mcc="234", pais="United Kingdom"
    ),
    ("77", "235"): Prestadora(
        nome="British Telecom", mnc="77", mcc="235", pais="United Kingdom"
    ),
    ("78", "234"): Prestadora(
        nome="Airwave Solutions Ltd",
        mnc="78",
        mcc="234",
        pais="United Kingdom",
    ),
    ("86", "234"): Prestadora(
        nome="EE Limited ( TM)", mnc="86", mcc="234", pais="United Kingdom"
    ),
    ("88", "234"): Prestadora(
        nome="Telet Research (N.I.) Limited",
        mnc="88",
        mcc="234",
        pais="United Kingdom",
    ),
    ("88", "235"): Prestadora(
        nome="Telet Research (N.I.) Limited",
        mnc="88",
        mcc="235",
        pais="United Kingdom",
    ),
    ("91", "235"): Prestadora(
        nome="Vodafone Limited", mnc="91", mcc="235", pais="United Kingdom"
    ),
    ("94", "235"): Prestadora(
        nome="Hutchison 3G UK Limited",
        mnc="94",
        mcc="235",
        pais="United Kingdom",
    ),
    ("95", "235"): Prestadora(
        nome="Network Rail Infrastructure Limited",
        mnc="95",
        mcc="235",
        pais="United Kingdom",
    ),
    ("010", "310"): Prestadora(
        nome="Verizon Wireless", mnc="010", mcc="310", pais="United States"
    ),
    ("010", "313"): Prestadora(
        nome="Cross Wireless LLC dba Bravado Wireless",
        mnc="010",
        mcc="313",
        pais="United States",
    ),
    ("010", "314"): Prestadora(
        nome="Boingo Wireless Inc",
        mnc="010",
        mcc="314",
        pais="United States",
    ),
    ("012", "310"): Prestadora(
        nome="Verizon Wireless", mnc="012", mcc="310", pais="United States"
    ),
    ("013", "310"): Prestadora(
        nome="Verizon Wireless", mnc="013", mcc="310", pais="United States"
    ),
    ("014", "310"): Prestadora(
        nome="TEST IMSI HNI", mnc="014", mcc="310", pais="United States"
    ),
    ("016", "310"): Prestadora(
        nome="AT&T Mobility", mnc="016", mcc="310", pais="United States"
    ),
    ("020", "310"): Prestadora(
        nome="Union Telephone Company",
        mnc="020",
        mcc="310",
        pais="United States",
    ),
    ("020", "312"): Prestadora(
        nome="Infrastructure Networks LLC",
        mnc="020",
        mcc="312",
        pais="United States",
    ),
    ("020", "313"): Prestadora(
        nome="CTC Telecom, INC. dba CTC Wireless",
        mnc="020",
        mcc="313",
        pais="United States",
    ),
    ("020", "314"): Prestadora(
        nome="Spectrum Wireless Holdings, LLC",
        mnc="020",
        mcc="314",
        pais="United States",
    ),
    ("030", "311"): Prestadora(
        nome="Indigo Wireless, Inc.",
        mnc="030",
        mcc="311",
        pais="United States",
    ),
    ("030", "312"): Prestadora(
        nome="Cross Wireless", mnc="030", mcc="312", pais="United States"
    ),
    ("030", "313"): Prestadora(
        nome="AT&T Mobility", mnc="030", mcc="313", pais="United States"
    ),
    ("030", "314"): Prestadora(
        nome="Baicells Technologies North America Inc.",
        mnc="030",
        mcc="314",
        pais="United States",
    ),
    ("035", "310"): Prestadora(
        nome="ETEX Communications, LP (d/b/a) ETEX Wireless",
        mnc="035",
        mcc="310",
        pais="United States",
    ),
    ("040", "310"): Prestadora(nome="Mobi", mnc="040", mcc="310", pais="United States"),
    ("040", "311"): Prestadora(
        nome="Commnet Wireless LLC",
        mnc="040",
        mcc="311",
        pais="United States",
    ),
    ("040", "312"): Prestadora(
        nome="Custer Telephone Cooperative Inc",
        mnc="040",
        mcc="312",
        pais="United States",
    ),
    ("040", "313"): Prestadora(
        nome="Nucla-Naturita Telephone Company",
        mnc="040",
        mcc="313",
        pais="United States",
    ),
    ("050", "310"): Prestadora(
        nome="Alaska Wireless Networks",
        mnc="050",
        mcc="310",
        pais="United States",
    ),
    ("050", "311"): Prestadora(
        nome="Thumb Cellular Limited Partnership",
        mnc="050",
        mcc="311",
        pais="United States",
    ),
    ("060", "311"): Prestadora(
        nome="Space Data Corporation",
        mnc="060",
        mcc="311",
        pais="United States",
    ),
    ("060", "313"): Prestadora(
        nome="Country Wireless", mnc="060", mcc="313", pais="United States"
    ),
    ("060", "314"): Prestadora(
        nome="Texas A&M University System – RELLIS Campus",
        mnc="060",
        mcc="314",
        pais="United States",
    ),
    ("061", "313"): Prestadora(
        nome="Country Wireless", mnc="061", mcc="313", pais="United States"
    ),
    ("070", "310"): Prestadora(
        nome="AT&T Mobility", mnc="070", mcc="310", pais="United States"
    ),
    ("070", "311"): Prestadora(
        nome="AT&T Mobility", mnc="070", mcc="311", pais="United States"
    ),
    ("070", "313"): Prestadora(
        nome="Midwest Network Solutions Hub LLC",
        mnc="070",
        mcc="313",
        pais="United States",
    ),
    ("070", "314"): Prestadora(
        nome="Texas A&M University System – RELLIS Campus",
        mnc="070",
        mcc="314",
        pais="United States",
    ),
    ("080", "310"): Prestadora(
        nome="AT&T Mobility", mnc="080", mcc="310", pais="United States"
    ),
    ("080", "311"): Prestadora(
        nome="Pine Telephone Company dba Pine Cellular",
        mnc="080",
        mcc="311",
        pais="United States",
    ),
    ("080", "312"): Prestadora(
        nome="South Georgia Regional Information Technology Authority",
        mnc="080",
        mcc="312",
        pais="United States",
    ),
    ("080", "313"): Prestadora(
        nome="Speedwavz LLP", mnc="080", mcc="313", pais="United States"
    ),
    ("080", "314"): Prestadora(
        nome="Texas A&M University System – RELLIS Campus",
        mnc="080",
        mcc="314",
        pais="United States",
    ),
    ("090", "310"): Prestadora(
        nome="AT&T Mobility", mnc="090", mcc="310", pais="United States"
    ),
    ("090", "311"): Prestadora(
        nome="AT&T Mobility", mnc="090", mcc="311", pais="United States"
    ),
    ("090", "312"): Prestadora(
        nome="AT&T Mobility", mnc="090", mcc="312", pais="United States"
    ),
    ("090", "313"): Prestadora(
        nome="Vivint Wireless, Inc",
        mnc="090",
        mcc="313",
        pais="United States",
    ),
    ("090", "314"): Prestadora(
        nome="Southern Communications Services, Inc. D/B/A Southern Linc",
        mnc="090",
        mcc="314",
        pais="United States",
    ),
    ("100", "310"): Prestadora(
        nome="New Mexico RSA 4 East Limited Partnership",
        mnc="100",
        mcc="310",
        pais="United States",
    ),
    ("100", "311"): Prestadora(
        nome="Nex-Tech Wireless LLC",
        mnc="100",
        mcc="311",
        pais="United States",
    ),
    ("100", "312"): Prestadora(
        nome="ClearSky Technologies Inc",
        mnc="100",
        mcc="312",
        pais="United States",
    ),
    ("100", "313"): Prestadora(
        nome="AT&T FirstNet", mnc="100", mcc="313", pais="United States"
    ),
    ("100", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="100",
        mcc="314",
        pais="United States",
    ),
    ("110", "310"): Prestadora(
        nome="PTI Pacifica, Inc.", mnc="110", mcc="310", pais="United States"
    ),
    ("110", "311"): Prestadora(
        nome="Verizon Wireless", mnc="110", mcc="311", pais="United States"
    ),
    ("110", "313"): Prestadora(
        nome="AT&T FirstNet", mnc="110", mcc="313", pais="United States"
    ),
    ("110", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="110",
        mcc="314",
        pais="United States",
    ),
    ("120", "310"): Prestadora(
        nome="T-Mobile USA", mnc="120", mcc="310", pais="United States"
    ),
    ("120", "311"): Prestadora(
        nome="PTI Pacifica, Inc.", mnc="120", mcc="311", pais="United States"
    ),
    ("120", "312"): Prestadora(
        nome="East Kentucky Network LLC dba Appalachian Wireless",
        mnc="120",
        mcc="312",
        pais="United States",
    ),
    ("120", "313"): Prestadora(
        nome="AT&T FirstNet", mnc="120", mcc="313", pais="United States"
    ),
    ("120", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="120",
        mcc="314",
        pais="United States",
    ),
    ("130", "310"): Prestadora(
        nome="Carolina West Wireless",
        mnc="130",
        mcc="310",
        pais="United States",
    ),
    ("130", "312"): Prestadora(
        nome="East Kentucky Network LLC dba Appalachian Wireless",
        mnc="130",
        mcc="312",
        pais="United States",
    ),
    ("130", "313"): Prestadora(
        nome="AT&T FirstNet", mnc="130", mcc="313", pais="United States"
    ),
    ("130", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="130",
        mcc="314",
        pais="United States",
    ),
    ("140", "310"): Prestadora(
        nome="GTA Wireless LLC", mnc="140", mcc="310", pais="United States"
    ),
    ("140", "311"): Prestadora(
        nome="Cross Telephone Company",
        mnc="140",
        mcc="311",
        pais="United States",
    ),
    ("140", "313"): Prestadora(
        nome="AT&T FirstNet", mnc="140", mcc="313", pais="United States"
    ),
    ("140", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="140",
        mcc="314",
        pais="United States",
    ),
    ("150", "310"): Prestadora(
        nome="AT&T Mobility", mnc="150", mcc="310", pais="United States"
    ),
    ("150", "312"): Prestadora(
        nome="Northwest Cell", mnc="150", mcc="312", pais="United States"
    ),
    ("150", "313"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="150",
        mcc="313",
        pais="United States",
    ),
    ("150", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="150",
        mcc="314",
        pais="United States",
    ),
    ("160", "310"): Prestadora(
        nome="T-Mobile USA", mnc="160", mcc="310", pais="United States"
    ),
    ("160", "312"): Prestadora(
        nome="RSA1 Limited Partnership dba Chat Mobility",
        mnc="160",
        mcc="312",
        pais="United States",
    ),
    ("160", "313"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="160",
        mcc="313",
        pais="United States",
    ),
    ("160", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="160",
        mcc="314",
        pais="United States",
    ),
    ("170", "310"): Prestadora(
        nome="AT&T Mobility", mnc="170", mcc="310", pais="United States"
    ),
    ("170", "311"): Prestadora(
        nome="Tampnet (formerly Broadpoint, LLC (former PetroCom, LLC) c/o MTPCS, LL",
        mnc="170",
        mcc="311",
        pais="United States",
    ),
    ("170", "313"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="170",
        mcc="313",
        pais="United States",
    ),
    ("170", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="170",
        mcc="314",
        pais="United States",
    ),
    ("180", "310"): Prestadora(
        nome="West Central Wireless",
        mnc="180",
        mcc="310",
        pais="United States",
    ),
    ("180", "311"): Prestadora(
        nome="AT&T Mobility", mnc="180", mcc="311", pais="United States"
    ),
    ("180", "312"): Prestadora(
        nome="Limitless Mobile, LLC",
        mnc="180",
        mcc="312",
        pais="United States",
    ),
    ("180", "313"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="180",
        mcc="313",
        pais="United States",
    ),
    ("180", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="180",
        mcc="314",
        pais="United States",
    ),
    ("190", "310"): Prestadora(
        nome="Alaska Wireless Networks",
        mnc="190",
        mcc="310",
        pais="United States",
    ),
    ("190", "311"): Prestadora(
        nome="AT&T Mobility", mnc="190", mcc="311", pais="United States"
    ),
    ("190", "312"): Prestadora(
        nome="T-Mobile USA", mnc="190", mcc="312", pais="United States"
    ),
    ("190", "313"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="190",
        mcc="313",
        pais="United States",
    ),
    ("190", "314"): Prestadora(
        nome="RESERVED FOR PUBLIC SAFETY",
        mnc="190",
        mcc="314",
        pais="United States",
    ),
    ("200", "310"): Prestadora(
        nome="T-Mobile USA", mnc="200", mcc="310", pais="United States"
    ),
    ("200", "311"): Prestadora(
        nome="Dish Wireless", mnc="200", mcc="311", pais="United States"
    ),
    ("200", "314"): Prestadora(
        nome="XF Wireless Investments",
        mnc="200",
        mcc="314",
        pais="United States",
    ),
    ("210", "310"): Prestadora(
        nome="T-Mobile USA", mnc="210", mcc="310", pais="United States"
    ),
    ("210", "311"): Prestadora(
        nome="Telnyx LLC", mnc="210", mcc="311", pais="United States"
    ),
    ("210", "312"): Prestadora(
        nome="ASPENTA, LLC", mnc="210", mcc="312", pais="United States"
    ),
    ("210", "313"): Prestadora(
        nome="AT&T Mobility", mnc="210", mcc="313", pais="United States"
    ),
    ("210", "314"): Prestadora(
        nome="Telecom Resource Center",
        mnc="210",
        mcc="314",
        pais="United States",
    ),
    ("220", "310"): Prestadora(
        nome="T-Mobile USA", mnc="220", mcc="310", pais="United States"
    ),
    ("220", "313"): Prestadora(
        nome="Custer Telephone Cooperative,Inc.",
        mnc="220",
        mcc="313",
        pais="United States",
    ),
    ("220", "314"): Prestadora(
        nome="Secrus Technologies",
        mnc="220",
        mcc="314",
        pais="United States",
    ),
    ("225", "311"): Prestadora(
        nome="U.S. Cellular", mnc="225", mcc="311", pais="United States"
    ),
    ("228", "311"): Prestadora(
        nome="U.S. Cellular", mnc="228", mcc="311", pais="United States"
    ),
    ("229", "311"): Prestadora(
        nome="U.S. Cellular", mnc="229", mcc="311", pais="United States"
    ),
    ("230", "310"): Prestadora(
        nome="T-Mobile USA", mnc="230", mcc="310", pais="United States"
    ),
    ("230", "311"): Prestadora(
        nome="Cellular South Inc.",
        mnc="230",
        mcc="311",
        pais="United States",
    ),
    ("230", "313"): Prestadora(
        nome="Velocity Communications Inc",
        mnc="230",
        mcc="313",
        pais="United States",
    ),
    ("230", "314"): Prestadora(
        nome="Trace-Tek", mnc="230", mcc="314", pais="United States"
    ),
    ("240", "310"): Prestadora(
        nome="T-Mobile USA", mnc="240", mcc="310", pais="United States"
    ),
    ("240", "311"): Prestadora(
        nome="Cordova Wireless Communications Inc",
        mnc="240",
        mcc="311",
        pais="United States",
    ),
    ("240", "313"): Prestadora(
        nome="Fundamental Holdings, Corp",
        mnc="240",
        mcc="313",
        pais="United States",
    ),
    ("240", "314"): Prestadora(
        nome="XF Wireless Investments",
        mnc="240",
        mcc="314",
        pais="United States",
    ),
    ("250", "310"): Prestadora(
        nome="T-Mobile USA", mnc="250", mcc="310", pais="United States"
    ),
    ("250", "312"): Prestadora(
        nome="T-Mobile USA", mnc="250", mcc="312", pais="United States"
    ),
    ("250", "313"): Prestadora(
        nome="Imperial County Office of Education",
        mnc="250",
        mcc="313",
        pais="United States",
    ),
    ("260", "310"): Prestadora(
        nome="T-Mobile USA", mnc="260", mcc="310", pais="United States"
    ),
    ("260", "311"): Prestadora(
        nome="T-Mobile", mnc="260", mcc="311", pais="United States"
    ),
    ("260", "312"): Prestadora(
        nome="WorldCell Solutions LLC",
        mnc="260",
        mcc="312",
        pais="United States",
    ),
    ("260", "313"): Prestadora(
        nome="Expeto Wireless Inc.",
        mnc="260",
        mcc="313",
        pais="United States",
    ),
    ("260", "314"): Prestadora(
        nome="AT&T Mobility", mnc="260", mcc="314", pais="United States"
    ),
    ("270", "310"): Prestadora(
        nome="T-Mobile USA", mnc="270", mcc="310", pais="United States"
    ),
    ("270", "311"): Prestadora(
        nome="Verizon Wireless", mnc="270", mcc="311", pais="United States"
    ),
    ("270", "312"): Prestadora(
        nome="Cellular Network Partnership dba Pioneer Cellular",
        mnc="270",
        mcc="312",
        pais="United States",
    ),
    ("270", "314"): Prestadora(
        nome="AT&T Mobility", mnc="270", mcc="314", pais="United States"
    ),
    ("271", "311"): Prestadora(
        nome="Verizon Wireless", mnc="271", mcc="311", pais="United States"
    ),
    ("272", "311"): Prestadora(
        nome="Verizon Wireless", mnc="272", mcc="311", pais="United States"
    ),
    ("273", "311"): Prestadora(
        nome="Verizon Wireless", mnc="273", mcc="311", pais="United States"
    ),
    ("274", "311"): Prestadora(
        nome="Verizon Wireless", mnc="274", mcc="311", pais="United States"
    ),
    ("275", "311"): Prestadora(
        nome="Verizon Wireless", mnc="275", mcc="311", pais="United States"
    ),
    ("276", "311"): Prestadora(
        nome="Verizon Wireless", mnc="276", mcc="311", pais="United States"
    ),
    ("277", "311"): Prestadora(
        nome="Verizon Wireless", mnc="277", mcc="311", pais="United States"
    ),
    ("278", "311"): Prestadora(
        nome="Verizon Wireless", mnc="278", mcc="311", pais="United States"
    ),
    ("279", "311"): Prestadora(
        nome="Verizon Wireless", mnc="279", mcc="311", pais="United States"
    ),
    ("280", "310"): Prestadora(
        nome="AT&T Mobility", mnc="280", mcc="310", pais="United States"
    ),
    ("280", "311"): Prestadora(
        nome="Verizon Wireless", mnc="280", mcc="311", pais="United States"
    ),
    ("280", "312"): Prestadora(
        nome="Cellular Network Partnership dba Pioneer Cellular",
        mnc="280",
        mcc="312",
        pais="United States",
    ),
    ("280", "313"): Prestadora(
        nome="King Street Wireless, LP",
        mnc="280",
        mcc="313",
        pais="United States",
    ),
    ("280", "314"): Prestadora(
        nome="Pollen Mobile LLC", mnc="280", mcc="314", pais="United States"
    ),
    ("281", "311"): Prestadora(
        nome="Verizon Wireless", mnc="281", mcc="311", pais="United States"
    ),
    ("282", "311"): Prestadora(
        nome="Verizon Wireless", mnc="282", mcc="311", pais="United States"
    ),
    ("283", "311"): Prestadora(
        nome="Verizon Wireless", mnc="283", mcc="311", pais="United States"
    ),
    ("284", "311"): Prestadora(
        nome="Verizon Wireless", mnc="284", mcc="311", pais="United States"
    ),
    ("285", "311"): Prestadora(
        nome="Verizon Wireless", mnc="285", mcc="311", pais="United States"
    ),
    ("286", "311"): Prestadora(
        nome="Verizon Wireless", mnc="286", mcc="311", pais="United States"
    ),
    ("287", "311"): Prestadora(
        nome="Verizon Wireless", mnc="287", mcc="311", pais="United States"
    ),
    ("288", "311"): Prestadora(
        nome="Verizon Wireless", mnc="288", mcc="311", pais="United States"
    ),
    ("289", "311"): Prestadora(
        nome="Verizon Wireless", mnc="289", mcc="311", pais="United States"
    ),
    ("290", "310"): Prestadora(
        nome="NEP Cellcorp Inc.", mnc="290", mcc="310", pais="United States"
    ),
    ("290", "312"): Prestadora(
        nome="Uintah Basin Electronic Telecommunications",
        mnc="290",
        mcc="312",
        pais="United States",
    ),
    ("290", "313"): Prestadora(
        nome="Gulf Coast Broadband LLC",
        mnc="290",
        mcc="313",
        pais="United States",
    ),
    ("290", "314"): Prestadora(nome="Wave", mnc="290", mcc="314", pais="United States"),
    ("300", "312"): Prestadora(
        nome="Telecom North America Mobile Inc.",
        mnc="300",
        mcc="312",
        pais="United States",
    ),
    ("300", "313"): Prestadora(
        nome="Southern California Edison",
        mnc="300",
        mcc="313",
        pais="United States",
    ),
    ("310", "310"): Prestadora(
        nome="T-Mobile USA", mnc="310", mcc="310", pais="United States"
    ),
    ("310", "312"): Prestadora(
        nome="Clear Stream Communications, LLC",
        mnc="310",
        mcc="312",
        pais="United States",
    ),
    ("310", "314"): Prestadora(
        nome="Terranet", mnc="310", mcc="314", pais="United States"
    ),
    ("320", "310"): Prestadora(
        nome="Smith Bagley, Inc. dba CellularOne",
        mnc="320",
        mcc="310",
        pais="United States",
    ),
    ("320", "311"): Prestadora(
        nome="Commnet Wireless LLC",
        mnc="320",
        mcc="311",
        pais="United States",
    ),
    ("320", "312"): Prestadora(
        nome="S and R Communications LLC",
        mnc="320",
        mcc="312",
        pais="United States",
    ),
    ("320", "313"): Prestadora(
        nome="Paladin Wireless", mnc="320", mcc="313", pais="United States"
    ),
    ("320", "314"): Prestadora(
        nome="Agri-Valley Communications, Inc",
        mnc="320",
        mcc="314",
        pais="United States",
    ),
    ("330", "310"): Prestadora(
        nome="Wireless Partners LLC",
        mnc="330",
        mcc="310",
        pais="United States",
    ),
    ("330", "311"): Prestadora(
        nome="Bug Tussel Wireless LLC",
        mnc="330",
        mcc="311",
        pais="United States",
    ),
    ("330", "312"): Prestadora(
        nome="Nemont Communications, Inc.",
        mnc="330",
        mcc="312",
        pais="United States",
    ),
    ("330", "313"): Prestadora(
        nome="CenturyTel Broadband Services LLC",
        mnc="330",
        mcc="313",
        pais="United States",
    ),
    ("330", "314"): Prestadora(
        nome="Nova Labs Inc.", mnc="330", mcc="314", pais="United States"
    ),
    ("340", "310"): Prestadora(
        nome="Limitless Mobile, LLC",
        mnc="340",
        mcc="310",
        pais="United States",
    ),
    ("340", "311"): Prestadora(
        nome="Illinois Valley Cellular",
        mnc="340",
        mcc="311",
        pais="United States",
    ),
    ("340", "313"): Prestadora(
        nome="Dish Network", mnc="340", mcc="313", pais="United States"
    ),
    ("340", "314"): Prestadora(
        nome="E-MARCONI LLC", mnc="340", mcc="314", pais="United States"
    ),
    ("350", "310"): Prestadora(
        nome="Verizon Wireless", mnc="350", mcc="310", pais="United States"
    ),
    ("350", "311"): Prestadora(
        nome="Sagebrush Cellular Inc dba Nemont",
        mnc="350",
        mcc="311",
        pais="United States",
    ),
    ("350", "312"): Prestadora(
        nome="Triangle Communication System Inc.",
        mnc="350",
        mcc="312",
        pais="United States",
    ),
    ("350", "313"): Prestadora(
        nome="Dish Network", mnc="350", mcc="313", pais="United States"
    ),
    ("350", "314"): Prestadora(
        nome="Evergy", mnc="350", mcc="314", pais="United States"
    ),
    ("360", "310"): Prestadora(
        nome="Cellular Network Partnership dba Pioneer Cellular",
        mnc="360",
        mcc="310",
        pais="United States",
    ),
    ("360", "311"): Prestadora(
        nome="Stelera Wireless LLC",
        mnc="360",
        mcc="311",
        pais="United States",
    ),
    ("360", "312"): Prestadora(
        nome="Wes-Tex Telecommunications, LTD",
        mnc="360",
        mcc="312",
        pais="United States",
    ),
    ("360", "313"): Prestadora(
        nome="Dish Network", mnc="360", mcc="313", pais="United States"
    ),
    ("360", "314"): Prestadora(
        nome="Oceus Networks, LLC",
        mnc="360",
        mcc="314",
        pais="United States",
    ),
    ("370", "310"): Prestadora(
        nome="Docomo Pacific Inc", mnc="370", mcc="310", pais="United States"
    ),
    ("370", "311"): Prestadora(
        nome="GCI Communications Corp",
        mnc="370",
        mcc="311",
        pais="United States",
    ),
    ("370", "312"): Prestadora(
        nome="Commnet Wireless", mnc="370", mcc="312", pais="United States"
    ),
    ("370", "313"): Prestadora(
        nome="Red Truck Wireless, LLC",
        mnc="370",
        mcc="313",
        pais="United States",
    ),
    ("370", "314"): Prestadora(
        nome="Texas A&M University – ITEC",
        mnc="370",
        mcc="314",
        pais="United States",
    ),
    ("380", "310"): Prestadora(
        nome="AT&T Mobility", mnc="380", mcc="310", pais="United States"
    ),
    ("380", "311"): Prestadora(
        nome="New Dimension Wireless Ltd",
        mnc="380",
        mcc="311",
        pais="United States",
    ),
    ("380", "312"): Prestadora(
        nome="Copper Valley Wireless",
        mnc="380",
        mcc="312",
        pais="United States",
    ),
    ("380", "313"): Prestadora(
        nome="OptimERA Inc.", mnc="380", mcc="313", pais="United States"
    ),
    ("380", "314"): Prestadora(
        nome="Circle Computer Resources, Inc.",
        mnc="380",
        mcc="314",
        pais="United States",
    ),
    ("390", "310"): Prestadora(
        nome="TX-11 Acquisition LLC",
        mnc="390",
        mcc="310",
        pais="United States",
    ),
    ("390", "311"): Prestadora(
        nome="Verizon Wireless", mnc="390", mcc="311", pais="United States"
    ),
    ("390", "312"): Prestadora(
        nome="FTC Communications LLC",
        mnc="390",
        mcc="312",
        pais="United States",
    ),
    ("390", "313"): Prestadora(
        nome="Altice USA Wireless, Inc.",
        mnc="390",
        mcc="313",
        pais="United States",
    ),
    ("390", "314"): Prestadora(nome="AT&T", mnc="390", mcc="314", pais="United States"),
    ("400", "311"): Prestadora(
        nome="TEST IMSI HNI", mnc="400", mcc="311", pais="United States"
    ),
    ("400", "313"): Prestadora(
        nome="Texoma Communications, LLC",
        mnc="400",
        mcc="313",
        pais="United States",
    ),
    ("400", "314"): Prestadora(
        nome="Cellular South Inc. dba C Spire",
        mnc="400",
        mcc="314",
        pais="United States",
    ),
    ("410", "310"): Prestadora(
        nome="AT&T Mobility", mnc="410", mcc="310", pais="United States"
    ),
    ("410", "312"): Prestadora(
        nome="Eltopia Communications, LLC",
        mnc="410",
        mcc="312",
        pais="United States",
    ),
    ("410", "313"): Prestadora(
        nome="Anterix Inc.", mnc="410", mcc="313", pais="United States"
    ),
    ("410", "314"): Prestadora(
        nome="Peeringhub Inc", mnc="410", mcc="314", pais="United States"
    ),
    ("420", "310"): Prestadora(
        nome="World Mobile Networks, Inc",
        mnc="420",
        mcc="310",
        pais="United States",
    ),
    ("420", "311"): Prestadora(
        nome="Northwest Cell", mnc="420", mcc="311", pais="United States"
    ),
    ("420", "312"): Prestadora(
        nome="Nex-Tech Wireless, LLC",
        mnc="420",
        mcc="312",
        pais="United States",
    ),
    ("420", "313"): Prestadora(
        nome="Hudson Valley Wireless",
        mnc="420",
        mcc="313",
        pais="United States",
    ),
    ("420", "314"): Prestadora(
        nome="Cox Communications, Inc",
        mnc="420",
        mcc="314",
        pais="United States",
    ),
    ("430", "310"): Prestadora(
        nome="GCI Communications Corp",
        mnc="430",
        mcc="310",
        pais="United States",
    ),
    ("430", "311"): Prestadora(
        nome="RSA 1 Limited Partnership dba Cellular 29 Plus",
        mnc="430",
        mcc="311",
        pais="United States",
    ),
    ("430", "312"): Prestadora(
        nome="Silver Star Communications",
        mnc="430",
        mcc="312",
        pais="United States",
    ),
    ("430", "314"): Prestadora(
        nome="Highway9 Networks, Inc.",
        mnc="430",
        mcc="314",
        pais="United States",
    ),
    ("440", "310"): Prestadora(
        nome="Numerex Corp", mnc="440", mcc="310", pais="United States"
    ),
    ("440", "311"): Prestadora(
        nome="Verizon Wireless", mnc="440", mcc="311", pais="United States"
    ),
    ("440", "313"): Prestadora(
        nome="Arvig Enterprises INC",
        mnc="440",
        mcc="313",
        pais="United States",
    ),
    ("440", "314"): Prestadora(
        nome="Tecore Global Services, LLC",
        mnc="440",
        mcc="314",
        pais="United States",
    ),
    ("450", "310"): Prestadora(
        nome="North East Cellular Inc.",
        mnc="450",
        mcc="310",
        pais="United States",
    ),
    ("450", "311"): Prestadora(
        nome="Panhandle Telecommunication Systems Inc.",
        mnc="450",
        mcc="311",
        pais="United States",
    ),
    ("450", "312"): Prestadora(
        nome="Cable & Communications Corporation",
        mnc="450",
        mcc="312",
        pais="United States",
    ),
    ("450", "313"): Prestadora(
        nome="Spectrum Wireless Holdings, LLC",
        mnc="450",
        mcc="313",
        pais="United States",
    ),
    ("450", "314"): Prestadora(
        nome="NUWAVE Communications, Inc.",
        mnc="450",
        mcc="314",
        pais="United States",
    ),
    ("460", "310"): Prestadora(
        nome="Eseye", mnc="460", mcc="310", pais="United States"
    ),
    ("460", "312"): Prestadora(
        nome="KPU Telecommunications Division",
        mnc="460",
        mcc="312",
        pais="United States",
    ),
    ("460", "313"): Prestadora(nome="Mobi", mnc="460", mcc="313", pais="United States"),
    ("460", "314"): Prestadora(
        nome="Texas A&M University",
        mnc="460",
        mcc="314",
        pais="United States",
    ),
    ("470", "310"): Prestadora(
        nome="Docomo Pacific Inc", mnc="470", mcc="310", pais="United States"
    ),
    ("470", "311"): Prestadora(
        nome="Vitelcom Cellular D/B/A Innovative Wireless",
        mnc="470",
        mcc="311",
        pais="United States",
    ),
    ("470", "312"): Prestadora(
        nome="Carolina West Wireless, Inc.",
        mnc="470",
        mcc="312",
        pais="United States",
    ),
    ("470", "313"): Prestadora(
        nome="San Diego Gas & Electric Company",
        mnc="470",
        mcc="313",
        pais="United States",
    ),
    ("470", "314"): Prestadora(
        nome="Manhattan Telecommunications Corporation LLC",
        mnc="470",
        mcc="314",
        pais="United States",
    ),
    ("480", "310"): Prestadora(
        nome="PTI Pacifica, Inc.", mnc="480", mcc="310", pais="United States"
    ),
    ("480", "311"): Prestadora(
        nome="Verizon Wireless", mnc="480", mcc="311", pais="United States"
    ),
    ("480", "312"): Prestadora(
        nome="Sagebrush Cellular, Inc.",
        mnc="480",
        mcc="312",
        pais="United States",
    ),
    ("480", "313"): Prestadora(
        nome="Ready Wireless, LLC",
        mnc="480",
        mcc="313",
        pais="United States",
    ),
    ("480", "314"): Prestadora(
        nome="Xcel Energy Services Inc.",
        mnc="480",
        mcc="314",
        pais="United States",
    ),
    ("481", "311"): Prestadora(
        nome="Verizon Wireless", mnc="481", mcc="311", pais="United States"
    ),
    ("482", "311"): Prestadora(
        nome="Verizon Wireless", mnc="482", mcc="311", pais="United States"
    ),
    ("483", "311"): Prestadora(
        nome="Verizon Wireless", mnc="483", mcc="311", pais="United States"
    ),
    ("484", "311"): Prestadora(
        nome="Verizon Wireless", mnc="484", mcc="311", pais="United States"
    ),
    ("485", "311"): Prestadora(
        nome="Verizon Wireless", mnc="485", mcc="311", pais="United States"
    ),
    ("486", "311"): Prestadora(
        nome="Verizon Wireless", mnc="486", mcc="311", pais="United States"
    ),
    ("487", "311"): Prestadora(
        nome="Verizon Wireless", mnc="487", mcc="311", pais="United States"
    ),
    ("488", "311"): Prestadora(
        nome="Verizon Wireless", mnc="488", mcc="311", pais="United States"
    ),
    ("489", "311"): Prestadora(
        nome="Verizon Wireless", mnc="489", mcc="311", pais="United States"
    ),
    ("490", "310"): Prestadora(
        nome="T-Mobile USA", mnc="490", mcc="310", pais="United States"
    ),
    ("490", "311"): Prestadora(
        nome="T-Mobile USA", mnc="490", mcc="311", pais="United States"
    ),
    ("490", "313"): Prestadora(
        nome="Puloli, Inc.", mnc="490", mcc="313", pais="United States"
    ),
    ("490", "314"): Prestadora(
        nome="Utah Education and Telehealth Network (UETN)",
        mnc="490",
        mcc="314",
        pais="United States",
    ),
    ("500", "310"): Prestadora(
        nome="Public Service Cellular, Inc.",
        mnc="500",
        mcc="310",
        pais="United States",
    ),
    ("500", "311"): Prestadora(nome="Mobi", mnc="500", mcc="311", pais="United States"),
    ("500", "313"): Prestadora(
        nome="Shelcomm, Inc", mnc="500", mcc="313", pais="United States"
    ),
    ("500", "314"): Prestadora(
        nome="Aetheros Inc", mnc="500", mcc="314", pais="United States"
    ),
    ("510", "310"): Prestadora(
        nome="Nsight", mnc="510", mcc="310", pais="United States"
    ),
    ("510", "311"): Prestadora(
        nome="Ligado Networks", mnc="510", mcc="311", pais="United States"
    ),
    ("510", "312"): Prestadora(nome="Wue", mnc="510", mcc="312", pais="United States"),
    ("510", "313"): Prestadora(
        nome="Puerto Rico Telephone Company",
        mnc="510",
        mcc="313",
        pais="United States",
    ),
    ("510", "314"): Prestadora(
        nome="SI Wireless LLC", mnc="510", mcc="314", pais="United States"
    ),
    ("520", "310"): Prestadora(
        nome="Transactions Network Services (TNS)",
        mnc="520",
        mcc="310",
        pais="United States",
    ),
    ("520", "314"): Prestadora(
        nome="Oklahoma Gas & Electric Company (OG&E)",
        mnc="520",
        mcc="314",
        pais="United States",
    ),
    ("530", "310"): Prestadora(
        nome="T-Mobile", mnc="530", mcc="310", pais="United States"
    ),
    ("530", "311"): Prestadora(
        nome="WorldCell Solutions LLC",
        mnc="530",
        mcc="311",
        pais="United States",
    ),
    ("530", "312"): Prestadora(
        nome="T-Mobile USA", mnc="530", mcc="312", pais="United States"
    ),
    ("530", "314"): Prestadora(
        nome="Agile Networks", mnc="530", mcc="314", pais="United States"
    ),
    ("540", "311"): Prestadora(
        nome="Coeur Rochester, Inc",
        mnc="540",
        mcc="311",
        pais="United States",
    ),
    ("540", "313"): Prestadora(
        nome="Nokia Innovations US LLC",
        mnc="540",
        mcc="313",
        pais="United States",
    ),
    ("540", "314"): Prestadora(
        nome="RGTN USA, Inc.", mnc="540", mcc="314", pais="United States"
    ),
    ("550", "310"): Prestadora(
        nome="Syniverse Technologies",
        mnc="550",
        mcc="310",
        pais="United States",
    ),
    ("550", "311"): Prestadora(
        nome="Commnet Wireless, LLC",
        mnc="550",
        mcc="311",
        pais="United States",
    ),
    ("550", "313"): Prestadora(
        nome="Mile High Networks LLC",
        mnc="550",
        mcc="313",
        pais="United States",
    ),
    ("560", "311"): Prestadora(
        nome="OTZ Communications Inc",
        mnc="560",
        mcc="311",
        pais="United States",
    ),
    ("560", "313"): Prestadora(
        nome="Boldyn Networks Transit US LLC",
        mnc="560",
        mcc="313",
        pais="United States",
    ),
    ("570", "310"): Prestadora(
        nome="Broadpoint, LLC (former PetroCom, LLC) c/o MTPCS, LLC dba CellularOne",
        mnc="570",
        mcc="310",
        pais="United States",
    ),
    ("570", "311"): Prestadora(
        nome="Mediacom", mnc="570", mcc="311", pais="United States"
    ),
    ("570", "312"): Prestadora(
        nome="Buffalo-Lake Erie Wireless Systems Co., LLC",
        mnc="570",
        mcc="312",
        pais="United States",
    ),
    ("570", "313"): Prestadora(
        nome="Cellular Network Partnership",
        mnc="570",
        mcc="313",
        pais="United States",
    ),
    ("580", "310"): Prestadora(
        nome="Inland Cellular Telephone Company",
        mnc="580",
        mcc="310",
        pais="United States",
    ),
    ("580", "311"): Prestadora(
        nome="U.S. Cellular", mnc="580", mcc="311", pais="United States"
    ),
    ("580", "312"): Prestadora(
        nome="Google LLC", mnc="580", mcc="312", pais="United States"
    ),
    ("580", "313"): Prestadora(
        nome="Telecall Telecommuncations Corp.",
        mnc="580",
        mcc="313",
        pais="United States",
    ),
    ("588", "311"): Prestadora(
        nome="U.S. Cellular", mnc="588", mcc="311", pais="United States"
    ),
    ("589", "311"): Prestadora(
        nome="U.S. Cellular", mnc="589", mcc="311", pais="United States"
    ),
    ("590", "310"): Prestadora(
        nome="Verizon Wireless", mnc="590", mcc="310", pais="United States"
    ),
    ("590", "311"): Prestadora(
        nome="Verizon Wireless", mnc="590", mcc="311", pais="United States"
    ),
    ("590", "312"): Prestadora(
        nome="Northern Michigan University",
        mnc="590",
        mcc="312",
        pais="United States",
    ),
    ("590", "313"): Prestadora(
        nome="Southern Communications Services, Inc. D/B/A Southern Linc",
        mnc="590",
        mcc="313",
        pais="United States",
    ),
    ("591", "310"): Prestadora(
        nome="Verizon Wireless", mnc="591", mcc="310", pais="United States"
    ),
    ("592", "310"): Prestadora(
        nome="Verizon Wireless", mnc="592", mcc="310", pais="United States"
    ),
    ("593", "310"): Prestadora(
        nome="Verizon Wireless", mnc="593", mcc="310", pais="United States"
    ),
    ("594", "310"): Prestadora(
        nome="Verizon Wireless", mnc="594", mcc="310", pais="United States"
    ),
    ("595", "310"): Prestadora(
        nome="Verizon Wireless", mnc="595", mcc="310", pais="United States"
    ),
    ("596", "310"): Prestadora(
        nome="Verizon Wireless", mnc="596", mcc="310", pais="United States"
    ),
    ("597", "310"): Prestadora(
        nome="Verizon Wireless", mnc="597", mcc="310", pais="United States"
    ),
    ("598", "310"): Prestadora(
        nome="Verizon Wireless", mnc="598", mcc="310", pais="United States"
    ),
    ("599", "310"): Prestadora(
        nome="Verizon Wireless", mnc="599", mcc="310", pais="United States"
    ),
    ("600", "310"): Prestadora(
        nome="NewCell dba Cellcom",
        mnc="600",
        mcc="310",
        pais="United States",
    ),
    ("600", "311"): Prestadora(
        nome="Limitless Mobile, LLC",
        mnc="600",
        mcc="311",
        pais="United States",
    ),
    ("600", "312"): Prestadora(
        nome="Sagebrush Cellular, Inc.",
        mnc="600",
        mcc="312",
        pais="United States",
    ),
    ("600", "313"): Prestadora(
        nome="ST Engineering iDirect",
        mnc="600",
        mcc="313",
        pais="United States",
    ),
    ("610", "312"): Prestadora(
        nome="ShawnTech Communications",
        mnc="610",
        mcc="312",
        pais="United States",
    ),
    ("610", "313"): Prestadora(
        nome="Point Broadband Fiber Holding, LLC",
        mnc="610",
        mcc="313",
        pais="United States",
    ),
    ("620", "310"): Prestadora(
        nome="Nsighttel Wireless, LLC",
        mnc="620",
        mcc="310",
        pais="United States",
    ),
    ("620", "311"): Prestadora(
        nome="TerreStar Networks Inc.",
        mnc="620",
        mcc="311",
        pais="United States",
    ),
    ("620", "312"): Prestadora(
        nome="GlobeTouch Inc.", mnc="620", mcc="312", pais="United States"
    ),
    ("620", "313"): Prestadora(
        nome="Omniprophis Corporation",
        mnc="620",
        mcc="313",
        pais="United States",
    ),
    ("630", "310"): Prestadora(
        nome="Choice Wireless", mnc="630", mcc="310", pais="United States"
    ),
    ("630", "311"): Prestadora(
        nome="Cellular South Inc.",
        mnc="630",
        mcc="311",
        pais="United States",
    ),
    ("630", "312"): Prestadora(
        nome="NetGenuity, Inc.", mnc="630", mcc="312", pais="United States"
    ),
    ("630", "313"): Prestadora(
        nome="LICT Corporation", mnc="630", mcc="313", pais="United States"
    ),
    ("640", "310"): Prestadora(
        nome="Numerex Corp", mnc="640", mcc="310", pais="United States"
    ),
    ("640", "311"): Prestadora(
        nome="Standing Rock Telecommunications",
        mnc="640",
        mcc="311",
        pais="United States",
    ),
    ("640", "313"): Prestadora(
        nome="Geoverse", mnc="640", mcc="313", pais="United States"
    ),
    ("650", "310"): Prestadora(
        nome="JASPER TECHNOLOGIES INC.",
        mnc="650",
        mcc="310",
        pais="United States",
    ),
    ("650", "311"): Prestadora(
        nome="United Wireless Inc",
        mnc="650",
        mcc="311",
        pais="United States",
    ),
    ("650", "312"): Prestadora(
        nome="Brightlink", mnc="650", mcc="312", pais="United States"
    ),
    ("650", "313"): Prestadora(
        nome="Chevron USA INC", mnc="650", mcc="313", pais="United States"
    ),
    ("660", "310"): Prestadora(
        nome="T-Mobile USA", mnc="660", mcc="310", pais="United States"
    ),
    ("660", "311"): Prestadora(
        nome="Metro PCS Wireless Inc",
        mnc="660",
        mcc="311",
        pais="United States",
    ),
    ("660", "313"): Prestadora(
        nome="Hudson Valley Wireless",
        mnc="660",
        mcc="313",
        pais="United States",
    ),
    ("670", "310"): Prestadora(
        nome="AT&T Mobility", mnc="670", mcc="310", pais="United States"
    ),
    ("670", "311"): Prestadora(
        nome="Pine Belt Cellular Inc dba Pine Belt Wireless",
        mnc="670",
        mcc="311",
        pais="United States",
    ),
    ("670", "312"): Prestadora(
        nome="AT&T Mobility", mnc="670", mcc="312", pais="United States"
    ),
    ("670", "313"): Prestadora(
        nome="Hudson Valley Wireless",
        mnc="670",
        mcc="313",
        pais="United States",
    ),
    ("680", "310"): Prestadora(
        nome="AT&T Mobility", mnc="680", mcc="310", pais="United States"
    ),
    ("680", "311"): Prestadora(
        nome="GreenFly LLC", mnc="680", mcc="311", pais="United States"
    ),
    ("680", "312"): Prestadora(
        nome="AT&T Mobility", mnc="680", mcc="312", pais="United States"
    ),
    ("680", "313"): Prestadora(
        nome="Hudson Valley Wireless",
        mnc="680",
        mcc="313",
        pais="United States",
    ),
    ("690", "310"): Prestadora(
        nome="Limitless Mobile, LLC",
        mnc="690",
        mcc="310",
        pais="United States",
    ),
    ("690", "311"): Prestadora(
        nome="TeleBeeper of New Mexico Inc",
        mnc="690",
        mcc="311",
        pais="United States",
    ),
    ("690", "312"): Prestadora(
        nome="TGS, LLC", mnc="690", mcc="312", pais="United States"
    ),
    ("690", "313"): Prestadora(
        nome="Shenandoah Cable Television, LLC",
        mnc="690",
        mcc="313",
        pais="United States",
    ),
    ("700", "310"): Prestadora(
        nome="Cross Valiant Cellular Partnership",
        mnc="700",
        mcc="310",
        pais="United States",
    ),
    ("700", "312"): Prestadora(
        nome="Wireless Partners,LLC",
        mnc="700",
        mcc="312",
        pais="United States",
    ),
    ("700", "313"): Prestadora(
        nome="Ameren Services Company",
        mnc="700",
        mcc="313",
        pais="United States",
    ),
    ("700", "316"): Prestadora(
        nome="Mile High Networks LLC",
        mnc="700",
        mcc="316",
        pais="United States",
    ),
    ("710", "310"): Prestadora(
        nome="Arctic Slope Telephone Association Cooperative",
        mnc="710",
        mcc="310",
        pais="United States",
    ),
    ("710", "312"): Prestadora(
        nome="Great North Woods Wireless LLC",
        mnc="710",
        mcc="312",
        pais="United States",
    ),
    ("710", "313"): Prestadora(
        nome="Extenet Systems", mnc="710", mcc="313", pais="United States"
    ),
    ("720", "310"): Prestadora(
        nome="Syniverse Technologies",
        mnc="720",
        mcc="310",
        pais="United States",
    ),
    ("720", "311"): Prestadora(
        nome="Maine PCS LLC", mnc="720", mcc="311", pais="United States"
    ),
    ("720", "312"): Prestadora(
        nome="Southern Communications Services, Inc. D/B/A SouthernLINC Wireless",
        mnc="720",
        mcc="312",
        pais="United States",
    ),
    ("720", "313"): Prestadora(
        nome="1st Point Communications, LLC",
        mnc="720",
        mcc="313",
        pais="United States",
    ),
    ("730", "312"): Prestadora(
        nome="Triangle Communication System Inc.",
        mnc="730",
        mcc="312",
        pais="United States",
    ),
    ("730", "313"): Prestadora(
        nome="TruAccess Networks", mnc="730", mcc="313", pais="United States"
    ),
    ("740", "310"): Prestadora(
        nome="Viaero Wireless", mnc="740", mcc="310", pais="United States"
    ),
    ("740", "311"): Prestadora(
        nome="Telalaska Cellular", mnc="740", mcc="311", pais="United States"
    ),
    ("740", "313"): Prestadora(
        nome="RTO Wireless", mnc="740", mcc="313", pais="United States"
    ),
    ("750", "310"): Prestadora(
        nome="East Kentucky Network LLC dba Appalachian Wireless",
        mnc="750",
        mcc="310",
        pais="United States",
    ),
    ("750", "312"): Prestadora(
        nome="Artemis", mnc="750", mcc="312", pais="United States"
    ),
    ("750", "313"): Prestadora(
        nome="CellTex Networks, LLC",
        mnc="750",
        mcc="313",
        pais="United States",
    ),
    ("760", "310"): Prestadora(
        nome="Lynch 3G Communications Corporation",
        mnc="760",
        mcc="310",
        pais="United States",
    ),
    ("760", "311"): Prestadora(
        nome="Reclaimed 06/21/2016",
        mnc="760",
        mcc="311",
        pais="United States",
    ),
    ("760", "312"): Prestadora(
        nome="ARCTIC SLOPE TELEPHONE ASSOCIATION COOPERATIVE",
        mnc="760",
        mcc="312",
        pais="United States",
    ),
    ("760", "313"): Prestadora(
        nome="Hologram", mnc="760", mcc="313", pais="United States"
    ),
    ("770", "310"): Prestadora(
        nome="T-Mobile", mnc="770", mcc="310", pais="United States"
    ),
    ("770", "311"): Prestadora(
        nome="Altiostar Networks, Inc.",
        mnc="770",
        mcc="311",
        pais="United States",
    ),
    ("770", "312"): Prestadora(
        nome="Verizon Wireless", mnc="770", mcc="312", pais="United States"
    ),
    ("770", "313"): Prestadora(
        nome="Tango Networks", mnc="770", mcc="313", pais="United States"
    ),
    ("780", "311"): Prestadora(
        nome="The American Samoa Telecommunications Authority",
        mnc="780",
        mcc="311",
        pais="United States",
    ),
    ("780", "312"): Prestadora(
        nome="RedZone Wireless LLC",
        mnc="780",
        mcc="312",
        pais="United States",
    ),
    ("780", "313"): Prestadora(
        nome="Windstream Services LLC",
        mnc="780",
        mcc="313",
        pais="United States",
    ),
    ("790", "310"): Prestadora(
        nome="PinPoint Communications Inc.",
        mnc="790",
        mcc="310",
        pais="United States",
    ),
    ("790", "311"): Prestadora(
        nome="Coleman County Telephone Cooperative, Inc.",
        mnc="790",
        mcc="311",
        pais="United States",
    ),
    ("790", "312"): Prestadora(
        nome="Gila Electronics", mnc="790", mcc="312", pais="United States"
    ),
    ("790", "313"): Prestadora(
        nome="Liberty Cablevision of Puerto Rico LLC",
        mnc="790",
        mcc="313",
        pais="United States",
    ),
    ("800", "310"): Prestadora(
        nome="T-Mobile USA", mnc="800", mcc="310", pais="United States"
    ),
    ("800", "311"): Prestadora(
        nome="Verizon Wireless", mnc="800", mcc="311", pais="United States"
    ),
    ("800", "312"): Prestadora(
        nome="Cirrus Core Networks",
        mnc="800",
        mcc="312",
        pais="United States",
    ),
    ("810", "310"): Prestadora(
        nome="Pacific Lightwave Inc.",
        mnc="810",
        mcc="310",
        pais="United States",
    ),
    ("810", "311"): Prestadora(
        nome="Verizon Wireless", mnc="810", mcc="311", pais="United States"
    ),
    ("810", "312"): Prestadora(
        nome="Bristol Bay Telephone Cooperative",
        mnc="810",
        mcc="312",
        pais="United States",
    ),
    ("810", "313"): Prestadora(
        nome="W.A.T.C.H. TV Co. dba Watch Communications",
        mnc="810",
        mcc="313",
        pais="United States",
    ),
    ("820", "310"): Prestadora(
        nome="Verizon Wireless", mnc="820", mcc="310", pais="United States"
    ),
    ("820", "311"): Prestadora(
        nome="Ribbon Communications",
        mnc="820",
        mcc="311",
        pais="United States",
    ),
    ("820", "313"): Prestadora(
        nome="Inland Cellular Telephone Company",
        mnc="820",
        mcc="313",
        pais="United States",
    ),
    ("830", "310"): Prestadora(
        nome="T-Mobile USA", mnc="830", mcc="310", pais="United States"
    ),
    ("830", "311"): Prestadora(
        nome="Thumb Cellular LLC", mnc="830", mcc="311", pais="United States"
    ),
    ("830", "312"): Prestadora(
        nome="Kings County Office of Education",
        mnc="830",
        mcc="312",
        pais="United States",
    ),
    ("830", "313"): Prestadora(
        nome="360 communications INC",
        mnc="830",
        mcc="313",
        pais="United States",
    ),
    ("840", "310"): Prestadora(
        nome="Telecom North America Mobile Inc",
        mnc="840",
        mcc="310",
        pais="United States",
    ),
    ("840", "311"): Prestadora(
        nome="Nsight", mnc="840", mcc="311", pais="United States"
    ),
    ("840", "312"): Prestadora(
        nome="South Georgia Regional Information Technology",
        mnc="840",
        mcc="312",
        pais="United States",
    ),
    ("840", "313"): Prestadora(
        nome="Celblox Acquisitions",
        mnc="840",
        mcc="313",
        pais="United States",
    ),
    ("850", "310"): Prestadora(
        nome="Aeris Communications, Inc.",
        mnc="850",
        mcc="310",
        pais="United States",
    ),
    ("850", "311"): Prestadora(
        nome="Nsight", mnc="850", mcc="311", pais="United States"
    ),
    ("850", "312"): Prestadora(
        nome="Onvoy Spectrum, LLC",
        mnc="850",
        mcc="312",
        pais="United States",
    ),
    ("850", "313"): Prestadora(
        nome="Softcom Internet Communications, Inc.",
        mnc="850",
        mcc="313",
        pais="United States",
    ),
    ("860", "311"): Prestadora(
        nome="Uintah Basin Electronic Telecommunications",
        mnc="860",
        mcc="311",
        pais="United States",
    ),
    ("860", "313"): Prestadora(
        nome="AMG Technology Investment Group dba Nextlink Internet",
        mnc="860",
        mcc="313",
        pais="United States",
    ),
    ("870", "311"): Prestadora(
        nome="T-Mobile USA", mnc="870", mcc="311", pais="United States"
    ),
    ("870", "312"): Prestadora(
        nome="GigSky Mobile, LLC", mnc="870", mcc="312", pais="United States"
    ),
    ("870", "313"): Prestadora(
        nome="Elektrafi LLC", mnc="870", mcc="313", pais="United States"
    ),
    ("880", "310"): Prestadora(
        nome="Advantage Cellular Systems, Inc.",
        mnc="880",
        mcc="310",
        pais="United States",
    ),
    ("880", "311"): Prestadora(
        nome="T-Mobile USA", mnc="880", mcc="311", pais="United States"
    ),
    ("880", "312"): Prestadora(
        nome="Albemarle County Public Schools",
        mnc="880",
        mcc="312",
        pais="United States",
    ),
    ("880", "313"): Prestadora(
        nome="Shuttle Wireless Solutions Inc.",
        mnc="880",
        mcc="313",
        pais="United States",
    ),
    ("882", "311"): Prestadora(
        nome="T-Mobile", mnc="882", mcc="311", pais="United States"
    ),
    ("890", "310"): Prestadora(
        nome="Verizon Wireless", mnc="890", mcc="310", pais="United States"
    ),
    ("890", "311"): Prestadora(
        nome="Globecomm Network Services Corporation",
        mnc="890",
        mcc="311",
        pais="United States",
    ),
    ("890", "312"): Prestadora(
        nome="Circle Gx", mnc="890", mcc="312", pais="United States"
    ),
    ("890", "313"): Prestadora(
        nome="Tulare County Office of Education",
        mnc="890",
        mcc="313",
        pais="United States",
    ),
    ("891", "310"): Prestadora(
        nome="Verizon Wireless", mnc="891", mcc="310", pais="United States"
    ),
    ("892", "310"): Prestadora(
        nome="Verizon Wireless", mnc="892", mcc="310", pais="United States"
    ),
    ("893", "310"): Prestadora(
        nome="Verizon Wireless", mnc="893", mcc="310", pais="United States"
    ),
    ("894", "310"): Prestadora(
        nome="Verizon Wireless", mnc="894", mcc="310", pais="United States"
    ),
    ("895", "310"): Prestadora(
        nome="Verizon Wireless", mnc="895", mcc="310", pais="United States"
    ),
    ("896", "310"): Prestadora(
        nome="Verizon Wireless", mnc="896", mcc="310", pais="United States"
    ),
    ("897", "310"): Prestadora(
        nome="Verizon Wireless", mnc="897", mcc="310", pais="United States"
    ),
    ("898", "310"): Prestadora(
        nome="Verizon Wireless", mnc="898", mcc="310", pais="United States"
    ),
    ("899", "310"): Prestadora(
        nome="Verizon Wireless", mnc="899", mcc="310", pais="United States"
    ),
    ("900", "311"): Prestadora(
        nome="Gigsky Inc.", mnc="900", mcc="311", pais="United States"
    ),
    ("900", "312"): Prestadora(
        nome="Flat West Wireless, LLC",
        mnc="900",
        mcc="312",
        pais="United States",
    ),
    ("900", "313"): Prestadora(
        nome="All Tribal Networks",
        mnc="900",
        mcc="313",
        pais="United States",
    ),
    ("910", "310"): Prestadora(
        nome="Verizon Wireless", mnc="910", mcc="310", pais="United States"
    ),
    ("910", "312"): Prestadora(
        nome="East Kentucky Network LLC dba Appalachian Wireless",
        mnc="910",
        mcc="312",
        pais="United States",
    ),
    ("910", "313"): Prestadora(
        nome="San Diego Gas and Electric",
        mnc="910",
        mcc="313",
        pais="United States",
    ),
    ("920", "310"): Prestadora(
        nome="James Valley Wireless LLC",
        mnc="920",
        mcc="310",
        pais="United States",
    ),
    ("920", "313"): Prestadora(
        nome="JCI US INC", mnc="920", mcc="313", pais="United States"
    ),
    ("930", "310"): Prestadora(
        nome="Copper Valley Wireless",
        mnc="930",
        mcc="310",
        pais="United States",
    ),
    ("930", "311"): Prestadora(
        nome="Cox Communications", mnc="930", mcc="311", pais="United States"
    ),
    ("930", "312"): Prestadora(
        nome="Hewlett-Packard Communication Services, LLC",
        mnc="930",
        mcc="312",
        pais="United States",
    ),
    ("930", "313"): Prestadora(
        nome="Standing Rock Telecom",
        mnc="930",
        mcc="313",
        pais="United States",
    ),
    ("940", "310"): Prestadora(
        nome="Tyntec Limited", mnc="940", mcc="310", pais="United States"
    ),
    ("940", "311"): Prestadora(
        nome="T-Mobile USA", mnc="940", mcc="311", pais="United States"
    ),
    ("940", "313"): Prestadora(
        nome="Motorola Solutions, Inc",
        mnc="940",
        mcc="313",
        pais="United States",
    ),
    ("950", "310"): Prestadora(
        nome="AT&T Mobility", mnc="950", mcc="310", pais="United States"
    ),
    ("950", "311"): Prestadora(
        nome="Sunman Telecommunications Corp.",
        mnc="950",
        mcc="311",
        pais="United States",
    ),
    ("950", "312"): Prestadora(
        nome="Custer Telephone Cooperative, Inc",
        mnc="950",
        mcc="312",
        pais="United States",
    ),
    ("950", "313"): Prestadora(
        nome="Cheyenne and Arapaho Development Group",
        mnc="950",
        mcc="313",
        pais="United States",
    ),
    ("960", "310"): Prestadora(
        nome="UBET Wireless", mnc="960", mcc="310", pais="United States"
    ),
    ("960", "313"): Prestadora(
        nome="Townes 5G, LLC", mnc="960", mcc="313", pais="United States"
    ),
    ("970", "310"): Prestadora(
        nome="Globalstar USA", mnc="970", mcc="310", pais="United States"
    ),
    ("970", "311"): Prestadora(
        nome="Big River Broadband LLC",
        mnc="970",
        mcc="311",
        pais="United States",
    ),
    ("970", "312"): Prestadora(
        nome="IOSAZ Intellectual Property LLC",
        mnc="970",
        mcc="312",
        pais="United States",
    ),
    ("970", "313"): Prestadora(
        nome="Tychron Corporation",
        mnc="970",
        mcc="313",
        pais="United States",
    ),
    ("980", "312"): Prestadora(
        nome="Mark Twain Communications Company",
        mnc="980",
        mcc="312",
        pais="United States",
    ),
    ("990", "310"): Prestadora(
        nome="Evolve Cellular Inc.",
        mnc="990",
        mcc="310",
        pais="United States",
    ),
    ("990", "311"): Prestadora(
        nome="VTel Wireless", mnc="990", mcc="311", pais="United States"
    ),
    ("990", "313"): Prestadora(
        nome="Ericsson US", mnc="990", mcc="313", pais="United States"
    ),
    ("01", "748"): Prestadora(
        nome="Administración Nacional de Telecomunicaciones (ANTEL)",
        mnc="01",
        mcc="748",
        pais="Uruguay",
    ),
    ("07", "748"): Prestadora(
        nome="Telefónica Móviles del Uruguay S.A. (Movistar)",
        mnc="07",
        mcc="748",
        pais="Uruguay",
    ),
    ("10", "748"): Prestadora(
        nome="AM Wireless Uruguay S.A. (Claro)",
        mnc="10",
        mcc="748",
        pais="Uruguay",
    ),
    ("15", "748"): Prestadora(nome="ENALUR S.A.", mnc="15", mcc="748", pais="Uruguay"),
    ("01", "434"): Prestadora(nome="Buztel", mnc="01", mcc="434", pais="Uzbekistan"),
    ("02", "434"): Prestadora(nome="Uzmacom", mnc="02", mcc="434", pais="Uzbekistan"),
    ("04", "434"): Prestadora(
        nome="Daewoo Unitel", mnc="04", mcc="434", pais="Uzbekistan"
    ),
    ("05", "434"): Prestadora(nome="Coscom", mnc="05", mcc="434", pais="Uzbekistan"),
    ("07", "434"): Prestadora(
        nome="Uzdunrobita", mnc="07", mcc="434", pais="Uzbekistan"
    ),
    ("01", "541"): Prestadora(nome="SMILE", mnc="01", mcc="541", pais="Vanuatu"),
    ("05", "541"): Prestadora(
        nome="Digicel Vanuatu", mnc="05", mcc="541", pais="Vanuatu"
    ),
    ("07", "541"): Prestadora(nome="WANTOK", mnc="07", mcc="541", pais="Vanuatu"),
    ("02", "734"): Prestadora(
        nome="Corporación Digitel",
        mnc="02",
        mcc="734",
        pais="Venezuela (Bolivarian Republic of)",
    ),
    ("03", "734"): Prestadora(
        nome="GALAXY ENTERTAINMENT DE VENEZUELA C.A.",
        mnc="03",
        mcc="734",
        pais="Venezuela (Bolivarian Republic of)",
    ),
    ("04", "734"): Prestadora(
        nome="Telcel, C.A.",
        mnc="04",
        mcc="734",
        pais="Venezuela (Bolivarian Republic of)",
    ),
    ("06", "734"): Prestadora(
        nome="Telecomunicaciones Movilnet, C.A.",
        mnc="06",
        mcc="734",
        pais="Venezuela (Bolivarian Republic of)",
    ),
    ("08", "734"): Prestadora(
        nome="PATRIACELL C.A.",
        mnc="08",
        mcc="734",
        pais="Venezuela (Bolivarian Republic of)",
    ),
    ("01", "452"): Prestadora(nome="MobiFone", mnc="01", mcc="452", pais="Viet Nam"),
    ("02", "452"): Prestadora(nome="Vinaphone", mnc="02", mcc="452", pais="Viet Nam"),
    ("04", "452"): Prestadora(nome="Viettel", mnc="04", mcc="452", pais="Viet Nam"),
    ("05", "452"): Prestadora(
        nome="Vietnamobile", mnc="05", mcc="452", pais="Viet Nam"
    ),
    ("07", "452"): Prestadora(nome="Gmobile", mnc="07", mcc="452", pais="Viet Nam"),
    ("08", "452"): Prestadora(nome="I-Telecom", mnc="08", mcc="452", pais="Viet Nam"),
    ("09", "452"): Prestadora(nome="REDDI", mnc="09", mcc="452", pais="Viet Nam"),
    ("01", "543"): Prestadora(
        nome="Manuia", mnc="01", mcc="543", pais="Wallis and Futuna"
    ),
    ("01", "421"): Prestadora(
        nome="Yemen Mobile Phone Company", mnc="01", mcc="421", pais="Yemen"
    ),
    ("02", "421"): Prestadora(nome="Spacetel Yemen", mnc="02", mcc="421", pais="Yemen"),
    ("04", "421"): Prestadora(nome="Y-Telecom", mnc="04", mcc="421", pais="Yemen"),
    ("01", "645"): Prestadora(
        nome="Airtel Zambia Limited", mnc="01", mcc="645", pais="Zambia"
    ),
    ("02", "645"): Prestadora(
        nome="MTN Zambia Limited", mnc="02", mcc="645", pais="Zambia"
    ),
    ("03", "645"): Prestadora(nome="Zamtel", mnc="03", mcc="645", pais="Zambia"),
    ("07", "645"): Prestadora(
        nome="Liquid Telecom Zambia Limited",
        mnc="07",
        mcc="645",
        pais="Zambia",
    ),
    ("01", "648"): Prestadora(nome="Net One", mnc="01", mcc="648", pais="Zimbabwe"),
    ("03", "648"): Prestadora(nome="Telecel", mnc="03", mcc="648", pais="Zimbabwe"),
    ("04", "648"): Prestadora(nome="Econet", mnc="04", mcc="648", pais="Zimbabwe"),
}
