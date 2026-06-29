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
4. **The new copy opens itself automatically** (in a new browser tab). Make sure you are now working in the *new* spreadsheet, not the old master, for every step that follows.

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
2. **"Google hasn't verified this app"** warning appears (this is expected for all custom spreadsheet scripts):
   - Click **Advanced** (bottom left).
   - Click **Go to Budget-YYYY-Scripts (unsafe)** — the script name matches your copy's name.
3. On the permissions screen, tick **Select all**, then click **Continue**.

!!! warning "About the \"unsafe\" wording"
    Despite the label, the app is **not** unsafe. Google shows this warning for every custom spreadsheet script that it hasn't formally verified — it isn't a sign of a problem. The budget system only accesses your own budget spreadsheet.

!!! tip
    If authorisation fails, refresh the page and try again — the system retries common authorisation issues automatically.

## Step 3: Build Your New-Year Budget (New Copy)

This is the manual heart of the process, done on the **Maintain Budget** sheet **before** you continue.

!!! danger "Do this BEFORE 'Continue EOY Setup'"
    The next step (Step 4) clears last year's **Actual** column on Maintain Budget. Once those actuals are gone you have nothing to size the new year against — so complete your budget here first.

On the **Maintain Budget** sheet:

1. In the **Budget Start Dates** table (Column F): the **Budget Start Date** has been **advanced for you automatically** to the new financial year, and each fortnightly/weekly source (Pension, Wages, etc.) has been **pre-filled with a suggested first pay-date**. **Check each against your latest bank statement** and adjust if needed. A valid date shows **green**; one that's out of range turns **red** — fix any red ones (see *Managing the Start Dates* below).
2. For each category, set its new **amount** and **frequency**, then **Distribute to Annual Budget** (tick the *Distribute* checkbox in Column H — *Press to Dist ALL* distributes everything).
3. To **add, delete, or re-map categories** for the new year, use **Period Processing → Maintain Budget → Maintain Categories**:
   - ➕ Add Category/Subcategory
   - 🗑️ Delete Category/Subcategory
   - 🏷️ Manage Category Lookups
   - 📋 **Step-by-Step Instructions** — *follow this guide when changing categories; the procedure must be followed in order to avoid problems.*
4. Ensure the **Maintain Budget** balance indicator reads **$0.00** before continuing.

!!! note "The Maintain Categories tools only appear during this window"
    During EOY setup the full **🏦 Budget** menu is hidden, so these category tools live under **Period Processing → Maintain Budget** instead. They are available from when the copy opens until you run **Continue EOY Setup**, after which they are removed automatically.

### Managing the Start Dates

The **Budget Start Dates** table (Column E = labels, Column F = dates) is the one genuinely delicate part of the whole EOY process — everything else is done for you by the script. Take a moment to understand it before you change anything.

!!! info "What the start dates are actually for"
    A start date only matters for an item paid **more often than monthly** — i.e. **fortnightly (26/year) or weekly (52/year)**. For those, the system needs the **first pay-date** so it can count how many pay-days fall in each month and spread the money correctly.

    Items paid **monthly or less often** (frequency 1, 2, 3, 4, 6 or 12) **do not use these dates at all** — they are spread evenly using the per-row **Start Mth (Column J)**.

!!! tip "Green means good — your at-a-glance check"
    Each fortnightly/weekly start date is **pre-filled with a suggestion** and **colour-coded live**: **green** = valid (its first pay-date falls within one pay-interval of the Budget Start Date), **red** = out of range or missing. Type a wrong date and the cell turns **red on the spot**, so typos are caught immediately. A "verify against your statement" note sits on each cell until you've addressed it (edit the date, or run Continue, and the note clears). **Aim for all green** before *Continue EOY Setup*.

The rules to follow:

1. **The Budget Start Date is set for you automatically** — advanced to the new financial year (last year + 1 year). Just **check it is correct**. It anchors every other calculation, so only change it deliberately.
2. **Never remove these three rows:** **Budget**, **Budget Period (months)**, and **Shopping Day** (Groceries depends on Shopping Day).
3. **Removing an income source is safe** — *provided* you no longer have a fortnightly/weekly category with that exact name. If you have stopped receiving Pension or FTB and have also removed those categories, removing their start dates is correct and harmless.
4. **The label must match the category name exactly.** When you *add* a new fortnightly/weekly source, add a row whose Column E label matches the subcategory name **character for character** (spelling, spacing and capitalisation), and put its **first actual pay-date of the new year** in Column F — it must fall **within one pay-interval of the Budget Start Date** (within **14 days** for fortnightly, **7 days** for weekly).
5. When removing a source, **delete the whole table row** so the table closes up cleanly — don't just clear the date and leave an orphaned label behind.

!!! warning "If you get the start dates wrong"
    Two safeguards catch mistakes before they can corrupt the new year:

    - **At Continue EOY Setup**, the process **refuses to proceed** if any fortnightly/weekly start date is missing, left over from last year, or set too far into the year. It tells you the exact valid range — e.g. *"Wages start date 06/07/2025 should be its first pay-date of the new year — set it between 01/07/2026 and 14/07/2026 (within 14 days of the Budget Start Date)."* Fix the dates and run Continue again.
    - **At Distribute**, if a fortnightly/weekly category has no matching start date at all, the system stops with *"Start date not configured for …"* rather than producing a wrong budget. Fix the table and Distribute again.

!!! danger "Safety net — you cannot harm your master"
    Throughout EOY you are working in a **copy**, never the master. If the copy ever becomes a mess — wrong start dates, a tangled budget, anything — the simplest and safest fix is to **delete the copy and start the EOY process again from your MASTER spreadsheet**. Nothing is lost: your master is untouched until the very last step (Finalize), so you can always begin again from a clean copy.

## Step 4: Continue Setup (New Copy)

### 4.1 Copy Balances and Clear Data

1. Go to **Period Processing → End of Year Setup → 2. Continue EOY Setup**.

    !!! warning "Start dates must be valid first"
        This step is blocked with **"🛑 Set the New-Year Start Dates First"** if any fortnightly/weekly start date is missing, **left over from last year**, or **set too far into the year** (it must be the first pay-date, within one pay-interval of the Budget Start Date). The message names each offending date and its valid range. Fix them on Maintain Budget (Step 3) and run Continue again.

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

2. The **Finalize End of Year Setup** dialog opens and runs the completion checks. When they pass it shows **✅ All verification checks have passed!** and explains that completing setup will:
   - Register this spreadsheet as your current budget master
   - Enable full budget functionality for the new fiscal year
   - Prepare the system for regular monthly operations

    Click **Complete Setup**. (Behind the scenes this marks the copy as the new **master** spreadsheet — `IS_MASTER = true`.)
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
**Problem:** Continue EOY Setup is blocked — a fortnightly/weekly start date is missing, left over from last year, or set too far into the year.
**Solution:** The message names each offending date and its valid range (its first pay-date, within one pay-interval of the Budget Start Date). On the Maintain Budget sheet, fix those dates in Column F, then run **2. Continue EOY Setup** again. (The Budget Start Date itself is advanced for you automatically — just confirm it.)

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

### ❌ "Start date not configured for …"
**Problem:** Distributing a fortnightly/weekly category fails because its start date is missing or the label doesn't match.
**Solution:** Open the **Budget Start Dates** table and make sure there is a row whose **Column E label matches the category name exactly**, with its first pay-date in **Column F**. See [Managing the Start Dates](#managing-the-start-dates). Then Distribute again.

### ❌ The copy has become a mess — start over
**Problem:** The new copy is in a confused state (wrong start dates, tangled budget, steps run out of order) and you're not sure how to recover.
**Solution:** Don't try to untangle it. **Delete the copy and start the EOY process again from your MASTER** (Step 1). You are always working in a copy, so the master is untouched until Finalize — beginning again from a fresh copy is the safest fix and loses nothing.

### ❌ "Print Instructions" does nothing
**Problem:** The print button shows the print preview (or nothing) but doesn't actually print.
**Solution:** This is **your PC's print queue, not the budget app** — the same button prints fine on a healthy system. It is a known local issue (a stuck print spooler or browser print process) that builds up during a session.

1. The simple fix: **reboot the PC** and try again.
2. Quick test: press **Ctrl+P** on any ordinary web page and print. If that *also* fails, it's your printer/print queue (not Sheets); if only Sheets fails, fully quit and reopen your browser.
3. Advanced users can clear the print queue instead of rebooting — see the [EOY Developer Guide](developer-guide.md#print-buttons-and-the-local-print-subsystem) for the exact commands.

It never affects your budget data or the EOY process — only the convenience print-out.

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
