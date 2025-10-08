---
title: 'Menu Reference'
description: 'Complete guide to all menu functions in the Budget System'
---

# Menu Functions Reference

<Note>
  All budget functions are organized in the menu bar for easy access. This guide
  explains each menu and its functions as they currently exist in the system.
</Note>

## 🏦 Budget Menu

<AccordionGroup>
  <Accordion title="Import Bank Transactions" icon="file-import">
    - **Access:** Click "🏦 Budget > Import Bank Transactions"
    - **Purpose:** Import new transactions from bank statements
    - **Features:**
      - Paste data from bank statements
      - Manual transaction entry
      - Automatic duplicate detection
      - Column mapping for different bank formats
      - Account selection and mapping
      - Cross-year duplicate detection
  </Accordion>

  <Accordion title="Reconciliation Dashboard" icon="check-double">
    - **Access:** Click "🏦 Budget > Reconciliation Dashboard"
    - **Purpose:** Match and verify transactions
    - **Features:**
      - Side-by-side transaction comparison
      - Automatic transaction matching
      - Split transaction handling
      - Bulk reconciliation
      - Category assignment
      - Performance diagnostics
  </Accordion>

  <Accordion title="Maintain Budget Submenu" icon="wrench">
    - **Access:** Click "🏦 Budget > Maintain Budget"
    - **Purpose:** Manage budget categories and transactions
    - **Functions:**
      - **📋 Maintain Budget Guide:** Shows workflow for adding/removing categories
      - **➕ Add Category/Subcategory:** Add new budget items with proper setup
      - **🗑️ Delete Category/Subcategory:** Safely remove items with cleanup
      - **✏️ Edit Transaction:** Modify existing transactions
  </Accordion>
</AccordionGroup>

## 📅 Period Processing Menu

<AccordionGroup>
  <Accordion title="Run End of Month Process" icon="calendar-check">
    - **Access:** Click "📅 Period Processing > Run End of Month Process"
    - **Purpose:** Close the monthly books and prepare for next month
    - **Requirements:**
      - All transactions reconciled
      - Categories verified
      - Balances checked (with option to proceed anyway)
    - **What it does:**
      - Copies Actual values to next month
      - Updates month formatting
      - Updates month statuses
      - Hides EOM option after completion
      - Validates balance consistency
  </Accordion>

  <Accordion title="End of Year Submenu" icon="calendar-year">
    - **Access:** Click "📅 Period Processing > End of Year"
    - **Purpose:** Complete End of Year setup and processing workflow
    - **Functions:**
      - **Start End of Year Process:** Begin EOY process (master spreadsheets only)
      - **1. Run Initial EOY Setup:** First setup step
      - **2. Continue EOY Setup:** Second setup step  
      - **3. Finalize EOY Setup:** Final setup step
      - **Initialize Month Statuses:** Set up month tracking system
    - **Workflow:** Start EOY Process → Steps 1-3 → Initialize Month Statuses
    - **Note:** Only available during June or in new year copies
    - **Features:**
      - Strict balance checking (no override option)
      - Bank balance validation
      - Automatic master spreadsheet creation
      - Guided step-by-step process
  </Accordion>
</AccordionGroup>

## ⚙️ Settings Menu

<AccordionGroup>
  <Accordion title="Import Settings" icon="gear">
    - **Access:** Click "⚙️ Settings > Import Settings"
    - **Purpose:** Configure bank statement import formats
    - **Features:**
      - Manage import templates
      - Configure bank-specific column mappings
      - Set duplicate detection rules
      - Account selection and mapping
  </Accordion>

  <Accordion title="Sheet Settings" icon="table">
    - **Access:** Click "⚙️ Settings > Sheet Settings"
    - **Purpose:** Manage budget categories and distribution
    - **Features:**
      - **Manage Categories:** Add/edit income and expense categories
      - **Bulk Distribute Items:** Distribute budget values across months
      - **Sync ACTIVE Flags:** Synchronize category active status
      - **Validate ACTIVE Flags:** Check category status consistency
  </Accordion>

  <Accordion title="Month Management" icon="calendar">
    - **Access:** Click "⚙️ Settings > Month Management"
    - **Purpose:** Control month processing and status
    - **Features:**
      - **Note:** Month management functions have been moved to Period Processing > End of Year
      - **Initialize Month Statuses:** Now available in Period Processing > End of Year submenu
  </Accordion>

  <Accordion title="Advanced Settings" icon="warning">
    - **Access:** Click "⚙️ Settings > Advanced Settings"
    - **Purpose:** Master spreadsheet management
    - **Features:**
      - **Archive This Master:** Archive current master spreadsheet
      - **Note:** Only available in master spreadsheets
      - **Critical:** Prepares for EOY process
  </Accordion>
</AccordionGroup>

## 🛠️ Developer Menu (Dev Mode Only)

<AccordionGroup>
  <Accordion title="Dev Mode Controls" icon="code">
    - **Access:** Click "🛠️ Developer > Dev Mode"
    - **Purpose:** Enable/disable development mode
    - **Functions:**
      - **Check Dev Mode Status:** View current development mode status
      - **Enable Dev Mode:** Turn on development features
      - **Disable Dev Mode:** Turn off development features
    - **Note:** Required for accessing other developer tools
  </Accordion>

  <Accordion title="System Status" icon="info-circle">
    - **Access:** Click "🛠️ Developer > System Status"
    - **Purpose:** Check and manage system configuration
    - **Functions:**
      - **Check Master Status:** Verify master spreadsheet status
      - **Set as Master Spreadsheet:** Mark current spreadsheet as master
  </Accordion>

  <Accordion title="Trigger Management" icon="cog">
    - **Access:** Click "🛠️ Developer > Triggers"
    - **Purpose:** Manage Google Apps Script triggers
    - **Functions:**
      - **🔧 Install onEdit Trigger:** Set up automatic edit detection
      - **❌ Remove onEdit Trigger:** Remove automatic edit detection
    - **Note:** Triggers handle automatic processing
  </Accordion>

  <Accordion title="Integrity Checker" icon="shield-check">
    - **Access:** Click "🛠️ Developer > Integrity Checker"
    - **Purpose:** Validate system integrity and fix issues
    - **Functions:**
      - **Run Comprehensive Check:** Full system validation
      - **Quick Integrity Check:** Fast validation check
      - **Fix Corrupted Formulas:** Repair broken formulas
  </Accordion>

  <Accordion title="Debug Tools" icon="bug">
    - **Access:** Click "🛠️ Developer > Debug Tools"
    - **Purpose:** Diagnostic and debugging utilities
    - **Functions:**
      - **📊 Named Ranges Report:** Check spreadsheet named ranges
      - **👁️ View Stored Mappings:** Check stored bank configurations
      - **📜 Import History:** View transaction import history
      - **🔄 Re-sync ACTIVE Flags:** Manually sync category status
  </Accordion>
</AccordionGroup>

<Note>
  For detailed information about all Developer menu functions, see the [Developer Menu Reference](../system/developer-menu.md).
</Note>

## ℹ️ Help Menu

<AccordionGroup>
  <Accordion title="Documentation" icon="book">
    - **Access:** Click "ℹ️ Help > Online Documentation"
    - **Purpose:** Access comprehensive system documentation
    - **Features:**
      - Complete user manual
      - Troubleshooting guides
      - Development documentation
      - Best practices
  </Accordion>

  <Accordion title="System Information" icon="info">
    - **Access:** Click "ℹ️ Help > About (Version Info)"
    - **Purpose:** Check system version and status
    - **Features:**
      - Current version information
      - System configuration details
      - Update status
  </Accordion>

  <Accordion title="Developer Mode Toggle" icon="code">
    - **Access:** Click "ℹ️ Help > Toggle Developer Mode"
    - **Purpose:** Switch between user and developer modes
    - **Note:** Enables/disables developer menu access
  </Accordion>
</AccordionGroup>

## Menu States

<CardGroup cols={2}>
<Card title="Normal Operations" icon="check">
- All standard menus visible
- Full user functionality
- Maintain Budget submenu available
- Standard workflow processes
  </Card>

<Card title="EOY Setup Mode" icon="calendar-year">
- Period Processing shows EOY steps
- Limited functionality during setup
- Guided setup process
- Strict balance checking
  </Card>

<Card title="Archived Mode" icon="archive">
- Minimal menu options
- Restore functionality only
- Read-only access
- No editing capabilities
  </Card>

<Card title="Developer Mode" icon="code">
- Additional debug tools
- Advanced diagnostics
- Trigger management
- Integrity checking tools
  </Card>
</CardGroup>

## Important Workflow Notes

<Warning>
**Critical:** Always use menu functions for category management. Manual deletion from sheets can cause balance inconsistencies.
</Warning>

<Note>
**ACTIVE Flag System:** Category active status is automatically managed. Use "Re-sync ACTIVE Flags" in Developer menu if needed.
</Note>

<Info>
**Balance Checking:** The system validates balances before critical operations. EOY processes require zero balance with no override option.
</Info>

## Best Practices

<Check>Always use "Delete Category/Subcategory" from Maintain Budget menu</Check>
<Check>Use "Add Category/Subcategory" for proper setup</Check>
<Check>Check balance indicators before running EOY processes</Check>
<Check>Review warning messages carefully</Check>
<Check>Use Developer menu tools for troubleshooting</Check>
<Warning>Don't manually delete rows from Annual Budget or Maintain Budget sheets</Warning>
<Warning>Don't modify sheet structure manually</Warning>
<Warning>Developer menu only appears when DEV_MODE is enabled</Warning>