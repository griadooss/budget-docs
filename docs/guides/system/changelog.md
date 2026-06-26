---
title: 'Changelog'
description: 'Detailed history of documentation updates'
---

# Changelog

!!! note
    A complete history of changes and updates to the Budget System documentation.

## Version History

### 2.2.0 (2026-06-26)

**Balance locator, ACTIVE-flag fix, and menu tidy-up**

=== "Balance"

    - New **⚖️ Check Annual Budget Balance** tool (Budget > Maintain Budget, and
      Developer > Integrity Checker) — read-only locator that points to the exact
      category/item behind an out-of-balance Annual Budget, with the dollar amount,
      and names a mis-placed payment month for non-monthly items
    - Confirmed and documented: a **\$0 budget item can be distributed** (only negative
      is blocked) and keeps a \$0 row in the Annual Budget; such items are now made
      inactive automatically

=== "ACTIVE flags"

    - **Fixed** a persistent "active but not budgeted" validation failure that a
      reload could never clear. An item is now ACTIVE only when it is **budgeted in
      Maintain Budget (amount > 0 and distributed) AND present in the Annual Budget** —
      previously the sync judged purely on Annual Budget presence while the validator
      used the budget rule, so the two could never agree
    - The Validate dialog now **lists the offending items** (not just counts) and drops
      a duplicated line

=== "Menus"

    - New **Maintain Categories** group under Budget > Maintain Budget (Add/Delete plus
      the guides)
    - The lookup editor moved here as **🏷️ Manage Category Lookups** (was Settings >
      Sheet Settings > "Manage Categories")
    - **Settings > Sheet Settings** renamed **LookUps Sheet**
    - Removed the vestigial **Clear Pending Transactions** item; retired the unused
      function-registry tooling

### 2.1.0 (2026-06-22)

**Distribution: Start Month + Checkbox Trigger**

=== "Distribution"

    - New **Start Mth** column (Maintain Budget Col J) — choose the month a
      non-monthly item's spread begins (e.g. Freq 3 / Aug → Aug, Dec, Apr)
    - Blank Start Mth = July (unchanged behaviour for untouched rows)
    - Month dropdown is frequency-filtered and rebuilds when Freq changes
    - Column-H trigger is now a **checkbox** ("Tick to Dist Single Items"),
      replacing the old "Distribute" dropdown
    - Row flags **red → green** as in-progress feedback during distribution

**Added**
- Developer → **Distribution Setup** submenu: *Setup Distribute Checkboxes (Col H)*
  and *Setup Start-Mth Column (Col J)*
- Documented the previously-undocumented *Audit / Fix Annual Budget Formulas*
  tools under Integrity Checker

**Fixed**
- The "stuck Distribute dropdown" bug — a checkbox tick is always a change, so the
  trigger can never fail to fire
- Normalised non-breaking hyphens to plain hyphens across the updated docs
  (Developer Menu, Basic Operations, and this changelog)

**Notes**
- Re-run both Distribution Setup items (and *Fix Annual Budget Formulas*) after the
  final Version History restore — content reverts, code persists

### 2.0.0 (2024-06-30)

**End of Year Process Documentation Overhaul**

=== "EOY Process"

    - Complete rewrite of End of Year documentation
    - Three-step process clarification
    - State-driven menu system documentation
    - Month restriction guidelines

=== "Technical Updates"

    - Updated developer guide with current implementation
    - Comprehensive testing checklist
    - Performance considerations
    - Security best practices

**Added**
- Comprehensive pre-setup verification requirements
- Step-by-step three-phase EOY process guide
- State-driven menu system explanation
- Automated master archiving documentation
- Month restriction (June only) guidelines
- Enhanced troubleshooting section
- Developer testing workflow and checklist
- Performance optimization guidance

**Changed**
- Complete restructure of EOY setup process documentation
- Updated process flow to reflect current three-step implementation
- Improved technical implementation details
- Enhanced user guidance with warnings and tips
- Modernized documentation format with better organization

**Fixed**
- Outdated process descriptions that didn't match current implementation
- Missing documentation for automated archiving feature
- Incomplete technical limitation explanations
- Lack of comprehensive testing guidance

### 1.0.0 (2024-02-22)

**Initial Release**

=== "Documentation"

    - Initial documentation structure
    - User manual sections
    - Quick start guides

=== "Features"

    - Basic operations guide
    - Menu reference
    - Troubleshooting guides

**Added**
- Complete user manual
- Transaction guides
- Support documentation

**Changed**
- N/A (Initial release)

**Fixed**
- N/A (Initial release)