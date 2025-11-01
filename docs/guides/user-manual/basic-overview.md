---
title: 'Basic Overview'
description: 'Summary of daily tasks in the Budget System'
---

# Daily Operations

<Note>
  This is the basic operations you'll perform regularly in the Budget
  System. Master these for effective budget management.
</Note>

## Workflow

1. Download your bank statements (UBank, NAB, or other banks)
2. Import the bank statements using the Import Wizard
3. Reconcile transactions using the Reconciliation Dashboard
4. Add any missing income or cash expenses
5. Run the end of month process when ready

<Tip>
  **Best Practices:**
  
  - Import weekly to stay current
  - Always check for duplicates
  - Verify account mappings before import
  - Reconcile before month-end
</Tip>

## Importing Bank Statements

<AccordionGroup>
  <Accordion title="Import Bank Transactions" icon="file-import">
    <strong>Access:</strong> 🏦 Budget > Import Bank Transactions

    ### Method 1: Paste Data
    1. <strong>Create new sheet</strong> - Click the + button at the bottom
    2. <strong>Copy bank data</strong> - From your bank statement or exported file
    3. <strong>Paste into sheet</strong> - Include headers in the paste
    4. <strong>Select bank format</strong> - Choose your bank type (NAB, CommBank, etc.)
    5. <strong>Review column mapping</strong> - Verify date, amount, description columns
    6. <strong>Enter account balance</strong> - Manually enter the statement balance
    7. <strong>Set lookback days</strong> - Default 7 days for duplicate detection
    8. <strong>Click "Process Import"</strong> - Review results and handle duplicates

    ### Method 2: Manual Entry
    1. <strong>Switch to Manual tab</strong> - Click "Manual Entry" tab
    2. <strong>Add transactions</strong> - Fill in date, amount, description, account, type
    3. <strong>Click "Add Transaction"</strong> - Add to pending list
    4. <strong>Review pending list</strong> - Check all transactions before processing
    5. <strong>Click "Process All"</strong> - Import all manual transactions

    ### Duplicate Detection
    - System automatically checks for duplicates within lookback period
    - Review potential duplicates before importing
    - Choose to skip, import selected, or import all
  </Accordion>

  <Accordion title="Bank Format Support" icon="bank">
    <strong>Supported Formats:</strong>
    
    - <strong>NAB Credit Card:</strong> Date, Amount, Description, Card Number
    - <strong>NAB Bank Account:</strong> Date, Amount, Description, Account Number
    - <strong>CommBank:</strong> Transaction Date, Debit/Credit Amount, Description, Reference
    - <strong>Other Banks:</strong> Flexible format with date, amount, description

    <strong>Column Mapping:</strong>
    - System automatically detects common column patterns
    - Manual adjustment available if needed
    - Save mappings for future imports
  </Accordion>
</AccordionGroup>

## Transaction Reconciliation

<AccordionGroup>
  <Accordion title="Reconciliation Dashboard" icon="check-double">
    <strong>Access:</strong> 🏦 Budget > Reconciliation Dashboard

    ### Opening the Dashboard
    1. <strong>Click menu option</strong> - Opens side-by-side transaction view
    2. <strong>Review transactions</strong> - Cash Flow (left) vs Bank Records (right)
    3. <strong>Check auto-matches</strong> - Green highlighted transactions are auto-matched
    4. <strong>Handle unmatched</strong> - Review and categorize unmatched transactions

    ### Transaction Matching
    - <strong>Auto-matches:</strong> System matches by amount and date (green highlight)
    - <strong>Manual matches:</strong> Click "Find Match" for unmatched transactions
    - <strong>Split transactions:</strong> Blue highlighted groups for split transactions
    - <strong>Bulk reconciliation:</strong> Select multiple transactions for batch processing

    ### Category Assignment
    - <strong>Single transactions:</strong> Select category and subcategory
    - <strong>Split transactions:</strong> Divide amount across multiple categories
    - <strong>Description editing:</strong> Modify transaction descriptions
    - <strong>Account verification:</strong> Confirm correct account assignment
  </Accordion>

  <Accordion title="Reconciliation Process" icon="arrows-split-up-and-left">
    ### Step-by-Step Process
    
    1. <strong>Review auto-matches</strong> - Verify green highlighted transactions
    2. <strong>Reconcile matches</strong> - Click "Reconcile Match" for verified pairs
    3. <strong>Handle unmatched</strong> - Click "Add to Cash Flow" for bank-only transactions
    4. <strong>Categorize transactions</strong> - Assign categories and subcategories
    5. <strong>Process splits</strong> - Handle split transactions with multiple categories
    6. <strong>Verify balances</strong> - Ensure all transactions are accounted for
    7. <strong>Refresh dashboard</strong> - Click refresh to update status

    ### Split Transactions
    - <strong>Identify splits:</strong> Look for blue highlighted transaction groups
    - <strong>Click "Find Match"</strong> - Locate corresponding bank transaction
    - <strong>Divide amount:</strong> Split across multiple categories as needed
    - <strong>Verify total:</strong> Ensure split amounts equal bank transaction
    - <strong>Reconcile group:</strong> Click "Reconcile Match" for complete split
  </Accordion>
</AccordionGroup>

<Warning>Always reconcile before running month-end processes</Warning>

## Monthly Processing

<CardGroup cols={2}>
<Card title="Pre-Process Checklist" icon="list-check">
- All transactions categorized
- Splits balanced correctly
- Bank balances verified
- Budget variances reviewed
- Reconciliation complete
  </Card>

<Card title="Running Month-End" icon="calendar-check">
1. **Verify all reconciled** - Check reconciliation dashboard
2. **Run end-of-month** - 📅 Period Processing > Run End of Month Process
3. **Confirm month** - Verify correct month is being processed
4. **Review results** - Check copied values and formatting
5. **Address warnings** - Handle any balance issues
  </Card>
</CardGroup>

## Managing Categories

<Tabs>
  <Tab title="Using Categories">
    - Select from existing options in dropdowns
    - Use consistent category names
    - Check subcategory assignments
    - Verify active/inactive status
  </Tab>

  <Tab title="Managing Categories">
    - **Access:** ⚙️ Settings > Sheet Settings > Manage Categories
    - **Add categories:** Create new income/expense categories
    - **Edit categories:** Modify names and descriptions
    - **Toggle status:** Activate/deactivate categories
    - **Add subcategories:** Create detailed breakdowns
  </Tab>

  <Tab title="Category Organization">
    - Keep related items together
    - Use meaningful, consistent names
    - Maintain hierarchy (category > subcategory)
    - Regular cleanup of unused categories
  </Tab>
</Tabs>

## Settings and Configuration

<CardGroup cols={3}>
<Card title="Import Settings" icon="gear">
**Manage Import Templates**
- Configure bank formats
- Set account mappings
- Save column mappings
  </Card>

<Card title="Month Management" icon="calendar">
**End of Year Processing**
- Initialize month statuses (moved to Period Processing > End of Year)
- EOY setup and processing workflow
- Month tracking system setup
  </Card>

<Card title="Advanced Settings" icon="warning">
**Archive Master**
- Prepare for EOY process
- Backup current system
- Create new year setup
  </Card>
</CardGroup>

## Next Steps

<Check>Practice regular imports</Check>
<Check>Set up your preferred views</Check>
<Check>Review the [Troubleshooting Guide](../troubleshooting/common-issues.md)</Check>
<Check>Learn about [End of Year Process](../yearly-tasks/end-of-year/overview.md)</Check>