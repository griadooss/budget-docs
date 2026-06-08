---
title: 'Menu Reference'
description: 'Complete guide to all menu functions in the Budget System'
---

# Menu Functions Reference

!!! note
    All budget functions are organised in the menu bar for easy access. This guide explains each menu and its functions as they currently exist in the system. Some items only appear in certain states (for example, in a master spreadsheet, a new-year copy, or when Developer Mode is enabled) — these are noted where relevant.

## 🏦 Budget Menu

??? file-import "Import Bank Transactions"
    - **Access:** Click "🏦 Budget > Import Bank Transactions"
    - **Purpose:** Import new transactions from bank statements
    - **Features:**
      - Paste data from bank statements
      - Manual transaction entry
      - Automatic duplicate detection
      - Column mapping for different bank formats
      - Account selection and mapping
      - Cross-year duplicate detection

??? check-double "Reconciliation Dashboard"
    - **Access:** Click "🏦 Budget > Reconciliation Dashboard"
    - **Purpose:** Match and verify transactions
    - **Features:**
      - Side-by-side transaction comparison
      - Automatic transaction matching
      - Split transaction handling
      - Bulk reconciliation
      - Category assignment
      - Performance diagnostics

??? wrench "Maintain Budget Submenu"
    - **Access:** Click "🏦 Budget > Maintain Budget"
    - **Purpose:** Manage budget categories, commitments, loans and transactions
    - **Functions:**
      - **📋 Guide** (sub-submenu) — three reference dialogs:
        - **📋 Step-by-Step Instructions** — the workflow for adding/removing budget items
        - **⚠️ Safety Warnings & Tips** — what to avoid when maintaining the budget
        - **🤖 Automation Details** — how the system reacts to your changes
      - **➕ Add Category/Subcategory:** Add new budget items with proper setup
      - **🗑️ Delete Category/Subcategory:** Safely remove items with cleanup
      - **📋 Commitment Management:** Review and manage outstanding commitments
      - **🧹 Clear Pending Transactions:** Remove pending (unconfirmed) transactions
      - **💰 Loan Transactions:** Record and track loan transactions by participant
      - **✏️ Edit Transaction:** Modify the currently selected transaction

## 📅 Period Processing Menu

??? calendar-check "Run End of Month Process"
    - **Access:** Click "📅 Period Processing > Run End of Month Process"
    - **Purpose:** Close the monthly books and prepare for next month
    - **Requirements:**
      - All transactions reconciled
      - Categories verified
      - Balances checked (with option to proceed anyway)
    - **What it does:**
      - Copies Actual values to next month
      - Updates month formatting
      - Updates month statuses
      - Hides EOM option after completion
      - Validates balance consistency
    - **Note:** In a new-year copy, once a month has been processed the EOM option is hidden until the next month is due.

??? calendar-year "End of Year Submenu"
    - **Access:** Click "📅 Period Processing > End of Year"
    - **Purpose:** Complete End of Year setup and processing workflow
    - **The submenu changes depending on where you are:**
      - **In the master spreadsheet:** a single item — **Start End of Year Process** (begins the EOY workflow; only offered during June)
      - **In a new-year copy:** the numbered setup steps —
        - **1. Run Initial EOY Setup**
        - **2. Continue EOY Setup**
        - **3. Finalize EOY Setup**
        - **Initialize Month Statuses** — set up the month-tracking system
    - **Workflow:** Start EOY Process (master) → open the new copy → Steps 1–3 → Initialize Month Statuses
    - **Note:** The EOY process can only be started during June.
    - **Features:**
      - Strict balance checking (no override option)
      - Bank balance validation
      - Guided step-by-step process
      - Commitment validation with a Fix Now vs Ignore choice
    - For the full walkthrough see the [End of Year Process Overview](../yearly-tasks/end-of-year/overview.md).

## ⚙️ Settings Menu

??? gear "Import Settings"
    - **Access:** Click "⚙️ Settings > Import Settings"
    - **Purpose:** Configure bank statement import formats
    - **Functions:**
      - **Manage Import Templates:** Create, edit and reuse bank-specific column mappings

??? table "Sheet Settings"
    - **Access:** Click "⚙️ Settings > Sheet Settings"
    - **Purpose:** Manage categories, ACTIVE flags and the LookUps sheet
    - **Functions:**
      - **Manage Categories:** Add/edit income and expense categories (LookUps manager)
      - **🔄 Sync ACTIVE Flags:** Synchronise category active status from budgeted items
      - **✅ Validate ACTIVE Flags:** Check category status consistency
      - **🔒 Hide LookUps Sheet:** Hide the LookUps sheet from view
      - **👁️ Show LookUps Sheet:** Reveal the LookUps sheet when you need to inspect it

??? warning "Advanced (Master spreadsheets only)"
    - **Access:** Click "⚙️ Settings > ⚠️ Advanced"
    - **Purpose:** Master spreadsheet management — only appears in a master spreadsheet
    - **Functions:**
      - **Archive This Master:** Archive the current master spreadsheet (used as part of the EOY process)
      - **📥 Import Properties to Master:** Import saved script properties into the master

## 🛠️ Developer Menu (Dev Mode Only)

!!! note
    The Developer menu only appears when Developer Mode is enabled (**ℹ️ Help > Toggle Developer Mode**). The submenus below are a summary — for the full list of every tool, including the large **Legacy** group, see the [Developer Menu Reference](../system/developer-menu.md).

??? code "Dev Mode"
    - Check Dev Mode Status / Enable Dev Mode / Disable Dev Mode

??? info-circle "System Status"
    - Check Master Status / Set as Master Spreadsheet

??? cog "Triggers"
    - 🔧 Install onEdit Trigger / ❌ Remove onEdit Trigger

??? shield-check "Integrity Checker"
    - Run Comprehensive Check / Quick Integrity Check

??? bug "Testing Tools"
    - Reset Month Statuses / Validate Script Properties

??? bug "Debug Tools"
    - 📊 Named Ranges Report
    - 👁️ View Stored Mappings
    - 📜 Import History
    - 🔄 Re-sync ACTIVE Flags
    - 🔍 Debug Income Budget Status

??? cog "Legacy"
    - A grouped set of legacy and diagnostic tools (Legacy System Cleanup, Cross-Year Detection, Advanced Testing, Debug & Diagnostics, Performance Testing). See the [Developer Menu Reference](../system/developer-menu.md) for details.

## ℹ️ Help Menu

??? book "Documentation"
    - **Access:** Click "ℹ️ Help > Online Documentation"
    - **Purpose:** Open this online documentation site

??? info "System Information"
    - **Access:** Click "ℹ️ Help > About (Version Info)"
    - **Purpose:** Check the current version and system configuration

??? code "Developer Mode Toggle"
    - **Access:** Click "ℹ️ Help > Toggle Developer Mode"
    - **Purpose:** Switch Developer Mode on or off (controls whether the 🛠️ Developer menu is shown)

## 📦 Archive Menu (Archived spreadsheets only)

??? box "Restore from Archive"
    - **Access:** Click "📦 Archive > Restore from Archive"
    - **Purpose:** In an archived spreadsheet, restore it for use. Archived spreadsheets show only this minimal menu plus Help.

## Menu States

=== "Normal Operations"

    - All standard menus visible (Budget, Period Processing, Settings, Help)
    - Full user functionality
    - Maintain Budget submenu available

=== "EOY Setup Mode (new copy)"

    - Period Processing shows the numbered EOY setup steps
    - Limited functionality during setup
    - Guided setup process with strict balance checking

=== "Master Spreadsheet"

    - Period Processing > End of Year shows only **Start End of Year Process** (June only)
    - Settings includes the master-only **⚠️ Advanced** submenu

=== "Archived Mode"

    - Minimal menu: **📦 Archive > Restore from Archive** plus Help
    - No editing capabilities

=== "Developer Mode"

    - Adds the 🛠️ Developer menu with debug, testing and legacy tools

## Important Workflow Notes

!!! warning "Critical"
    Always use menu functions for category management. Manual deletion from sheets can cause balance inconsistencies.

!!! note "ACTIVE Flag System"
    Category active status is managed automatically (and re-synced on startup in Developer Mode). If you suspect it is out of step, use **Sync ACTIVE Flags** / **Validate ACTIVE Flags** under Settings > Sheet Settings, or **🔄 Re-sync ACTIVE Flags** under the Developer menu's Debug Tools.

!!! info "Balance Checking"
    The system validates balances before critical operations. EOY processes require a zero balance with no override option.

## Best Practices

!!! tip "Best Practices"
    - Always use **Delete Category/Subcategory** from the Maintain Budget menu
    - Use **Add Category/Subcategory** for proper setup
    - Check balance indicators before running EOY processes
    - Review warning messages carefully
    - Use Developer menu tools only when troubleshooting

!!! warning
    Don't manually delete rows from Annual Budget or Maintain Budget sheets

!!! warning
    Don't modify sheet structure manually

!!! warning
    The Developer menu only appears when Developer Mode is enabled
