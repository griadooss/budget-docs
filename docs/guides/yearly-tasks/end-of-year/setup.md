---
title: 'EOY Budget Setup'
description: 'Step-by-step guide for the End of Year budget setup process'
---

# EOY Budget Setup

This guide gives direct, step-by-step instructions for completing the End of Year (EOY) process to set up your new fiscal year budget. The wording and menu paths below match exactly what you see on screen.

!!! warning "Timing"
    The EOY process can only be started during June (the final month of the fiscal year). The system will block access during other months.

## Before You Start

### ✅ Prerequisites (Must Complete First)

1. **Current month must be June** — the system checks this automatically.
2. **All balances must be zero:**
   - **Banks sheet:** "BOOKS BALANCED" indicator = $0.00
   - **Annual Budget sheet:** "BUDGET BALANCED" indicator = $0.00
   - **Maintain Budget sheet:** balance indicator = $0.00

!!! warning "Critical"
    If any balance is not zero, the EOY process is blocked — there is no "proceed anyway" option. Fix balance issues using the Reconciliation Dashboard before starting EOY.

!!! note "You may also see an \"EOY Warnings\" dialog"
    When you start EOY, if you have **outstanding informal loans** (a negative LOANS REGISTER balance) or **missed budgeted repayments (commitments)**, an **⚠️ EOY Warnings** dialog appears first. It offers two choices:

    - **Continue with EOY** — acknowledge the warnings and proceed
    - **Cancel & Address Issues** — stop and fix them first

    These are warnings, not blockers. (Note: because commitments are checked here at the start, they are **not** re-checked during the End of Month step later in the EOY flow.)

## Step 1: Start EOY Process (Master Spreadsheet)

### 1.1 Export Properties

1. In your **master spreadsheet** (June only), go to **Period Processing → End of Year → Start End of Year Process**.
2. If the **⚠️ EOY Warnings** dialog appears (see note above), choose **Continue with EOY** to proceed.
3. A **"Setting Up a New Budget"** instruction dialog opens. It lists the steps ahead and has buttons: **View Documentation**, **Print Instructions**, **Close**, and **Export Properties Now**.

    !!! tip
        Click **Print Instructions** if you'd like a paper copy of these steps to follow alongside the process.

4. Click **Export Properties Now**. This saves your critical settings to a hidden `_Properties` sheet that travels with the copy.
5. Wait for the **"✅ Properties Exported"** confirmation, then click **OK**.

### 1.2 Create the New Copy

1. Go to **File → Make a copy**.
2. In the **Copy document** dialog:
   - **Name** it `Budget-YYYY` (e.g. `Budget-2026`).
   - **Folder** defaults to **My Drive** — leave it there or choose another destination.
   - Tick **Share it with the same people** and **Copy comments** so nothing is lost in the new copy.
3. Click **Make a copy**.
4. **Open the new copy** — and make sure you are now working in the *new* spreadsheet, not the old master, for every step that follows.

## Step 2: Initial Setup (New Copy)

### 2.1 Run Initial EOY Setup

In the **new copy**, go to **Period Processing → End of Year Setup → 1. Run Initial EOY Setup**.

The first time you run anything in the copy, Google asks you to authorise the scripts. **This is normal and safe** — see [Authorising the new copy](#authorising-the-new-copy) below for the exact clicks.

After authorising, the setup runs through several dialogs:

1. **✅ Verification Passed** — confirms the required sheets, named ranges and lookups are present. Click **OK**.
2. **⚠️ Timezone Verification** — shows your current timezone (e.g. *Australia/Perth*). If correct, click **Yes**.
3. **🔄 New Year Budget Setup** — asks *"Ready to configure the new budget?"* and lists what it will do (import settings, set up the budget period, configure payment dates, guide you through the manual budget, and clear old transactions when complete). Click **Yes**.
4. **⚙️ Setup Progress** runs (importing properties, setting up configuration).
5. **✅ Properties Imported** — confirms the import and notes that this copy's `IS_MASTER` flag is set to **FALSE** until EOY is finalised. Click **OK**.
6. **📋 Next Step: Create New Budget** — on-screen instructions for building the new-year budget (covered in Step 3). Click **Got It!** (or **Print Instructions**).

### Authorising the new copy

When you first run the setup, Google walks you through authorisation. **Don't worry — this is normal and safe.**

1. **"Authorization required"** dialog appears — click **OK**.
2. **Choose your Google account** — the same one you use for the spreadsheet.
3. **"Google hasn't verified this app"** warning appears (this is expected for all custom spreadsheet scripts):
   - Click **Advanced** (bottom left).
   - Click **Go to Budget-YYYY-Scripts (unsafe)** — the script name matches your copy's name.
4. On the permissions screen, tick **Select all**, then click **Continue**.

!!! warning "About the \"unsafe\" wording"
    Despite the label, the app is **not** unsafe. Google shows this warning for every custom spreadsheet script that it hasn't formally verified — it isn't a sign of a problem. The budget system only accesses your own budget spreadsheet.

!!! tip
    If authorisation fails, refresh the page and try again — the system retries common authorisation issues automatically.

## Step 3: Build Your New-Year Budget (New Copy)

This is the manual heart of the process, done on the **Maintain Budget** sheet **before** you continue.

!!! danger "Do this BEFORE 'Continue EOY Setup'"
    The next step (Step 4) clears last year's **Actual** column on Maintain Budget. Once those actuals are gone you have nothing to size the new year against — so complete your budget here first.

On the **Maintain Budget** sheet:

1. In the **Budget Start Dates** table, set the new year's start dates in **Column F** — set the **Budget Start Date first**.
2. For each category, set its new **amount** and **frequency**, then **Distribute to Annual Budget** (tick the *Distribute* checkbox in Column H — *Press to Dist ALL* distributes everything).
3. To **add, delete, or re-map categories** for the new year, use **Period Processing → Maintain Budget → Maintain Categories**:
   - ➕ Add Category/Subcategory
   - 🗑️ Delete Category/Subcategory
   - 🏷️ Manage Category Lookups
   - 📋 **Step-by-Step Instructions** — *follow this guide when changing categories; the procedure must be followed in order to avoid problems.*
4. Ensure the **Maintain Budget** balance indicator reads **$0.00** before continuing.

!!! note "The Maintain Categories tools only appear during this window"
    During EOY setup the full **🏦 Budget** menu is hidden, so these category tools live under **Period Processing → Maintain Budget** instead. They are available from when the copy opens until you run **Continue EOY Setup**, after which they are removed automatically.

## Step 4: Continue Setup (New Copy)

### 4.1 Copy Balances and Clear Data

1. Go to **Period Processing → End of Year Setup → 2. Continue EOY Setup**.

    !!! warning "Start dates must be set first"
        If you haven't set the new year's start dates, this step is blocked with **"🛑 Set the New-Year Start Dates First"**. Set them on Maintain Budget (Step 3) and run Continue again.

2. At the **"🔄 Continue End of Year Setup"** confirmation — *"Ready to complete the EOY setup?"* — click **Yes**. The system then:
   - Copies current bank balances to opening positions
   - Clears the Cash Flow and Bank Records sheets
   - Updates the monthly headers for the new year
3. The menu refreshes: the **Maintain Categories** tools disappear and **Run End of Month Process** appears.

## Step 5: Run End of Month Process (New Copy)

1. Go to **Period Processing → Run End of Month Process**.
2. Complete the final month processing for June. This transitions the system from **June to July**.

!!! note "No commitment prompt here"
    During the EOY flow, the commitment check is **not** repeated at this step — it was already handled by the **EOY Warnings** dialog back at Step 1. (The "Fix Now / Ignore" commitment prompt only appears during a *normal* monthly End of Month run, not inside EOY.)

## Step 6: Finalize Setup (New Copy)

1. Go to **Period Processing → End of Year Setup → 3. Finalize EOY Setup**.

    !!! warning "End of Month must be done first"
        If you haven't run End of Month yet, finalisation is blocked with **"⚠️ End of Month Processing Required"** (the current month must be July). Run Step 5 first.

2. Click **Yes** to finalise. The system verifies all completion criteria and then marks this copy as the new **master** spreadsheet (`IS_MASTER = true`).
3. A completion dialog appears with your next step — archiving the old master (Step 7).

## Step 7: Archive the Old Master (Manual Step)

1. Go **back to your original master spreadsheet** (the one you copied from).
2. Go to **Settings → ⚠️ Advanced → Archive This Master**.
3. **Confirm** when prompted. The system renames the spreadsheet with an `_ARCHIVED_FY{year}` suffix and marks it archived. This completes the EOY process.

## What Happens Automatically

### ✅ The System Handles These

- **Property transfer** from master to new copy (export then import)
- **Bank balance copying** to opening positions
- **Transaction sheet clearing** (Cash Flow and Bank Records)
- **Monthly header updates** for the new fiscal year
- **Menu updates** as you progress through each stage

### 📋 You Must Do These

- **Build the new-year budget** — start dates, category amounts/frequencies, and Distribute to Annual Budget (Step 3)
- **Ensure the budget balances** (Maintain Budget indicator = $0.00)
- **Archive the old master** manually (Step 7)

## After EOY Completion

### ✅ Your New System

- **New master spreadsheet** ready for the new fiscal year (July–June)
- **July** set as the current month
- **All transaction sheets cleared** for a fresh start
- **Budget amounts updated** for the new year

### 📁 Your Archived System

- **Previous master archived** with a clear `_ARCHIVED_FY{year}` name
- **All historical data preserved** and available for reference, but not for active use

## Troubleshooting

### ❌ "Balance Check Failed"
**Problem:** EOY blocked due to non-zero balances.

**Solution:**

1. Update bank balances to 30 June accuracy.
2. Use the Reconciliation Dashboard to fix transaction issues.
3. Ensure all three balance indicators show $0.00.

### ❌ "Process Not Available"
**Problem:** The EOY menu option isn't available.
**Solution:** Wait until June — EOY only works in the final fiscal month.

### ❌ "🛑 Set the New-Year Start Dates First"
**Problem:** Continue EOY Setup is blocked.
**Solution:** On the Maintain Budget sheet, set the new year's start dates in Column F (Budget Start Date first), then run **2. Continue EOY Setup** again.

### ❌ Authorisation warning ("Google hasn't verified this app")
**Problem:** Google shows the "unsafe" warning.

**Solution:**

1. **Don't panic** — this is Google's standard warning for all custom scripts; the app is not actually unsafe.
2. Click **Advanced** (bottom left).
3. Click **Go to Budget-YYYY-Scripts (unsafe)**.
4. Tick **Select all**, then click **Continue**.

**If authorisation fails:** refresh the page, try again, and make sure you're using the same Google account as the spreadsheet.

### ❌ "End of Month Processing Required"
**Problem:** Finalisation is blocked.
**Solution:** Run **Period Processing → Run End of Month Process** first to transition from June to July.

## Quick Reference

### Menu Flow

1. **Master (June):** Period Processing → End of Year → Start End of Year Process
2. **New Copy:** Period Processing → End of Year Setup → 1. Run Initial EOY Setup
3. **New Copy:** *(build the budget on Maintain Budget — start dates, amounts, Distribute)*
4. **New Copy:** Period Processing → End of Year Setup → 2. Continue EOY Setup
5. **New Copy:** Period Processing → Run End of Month Process
6. **New Copy:** Period Processing → End of Year Setup → 3. Finalize EOY Setup
7. **Old Master:** Settings → ⚠️ Advanced → Archive This Master

### Critical Balance Indicators

- **Banks sheet:** "BOOKS BALANCED" indicator = $0.00
- **Annual Budget sheet:** "BUDGET BALANCED" indicator = $0.00
- **Maintain Budget sheet:** balance indicator = $0.00

### Key Dates

- **EOY Start:** June (final fiscal month)
- **New Year Start:** 1 July
- **Fiscal Year:** July–June

!!! note
    You don't have to complete EOY in one session — you can pause between steps. The menu adapts to show the next appropriate option at each stage.
