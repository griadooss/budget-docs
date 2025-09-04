---
title: 'Basic Operations'
description: 'Core processes and daily tasks in the Budget System'
---

# Basic Operations

<Note>
  These are the fundamental operations you'll perform regularly in the Budget
  System. Master these for effective budget management. Updated to reflect current system implementation.
</Note>

## Importing Transactions

<Steps>
  1. **Download your bank statement** (CSV format preferred)
  2. **Open the Import Wizard** - Click "🏦 Budget > Import Bank Transactions"
  3. **Select your bank's format** - Choose from available templates
  4. **Map Columns** (if needed) - Match bank columns to system fields
  5. **Review & Import** - Check for duplicates and verify amounts
  6. **Confirm import** - System will show import summary
</Steps>

<Tip>
  **Best Practices:**
  - Import weekly to stay current
  - Always check for duplicates (system has automatic detection)
  - Verify account mappings before import
  - Use cross-year duplicate detection for year-end imports
</Tip>

## Transaction Reconciliation

<AccordionGroup>
  <Accordion title="Opening the Dashboard" icon="rectangle-list">
    1. Click "🏦 Budget > Reconciliation Dashboard"
    2. Review unreconciled transactions
    3. Sort by date if needed
    4. Use filters to focus on specific accounts or date ranges
  </Accordion>

  <Accordion title="Reconciliation Steps" icon="check-double">
    For each transaction:
    - Match to bank record
    - Verify category/subcategory assignment
    - Check split transactions
    - Mark as reconciled when complete
    - Use bulk reconciliation for multiple items
  </Accordion>

  <Accordion title="Split Transactions" icon="arrows-split-up-and-left">
    1. Select transaction to split
    2. Enter split amounts
    3. Assign categories to each part
    4. Verify total matches original amount
    5. Save split configuration
  </Accordion>
</AccordionGroup>

<Warning>Always reconcile before running month-end processes. Unreconciled transactions can cause balance issues.</Warning>

## Monthly Processing

<CardGroup cols={2}>
<Card title="Pre-Process Checklist" icon="list-check">
- All transactions categorized and reconciled
- Splits balanced correctly
- Bank balances verified and current
- Budget variances reviewed
- Balance indicators checked
  </Card>

<Card title="Running Month-End" icon="calendar-check">
1. Verify all transactions reconciled
2. Check balance indicators
3. Run "📅 Period Processing > Run End of Month Process"
4. Review summary and address any warnings
5. System will hide EOM option after completion
  </Card>
</CardGroup>

<Note>
**Balance Checking:** The system will check balances before processing. You can proceed with warnings for monthly processing, but EOY processes require zero balance.
</Note>

## Managing Categories

<Tabs>
  <Tab title="Adding Categories">
    **Use the proper workflow:**
    1. Go to "🏦 Budget > Maintain Budget > ➕ Add Category/Subcategory"
    2. Follow the guided workflow
    3. System will properly set up the item across all sheets
    4. ACTIVE flags will be automatically managed
    
    **Important:** Always use the menu function, not manual sheet editing.
  </Tab>

  <Tab title="Deleting Categories">
    **Critical - Use proper deletion process:**
    1. Go to "🏦 Budget > Maintain Budget > 🗑️ Delete Category/Subcategory"
    2. System will run safety checks
    3. Proper cleanup across all sheets
    4. ACTIVE flags updated automatically
    
    **Warning:** Never manually delete rows from sheets - this causes balance inconsistencies.
  </Tab>

  <Tab title="Category Status">
    **ACTIVE Flag System:**
    - Categories are automatically marked ACTIVE when budgeted
    - Status is synchronized across all sheets
    - Use "🔄 Re-sync ACTIVE Flags" in Developer menu if needed
    - System prevents deletion of items with reconciled transactions
  </Tab>
</Tabs>

<Warning>
**Critical:** Always use menu functions for category management. Manual sheet editing can cause serious balance inconsistencies.
</Warning>

## Budget Distribution

<AccordionGroup>
  <Accordion title="Individual Distribution" icon="arrow-right">
    1. Go to Maintain Budget sheet
    2. Set budget amount for item
    3. Click "Distribute" button
    4. System validates budget balance
    5. ACTIVE flags updated automatically
  </Accordion>

  <Accordion title="Bulk Distribution" icon="arrows-right">
    1. Use "⚙️ Settings > Sheet Settings > Bulk Distribute Items"
    2. System filters items with budget > 0
    3. Validates overall budget balance
    4. Distributes all eligible items
    5. ACTIVE flags synchronized
  </Accordion>
</AccordionGroup>

<Note>
**Balance Validation:** Distribution requires balanced budget (income = expenses). System will warn if unbalanced but allows override for individual distribution.
</Note>

## Next Steps

<Check>Practice regular imports and reconciliation</Check>
<Check>Use proper category management workflows</Check>
<Check>Understand balance checking requirements</Check>
<Check>Review the [Troubleshooting Guide](../troubleshooting/common-issues.md)</Check>
<Check>Familiarize yourself with [Menu Reference](menu-reference.md)</Check>