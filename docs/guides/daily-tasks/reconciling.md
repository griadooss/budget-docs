---
title: 'Reconciling Transactions'
description: 'How to reconcile transactions using the Reconciliation Dashboard'
---

# Reconciling Transactions

This guide covers how to use the Reconciliation Dashboard to match and verify transactions between your bank records and cash flow entries.

## Overview

Reconciliation is the process of matching transactions from your bank statements with entries in your cash flow sheet. The Reconciliation Dashboard provides a side-by-side view to help you identify and resolve discrepancies.

## Getting Started

### Prerequisites
- Transactions imported from bank statements
- Cash flow entries for income and expenses
- Categories set up in the system

### Access the Dashboard
1. Open your budget spreadsheet
2. Click **🏦 Budget > Reconciliation Dashboard**
3. The dashboard will open in a new window

## Dashboard Interface

### Layout
The dashboard displays two columns:

<CardGroup cols={2}>
<Card title="Cash Flow (Left)" icon="list">
- Your categorized transactions
- Income and expense entries
- Split transaction groups
- Unreconciled entries
  </Card>

<Card title="Bank Records (Right)" icon="bank">
- Imported bank transactions
- Unmatched bank entries
- Transaction details
- Account information
  </Card>
</CardGroup>

### Transaction Status Indicators

<CardGroup cols={3}>
<Card title="Green Highlight" icon="check">
**Auto-matched transactions**
- System matched by amount and date
- Ready for reconciliation
  </Card>

<Card title="Blue Highlight" icon="arrows-split">
**Split transaction groups**
- Multiple cash flow entries
- Match to single bank transaction
  </Card>

<Card title="No Highlight" icon="question">
**Unmatched transactions**
- Need manual processing
- Require categorization
  </Card>
</CardGroup>

## Reconciliation Process

### Step 1: Review Auto-Matches
1. **Identify green highlights** - These are automatically matched
2. **Verify details** - Check amount, date, and description
3. **Reconcile matches** - Click "Reconcile Match" for verified pairs

### Step 2: Handle Unmatched Transactions
1. **Review bank transactions** - Look for transactions without matches
2. **Click "Add to Cash Flow"** - For bank-only transactions
3. **Categorize transactions** - Assign categories and subcategories
4. **Add descriptions** - Modify transaction descriptions as needed

### Step 3: Process Split Transactions
1. **Identify blue highlights** - These are split transaction groups
2. **Click "Find Match"** - Locate corresponding bank transaction
3. **Verify split amounts** - Ensure total equals bank transaction
4. **Reconcile group** - Click "Reconcile Match" for complete split

### Step 4: Bulk Reconciliation
1. **Select multiple transactions** - Use checkboxes for batch processing
2. **Click "Bulk Reconcile"** - Process multiple pairs at once
3. **Review results** - Check for any failed reconciliations

## Transaction Types

### Single Transactions
- **Standard transactions** - One-to-one matching
- **Category assignment** - Select from dropdown menus
- **Description editing** - Modify transaction descriptions
- **Account verification** - Confirm correct account assignment

### Split Transactions
- **Multiple categories** - Divide amount across categories
- **Group identification** - Blue highlighted groups
- **Total verification** - Ensure split amounts equal bank transaction
- **Category assignment** - Assign categories to each split

### Manual Entries
- **Cash transactions** - Expenses paid in cash
- **Income entries** - Salary, gifts, or other income
- **Account reconciliation** - Verify against bank balance

## Category Assignment

### Selecting Categories
1. **Choose transaction type** - Income or Expense
2. **Select main category** - From dropdown menu
3. **Choose subcategory** - More specific classification
4. **Add description** - Modify transaction description

### Category Management
- **Active categories only** - Inactive categories are hidden
- **Consistent naming** - Use standard category names
- **Subcategory hierarchy** - Maintain category structure

## Advanced Features

### Search and Filter
- **Search transactions** - Find specific transactions
- **Filter by status** - Show reconciled/unreconciled
- **Filter by account** - Focus on specific accounts

### Performance Diagnostics
- **Run diagnostics** - Test system performance
- **Check data loading** - Verify transaction retrieval
- **Monitor processing** - Track reconciliation speed

### Refresh and Update
- **Refresh dashboard** - Update transaction status
- **Close dashboard** - Update reconciliation date
- **Auto-save** - Changes are saved automatically

## Troubleshooting

### Common Issues

<AccordionGroup>
  <Accordion title="Missing Transactions" icon="alert">
    **Problem:** Transactions not appearing in dashboard
    **Solution:**
    - Check if transactions are already reconciled
    - Verify import was successful
    - Refresh the dashboard
  </Accordion>

  <Accordion title="Wrong Matches" icon="x">
    **Problem:** Incorrect auto-matches
    **Solution:**
    - Manually reconcile correct pairs
    - Add missing transactions to cash flow
    - Review transaction dates and amounts
  </Accordion>

  <Accordion title="Split Transaction Issues" icon="arrows-split">
    **Problem:** Split amounts don't match
    **Solution:**
    - Verify split total equals bank transaction
    - Check for rounding errors
    - Review individual split amounts
  </Accordion>

  <Accordion title="Performance Issues" icon="clock">
    **Problem:** Dashboard is slow
    **Solution:**
    - Run performance diagnostics
    - Check transaction count
    - Consider processing in smaller batches
  </Accordion>
</AccordionGroup>

## Best Practices

<Check>Reconcile regularly (weekly recommended)</Check>
<Check>Verify all auto-matches before reconciling</Check>
<Check>Use consistent category names</Check>
<Check>Review split transactions carefully</Check>
<Check>Keep descriptions clear and consistent</Check>
<Check>Refresh dashboard after major changes</Check>

## Completion Checklist

Before closing the dashboard:
- [ ] All auto-matches reviewed and reconciled
- [ ] Unmatched transactions categorized
- [ ] Split transactions verified and reconciled
- [ ] All bank transactions accounted for
- [ ] Cash flow entries complete
- [ ] Balances verified

## Next Steps

After reconciliation:
1. **Review balances** - Check account balances
2. **Run month-end process** - If all transactions reconciled
3. **Update categories** - Add new categories if needed
4. **Archive data** - Keep records for future reference

<Note>
  For month-end processing instructions, see the [Monthly Tasks Guide](../monthly-tasks/end-of-month.md).
</Note>