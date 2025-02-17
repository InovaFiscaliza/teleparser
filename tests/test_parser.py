import re
from pprint import pprint as print
# import pandas as pd

# Sample data as a string (replace this with reading from a file)
data = """
0 > 1 UMTSGSMPLMNCallDataRecord=[roamingCallForwarding=[callPosition="01" chargeableDuration="00:00:00.0" dateForStartOfCharge="24.12.14" exchangeIdentity="ZCTA09P BR00308" interruptionTime="00:00:00" recordSequenceNumber="1443930" tariffClass="1" timeForStartOfCharge="11:00:15" timeForStopOfCharge="11:00:15" switchIdentity="9535" calledPartyNumber="043988111780" mobileStationRoamingNumber="+55*03210000043988111780" mSCIdentification="+550044101009" calledSubscriberIMSI="103210000000000" networkCallReference="2DA020253F" callingPartyNumber="43920025120" incomingRoute="41TWYMI" presentationAndScreeningIndicator="B'0011 0000" redirectionCounter="0" relatedCallNumber="8141740" callIdentificationNumber="8141794" typeOfCallingSubscriber="1" tAC="000204" subscriptionType="00" originForCharging="0" internalCauseAndLoc="0217" timeFromRegisterSeizureToStartOfCharging="00:00:00" chargedParty="00" disconnectingParty="02" outgoingRoute="ZFN3AEO" eosInfo="54"]]
194 > 2 UMTSGSMPLMNCallDataRecord=[transit=[callPosition="01" chargeableDuration="00:00:00.0" dateForStartOfCharge="24.12.14" exchangeIdentity="ZCTA09P BR00308" interruptionTime="00:00:00" recordSequenceNumber="1443931" tariffClass="1" timeForStartOfCharge="11:00:15" timeForStopOfCharge="11:00:15" switchIdentity="9535" 0.0.90="410A230100003489181187F0" internalCauseAndLoc="0217" faultCode="3754" disconnectingParty="02" typeOfCallingSubscriber="1" translatedNumber="+5543988111780" tAC="000201" timeFromRegisterSeizureToStartOfCharging="00:00:00" subscriptionType="00" redirectionCounter="0" originatedCode="02" originForCharging="0" networkCallReference="2DA020253F" outgoingRoute="HLR437" incomingRoute="41TWYMI" chargedParty="00" callingPartyNumber="43920025120" calledPartyNumber="043988111780" eosInfo="54" callIdentificationNumber="8141740"]]
"""

# Regular expression to extract key-value pairs
pattern = re.compile(r'(\w+)=("[^"]*"|\S+)')

# List to hold the parsed records
records = []

# Split the data into lines and process each line
for line in data.strip().split("\n"):
    # Extract the key-value pairs using the regex
    matches = pattern.findall(line)

    # Convert matches to a dictionary
    record = {key: value.strip('"') for key, value in matches}

    # Append the dictionary to the records list
    records.append(record)

print(records)

# # Create a DataFrame from the list of dictionaries
# df = pd.DataFrame(records)

# # Save the DataFrame as a Parquet file
# df.to_parquet("call_details.parquet", engine="pyarrow")

# print("DataFrame saved as call_details.parquet")
