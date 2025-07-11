---
title: 'Menu Reference'
description: 'Guide to all menu functions in the Budget System'
---

# Menu Functions Reference

<Note>
  All budget functions are organized in the menu bar for easy access. This guide
  explains each menu and its functions.
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

  <Accordion title="Edit Transaction" icon="edit">
    - **Access:** Click "🏦 Budget > Edit Transaction"
    - **Purpose:** Modify existing transactions
    - **Features:**
      - Select transaction from Cash Flow sheet
      - Update categories and descriptions
      - Modify amounts and dates
      - Handle split transactions
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
      - Balances checked
    - **What it does:**
      - Copies Actual values to next month
      - Updates month formatting
      - Updates month statuses
      - Hides EOM option after completion
  </Accordion>

  <Accordion title="End of Year Setup" icon="calendar-year">
    - **Access:** Click "📅 Period Processing > End of Year Setup"
    - **Purpose:** Set up new fiscal year (only available in new copies)
    - **Steps:**
      1. Run Initial EOY Setup
      2. Continue EOY Setup
      3. Finalize EOY Setup
    - **Note:** Only available during June or in new year copies
  </Accordion>

  <Accordion title="Start End of Year Process" icon="calendar-year">
    - **Access:** Click "📅 Period Processing > Start End of Year Process"
    - **Purpose:** Begin EOY process (only available in master spreadsheets)
    - **Shows:** EOY instructions and setup guide
    - **Note:** Only available in master spreadsheets during June
  </Accordion>
</AccordionGroup>

## ⚙️ Settings Menu

<AccordionGroup>
  <Accordion title="Import Settings" icon="gear">
    - **Manage Import Templates:** Configure bank statement import formats
    - **Purpose:** Set up automatic column mapping for different banks
    - **Features:**
      - Save bank-specific templates
      - Configure account mappings
      - Set duplicate detection rules
  </Accordion>

  <Accordion title="Sheet Settings" icon="table">
    - **Manage Categories:** Add/edit income and expense categories
    - **Bulk Distribute Items:** Distribute budget values across months
    - **Sync ACTIVE Flags:** Synchronize category active status
    - **Validate ACTIVE Flags:** Check category status consistency
  </Accordion>

  <Accordion title="Month Management" icon="calendar">
    - **Set Current Month:** Manually set the current processing month
    - **Initialize Month Statuses:** Set up month tracking system
  </Accordion>

  <Accordion title="Advanced Settings" icon="warning">
    - **Archive This Master:** Archive current master spreadsheet
    - **Purpose:** Prepare for EOY process
    - **Note:** Only available in master spreadsheets
  </Accordion>
</AccordionGroup>

## 🛠️ Developer Menu (Dev Mode Only)

<AccordionGroup>
  <Accordion title="Testing Tools" icon="flask">
    - **Test Distribute:** Test budget distribution functionality
    - **Test EOY Process:** Test end-of-year process
    - **Clear Test Sheet:** Reset test environment
    - **Reset Month Statuses:** Reset month tracking
    - **Test ACTIVE Flag System:** Test category status system
  </Accordion>

  <Accordion title="Debug Tools" icon="bug">
    - **Check Master Status:** Verify master spreadsheet status
    - **Set as Master Spreadsheet:** Mark as master
    - **Dev Mode Controls:** Enable/disable development mode
    - **View Bank Mappings:** Check stored bank configurations
    - **Export/Import Properties:** Backup/restore settings
  </Accordion>

  <Accordion title="Cross-Year Detection" icon="calendar-year">
    - **Cross-Year Detection Info:** View detection system details
    - **Quick Diagnose Cross-Year Issue:** Troubleshoot year transitions
    - **Test Cross-Year Detection:** Test year boundary detection
    - **Find & Move Archived Masters:** Locate archived spreadsheets
  </Accordion>

  <Accordion title="Advanced Tools" icon="wrench">
    - **Scan Codebase:** Analyze code structure
    - **Reconciliation Diagnostics:** Test reconciliation system
    - **Setup Auto ACTIVE Sync:** Configure automatic synchronization
    - **View Named Ranges Report:** Check spreadsheet named ranges
  </Accordion>
</AccordionGroup>

## ℹ️ Help Menu

<AccordionGroup>
  <Accordion title="Documentation" icon="book">
    - **User Manual:** Access this documentation
    - **Online Documentation:** Open web-based help
  </Accordion>

  <Accordion title="System Information" icon="info">
    - **About (Version Info):** Check current version and updates
    - **Toggle Developer Mode:** Switch between user and developer modes
  </Accordion>
</AccordionGroup>

## Menu States

<CardGroup cols={2}>
<Card title="Normal Operations" icon="check">
- All menus visible
- Standard functionality
- User-friendly interface
  </Card>

<Card title="EOY Setup Mode" icon="calendar-year">
- Period Processing shows EOY steps
- Limited functionality
- Guided setup process
  </Card>

<Card title="Archived Mode" icon="archive">
- Minimal menu options
- Restore functionality
- Read-only access
  </Card>

<Card title="Developer Mode" icon="code">
- Additional debug tools
- Testing capabilities
- Advanced diagnostics
  </Card>
</CardGroup>

## Best Practices

<Check>Always use menu functions instead of direct sheet edits</Check>
<Check>Check the status bar for processing feedback</Check>
<Check>Review any warning messages carefully</Check>
<Warning>Don't modify sheet structure manually</Warning>
<Warning>Developer menu only appears in development mode</Warning>