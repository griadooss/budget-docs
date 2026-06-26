---
title: 'Basic Operations'
description: 'Core processes and daily tasks in the Budget System'
---

# Basic Operations

!!! note
    These are the fundamental operations you'll perform regularly in the Budget System. Master these for effective budget management. Updated to reflect current system implementation.

## Importing Transactions

1. **Download your bank statement** (CSV format preferred)
2. **Open the Import Wizard** - Click "🏦 Budget > Import Bank Transactions"
3. **Select your bank's format** - Choose from available templates
4. **Map Columns** (if needed) - Match bank columns to system fields
5. **Review & Import** - Check for duplicates and verify amounts
6. **Confirm import** - System will show import summary

!!! tip "Best Practices"
    - Import weekly to stay current
    - Always check for duplicates (system has automatic detection)
    - Verify account mappings before import
    - Use cross-year duplicate detection for year-end imports

## Transaction Reconciliation

??? rectangle-list "Opening the Dashboard"
    1. Click "🏦 Budget > Reconciliation Dashboard"
    2. Review unreconciled transactions
    3. Sort by date if needed
    4. Use filters to focus on specific accounts or date ranges

??? check-double "Reconciliation Steps"
    For each transaction:
    - Match to bank record
    - Verify category/subcategory assignment
    - Check split transactions
    - Mark as reconciled when complete
    - Use bulk reconciliation for multiple items

??? arrows-split-up-and-left "Split Transactions"
    1. Select transaction to split
    2. Enter split amounts
    3. Assign categories to each part
    4. Verify total matches original amount
    5. Save split configuration

!!! warning
    Always reconcile before running month-end processes. Unreconciled transactions can cause balance issues.

## Monthly Processing

=== "Pre-Process Checklist"

    - All transactions categorized and reconciled
    - Splits balanced correctly
    - Bank balances verified and current
    - Budget variances reviewed
    - Balance indicators checked

=== "Running Month-End"

    1. Verify all transactions reconciled
    2. Check balance indicators
    3. Run "📅 Period Processing > Run End of Month Process"
    4. Review summary and address any warnings
    5. System will hide EOM option after completion

!!! note "Balance Checking"
    The system will check balances before processing. You can proceed with warnings for monthly processing, but EOY processes require zero balance.

## Managing Categories

=== "Adding Categories"

    **Use the proper workflow:**

    1. Go to "🏦 Budget > Maintain Budget > Maintain Categories > ➕ Add Category/Subcategory"
    2. Follow the guided workflow
    3. System will properly set up the item across all sheets
    4. ACTIVE flags will be automatically managed

    **Important:** Always use the menu function, not manual sheet editing.

=== "Deleting Categories"

    **Critical - Use proper deletion process:**

    1. Go to "🏦 Budget > Maintain Budget > Maintain Categories > 🗑️ Delete Category/Subcategory"
    2. System will run safety checks
    3. Proper cleanup across all sheets
    4. ACTIVE flags updated automatically

    **Warning:** Never manually delete rows from sheets - this causes balance inconsistencies.

=== "Category Status"

    **ACTIVE Flag System:**

    - An item is marked ACTIVE (and so appears in transaction dropdowns) only when it is **budgeted in Maintain Budget (amount > 0 and distributed) AND present in the Annual Budget**
    - Zeroing an item's budget for the year therefore makes it inactive — it leaves the dropdowns but the category stays in LookUps, ready to re-budget any year
    - Status is synchronised automatically and re-synced every time the spreadsheet opens
    - To check or force it, use **Sync ACTIVE Flags** / **Validate ACTIVE Flags** under Settings > LookUps Sheet
    - System prevents deletion of items with reconciled transactions

!!! warning "Critical"
    Always use menu functions for category management. Manual sheet editing can cause serious balance inconsistencies.

## Budget Distribution

Distribution spreads each **Maintain Budget** item across the months of the
financial year on the **Annual Budget** sheet.

??? arrow-right "Individual Distribution"
    1. Go to the **Maintain Budget** sheet
    2. Set the item's **Budget** (Col E) and **Freq** (Col F — how many times a year)
    3. *(Optional)* set the **Start Mth** (Col J — the month the first payment falls)
    4. **Tick the Column-H checkbox** ("Tick to Dist Single Items")
    5. The row flags **red** while it posts, then **green** when done
    6. System validates budget balance; ACTIVE flags update automatically

??? arrows-right "Bulk Distribution"
    1. Press the **"Press to Dist ALL"** button (Column I header)
    2. Confirm the prompt — it distributes every eligible item in one pass
    3. A progress toast shows where it's up to
    4. A summary reports distributed / created / skipped counts; ACTIVE flags sync

!!! tip "Start Month (Col J)"
    For non-monthly items you can choose when the spread begins — e.g. a quarterly
    item (**Freq 3**) starting **August** lands on **Aug, Dec, Apr**. Leave it
    **blank for July** (the default, unchanged behaviour). The dropdown only offers
    the months that make a difference for that frequency; **monthly (Freq 12)** and
    **weekly/fortnightly (26/52)** rows show **"—"** because there's no per-row choice
    (26/52 are driven by the "Budget Start Dates" config table). Changing a Start Mth
    re-flags the item for re-distribution.

!!! note "Balance Validation"
    Distribution requires a balanced budget (income = expenses). The system warns if
    unbalanced but allows an override for individual distribution.

!!! info "Zero-budget items"
    You **can** distribute an item whose budget is **\$0** (only a negative budget is
    blocked). It simply spreads zeros, so the item keeps a row in the Annual Budget with
    a **\$0** total — handy for a category you're not funding this year but want to keep in
    place. A \$0 item does not unbalance anything (0 = 0), and it is automatically made
    **inactive** (it leaves the transaction dropdowns) until you give it a budget again.

### Finding an out-of-balance Annual Budget

If the **Annual Budget** ever shows a non-zero balance — most often after you've
hand-edited a monthly figure to match an uneven real-world payment and slipped — use
**🏦 Budget > Maintain Budget > ⚖️ Check Annual Budget Balance**.

It's **read-only** and pinpoints the problem instead of making you hunt:

- It lists every item whose distributed total (Annual Budget) doesn't match its budget
  (Maintain Budget), with the exact **dollar amount it's off by**.
- For non-monthly items it also names a **mis-placed payment month** — a value sitting in
  a month that should be empty, or a month that should hold a payment but is blank.
- An intentional **unequal** spread that still adds up correctly is never flagged.

From there you can correct the cell by eye, re-tick the row's checkbox to re-distribute
just that item, or — only as a last resort — re-distribute everything.

## Next Steps

!!! tip "Next Steps"
    - Practice regular imports and reconciliation
    - Use proper category management workflows
    - Understand balance checking requirements
    - Review the [Troubleshooting Guide](../troubleshooting/common-issues.md)
    - Familiarize yourself with [Menu Reference](menu-reference.md)