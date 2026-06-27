---
title: 'End of Year Process Overview'
description: 'Learn about the End of Year (EOY) process for creating a new budget year'
---

# End of Year Process Overview

The End of Year (EOY) process helps you transition from one financial year to the next while maintaining your budget history and setting up a fresh budget for the new year.

## When to Use

The EOY process should be initiated when:

- **You're in June** (the final month of the fiscal year)
- All transactions for the current year have been reconciled
- You're ready to start planning for the next financial year (July-June)

!!! warning "⏰ CRITICAL TIMING"
    Complete the EOY process **immediately** after your fiscal year ends (June 30). Then import July transactions **within 7 days** to enable cross-year duplicate detection.

    **Why This Matters:** Banks often advance transaction processing dates by 2-7 days, moving late June transactions into July. Delayed reconciliation prevents the system from catching these duplicates automatically.

!!! note "Important"
    The EOY process can only be started during June. If you try to access it in other months, the system will display a restriction message and block the process.

## Process Summary

The EOY process consists of **four main steps** with clear menu-driven progression:

### 1. **Start EOY Process** (in Master Spreadsheet)
   - **Menu:** Period Processing → End of Year → **Start End of Year Process**
   - Acknowledge the **⚠️ EOY Warnings** dialog if outstanding loans/commitments are found
   - Export critical properties to ensure a smooth transition
   - Create a copy of your current budget spreadsheet
   - The master spreadsheet remains unchanged during this phase

### 2. **Initial Setup & Budget Build** (in New Copy)
   - **Menu:** Period Processing → End of Year Setup → **1. Run Initial EOY Setup**
   - Authorise scripts in the new copy
   - The system imports settings and sets the budget period and payment dates
   - **Build the new-year budget on the Maintain Budget sheet** — set start dates (Column F, Budget Start Date first), then each category's amount + frequency, and Distribute to Annual Budget. Do this **before** Continue. (Category tools are under Period Processing → Maintain Budget → Maintain Categories during this window.)

### 3. **Continue Setup** (in New Copy)
   - **Menu:** Period Processing → End of Year Setup → **2. Continue EOY Setup** — copies bank balances and clears the transaction sheets
   - **Menu:** Period Processing → **Run End of Month Process** — completes the final month and moves June → July

### 4. **Finalization** (in New Copy)
   - **Menu:** Period Processing → End of Year Setup → **3. Finalize EOY Setup**
   - Verify all completion criteria are met
   - Register the new copy as the active master spreadsheet
   - **Archive the previous master** with an `_ARCHIVED_FY{year}` suffix (a manual step on the old master)

## State-Driven Menu System

The EOY process uses an intelligent menu system that adapts based on your progress:

### In Master Spreadsheet (June only)
- **Period Processing → End of Year → Start End of Year Process** — begin the EOY workflow

### In Fresh Copy (During EOY Setup)
- **Period Processing → End of Year Setup** shows the EOY steps:
  - **1. Run Initial EOY Setup**
  - **2. Continue EOY Setup**
  - **3. Finalize EOY Setup**
- **Period Processing → Maintain Budget → Maintain Categories** is also available while you build the new-year budget — it is removed automatically once you run Continue EOY Setup.

### In Fresh Copy (After Setup Complete)
- **Period Processing** shows the normal menu:
  - **Run End of Month Process** — normal monthly operations
  - **End of Year → Start End of Year Process** — for next year's EOY

!!! note
    The menu system automatically adapts based on your EOY completion status, ensuring you always see the appropriate options for your current stage.

## Pre-EOY Requirements

Before beginning the EOY process, ensure these conditions are met:

### 1. **Month Restriction**
- Must be June (final fiscal month)
- System automatically validates this requirement

### 2. **Account Reconciliation**
- LastReconciliationDate should be at or near June 30
- All transactions properly categorized and reconciled

### 3. **Balanced Sheets** (CRITICAL - Strictly Enforced)
- **Banks sheet:** "BOOKS BALANCED" indicator must show $0.00
- **Annual Budget sheet:** "BUDGET BALANCED" indicator must show $0.00
- **Maintain Budget sheet:** Balance indicator must show $0.00

!!! warning "🚨 CRITICAL REQUIREMENT"
    The system now **strictly enforces** balance checking and will **block the EOY process** if any sheet is unbalanced.

    **Why This Matters:** The EOY process copies current bank balances to become opening balances for the new fiscal year. If these are incorrect, your entire new year will start with wrong foundation data.

    **❌ No Override Available:** Unlike End of Month processing, there is no "proceed anyway" option for EOY to prevent catastrophic data issues.

    **💡 Solution:**

    1. **First** - Update ALL bank balances to be accurate as at June 30 (banks often apply monthly interest as final transaction)
    2. **Second** - Use 'Reconciliation Dashboard' to resolve any Cash Flow transaction issues (missing, extra, or unreconciled transactions)
    3. **Third** - Ensure all three balance indicators show $0.00 before starting EOY process

### 4. **Outstanding Loans & Commitments** (Warning, not a blocker)
- When you **Start End of Year Process**, the system checks for outstanding informal loans (a negative LOANS REGISTER balance) and missed budgeted repayments (commitments).
- If any are found, an **⚠️ EOY Warnings** dialog appears with two choices:
  - **Continue with EOY** — acknowledge the warnings and proceed
  - **Cancel & Address Issues** — stop and fix them first
- Because commitments are checked here at the start, they are **not** re-checked during the End of Month step inside the EOY flow.

## Master Archiving Process

The EOY process includes a **guided archiving system** for your previous master spreadsheet:

### What Happens During Finalization
When you complete "3. Finalize EOY Setup":

1. **New copy becomes the master** - Marked with `IS_MASTER = true`
2. **Completion dialog appears** - Shows next steps including archiving instructions
3. **Old master remains active** - Still accessible and functional
4. **User guidance provided** - Clear instructions for manual archiving

### Manual Archiving Required
After EOY finalization, you must manually archive the old master:

1. **Go to your old master spreadsheet** (the one you copied from)
2. **Navigate to Settings → ⚠️ Advanced → Archive This Master**
3. **Confirm archiving** when prompted
4. **System automatically:**
   - Renames spreadsheet with "_ARCHIVED_FY{year}" suffix
   - Adds archive metadata in hidden "_Archive" sheet
   - Marks as archived (`IS_ARCHIVED = true`)

### Benefits
- **User control** - You decide when to archive the old master
- **Clear naming convention** - Archived spreadsheets are easily identifiable
- **Preserved history** - All previous data remains intact and accessible
- **Reversible process** - Can restore from archive if needed

## Authorization Process

When working with a new copy, you'll need to authorize the scripts. **Don't worry - this is normal and safe:**

1. **"Authorization required" dialog** appears — click **OK**
2. **Choose your Google account** (the same one you use for the spreadsheet)
3. **Security warning** — Google shows a warning that looks alarming but is normal:
   - "Google hasn't verified this app"
   - "The app is requesting access to sensitive info"
   - **This is expected** — Google shows this for all custom spreadsheet scripts
4. **Continue despite the warning:**
   - Click **Advanced** (bottom left of the dialog)
   - Click **Go to Budget-YYYY-Scripts (unsafe)** — the script name matches your copy's name; despite the label it is **not** unsafe
   - Tick **Select all** to grant the required permissions
   - Click **Continue**
5. **Verification** — the system automatically validates the setup

!!! warning "About the \"Unsafe\" Warning"
    Google shows this warning for ALL custom spreadsheet scripts, not because there's actually a problem. The budget system is safe to authorize - it only accesses your budget spreadsheet data and nothing else.

!!! tip
    If authorization fails, refresh the page and try again. The system includes retry logic for common authorization issues.

## Getting Started

### From Master Spreadsheet (June only)
1. Navigate to **Period Processing → End of Year → Start End of Year Process**
2. Follow the guided instructions in the help dialog (you can **Print Instructions**)
3. Export properties when prompted
4. Create a copy of your spreadsheet

### From New Copy
1. Open the new copy
2. Navigate to **Period Processing → End of Year Setup → 1. Run Initial EOY Setup**
3. **Complete authorisation when prompted** — Google shows alarming-looking warnings but this is normal and safe
4. Build your new-year budget, then follow the steps through to finalisation

## Documentation and Support

- **Step-by-step instructions:** [EOY Budget Setup](setup.md)
- **Technical details:** [Developer Guide](developer-guide.md)
- **Troubleshooting:** [Common Issues](../../troubleshooting/common-issues.md)

!!! note
    The complete documentation is accessible at any time during the EOY process through menu links and help dialogs. You don't need to complete the process in one session - you can refer back to the documentation as needed.