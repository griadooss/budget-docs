---
title: 'EOY Process Developer Guide'
description: 'Technical information for developers working on the End of Year process'
---

# EOY Process Developer Guide

This guide contains technical information for developers who are maintaining or enhancing the End of Year (EOY) process. End users should refer to the [End of Year Process Overview](overview.md) and [EOY Budget Setup](setup.md) guides instead.

## Current Implementation Overview

The EOY process has been significantly improved from the original design and now features:

### Key Architectural Features
- **Month-Restricted Access** - Process only available in June (final fiscal month)
- **State-Driven Menu System** - Menus adapt based on EOY completion status
- **Three-Step Progressive Workflow** - Clear progression through setup phases
- **Automated Master Archiving** - Previous master automatically archived on completion
- **Comprehensive Verification** - Multiple validation checkpoints throughout process

### Core Functions and Files
The EOY implementation is primarily contained in `src/utility/yearEndBudget.js`:

- **Main Entry Points:**
  - `showYearEndHelp()` - Initial help dialog in master spreadsheet
  - `setupNewYearBudget()` - Step 1: Initial EOY setup
  - `continueEOYSetup()` - Step 2: Continue configuration and budget update
  - `finalizeEOYSetup()` - Step 3: Finalization and master archiving

- **Supporting Functions:**
  - `exportPropertiesToSheet()` / `importPropertiesFromSheet()` - Property management
  - `clearTransactionSheets()` - Clean Cash Flow and Bank Records sheets
  - `copyBankBalancesToOpeningPositions()` - Transfer bank balances
  - `updateMonthlyHeaders()` - Update fiscal year headers across sheets
  - `archiveLegacyMaster()` - Automatic master archiving

## Development and Testing Workflow

### Critical Development Process

When developing and testing the EOY process, you **must** follow this workflow to ensure you're testing the latest code:

1. **Development Phase:**
   - Make all script changes in the **MASTER** spreadsheet
   - Test individual functions using Apps Script editor
   - Push changes using `clasp push` to update MASTER's script project

2. **Testing Phase:**
   - **Always delete existing test copies** before creating new ones
   - Make a **fresh copy** of MASTER for each test cycle
   - Each copy gets its own Apps Script project with the current code
   - Test the complete EOY process in the fresh copy

3. **Issue Resolution:**
   - Document any issues found during testing
   - Make fixes in the **MASTER** spreadsheet
   - Push changes to MASTER using `clasp push`
   - Delete test copy and create a new one for retesting

<Warning>
**Critical:** Never use old test copies. Each copy has its own script project, and using an old copy will test outdated code, leading to false results and wasted development time.
</Warning>

### Month Restriction Testing

The EOY process includes month validation that restricts access to June only:

```javascript
// In setupNewYearBudget() and showYearEndHelp()
const currentMonth = getCurrentMonth();
if (currentMonth && currentMonth.month !== 6) {
  // Block access with user-friendly message
  ui.alert("Process Not Available",
           "The 'Start End of Year Process' is only available in June...");
  return;
}
```

**Testing Considerations:**
- **Production:** Process only works in June
- **Development:** You may need to temporarily bypass month checking for testing
- **Test Mode:** Use `testMode` parameters in functions where available

## State Management and Menu System

### EOY State Tracking

The system uses script properties to track EOY progress:

```javascript
// Key properties for state management
- IS_MASTER: "true"/"false" - Whether spreadsheet is the active master
- EOY_SETUP_COMPLETE: "true"/"false" - Whether EOY setup is finished
- EOY_READY_FOR_EOM: "true"/"false" - Intermediate state during setup
- CURRENT_SPREADSHEET_ID: "{id}" - Current spreadsheet identifier
- MASTER_SPREADSHEET_ID: "{id}" - ID of the master spreadsheet
```

### Menu State Logic

The menu system in `onOpen.js` adapts based on these states:

```javascript
// In createBasicMenus()
if (!isMaster && !eoySetupComplete && !eoyReadyForEom) {
  // Fresh copy - show only EOY setup options
  periodMenu.addSubMenu(
    ui.createMenu("End of Year Setup")
      .addItem("1. Run Initial EOY Setup", "setupNewYearBudget")
      .addItem("2. Continue EOY Setup", "continueEOYSetup")
      .addItem("3. Finalize EOY Setup", "finalizeEOYSetup")
  );
}
```

### State Transitions

1. **Fresh Copy Creation:**
   - `IS_MASTER = false` (imported from master)
   - `EOY_SETUP_COMPLETE = false`
   - `EOY_READY_FOR_EOM = false`
   - Menu shows only EOY setup options

2. **After Initial Setup:**
   - Properties updated to reflect progress
   - Menu options remain EOY-focused

3. **After Finalization:**
   - `IS_MASTER = true`
   - `EOY_SETUP_COMPLETE = true`
   - Menu shows normal operational options

## Technical Implementation Details

### Property Export/Import System

The property management system ensures continuity between master and copy:

```javascript
// Export from master to hidden sheet
function exportPropertiesToSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("_Properties");

  if (!sheet) {
    sheet = ss.insertSheet("_Properties");
    sheet.hideSheet();
  }

  const props = PropertiesService.getScriptProperties().getProperties();
  // Write properties to sheet for copying
}

// Import from hidden sheet in new copy
function importPropertiesFromSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("_Properties");

  if (sheet) {
    // Read properties from sheet and set in new copy
    // Adjust IS_MASTER to false for new copy
  }
}
```

### Verification System

Multiple verification points ensure system integrity:

1. **Sheet Structure Verification** (`validateSheets()`)
   - Verifies all required sheets exist
   - Checks sheet naming conventions
   - Validates critical named ranges

2. **Budget Formula Verification** (`verifyBudgetSetup()`)
   - Checks Annual Budget formulas
   - Validates Maintain Budget structure
   - Ensures proper formula references

3. **Balance Verification** (in `finalizeEOYSetup()`)
   - Banks sheet: Cell C30 = 0
   - Annual Budget: Cell B106 = 0
   - Maintain Budget: Cell E120 = 0

### Automatic Master Archiving

The archiving system provides automatic legacy master management:

```javascript
function archiveLegacyMaster(spreadsheetId, testMode = false) {
  try {
    const targetSS = SpreadsheetApp.openById(spreadsheetId);
    const fiscalYear = getFiscalYearFromSpreadsheet(targetSS);

    if (testMode) {
      // Create test copy for verification
      return targetSS.copy(`${targetSS.getName()}_ARCHIVED_TEST`);
    }

    // Rename with archived suffix
    const newName = `${targetSS.getName()}_ARCHIVED_FY${fiscalYear}`;
    targetSS.rename(newName);

    // Add hidden archive metadata sheet
    const archiveSheet = targetSS.insertSheet("_Archive");
    archiveSheet.hideSheet();

    // Set archive metadata
    archiveSheet.getRange("A1").setValue("ARCHIVED_DATE");
    archiveSheet.getRange("B1").setValue(new Date());
    archiveSheet.getRange("A2").setValue("FORMER_MASTER");
    archiveSheet.getRange("B2").setValue(true);

  } catch (error) {
    console.error("Error archiving legacy master:", error);
    throw error;
  }
}
```

## Known Technical Limitations

### Script Property Isolation

**Issue:** Google Apps Script security model prevents modifying script properties of other spreadsheets.

**Impact:** Archived masters retain `IS_MASTER = true` in their script properties.

**Mitigation Strategies:**
1. **Renamed Title** - Archived spreadsheets have clear "\_ARCHIVED_FY{year}" suffix
2. **Archive Metadata** - Hidden "\_Archive" sheet marks archival status
3. **User Documentation** - Clear guidance to avoid using archived spreadsheets

### Google Authorization User Experience

**Issue:** Google shows intimidating "unsafe" warnings for all custom spreadsheet scripts.

**Impact:** Users may be reluctant to continue authorization due to scary warning language.

**User Experience Challenges:**
- "Google hasn't verified this app" warning appears threatening
- "Go to Budget App Scripts (unsafe)" button seems dangerous
- Users may abandon the process thinking something is wrong

**Mitigation Strategies:**
1. **Clear Documentation** - Detailed explanation that warnings are normal
2. **Step-by-Step Instructions** - Specific guidance through each authorization step
3. **Reassurance** - Explicit statements that the process is safe and expected

## Testing and Quality Assurance

### Comprehensive Testing Checklist

#### Before Testing Session
- [ ] All changes pushed to MASTER spreadsheet
- [ ] Old test copies deleted
- [ ] Fresh copy created from MASTER
- [ ] Test environment prepared

#### During Testing - Step 1 (Initial Setup)
- [ ] Month restriction working (if testing in non-June month)
- [ ] Help dialog displays correctly with documentation links
- [ ] Property export completes successfully
- [ ] New copy creation process works
- [ ] Menu system shows only EOY options in new copy

#### During Testing - Step 2 (Configuration)
- [ ] Authorization process works smoothly
- [ ] Verification checks pass for valid setup
- [ ] Configuration dialog accepts valid inputs
- [ ] Manual budget update process functions
- [ ] Budget balance validation works
- [ ] Continue setup processes correctly

#### During Testing - Step 3 (Finalization)
- [ ] Final verification checks function properly
- [ ] Master archiving completes without errors
- [ ] New copy marked as master successfully
- [ ] Menu system updates to normal operational mode
- [ ] All transaction sheets properly cleared

#### Post-Testing Verification
- [ ] Master functionality works in new spreadsheet
- [ ] Archived master properly renamed and marked
- [ ] Historical data preserved in archived master
- [ ] No script errors in new master
- [ ] Documentation links work correctly

### Testing Functions

Several helper functions support testing:

```javascript
// Test archiving without affecting production
function testArchiveMaster() {
  const currentId = SpreadsheetApp.getActiveSpreadsheet().getId();
  return archiveLegacyMaster(currentId, true); // testMode = true
}

// Test EOY process with safety checks
function testEOYProcess() {
  console.log("Starting EOY test process...");
  return setupNewYearBudget(true); // testMode = true
}

// Safe refresh function for testing
function runRefreshSafely() {
  try {
    SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Annual Budget");
    // Additional safety checks
  } catch (error) {
    console.error("Refresh safety check failed:", error);
  }
}
```

## Performance Considerations

### Optimization Strategies

1. **Minimal Sheet Operations:**
   - Batch range operations where possible
   - Avoid excessive individual cell operations
   - Use getValues()/setValues() for bulk operations

2. **Property Management:**
   - Cache frequently accessed properties
   - Minimize property service calls
   - Use batch property operations

3. **Verification Efficiency:**
   - Combine multiple checks into single functions
   - Early exit on validation failures
   - Provide specific error messages for quick resolution

### Resource Management

```javascript
// Example of efficient batch operations
function updateMonthlyHeaders() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                             .getSheetByName("Annual Budget");

  // Get all headers in one operation
  const headerRange = sheet.getRange(1, 1, 1, sheet.getLastColumn());
  const headers = headerRange.getValues()[0];

  // Process headers in memory
  const updatedHeaders = headers.map(header => {
    // Update logic here
    return processHeader(header);
  });

  // Write all headers back in one operation
  headerRange.setValues([updatedHeaders]);
}
```

## Future Enhancement Opportunities

### Planned Improvements

1. **Enhanced Pre-EOY Validation:**
   - Automatic verification of balance requirements
   - Account reconciliation status checking
   - Data integrity validation before process start

2. **Improved Error Recovery:**
   - Process checkpoint system for resuming interrupted operations
   - Better error messages with specific resolution steps
   - Automatic retry mechanisms for transient failures

3. **Advanced State Management:**
   - More granular progress tracking
   - Session persistence across browser refreshes
   - Better handling of concurrent user access

### Technical Debt Reduction

1. **Script Property Limitation Resolution:**
   - Research Google Workspace APIs for property management
   - Implement alternative master tracking systems
   - Develop more robust archiving mechanisms

2. **Code Organization:**
   - Modularize large functions for better maintainability
   - Implement consistent error handling patterns
   - Add comprehensive inline documentation

3. **Testing Infrastructure:**
   - Automated testing framework for EOY process
   - Mock data generation for consistent testing
   - Performance benchmarking tools

## Security and Access Considerations

### Permission Requirements

The EOY process requires specific permissions:
- **Script execution** in both master and new copy
- **Spreadsheet access** for reading/writing operations
- **File creation** for making copies
- **Property management** for state tracking

### Security Best Practices

1. **Property Validation:**
   - Validate all imported properties
   - Sanitize user inputs in configuration dialogs
   - Check property values before using in operations

2. **Error Information Exposure:**
   - Avoid exposing sensitive system information in error messages
   - Log detailed errors for developers without showing to users
   - Provide user-friendly error messages with actionable guidance

3. **State Consistency:**
   - Verify state transitions are atomic where possible
   - Implement rollback mechanisms for critical operations
   - Validate system state before proceeding with operations

This developer guide provides the technical foundation for maintaining and enhancing the EOY process. For implementation details of specific functions, refer to the source code in `src/utility/yearEndBudget.js` and related files.