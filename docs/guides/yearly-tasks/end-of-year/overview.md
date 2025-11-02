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
   - **Menu Item:** "Start End of Year Process"
   - Export critical properties to ensure smooth transition
   - Create a copy of your current budget spreadsheet
   - The master spreadsheet remains unchanged during this phase

### 2. **Initial Setup** (in New Copy)
   - **Menu Item:** "1. Run Initial EOY Setup"
   - Authorize scripts in the new copy
   - Configure new year settings (dates, payment schedules)
   - **Manual budget update** - Review and update all income and expense amounts

### 3. **Continue Setup** (in New Copy)
   - **Menu Item:** "2. Continue EOY Setup" - Copy bank balances and clear transaction sheets
   - **Menu Item:** "Run End of Month Process" - Complete final month processing for fiscal year
   - **Commitment Validation** - System checks for outstanding commitments with user choice (Fix Now vs Ignore)

### 4. **Finalization** (in New Copy)
   - **Menu Item:** "3. Finalize EOY Setup"
   - Verify all completion criteria are met
   - Register the new copy as the active master spreadsheet
   - **Archive the previous master** with "_ARCHIVED_FY{year}" suffix

## State-Driven Menu System

The EOY process uses an intelligent menu system that adapts based on your progress:

### In Master Spreadsheet (June only)
- **Period Processing** → **Start End of Year Process** - Begin the EOY workflow

### In Fresh Copy (Before Setup)
- **Period Processing** shows only EOY Setup options:
  - **1. Run Initial EOY Setup** - Start configuration
  - **2. Continue EOY Setup** - Available after initial setup
  - **3. Finalize EOY Setup** - Available after continuation

### In Fresh Copy (After Setup Complete)
- **Period Processing** shows normal menu:
  - **Run End of Month Process** - Normal monthly operations
  - **Start End of Year Process** - For next year's EOY

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

### 4. **Commitment Validation** (User Choice)
- System checks for outstanding commitments during End of Month processing
- **User Choice Dialog:** Choose between "Fix Now" (NO) or "Ignore" (YES)
- **Fix Now (NO):** Address commitments before proceeding with EOM
- **Ignore (YES):** Proceed with EOM despite outstanding commitments

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

1. **Initial Prompt** - "Authorization Required" dialog appears
2. **Google Authorization** - Select your account
3. **Security Warning** - Google will show a warning that looks scary but is normal:
   - You'll see "Google hasn't verified this app"
   - You'll see "The app is requesting access to sensitive info"
   - **This is expected** - Google shows this for all custom spreadsheet scripts
4. **Continue Despite Warning:**
   - Click **"Advanced"** (bottom left of the dialog)
   - Click **"Go to Budget App Scripts (unsafe)"** - *this is safe, just Google's standard warning*
   - **Check "Select all"** to grant required permissions
   - Click **"Allow"**
5. **Verification** - System automatically validates setup

!!! warning "About the \"Unsafe\" Warning"
    Google shows this warning for ALL custom spreadsheet scripts, not because there's actually a problem. The budget system is safe to authorize - it only accesses your budget spreadsheet data and nothing else.

!!! tip
    If authorization fails, refresh the page and try again. The system includes retry logic for common authorization issues.

## Getting Started

### From Master Spreadsheet (June only)
1. Navigate to **Period Processing** → **Start End of Year Process**
2. Follow the guided instructions in the help dialog
3. Export properties when prompted
4. Create a copy of your spreadsheet

### From New Copy
1. Open the new copy
2. Navigate to **Period Processing** → **1. Run Initial EOY Setup**
3. **Complete authorization when prompted** - Google will show scary warnings but this is normal and safe
4. Follow the four-step process through to finalization

## Documentation and Support

- **Step-by-step instructions:** [EOY Budget Setup](setup.md)
- **Technical details:** [Developer Guide](developer-guide.md)
- **Troubleshooting:** [Common Issues](../../troubleshooting/common-issues.md)

!!! note
    The complete documentation is accessible at any time during the EOY process through menu links and help dialogs. You don't need to complete the process in one session - you can refer back to the documentation as needed.