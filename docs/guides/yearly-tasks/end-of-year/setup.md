---
title: 'EOY Budget Setup'
description: 'Simple step-by-step guide for the End of Year budget setup process'
---

# EOY Budget Setup

This guide provides simple, direct instructions for completing the End of Year (EOY) process to set up your new fiscal year budget.

<Warning>
**Timing:** The EOY process can only be started during June (the final month of the fiscal year). The system will block access during other months.
</Warning>

## Before You Start

### ✅ Prerequisites (Must Complete First)

1. **Current month must be June** - System automatically checks this
2. **All balances must be zero:**
   - **Banks sheet:** Cell C30 = $0.00
   - **Annual Budget sheet:** Cell B106 = $0.00
   - **Maintain Budget sheet:** Cell E120 = $0.00

<Warning>
**Critical:** If any balance is not zero, the EOY process will be blocked. Fix balance issues using the Reconciliation Dashboard before starting EOY.
</Warning>

## Step 1: Start EOY Process (Master Spreadsheet)

### 1.1 Export Properties
1. In your **master spreadsheet** (June only)
2. Go to **Period Processing** → **Start End of Year Process**
3. Click **Export Properties Now** when prompted
4. Wait for success confirmation

### 1.2 Create New Copy
1. Go to **File** → **Make a copy**
2. Name it "Budget-2025" (or your new year)
3. Choose destination folder
4. Click **Make a copy**
5. **Open the new copy**

## Step 2: Initial Setup (New Copy)

### 2.1 Run Initial Setup
1. In the **new copy**, go to **Period Processing** → **1. Run Initial EOY Setup**
2. **Complete authorization** when prompted (Google warnings are normal and safe)
3. Click **YES** to proceed with setup

### 2.1a Authorization Process (Important!)

When you run the initial setup, Google will ask you to authorize the scripts. **Don't worry - this is normal and safe!**

**What you'll see:**

1. **"Authorization Required" dialog appears**
   - Click **"Continue"** to proceed

2. **Google Account Selection**
   - Select your Google account (the same one you use for Google Sheets)

3. **⚠️ Scary-looking Security Warning** (This is normal!)
   - You'll see: **"Google hasn't verified this app"**
   - You'll see: **"The app is requesting access to sensitive info"**
   - **Don't panic!** This is Google's standard warning for ALL custom spreadsheet scripts

4. **Continue Despite Warning:**
   - Click **"Advanced"** (bottom left of the dialog)
   - Click **"Go to Budget App Scripts (unsafe)"** - *this is safe, just Google's standard warning*
   - **Check "Select all"** checkbox to grant required permissions
   - Click **"Continue"**

5. **Success Confirmation**
   - You'll see a success message
   - The setup process will continue automatically

<Warning>
**About the "Unsafe" Warning:** Google shows this warning for ALL custom spreadsheet scripts, not because there's actually a problem. The budget system is safe to authorize - it only accesses your budget spreadsheet data and nothing else.
</Warning>

<Tip>
If authorization fails, refresh the page and try again. The system includes retry logic for common authorization issues.
</Tip>

### 2.2 Configure New Year
1. **Budget Start Date:** Enter July 1, 2025
2. **Payment Dates:** Update your payment schedules for the new year
3. Click **Save Configuration**

### 2.3 Update Budget Amounts
1. **Income Section:** Update all income amounts for new year
2. **Expense Section:** Update all expense amounts for new year
3. **Ensure balance:** Cell E120 must show $0.00
4. Click **REFRESH** button at bottom of configuration

## Step 3: Continue Setup (New Copy)

### 3.1 Copy Balances and Clear Data
1. Go to **Period Processing** → **2. Continue EOY Setup**
2. Click **YES** to proceed
3. System automatically:
   - Copies bank balances to opening positions
   - Clears transaction sheets
   - Updates monthly headers

### 3.2 Run End of Month Process
1. Go to **Period Processing** → **Run End of Month Process**
2. **Commitment Validation Dialog** will appear if there are outstanding commitments:
   - **NO = Fix Now:** Address commitments before proceeding
   - **YES = Ignore:** Proceed with EOM despite outstanding commitments
3. Complete the final month processing for June
4. This transitions the system from June to July

## Step 4: Finalize Setup (New Copy)

### 4.1 Complete Finalization
1. Go to **Period Processing** → **3. Finalize EOY Setup**
2. Click **YES** to finalize
3. System automatically:
   - Marks this as the new master spreadsheet

### 4.2 Archive Legacy Master
1. **Go back to your original master spreadsheet**
2. Go to **Settings** → **⚠️ Advanced** → **Archive This Master**
3. This completes the EOY process

## What Happens Automatically

### ✅ System Handles These Tasks
- **Property transfer** from master to new copy
- **Bank balance copying** to opening positions
- **Transaction sheet clearing** (Cash Flow and Bank Records)
- **Monthly header updates** for new fiscal year
- **Menu system updates** to show normal operations

### 📋 You Must Do These Tasks
- **Update budget amounts** for income and expenses
- **Ensure budget balance** (Cell E120 = $0.00)
- **Archive the legacy master** manually

## After EOY Completion

### ✅ Your New System
- **New master spreadsheet** ready for July 2025 - June 2026
- **July set as current month**
- **All transaction sheets cleared** for fresh start
- **Budget amounts updated** for new fiscal year

### 📁 Your Archived System
- **Previous master archived** with clear naming
- **All historical data preserved**
- **Available for reference** but not for active use

## Troubleshooting

### ❌ "Balance Check Failed"
**Problem:** EOY process blocked due to non-zero balances
**Solution:**
1. Update bank balances to June 30 accuracy
2. Use Reconciliation Dashboard to fix transaction issues
3. Ensure all three balance cells show $0.00

### ❌ "Process Not Available"
**Problem:** EOY menu option not available
**Solution:** Wait until June - EOY only works in final fiscal month

### ❌ Authorization Warnings
**Problem:** Google shows scary "unsafe" warnings
**Solution:**
1. **Don't panic** - This is Google's standard warning for ALL custom scripts
2. Click **"Advanced"** (bottom left of warning dialog)
3. Click **"Go to Budget App Scripts (unsafe)"** - This is safe to do
4. **Check "Select all"** to grant required permissions
5. Click **"Allow"**

**If authorization fails:**
- Refresh the browser page
- Try the authorization process again
- Check that you're using the same Google account as your spreadsheet

### ❌ "End of Month Processing Required"
**Problem:** Finalization blocked
**Solution:** Run "Period Processing → Run End of Month Process" first to transition from June to July

### ❌ "Outstanding Commitments Warning"
**Problem:** Commitment validation dialog appears during EOM processing
**Solution:**
- **NO = Fix Now:** Address the listed commitments before proceeding
- **YES = Ignore:** Proceed with EOM despite outstanding commitments
- Use the Reconciliation Dashboard to identify and fix commitment issues

## Quick Reference

### Menu Flow
1. **Master (June):** Period Processing → Start End of Year Process
2. **New Copy:** Period Processing → 1. Run Initial EOY Setup
3. **New Copy:** Period Processing → 2. Continue EOY Setup
4. **New Copy:** Period Processing → Run End of Month Process
5. **New Copy:** Period Processing → 3. Finalize EOY Setup
6. **Master:** Settings → ⚠️ Advanced → Archive This Master

### Critical Cells
- **Banks balance:** C30 = $0.00
- **Annual Budget balance:** B106 = $0.00
- **Maintain Budget balance:** E120 = $0.00

### Key Dates
- **EOY Start:** June (final fiscal month)
- **New Year Start:** July 1, 2025
- **Fiscal Year:** July 2025 - June 2026

<Note>
The EOY process is designed to be completed in one session, but you can pause between steps if needed. The menu system will guide you to the next appropriate step.
</Note>