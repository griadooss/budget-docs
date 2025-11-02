---
title: 'Basic Overview'
description: 'Summary of daily tasks in the Budget System'
---

# Daily Operations

!!! note
    This is the basic operations you'll perform regularly in the Budget System. Master these for effective budget management.

## Workflow

1. Download your bank statements (UBank, NAB, or other banks)
2. Import the bank statements using the Import Wizard
3. Reconcile transactions using the Reconciliation Dashboard
4. Add any missing income or cash expenses
5. Run the end of month process when ready

!!! tip "Best Practices"
    - Import weekly to stay current
    - Always check for duplicates
    - Verify account mappings before import
    - Reconcile before month-end

## Importing Bank Statements

??? file-import "Import Bank Transactions"
    **Access:** 🏦 Budget > Import Bank Transactions

    ### Method 1: Paste Data

    - Create new sheet - Click the + button at the bottom
    - Copy bank data - From your bank statement or exported file
    - Paste into sheet - Include headers in the paste
    - Select bank format - Choose your bank type (NAB, CommBank, etc.)
    - Review column mapping - Verify date, amount, description columns
    - Enter account balance - Manually enter the statement balance
    - Set lookback days - Default 7 days for duplicate detection
    - Click "Process Import" - Review results and handle duplicates

    ### Method 2: Manual Entry

    - Switch to Manual tab - Click "Manual Entry" tab
    - Add transactions - Fill in date, amount, description, account, type
    - Click "Add Transaction" - Add to pending list
    - Review pending list - Check all transactions before processing
    - Click "Process All" - Import all manual transactions

    ### Duplicate Detection

    - System automatically checks for duplicates within lookback period
    - Review potential duplicates before importing
    - Choose to skip, import selected, or import all

??? bank "Bank Format Support"
    **Supported Formats:**

    - NAB Credit Card: Date, Amount, Description, Card Number
    - NAB Bank Account: Date, Amount, Description, Account Number
    - CommBank: Transaction Date, Debit/Credit Amount, Description, Reference
    - Other Banks: Flexible format with date, amount, description

    **Column Mapping:**

    - System automatically detects common column patterns
    - Manual adjustment available if needed
    - Save mappings for future imports

## Transaction Reconciliation

??? check-double "Reconciliation Dashboard"
    **Access:** 🏦 Budget > Reconciliation Dashboard

    ### Opening the Dashboard

    - Click menu option - Opens side-by-side transaction view
    - Review transactions - Cash Flow (left) vs Bank Records (right)
    - Check auto-matches - Green highlighted transactions are auto-matched
    - Handle unmatched - Review and categorize unmatched transactions

    ### Transaction Matching

    - Auto-matches: System matches by amount and date (green highlight)
    - Manual matches: Click "Find Match" for unmatched transactions
    - Split transactions: Blue highlighted groups for split transactions
    - Bulk reconciliation: Select multiple transactions for batch processing

    ### Category Assignment

    - Single transactions: Select category and subcategory
    - Split transactions: Divide amount across multiple categories
    - Description editing: Modify transaction descriptions
    - Account verification: Confirm correct account assignment

??? arrows-split-up-and-left "Reconciliation Process"
    ### Step-by-Step Process

    - Review auto-matches - Verify green highlighted transactions
    - Reconcile matches - Click "Reconcile Match" for verified pairs
    - Handle unmatched - Click "Add to Cash Flow" for bank-only transactions
    - Categorize transactions - Assign categories and subcategories
    - Process splits - Handle split transactions with multiple categories
    - Verify balances - Ensure all transactions are accounted for
    - Refresh dashboard - Click refresh to update status

    ### Split Transactions

    - Identify splits: Look for blue highlighted transaction groups
    - Click "Find Match" - Locate corresponding bank transaction
    - Divide amount: Split across multiple categories as needed
    - Verify total: Ensure split amounts equal bank transaction
    - Reconcile group: Click "Reconcile Match" for complete split

!!! warning
    Always reconcile before running month-end processes

## Monthly Processing

=== "Pre-Process Checklist"

    - All transactions categorized
    - Splits balanced correctly
    - Bank balances verified
    - Budget variances reviewed
    - Reconciliation complete

=== "Running Month-End"

    1. **Verify all reconciled** - Check reconciliation dashboard
    2. **Run end-of-month** - 📅 Period Processing > Run End of Month Process
    3. **Confirm month** - Verify correct month is being processed
    4. **Review results** - Check copied values and formatting
    5. **Address warnings** - Handle any balance issues

## Managing Categories

=== "Using Categories"
    - Select from existing options in dropdowns
    - Use consistent category names
    - Check subcategory assignments
    - Verify active/inactive status

=== "Managing Categories"
    - **Access:** ⚙️ Settings > Sheet Settings > Manage Categories
    - **Add categories:** Create new income/expense categories
    - **Edit categories:** Modify names and descriptions
    - **Toggle status:** Activate/deactivate categories
    - **Add subcategories:** Create detailed breakdowns

=== "Category Organization"
    - Keep related items together
    - Use meaningful, consistent names
    - Maintain hierarchy (category > subcategory)
    - Regular cleanup of unused categories

## Settings and Configuration

=== "Import Settings"

    **Manage Import Templates**

    - Configure bank formats
    - Set account mappings
    - Save column mappings

=== "Month Management"

    **End of Year Processing**

    - Initialize month statuses (moved to Period Processing > End of Year)
    - EOY setup and processing workflow
    - Month tracking system setup

=== "Advanced Settings"

    **Archive Master**

    - Prepare for EOY process
    - Backup current system
    - Create new year setup

## Next Steps

!!! tip "Next Steps"
    - Practice regular imports
    - Set up your preferred views
    - Review the [Troubleshooting Guide](../troubleshooting/common-issues.md)
    - Learn about [End of Year Process](../yearly-tasks/end-of-year/overview.md)