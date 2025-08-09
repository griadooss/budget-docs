---
title: 'Common Issues & Troubleshooting'
description: 'Solutions for common problems with the budget system'
---

# Common Issues & Troubleshooting

This guide covers the most common issues you might encounter with the budget system and how to resolve them.

## End of Year Process Issues

### ❌ "Balance Check Failed - EOY Process Blocked"

**Problem:** The system displays a blocking error message preventing you from starting the End of Year process.

**Error Message:**
```
🚨 Balance Check Failed - EOY Process Blocked

Critical balance issues found:
• Banks sheet is not balanced (X.XX)

🔴 CRITICAL: The End of Year process copies current bank
balances to become opening balances for the new fiscal year.

❌ EOY process cannot proceed until all balances are zero.

💡 Tip: Use 'Reconciliation Dashboard' to fix balance issues.
```

**Why This Happens:**
- The system detected that one or more of your balance sheets are not at zero
- **Banks sheet** (cell C30) is not balanced
- **Annual Budget sheet** (cell B106) is not balanced
- **Maintain Budget sheet** (cell E120) is not balanced

**Solution:**
1. **First: Update Bank Balances (Critical for EOY):**
   - Go to **Banks** sheet and update ALL bank account balances
   - Ensure balances are **accurate as at end of financial year (June 30)**
   - **Important:** Banks often apply monthly interest as a final transaction
   - Download final statements and enter any end-of-year transactions
   - Bank balances MUST reflect the true position at fiscal year end

2. **Second: Use Reconciliation Dashboard:**
   - If bank balances are current but system still unbalanced, the issue is Cash Flow transactions
   - Go to **Budget** → **Reconciliation Dashboard**
   - **Missing transactions:** Import any transactions not yet in the system
   - **Extra transactions:** Remove duplicate or incorrect entries
   - **Unreconciled transactions:** Match transactions to budget categories
   - Work through all unreconciled items until dashboard is clear

3. **Verify All Balance Cells:**
   - **Banks sheet** (C30): Should show $0.00 when bank balances match Cash Flow
   - **Annual Budget sheet** (B106): Should show $0.00 when budget is balanced
   - **Maintain Budget sheet** (E120): Should show $0.00 when income equals expenses

4. **Retry EOY Process:**
   - Once all three balance cells show $0.00, retry the EOY process
   - The system will allow you to proceed

<Note>
**Why No Override:** Unlike End of Month processing, EOY has no "proceed anyway" option because incorrect bank balances would be copied to your new fiscal year, corrupting your entire budget foundation.
</Note>

### ❌ "Process Not Available" (Wrong Month)

**Problem:** EOY menu option is grayed out or shows error message.

**Error Message:**
```
Process Not Available

The 'Start End of Year Process' is only available in June,
the final month of the fiscal year.
```

**Solution:**
- **Wait until June:** EOY process is only available during the final fiscal month
- **Check System Month:** Ensure your system month is set to June (6)
- **Complete Monthly Processing:** Finish all End of Month processes through May first

### ❌ Authorization Failures

**Problem:** Google shows scary warnings during script authorization.

**What You'll See:**
- "Google hasn't verified this app"
- "The app is requesting access to sensitive info"
- "Go to Budget App Scripts (unsafe)"

**Solution:**
1. **Don't Panic** - This is Google's standard warning for ALL custom scripts
2. **Click "Advanced"** (bottom left of warning dialog)
3. **Click "Go to Budget App Scripts (unsafe)"** - This is safe to do
4. **Check "Select all"** to grant required permissions
5. **Click "Allow"**

<Warning>
**These warnings are normal!** Google shows these warnings for any custom spreadsheet script that isn't published in their official store. Your budget system is completely safe.
</Warning>

## End of Month Process Issues

### ⚠️ "Balance Check Failed" (End of Month)

**Problem:** System warns about balance issues during End of Month processing.

**Key Difference:** End of Month processing allows you to "proceed anyway" because monthly imbalances can be corrected later.

**Solution Options:**
1. **Fix Balances First (Recommended):**
   - Use Reconciliation Dashboard to resolve issues
   - Ensures clean monthly processing

2. **Proceed Anyway:**
   - Click "Yes" to continue despite warnings
   - Fix balance issues in subsequent reconciliation
   - Monthly processing is more forgiving than EOY

## Import and Reconciliation Issues

### ⚠️ Cross-Year/Month Duplicate Detection Issues

**Problem:** Transactions appear duplicated across months/years, or cross-year detection doesn't trigger.

**Root Cause:** Banks advance transaction processing dates by 2-7 days, moving transactions from one period to another.

**Why Cross-Year Detection Fails:**
- **7-day time window exceeded:** Detection only works within 7 days of fiscal year start
- **Too many existing transactions:** System assumes it's not the "first" import anymore
- **Delayed reconciliation:** August imports are too late to catch June→July transaction movements

**Impact:**
- **Balance reconciliation fails:** Historical bank balances become incorrect
- **Manual corrections required:** Must visually compare end/start of periods
- **Zero balance disrupted:** Cannot achieve accurate zero balance retrospectively

**Prevention (CRITICAL):**
1. **Complete EOY process immediately** after June 30
2. **Import July transactions within 7 days** of fiscal year start
3. **Reconcile monthly within 1 week** of month end
4. **Update bank balances immediately** before month/year-end processing

**Recovery Solutions:**
1. **Visual comparison:** Compare last 7 days of previous period with first 7 days of current period
2. **Look for identical amounts and descriptions** between periods
3. **Manually adjust historical bank balances** to restore zero balance
4. **Use calculated "must have been" balances** rather than relying on historical records

<Warning>
**There is no automated fix for delayed reconciliation** - bank date changes invalidate historical data integrity. Prevention through timely processing is the only reliable solution.
</Warning>

### ❌ Bank Import Failures

**Problem:** Cannot import bank transactions or import maps incorrectly.

**Common Causes:**
- Changed bank file format
- Missing column mappings
- Incorrect file type (CSV vs PDF)

**Solutions:**
1. **Check File Format:**
   - Ensure using correct file type for your bank
   - Most banks require CSV format
   - Some banks only provide PDF (requires manual entry)

2. **Update Column Mappings:**
   - Go to import settings
   - Verify column mappings match your bank's format
   - Update mappings if bank changed their export format

3. **Clear Previous Mappings:**
   - Use "Clear Stored Mappings" in debug menu
   - Re-configure mappings from scratch

### ❌ Reconciliation Dashboard Issues

**Problem:** Transactions not appearing or reconciliation not working.

**Solutions:**
1. **Refresh Data:**
   - Close and reopen Reconciliation Dashboard
   - Reload spreadsheet if needed

2. **Check Transaction Dates:**
   - Ensure transactions are in correct date range
   - Verify date format is correct

3. **Verify Categories:**
   - Ensure budget categories exist
   - Check for typos in category names

## Performance Issues

### 🐌 Slow Processing

**Problem:** EOY or EOM processes take a long time or seem stuck.

**Solutions:**
1. **Be Patient:**
   - EOY process involves copying large amounts of data
   - Large spreadsheets take longer to process

2. **Check Script Execution:**
   - Look for "Running script" indicator
   - Don't close browser during processing

3. **Restart if Stuck:**
   - If truly stuck (no progress for 10+ minutes)
   - Refresh browser and try again
   - Process is designed to be resumable

## Developer Mode

### 🔧 Testing and Development

**Problem:** Need to test processes without perfect balance.

**Solution:**
- **Enable DEV_MODE** in script properties
- Balance checks are bypassed with console logging
- Allows testing of process logic without balance setup

**How to Enable:**
1. Go to **Extensions** → **Apps Script**
2. Go to **Settings** → **Script Properties**
3. Add property: `DEV_MODE` = `true`
4. Save and refresh spreadsheet

<Warning>
**Production Use:** Always disable DEV_MODE for normal budget operations. It bypasses critical safety checks.
</Warning>

## Getting Help

### When to Contact Support

If you encounter issues not covered here:

1. **Document the Problem:**
   - Screenshot error messages
   - Note what you were trying to do
   - Record any console errors (F12 in browser)

2. **Check Recent Changes:**
   - Did you modify the spreadsheet structure?
   - Were there recent Google Sheets updates?
   - Did you change any formulas?

3. **Try Basic Troubleshooting:**
   - Refresh the browser
   - Close and reopen the spreadsheet
   - Clear browser cache if needed

### Emergency Recovery

**If Your Budget System Breaks:**

1. **Don't Panic** - Your data is preserved
2. **Use Archived Copies** - Previous versions are automatically saved
3. **Check Version History** - Google Sheets maintains automatic backups
4. **Contact Support** - With specific error details

<Note>
The budget system is designed with multiple safety mechanisms. In most cases, issues can be resolved without data loss.
</Note>