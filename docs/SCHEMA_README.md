# Ericsson Voice CDR Database Schema

## Overview
This schema definition (`ericsson_voz.sql`) provides a comprehensive database structure for storing Ericsson Voice Call Detail Records (CDR).

## Schema Statistics

### ENUM Types: 53
Custom enumerated types defined from the `enums.py` VALUES dictionaries:

- **AirInterfaceUserRateEnum** (11 values)
- **AsyncSyncIndicatorEnum** (2 values)
- **BearerServiceCodeEnum** (14 values)
- **BitRateEnum** (12 values)
- **CallAttemptStateEnum** (8 values)
- **CallPositionEnum** (4 values)
- **CarrierSelectionSubstitutionInformationEnum** (7 values)
- **ChannelAllocationPriorityLevelEnum** (15 values)
- **ChargedPartyEnum** (3 values)
- **DefaultCallHandlingEnum** (2 values)
- **DisconnectingPartyEnum** (3 values)
- **EosInfoEnum** (39 values)
- **INMarkingOfMSEnum** (13 values)
- **MessageTypeIndicatorEnum** (6 values)
- **SSCodeEnum** (54 values)
- **TeleServiceCodeEnum** (22 values)
- **TriggerDetectionPointEnum** (26 values)
- **UserRateEnum** (31 values)
... and 35 more ENUM types

### Table Columns: 371
Comprehensive coverage of all Ericsson CDR datatypes:

#### Column Types Distribution:
- **ENUM columns**: 53 (typed with specific enumerated values)
- **VARCHAR columns**: 318 (flexible text fields)

#### Categories:
- Call identification and routing
- Subscriber information (IMSI, IMEI, MSISDN)
- Location information (cell, LAC, RNC)
- Charging and billing data
- Service codes and triggers
- Quality of Service parameters
- CAMEL/IN service data
- SMS-specific fields

## Schema Features

### 1. Type Safety
- 53 ENUM types provide compile-time validation
- Prevents invalid values in critical fields
- Self-documenting valid values

### 2. Comprehensive Coverage
- All module types: MSOriginating, MSTerminating, Transit, etc.
- All datatype classes with value dictionaries
- Nested field support (e.g., `calledPartyNumber.digits`)

### 3. Standards Compliance
- All column names quoted with double quotes
- Alphabetically sorted for easy navigation
- No duplicates
- Clean SQL syntax

## Usage Example

```sql
-- Create the schema
\i ericsson_voz.sql

-- Insert a record
INSERT INTO ericsson_voz (
  "callIdentificationNumber",
  "asyncSyncIndicator",
  "bearerServiceCode",
  "callPosition"
) VALUES (
  '123456',
  'syncData',
  'General - data CDA',
  'answerHasBeenReceived'
);

-- Query with type safety
SELECT 
  "callIdentificationNumber",
  "disconnectingParty",
  "chargeableDuration"
FROM ericsson_voz
WHERE "callPosition" = 'answerHasBeenReceived';
```

## File Structure

```
ericsson_voz.sql (1044 lines)
├── Header (lines 1-10)
├── ENUM Definitions (lines 11-650)
│   ├── AirInterfaceUserRateEnum
│   ├── AsyncSyncIndicatorEnum
│   └── ... (51 more)
└── Table Definition (lines 651-1044)
    └── 371 columns (alphabetically sorted)
```

## Maintenance

To regenerate or update the schema:
1. Update datatype classes in `src/teleparser/decoders/ericsson/datatypes/`
2. Update module definitions in `src/teleparser/decoders/ericsson/modules.py`
3. Run the extraction and generation scripts
4. Review and commit changes

## Notes

- Some ENUM types may have numerous values (e.g., SSCode has 54 values)
- Dotted notation used for nested fields (e.g., `"calledPartyNumber.digits"`)
- All ENUM values are strings for maximum compatibility
- VARCHAR used for complex or variable-length fields

## Version
Generated: 2025-10-09
Source: teleparser project datatypes and modules
