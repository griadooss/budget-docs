---
title: 'End of Month Process'
description: 'How to complete the monthly budget processing'
---

# End of Month Process

This guide covers how to complete the monthly budget processing to close the current month and prepare for the next month.

## Overview

The End of Month (EOM) process is a critical monthly procedure that:
- Copies actual values to the next month
- Updates month formatting and status
- Prepares the system for the next month's processing
- Prevents duplicate processing

## Prerequisites

### Before Running EOM

!!! tip "Prerequisites"
    - All transactions reconciled
    - Categories verified and assigned
    - Bank balances verified
    - Budget variances reviewed
    - No pending transactions

### System Requirements
- Current month properly set
- Month statuses initialized
- All sheets accessible
- Proper authorization

## Running the Process

### Access the EOM Process
1. Open your budget spreadsheet
2. Click **📅 Period Processing > Run End of Month Process**
3. The system will verify prerequisites and show confirmation

### Confirmation Dialog

The system will display:

- **Current month** being processed
- **Column ranges** for current and next month
- **Confirmation prompt** to proceed

!!! warning "Important"
    Verify the correct month is selected before proceeding

### Balance Check

The system performs a comprehensive balance check:

- **Bank balances** - Verify account balances
- **Budget balances** - Check budget vs actual
- **Transaction reconciliation** - Ensure all transactions reconciled

If issues are found:

- **Review warnings** - Check each issue
- **Fix problems** - Resolve before proceeding
- **Re-run check** - Verify fixes before EOM

## What the Process Does

### Step 1: Copy Actual Values
- **Source:** Current month's Actual column (right column)
- **Target:** Next month's Actual column
- **Range:** Rows 5-114 (budget items)
- **Method:** Natural copy with formula adjustment

### Step 2: Update Formatting
- **Current month:** Apply historical formatting (gray background)
- **Next month:** Apply current month formatting (blue highlights)
- **Method:** Paint Format copy from template

### Step 3: Update Status Tracking
- **Mark current month:** Set status to "historical"
- **Mark next month:** Set status to "current"
- **Update properties:** Store processing information
- **Hide EOM option:** Prevent duplicate processing

### Step 4: EOY Transition (June Only)

If processing June (end of fiscal year):

- **Increment year:** Update to next fiscal year
- **Clear formulas:** Remove formulas from all months except July
- **Update headers:** Set up new fiscal year headers
- **Initialize July:** Set up July as current month

## Post-Processing

### Verification Steps
1. **Check copied values** - Verify Actual column in next month
2. **Review formatting** - Confirm month highlighting is correct
3. **Verify status** - Check month status tracking
4. **Test functionality** - Ensure system is ready for next month

### Menu Updates
- **EOM option hidden** - No longer available for processed month
- **Next month ready** - System prepared for next month
- **Status indicators** - Updated throughout interface

## Troubleshooting

### Common Issues

??? warning "Balance Check Failed"
    **Problem:** System shows balance issues

    **Solution:**

    - Review each balance issue
    - Reconcile missing transactions
    - Verify account mappings
    - Re-run balance check

??? calendar "Wrong Month Selected"
    **Problem:** Incorrect month being processed

    **Solution:**

    - Cancel the process
    - Set correct current month
    - Initialize month statuses
    - Re-run EOM process

??? palette "Formatting Issues"
    **Problem:** Month formatting not applied correctly

    **Solution:**

    - Check template month availability
    - Verify column ranges
    - Re-run formatting manually
    - Contact support if persistent

??? settings "Status Update Failed"
    **Problem:** Month statuses not updated

    **Solution:**

    - Check system properties
    - Verify month tracking
    - Re-initialize month statuses
    - Re-run EOM process

### EOY-Specific Issues

??? calendar-year "Year Transition Error"
    **Problem:** Year not incremented properly

    **Solution:**

    - Verify June processing
    - Check fiscal year settings
    - Review year transition logic
    - Re-run EOM process

??? code "Formula Clearing Issues"
    **Problem:** Formulas not cleared from old months

    **Solution:**

    - Check July setup
    - Verify formula clearing logic
    - Review month column ranges
    - Contact support

## Best Practices

!!! tip "Best Practices"
    - Always reconcile before EOM
    - Verify current month before processing
    - Review balance check results
    - Test system after EOM completion
    - Keep backup before major changes
    - Document any issues encountered

## Completion Checklist

After EOM processing:

- [x] **Actual values** - Copied to next month
- [x] **Current month** - Formatted as historical
- [x] **Next month** - Formatted as current
- [x] **Month statuses** - Updated
- [x] **EOM option** - Hidden for processed month
- [x] **System** - Ready for next month
- [x] **All balances** - Verified
- [x] **No errors** - In processing

## Next Steps

After successful EOM:

1. **Begin next month** - Start importing new transactions
2. **Update budget** - Adjust budget for next month
3. **Monitor performance** - Track budget vs actual
4. **Prepare for EOY** - If approaching June

!!! note
    For End of Year processing, see the [EOY Guide](../yearly-tasks/end-of-year/overview.md).

## Advanced Features

### Performance Monitoring
- **Processing time** - Track EOM completion time
- **Error logging** - Monitor for processing issues
- **Status tracking** - Verify all steps completed
- **System health** - Check overall system status

### Backup and Recovery
- **Pre-EOM backup** - Automatic backup before processing
- **Rollback capability** - Revert if issues occur
- **Data integrity** - Verify data consistency
- **Error recovery** - Handle processing failures

### Integration
- **Month tracking** - Integrated with month status system
- **Menu updates** - Automatic menu refresh
- **Status synchronization** - Consistent status across system
- **Property management** - Update system properties