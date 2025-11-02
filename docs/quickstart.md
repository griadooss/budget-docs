---
title: 'Quickstart Guide'
description: 'Get started with the Budget System quickly'
---

# Quickstart Guide

Welcome to the Budget System! This guide will help you get started with the basic operations you'll use regularly.

## First Steps

### 1. Access Your Budget Spreadsheet
- Open your Google Sheets budget spreadsheet
- Wait for the custom menus to load (🏦 Budget, 📅 Period Processing, etc.)
- Verify you can see the main menu options

### 2. Check System Status
- Look for the current month highlighted in blue
- Verify all sheets are accessible (Annual Budget, Cash Flow, Bank Records)
- Check that categories are set up in the LookUps sheet

## Daily Workflow

### Import Bank Transactions
1. **Download bank statements** - Get CSV or spreadsheet format
2. **Open Import Tool** - Click 🏦 Budget > Import Bank Transactions
3. **Choose method:**
   - **Paste Data:** Copy/paste from bank statement
   - **Manual Entry:** Enter transactions manually
4. **Select bank format** - Choose your bank type
5. **Review column mapping** - Verify date, amount, description
6. **Process import** - Handle duplicates and review results

### Reconcile Transactions
1. **Open Dashboard** - Click 🏦 Budget > Reconciliation Dashboard
2. **Review auto-matches** - Green highlighted transactions
3. **Handle unmatched** - Click "Add to Cash Flow" for bank-only transactions
4. **Categorize transactions** - Assign categories and subcategories
5. **Process splits** - Handle split transactions with multiple categories
6. **Verify completion** - Ensure all transactions reconciled

### Manage Categories
1. **Access Category Manager** - Click ⚙️ Settings > Sheet Settings > Manage Categories
2. **Add categories** - Create new income/expense categories
3. **Edit categories** - Modify names and descriptions
4. **Toggle status** - Activate/deactivate categories as needed
5. **Add subcategories** - Create detailed breakdowns

## Monthly Tasks

### End of Month Process
1. **Verify reconciliation** - Ensure all transactions reconciled
2. **Check balances** - Verify account and budget balances
3. **Run EOM process** - Click 📅 Period Processing > Run End of Month Process
4. **Confirm month** - Verify correct month is being processed
5. **Review results** - Check copied values and formatting

### Month Management
1. **Initialize statuses** - Click 📅 Period Processing > End of Year > Initialize Month Statuses
2. **Verify highlighting** - Check current month is highlighted in blue
3. **Note:** Month management functions moved to Period Processing > End of Year submenu

## Settings and Configuration

### Import Settings
1. **Manage templates** - Click ⚙️ Settings > Import Settings > Manage Import Templates
2. **Configure banks** - Set up column mappings for your banks
3. **Save mappings** - Store configurations for future imports

### Advanced Settings
1. **Archive master** - Click ⚙️ Settings > Advanced Settings > Archive This Master
2. **Sync categories** - Click ⚙️ Settings > Sheet Settings > Sync ACTIVE Flags
3. **Validate system** - Click ⚙️ Settings > Sheet Settings > Validate ACTIVE Flags

## End of Year Process

!!! warning "Important Annual Process"
    The End of Year (EOY) process is a critical annual procedure that must be completed in June to transition to the new fiscal year.

### When You Need EOY Setup
The EOY process is required when:
- **It's June** (final month of fiscal year) - System only allows access during June
- You've completed all reconciliation for the current fiscal year
- You're ready to set up the budget for the next financial year (July-June)

### EOY Process Overview
The modern EOY process is a **four-step guided workflow**:

1. **Initial Setup** (in master spreadsheet) - Export settings and create new copy
2. **Configuration & Budget Update** (in new copy) - Set up new year and update budget amounts
3. **Month Processing** (in new copy) - Run EOM to transition from June to July
4. **Finalization** (in new copy) - Complete setup and archive previous master

=== "EOY Overview"
    [Learn about the End of Year process](/guides/yearly-tasks/end-of-year/overview)

=== "EOY Setup"
    [Step-by-step EOY setup instructions](/guides/yearly-tasks/end-of-year/setup)

## Troubleshooting

### Common Issues

??? warning "Menus Not Loading"
    **Problem:** Custom menus not appearing

    **Solution:**

    - Refresh the page (Ctrl+F5)
    - Check script authorization
    - Verify spreadsheet access

??? danger "Import Errors"
    **Problem:** Can't import transactions

    **Solution:**

    - Check bank format selection
    - Verify column mapping
    - Review data format
    - Try manual entry method

??? warning "Reconciliation Issues"
    **Problem:** Dashboard not working

    **Solution:**

    - Refresh the dashboard
    - Check transaction data
    - Verify sheet access
    - Run performance diagnostics

??? calendar-check "EOM Process Errors"
    **Problem:** End of month process fails

    **Solution:**

    - Verify all transactions reconciled
    - Check current month setting
    - Review balance issues
    - Initialize month statuses

## Best Practices

!!! tip "Best Practices"
    - Import transactions weekly
    - Reconcile before month-end
    - Use consistent category names
    - Keep backup copies
    - Review balances regularly
    - Document any issues

## Next Steps

=== "Daily Tasks"
    [Learn about importing and reconciling](guides/daily-tasks/importing)

=== "Monthly Tasks"
    [Understand month-end processing](guides/monthly-tasks/end-of-month)

=== "Troubleshooting"
    [Get help with common issues](guides/troubleshooting/common-issues)

## Getting Help

- **Online Documentation:** Click ℹ️ Help > Online Documentation
- **Version Info:** Click ℹ️ Help > About (Version Info)
- **Developer Mode:** Click ℹ️ Help > Toggle Developer Mode (for advanced users)

!!! note
    For detailed instructions on any process, refer to the specific guides in the documentation.