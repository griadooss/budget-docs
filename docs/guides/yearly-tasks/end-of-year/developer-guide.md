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
- **Guided Master Archiving** - User manually archives previous master with system guidance
- **Comprehensive Verification** - Multiple validation checkpoints throughout process
- **User Choice Dialogs** - Commitment validation with Fix Now vs Ignore options
- **Draggable Warning Dialogs** - Improved user experience for all warning dialogs

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
  - `archiveThisMaster()` - Manual master archiving (user-initiated)
  - `validateCommitments()` - Check for outstanding commitments
  - `checkAllBalances()` - Comprehensive balance validation

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

!!! warning "Critical"
    Never use old test copies. Each copy has its own script project, and using an old copy will test outdated code, leading to false results and wasted development time.

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

### Commitment Validation System

The EOY process now includes a sophisticated commitment validation system that provides user choice rather than blocking:

```javascript
// In endOfMonthProcessing() - commitment validation
if (!isDev && !eoyReadyForEom) {
  const commitmentCheck = validateCommitments();
  
  if (!commitmentCheck.isValid) {
    // Show user choice dialog instead of blocking
    const userChoice = ui.alert(
      "⚠️ Outstanding Commitments Warning",
      `The following commitments have not been met for ${monthNames[currentMonth]} ${currentYear}:\n\n` +
        commitmentCheck.issues.join("\n") +
        "\n\n⚠️ WARNING: These commitments are outstanding.\n\n" +
        "Choose your action:\n" +
        "• NO = Fix Now: Address commitments before EOM processing\n" +
        "• YES = Ignore: Proceed with EOM despite outstanding commitments",
      ui.ButtonSet.YES_NO
    );
    
    if (userChoice === ui.Button.NO) {
      // User chose to fix commitments - block EOM
      return;
    }
    // User chose to ignore - continue with EOM
  }
}
```

**Key Features:**
- **Non-blocking Design:** Users can choose to proceed despite outstanding commitments
- **Clear User Interface:** Intuitive button mapping (NO = Fix Now, YES = Ignore)
- **Month/Year Display:** Shows correct month and year from script properties
- **Detailed Issue Reporting:** Lists specific commitment problems for user review

### Improved Dialog System

All warning dialogs in the EOY process now use a draggable, user-friendly interface:

```javascript
// Example of draggable dialog implementation
function showEOYSetupIncompleteDialog(issues) {
  const htmlOutput = HtmlService.createHtmlOutput(`
    <div style="font-family: Arial, sans-serif; padding: 20px;">
      <h3>⚠️ EOY Setup Incomplete</h3>
      <p>The following issues must be resolved before finalization:</p>
      <ul>${issues.map(issue => `<li>${issue}</li>`).join('')}</ul>
      <p>Please address these issues and try again.</p>
    </div>
  `)
  .setWidth(500)
  .setHeight(300);
  
  SpreadsheetApp.getUi().showModelessDialog(htmlOutput, "EOY Setup Incomplete");
}
```

**Benefits:**
- **Better User Experience:** Dialogs can be moved and don't block the interface
- **Consistent Design:** All dialogs follow the same visual pattern
- **Improved Readability:** Better formatting and layout for complex information
- **Non-intrusive:** Users can continue working while reviewing dialog content

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
   - Banks sheet: "BOOKS BALANCED" indicator = 0
   - Annual Budget: "BUDGET BALANCED" indicator = 0
   - Maintain Budget: Balance indicator = 0

### Manual Master Archiving Process

The archiving system requires **user-initiated action** rather than automatic archiving:

#### What Actually Happens During EOY Finalization

```javascript
// In proceedWithFinalization() - NO automatic archiving occurs
function proceedWithFinalization() {
  // 1. Mark new copy as master
  props.setProperty("IS_MASTER", "true");
  props.setProperty("EOY_SETUP_COMPLETE", "true");
  
  // 2. Show completion dialog with archiving instructions
  const htmlContent = `
    <h3>THEN: Archive Your Old Spreadsheet</h3>
    <p><strong>Go to your old spreadsheet (last year's budget) and archive it:</strong></p>
    <p>Settings → ⚠️ Advanced → Archive This Master</p>
  `;
  
  // 3. User must manually navigate to old master and run archiveThisMaster()
  // NO automatic archiving happens here
}
```

#### User-Initiated Archiving Function

```javascript
function archiveThisMaster() {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const ui = SpreadsheetApp.getUi();
    
    // 1. Get fiscal year for naming
    const fiscalYear = getFiscalYearFromSpreadsheet(ss);
    const currentName = ss.getName();
    const archiveName = `${currentName}_ARCHIVED_FY${fiscalYear.toString().slice(-2)}`;
    
    // 2. Confirm with user
    const confirmResponse = ui.alert(
      "📦 Archive This Master",
      `This will rename to: "${archiveName}" and mark as archived. Continue?`,
      ui.ButtonSet.YES_NO
    );
    
    if (confirmResponse !== ui.Button.YES) return false;
    
    // 3. Create archive metadata sheet
    const archiveSheet = ss.insertSheet("_Archive");
    archiveSheet.hideSheet();
    
    // 4. Update properties to mark as archived
    props.setProperty("IS_MASTER", "false");
    props.setProperty("IS_ARCHIVED", "true");
    props.setProperty("ARCHIVED_DATE", new Date().toISOString());
    
    // 5. Rename the spreadsheet
    ss.rename(archiveName);
    
    return true;
  } catch (error) {
    console.error("Error in archiveThisMaster:", error);
    return false;
  }
}
```

#### Key Technical Points

- **No Automatic Archiving:** The EOY finalization does NOT automatically archive the old master
- **User Control:** Archiving is completely user-initiated via Settings menu
- **Two-Step Process:** EOY finalization + Manual archiving = Complete EOY process
- **Reversible:** `restoreFromArchive()` function can undo the archiving

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
- [ ] Commitment validation dialogs work correctly
- [ ] User choice options (Fix Now vs Ignore) function properly

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