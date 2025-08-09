---
title: 'Importing Bank Transactions'
description: 'How to import bank transactions with optimal timing for duplicate detection'
---

# Importing Bank Transactions

This guide covers how to import bank transactions from your financial institutions, with special emphasis on timing to prevent duplicate detection issues.

## Overview

Bank transaction importing is the foundation of effective budget reconciliation. **When you import matters as much as what you import** - banks can change transaction processing dates, affecting your reconciliation accuracy.

## Critical Timing Guidelines

### ⏰ **Timing Rules for Success**

<CardGroup cols={2}>
<Card title="Monthly Imports" icon="calendar-days">
**Import within 7 days of month-end**
- Prevents bank date advancement issues
- Enables cross-month duplicate detection
- Maintains historical data integrity
</Card>

<Card title="End-of-Year Imports" icon="calendar-year">
**Import July within 7 days of EOY completion**
- Critical for cross-year duplicate detection
- Prevents June→July transaction movement
- Maintains fiscal year boundary accuracy
</Card>
</CardGroup>

### 🚨 **Why Timing Matters**

Banks routinely advance transaction processing dates by 2-7 days after initial processing. This means:

- **June 30 transactions** may appear as **July 1-7 transactions** 
- **Month-end transactions** may appear in the **following month**
- **Historical bank balances** become incorrect if reconciliation is delayed
- **Cross-year duplicate detection** fails if import timing exceeds system windows

## Import Process

### Step 1: Download Bank Statements

1. **Log into your bank's website or app**
2. **Select the account** you want to import
3. **Choose date range** - typically one month at a time
4. **Download in CSV format** (preferred) or PDF if CSV unavailable
5. **Save to a known location** on your computer

<Note>
**File Format Priority:** Most banks offer multiple export formats. Always choose CSV over PDF when available - it imports more accurately and faster.
</Note>

### Step 2: Access Import Function

1. **Open your budget spreadsheet**
2. **Navigate to Budget → Import Bank Transactions**
3. **Select your bank template** or configure if first time
4. **Upload your downloaded file**

### Step 3: Configure Import Settings

**For First-Time Setup:**
1. **Map columns** - Tell system which columns contain dates, amounts, descriptions
2. **Set lookback days** - Usually 7 days for duplicate detection
3. **Configure account rules** - How to identify which account transactions belong to
4. **Save as template** - Reuse settings for future imports

**For Regular Imports:**
1. **Select saved template** for your bank
2. **Verify column mapping** (banks occasionally change formats)
3. **Proceed with import**

### Step 4: Review and Process

1. **Review potential duplicates** - System shows transactions that might already exist
2. **Verify new transactions** - Check amounts, dates, descriptions are correct
3. **Confirm account assignment** - Ensure transactions go to correct bank account
4. **Complete import** - Add transactions to your budget system

## Import Templates and Settings

### Lookback Days Configuration

**Default: 7 days** - Appropriate for most situations

- **Monthly reconciliation:** 7 days catches bank date advances
- **Delayed reconciliation:** Won't catch older duplicates (intentional safety feature)
- **Cross-year detection:** Automatically uses template settings

### Bank-Specific Templates

Save templates for each bank you use:
- **Column mappings** for your bank's CSV format
- **Account identification rules**
- **Default descriptions** for common transaction types
- **Lookback day preferences** 

### Account Rules

Configure how the system identifies which account transactions belong to:
- **Credit cards:** Often use ending digits (e.g., ending-1234)
- **Bank accounts:** May use full account number
- **Manual selection:** Choose account during import

## Best Practices

### 🎯 **Timing Best Practices**

<Check>**Import within 7 days** of transaction dates</Check>
<Check>**Complete EOY imports immediately** after fiscal year end</Check>
<Check>**Process month-end imports promptly** (within 1 week)</Check>
<Check>**Monitor for bank format changes** quarterly</Check>

### 🎯 **Data Quality Best Practices**

<Check>**Verify dates before importing** - Check for obvious errors</Check>
<Check>**Review amounts for reasonableness** - Catch decimal point errors</Check>
<Check>**Check descriptions for completeness** - Some banks truncate descriptions</Check>
<Check>**Confirm account assignments** - Ensure transactions go to correct accounts</Check>

### 🎯 **File Management Best Practices**

<Check>**Use consistent naming** - e.g., "NAB-Checking-2025-07.csv"</Check>
<Check>**Keep monthly exports organized** - Separate folders by year/month</Check>
<Check>**Archive import files** - Keep for audit trail and re-import if needed</Check>
<Check>**Delete temporary downloads** - Clean up download folder regularly</Check>

## Troubleshooting Common Issues

### ❌ **Import Fails or Maps Incorrectly**

**Solutions:**
1. **Check file format** - Ensure CSV not PDF
2. **Verify column mappings** - Bank may have changed format
3. **Clear stored mappings** - Start fresh if bank changed significantly
4. **Update template** - Save new configuration for future use

### ❌ **Too Many Duplicates Detected**

**Causes:**
- Importing overlapping date ranges
- Re-importing same file
- Bank file contains previously imported transactions

**Solutions:**
1. **Check date ranges** - Don't overlap with previous imports
2. **Review file contents** - Ensure new transactions only
3. **Use duplicate review** - System shows why it thinks transactions are duplicates

### ❌ **Missing Transactions**

**Causes:**
- Bank file doesn't contain all transactions
- Date range too narrow
- CSV export excluded some transaction types

**Solutions:**
1. **Verify date range** - Check if bank export covers full period
2. **Check account settings** - Some accounts exclude certain transaction types
3. **Download separate files** - Some banks separate credits and debits
4. **Manual entry backup** - Add missing transactions manually if needed

### ⚠️ **Cross-Year/Month Detection Not Working**

**Most Common Cause:** **Delayed import timing**

**Why This Happens:**
- System only detects cross-period duplicates within 7-day window
- Late imports assume it's not "first import" of new period
- Bank date advancement occurs between import and reconciliation

**Prevention:**
- **Import immediately** after period end
- **Complete EOY process promptly** 
- **Don't delay monthly reconciliation**

**Recovery:**
- **Manual comparison** - Visual check of period boundaries
- **Adjust bank balances** - Restore zero balance manually

## Integration with Reconciliation

### After Import: Next Steps

1. **Open Reconciliation Dashboard** - Budget → Reconciliation Dashboard
2. **Review auto-matches** - Verify system-suggested matches are correct
3. **Process unmatched transactions** - Categorize and assign to budget
4. **Complete reconciliation** - Match all transactions to achieve zero balance

### Reconciliation Timing

**Critical Window:** Complete reconciliation **within 7 days** of import to maintain data integrity and prevent bank date advancement issues from affecting your budget accuracy.

## Advanced Features

### Manual Transaction Entry

For banks that only provide PDF statements:
1. **Use Transaction Editor** - Budget → Edit Transaction
2. **Enter transactions individually** - Date, amount, description, account
3. **Categorize immediately** - Assign to budget categories
4. **No duplicate detection** - Manual entries skip duplicate checking

### Bulk Processing

For multiple accounts or months:
1. **Import each account separately** - Maintains clear audit trail
2. **Process chronologically** - Import older months first
3. **Reconcile between imports** - Don't accumulate unreconciled transactions
4. **Monitor system performance** - Large imports may take longer

<Warning>
**Bulk Import Limitation:** Cross-year detection expects "first import" to be small. Importing 70+ transactions at once may bypass detection even within the 7-day window.
</Warning>

## Next Steps

After successful import:
1. **[Reconcile transactions](reconciling.md)** - Match imports to budget categories
2. **[Run month-end process](../monthly-tasks/end-of-month.md)** - When all transactions reconciled
3. **[Update categories](../../system/changelog.md)** - Add new categories if needed

<Note>
Remember: **Import timing affects reconciliation accuracy.** The few minutes saved by delaying imports can cost hours of manual correction later.
</Note>
