---
title: 'Developer Menu Reference'
description: 'Complete guide to all Developer menu functions and tools'
---

# Developer Menu Reference

<Note>
  The Developer menu is only available when Developer Mode is enabled. To enable Developer Mode, go to **ℹ️ Help > Toggle Developer Mode**.
</Note>

<Warning>
  **Developer Mode Warning:** Developer mode bypasses critical safety checks and should only be used for development and testing purposes. Always disable Developer Mode for normal budget operations.
</Warning>

## 🛠️ Developer Menu Overview

The Developer menu provides access to advanced system tools, debugging utilities, and legacy functions. It's organized into several submenus for easy navigation:

- **Dev Mode** - Developer mode controls
- **System Status** - System configuration management  
- **Triggers** - Google Apps Script trigger management
- **Integrity Checker** - System validation and repair tools
- **Testing Tools** - Development testing utilities
- **Debug Tools** - Diagnostic and debugging functions
- **Legacy** - Legacy system tools and advanced testing

## 🔧 Dev Mode Controls

<AccordionGroup>
  <Accordion title="Check Dev Mode Status" icon="info">
    - **Function:** `checkDevMode()`

    
    - **Purpose:** Display current developer mode status

    
    - **When to Use:** Verify if developer mode is active

    
    - **Output:** Shows current DEV_MODE property value

    
    - **Dependencies:** None

  </Accordion>

  <Accordion title="Enable Dev Mode" icon="toggle-on">
    - **Function:** `enableDevMode()`

    
    - **Purpose:** Turn on developer mode

    
    - **When to Use:** When you need access to developer tools

    
    - **Effect:** Enables all developer menu functions

    
    - **Dependencies:** Script properties access

  </Accordion>

  <Accordion title="Disable Dev Mode" icon="toggle-off">
    - **Function:** `disableDevMode()`

    
    - **Purpose:** Turn off developer mode

    
    - **When to Use:** After completing development work

    
    - **Effect:** Disables developer menu access

    
    - **Dependencies:** Script properties access

  </Accordion>
</AccordionGroup>

## 📊 System Status

<AccordionGroup>
  <Accordion title="Check Master Status" icon="info-circle">
    - **Function:** `checkMasterStatus()`

    - **Purpose:** Verify if current spreadsheet is the master

    - **When to Use:** Before performing master-only operations

    - **Output:** Shows IS_MASTER property and related status

    - **Dependencies:** Script properties access

  </Accordion>

  <Accordion title="Set as Master Spreadsheet" icon="crown">
    - **Function:** `setAsMaster()`

    - **Purpose:** Mark current spreadsheet as the master

    - **When to Use:** When setting up a new master spreadsheet

    - **Effect:** Sets IS_MASTER property to true

    - **Dependencies:** Script properties access

    - **Warning:** Only use on the intended master spreadsheet

  </Accordion>
</AccordionGroup>

## ⚙️ Triggers

<AccordionGroup>
  <Accordion title="Install onEdit Trigger" icon="plus">
    - **Function:** `installOnEditTrigger()`

    - **Purpose:** Set up automatic edit detection

    - **When to Use:** When automatic processing is needed

    - **Effect:** Creates onEdit trigger for automatic processing

    - **Dependencies:** Trigger creation permissions

  </Accordion>

  <Accordion title="Remove onEdit Trigger" icon="minus">
    - **Function:** `removeOnEditTrigger()`

    - **Purpose:** Remove automatic edit detection

    - **When to Use:** When automatic processing is not needed

    - **Effect:** Deletes existing onEdit trigger

    - **Dependencies:** Trigger management permissions

  </Accordion>
</AccordionGroup>

## 🛡️ Integrity Checker

<AccordionGroup>
  <Accordion title="Run Comprehensive Check" icon="shield-check">
    - **Function:** `runComprehensiveIntegrityCheck()`

    - **Purpose:** Full system validation and health check

    - **When to Use:** When investigating system issues or before major changes

    - **Output:** Detailed report of system integrity status

    - **Dependencies:** Access to all system sheets

    - **Duration:** May take several minutes for large datasets

  </Accordion>

  <Accordion title="Quick Integrity Check" icon="bolt">
    - **Function:** `quickIntegrityCheck()`

    - **Purpose:** Fast validation check for common issues

    - **When to Use:** Regular system health monitoring

    - **Output:** Quick summary of critical issues

    - **Dependencies:** Basic sheet access

    - **Duration:** Usually completes in under 30 seconds

  </Accordion>

  <Accordion title="Fix Corrupted Formulas" icon="wrench">
    - **Function:** `fixCorruptedFormulas()`

    - **Purpose:** Repair broken or corrupted formulas

    - **When to Use:** When formulas are not calculating correctly

    - **Effect:** Attempts to repair identified formula issues

    - **Dependencies:** Write access to sheets with formulas

    - **Warning:** Creates backup before making changes

  </Accordion>
</AccordionGroup>

## 🧪 Testing Tools

<AccordionGroup>
  <Accordion title="Reset Month Statuses" icon="refresh">
    - **Function:** `resetMonthStatuses()`

    - **Purpose:** Reset month processing statuses

    - **When to Use:** When month statuses are corrupted or incorrect

    - **Effect:** Resets all month status flags to default state

    - **Dependencies:** Write access to month status ranges

    - **Warning:** May affect month processing workflow

  </Accordion>

  <Accordion title="Validate Script Properties" icon="check-double">
    - **Function:** `validateScriptProperties()`

    - **Purpose:** Check script properties for consistency

    - **When to Use:** When system behavior is unexpected

    - **Output:** Report of script properties and their values

    - **Dependencies:** Script properties access

  </Accordion>
</AccordionGroup>

## 🐛 Debug Tools

<AccordionGroup>
  <Accordion title="Named Ranges Report" icon="list">
    - **Function:** `verifyNamedRanges()`

    - **Purpose:** Check spreadsheet named ranges

    - **When to Use:** When named ranges are not working correctly

    - **Output:** Complete list of all named ranges and their status

    - **Dependencies:** Named ranges access

  </Accordion>

  <Accordion title="View Stored Mappings" icon="eye">
    - **Function:** `viewStoredMappings()`

    - **Purpose:** Check stored bank configurations

    - **When to Use:** When import mappings are not working

    - **Output:** Display of all stored bank import mappings

    - **Dependencies:** Stored mappings access

  </Accordion>

  <Accordion title="Import History" icon="history">
    - **Function:** `showImportHistory()`

    - **Purpose:** View transaction import history

    - **When to Use:** When investigating import issues

    - **Output:** List of recent imports with timestamps and details

    - **Dependencies:** Import history data access

  </Accordion>

  <Accordion title="Re-sync ACTIVE Flags" icon="sync">
    - **Function:** `cleanupActiveFlagInconsistencies()`

    - **Purpose:** Manually sync category active status

    - **When to Use:** When ACTIVE flags are out of sync

    - **Effect:** Synchronizes ACTIVE flags across all categories

    - **Dependencies:** Category data access

  </Accordion>

  <Accordion title="Debug Income Budget Status" icon="chart-line">
    - **Function:** `debugIncomeBudgetStatus()`

    - **Purpose:** Debug income budget calculations

    - **When to Use:** When income budget calculations are incorrect

    - **Output:** Detailed analysis of income budget status

    - **Dependencies:** Income budget data access

  </Accordion>
</AccordionGroup>

## 🏛️ Legacy Menu

The Legacy menu contains advanced developer tools and legacy system functions organized into specialized submenus.

### Legacy System Cleanup

<AccordionGroup>
  <Accordion title="Find Legacy Named Ranges" icon="search">
    - **Function:** `findLegacyNamedRanges()`

    - **Purpose:** Identify legacy named ranges from old system

    - **When to Use:** During system cleanup or migration

    - **Output:** List of legacy named ranges that can be removed

    - **Dependencies:** Named ranges access

  </Accordion>

  <Accordion title="Get Cleanup Instructions" icon="list-alt">
    - **Function:** `getLegacyCleanupInstructions()`

    - **Purpose:** Get step-by-step cleanup instructions

    - **When to Use:** When removing legacy system components

    - **Output:** Detailed instructions for legacy system removal

    - **Dependencies:** None

  </Accordion>

</AccordionGroup>

### Cross-Year Detection

<AccordionGroup>
  <Accordion title="Test Cross-Year Detection" icon="flask">
    - **Function:** `testCrossYearDetection()`

    - **Purpose:** Test cross-year duplicate detection system

    - **When to Use:** When testing or debugging cross-year functionality

    - **Output:** Test results and diagnostic information

    - **Dependencies:** Cross-year detection system

  </Accordion>

  <Accordion title="Quick Diagnose Cross-Year" icon="stethoscope">
    - **Function:** `quickDiagnoseCrossYearIssue()`

    - **Purpose:** Quick diagnostic for cross-year issues

    - **When to Use:** When cross-year detection is not working

    - **Output:** Quick diagnosis of cross-year detection problems

    - **Dependencies:** Cross-year detection system

  </Accordion>

  <Accordion title="Show Cross-Year Info" icon="info">
    - **Function:** `showCrossYearDetectionInfo()`

    - **Purpose:** Display cross-year detection information

    - **When to Use:** When understanding cross-year system status

    - **Output:** Information about cross-year detection configuration

    - **Dependencies:** Cross-year detection system

  </Accordion>


  <Accordion title="Debug Archive Detection" icon="search-plus">
    - **Function:** `debugArchiveFileDetection()`

    - **Purpose:** Debug archive file detection

    - **When to Use:** When archive file detection is failing

    - **Output:** Debug information about archive file detection

    - **Dependencies:** Archive system access

  </Accordion>

  <Accordion title="Create Missing Named Ranges" icon="wrench">
    - **Function:** `createMissingNamedRanges()`

    - **Purpose:** Create missing named ranges required by the system

    - **When to Use:** When functions fail due to missing named ranges

    - **Output:** Creates BudgetStartDate and other critical named ranges

    - **Dependencies:** Maintain Budget sheet access

  </Accordion>
</AccordionGroup>

### Advanced Testing

<AccordionGroup>



  <Accordion title="Test Integrity Checker" icon="flask">
    - **Function:** `testIntegrityChecker()`

    - **Purpose:** Test integrity checker functionality

    - **When to Use:** When testing integrity checker system

    - **Output:** Test results for integrity checker

    - **Dependencies:** Integrity checker system access

  </Accordion>

  <Accordion title="Test Commitment Validation" icon="flask">
    - **Function:** `testCommitmentValidation()`

    - **Purpose:** Test commitment validation system

    - **When to Use:** When testing commitment validation

    - **Output:** Test results for commitment validation

    - **Dependencies:** Commitment system access

  </Accordion>
</AccordionGroup>

### Debug & Diagnostics

<AccordionGroup>
  <Accordion title="Debug Template Check" icon="bug">
    - **Function:** `debugTemplateCheck()`

    - **Purpose:** Debug template checking functionality

    - **When to Use:** When template checking is not working

    - **Output:** Debug information about template checking

    - **Dependencies:** Template system access

  </Accordion>

  <Accordion title="Debug Template Comprehensive" icon="bug">
    - **Function:** `debugTemplateComprehensive()`

    - **Purpose:** Comprehensive template debugging

    - **When to Use:** When detailed template debugging is needed

    - **Output:** Comprehensive debug information about templates

    - **Dependencies:** Template system access

  </Accordion>

  <Accordion title="Debug Accounts" icon="bug">
    - **Function:** `debugAccounts()`

    - **Purpose:** Debug account mapping functionality

    - **When to Use:** When account mapping is not working

    - **Output:** Debug information about account mapping

    - **Dependencies:** Account mapping system access

  </Accordion>


  <Accordion title="Debug Annual Budget Categories" icon="bug">
    - **Function:** `debugAnnualBudgetCategories()`

    - **Purpose:** Debug Annual Budget categories

    - **When to Use:** When Annual Budget categories have issues

    - **Output:** Debug information about Annual Budget categories

    - **Dependencies:** Annual Budget access

  </Accordion>

</AccordionGroup>

### Performance Testing

<AccordionGroup>
  <Accordion title="Test Sheet Access Performance" icon="tachometer">
    - **Function:** `testSheetAccessPerformance()`

    - **Purpose:** Test sheet access performance and identify bottlenecks

    - **When to Use:** When investigating performance issues

    - **Output:** Detailed performance metrics for sheet access operations

    - **Dependencies:** Access to all system sheets

    - **Example Output:**
      ```
      Get spreadsheet: 1ms
      Get Cash Flow sheet: 457ms
      Get Cash Flow data range: 200ms
      Get Cash Flow values: 105ms
      Total Sheet Access Time: 1223ms
      ```
  </Accordion>

  <Accordion title="Test Reconciliation Updates" icon="tachometer">
    - **Function:** `testReconciliationDateUpdateDetailed()`

    - **Purpose:** Test reconciliation date update performance

    - **When to Use:** When reconciliation updates are slow

    - **Output:** Performance metrics for reconciliation updates

    - **Dependencies:** Reconciliation system access

  </Accordion>

  <Accordion title="Test Loan Participants" icon="tachometer">
    - **Function:** `testLoanParticipants()`

    - **Purpose:** Test loan participants loading performance

    - **When to Use:** When loan participant loading is slow

    - **Output:** Performance metrics for loan participant loading

    - **Dependencies:** Loan system access

  </Accordion>

  <Accordion title="Test Loan Categories" icon="tachometer">
    - **Function:** `testLoanCategories()`

    - **Purpose:** Test loan category handling performance

    - **When to Use:** When loan category operations are slow

    - **Output:** Performance metrics for loan category operations

    - **Dependencies:** Loan system access

  </Accordion>

</AccordionGroup>

## 🚨 Important Notes

### Developer Mode Safety

<Warning>
  **Critical Safety Warning:** Developer mode bypasses important safety checks and validation. Always disable Developer Mode when not actively developing or testing.
</Warning>

### Function Dependencies

Many developer functions require specific permissions and access levels:

- **Script Properties Access** - Required for most configuration functions
- **Sheet Write Access** - Required for repair and modification functions  
- **Trigger Management** - Required for trigger installation/removal
- **System Data Access** - Required for diagnostic and testing functions

### Performance Considerations

- **Large Dataset Impact** - Some functions may take several minutes on large datasets
- **Resource Usage** - Performance testing functions may consume significant resources
- **Concurrent Usage** - Avoid running multiple performance tests simultaneously

### Troubleshooting

If developer functions are not working:

1. **Check Developer Mode** - Ensure Developer Mode is enabled
2. **Verify Permissions** - Ensure you have necessary script permissions
3. **Check Dependencies** - Verify all required system components are available
4. **Review Console** - Check browser console for error messages
5. **Test Individually** - Run functions one at a time to isolate issues

## 📚 Related Documentation

- [Menu Reference](menu-reference.md) - Complete menu system overview
- [Troubleshooting Guide](troubleshooting/common-issues.md) - Common issues and solutions
- [EOY Developer Guide](yearly-tasks/end-of-year/developer-guide.md) - End of Year development
- [System Changelog](system/changelog.md) - System changes and updates
