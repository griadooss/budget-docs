---
title: 'EOY Process Developer Guide'
description: 'Technical information for developers working on the End of Year process'
---

# EOY Process Developer Guide

!!! danger "Developers only — not part of normal budgeting"
    This page documents the app's internal code, CLASP sync, and Script IDs for whoever maintains the software. **You do not need anything here to run your budget or to complete End of Year** — follow the [EOY Setup](../guides/yearly-tasks/end-of-year/setup.md) guide instead. Acting on these instructions without understanding the code can damage the live spreadsheet.

This guide contains technical information for developers who are maintaining or enhancing the End of Year (EOY) process. End users should refer to the [End of Year Process Overview](../guides/yearly-tasks/end-of-year/overview.md) and [EOY Budget Setup](../guides/yearly-tasks/end-of-year/setup.md) guides instead.

## Current Implementation Overview

The EOY process has been significantly improved from the original design and now features:

### Key Architectural Features
- **Month-Restricted Access** - Process only available in June (final fiscal month)
- **State-Driven Menu System** - Menus adapt based on EOY completion status
- **Three-Step Setup Workflow** - The three numbered menu steps (`1. Run Initial EOY Setup` → `2. Continue EOY Setup` → `3. Finalize EOY Setup`) that follow the initial **Start EOY Process**. The [user-facing overview](../guides/yearly-tasks/end-of-year/overview.md) describes the whole journey as four phases by counting *Start EOY Process* as phase 1.
- **Guided Master Archiving** - User manually archives previous master with system guidance
- **Comprehensive Verification** - Multiple validation checkpoints throughout process
- **User Choice Dialogs** - Commitment validation with Fix Now vs Ignore options (this fires during a *normal* End of Month run; inside the EOY flow loans/commitments are surfaced up-front via the EOY Warnings dialog instead — see [Commitment Validation System](#commitment-validation-system))
- **Category Tools During Build** - While the new-year budget is being built, Maintain Categories is surfaced under Period Processing, then removed once Continue EOY Setup runs
- **Draggable Warning Dialogs** - Improved user experience for all warning dialogs

### Core Functions and Files
The EOY implementation is primarily contained in `src/utility/yearEndBudget.js`:

- **Main Entry Points:**
  - `showYearEndHelp()` - Initial help dialog in master spreadsheet
  - `setupNewYearBudget()` - Step 1: Initial EOY setup (then the user builds the budget manually)
  - `continueEOYSetup()` - Step 2: copy bank balances, clear transaction sheets, update headers
  - `finalizeEOYSetup()` - Step 3: Finalization and master archiving

- **Supporting Functions:**
  - `exportPropertiesToSheet()` / `importPropertiesFromSheet()` - Property management
  - `clearTransactionSheets()` - Clean Cash Flow and Bank Records sheets
  - `copyBankBalancesToOpeningPositions()` - Transfer bank balances
  - `updateMonthlyHeaders()` - Update fiscal year headers across sheets
  - `archiveThisMaster()` - Manual master archiving (user-initiated)
  - `validateCommitments()` - Check for outstanding commitments
  - `checkAllBalances()` - Comprehensive balance validation

## Development and Testing Workflow

!!! info "See also: EOY-TESTING.md (budget-app repo)"
    For the copy-hygiene and deploy mechanics behind this workflow — why `clasp push` never reaches an existing copy, the orphan-script cleanup checklist, the protected master Script IDs, and the reuse-one-copy approach — see [`EOY-TESTING.md`](https://github.com/griadooss/GS-Budget-App/blob/main/EOY-TESTING.md) in the budget-app repository.

### Critical Development Process

When developing and testing the EOY process, you **must** follow this workflow to ensure you're testing the latest code:

1. **Development Phase:**
   - Make all script changes in the **MASTER** spreadsheet
   - Test individual functions using Apps Script editor
   - Push changes using `clasp push` to update MASTER's script project

2. **Testing Phase:**
   - **Always delete existing test copies** before creating new ones
   - Make a **fresh copy** of MASTER for each test cycle
   - Each copy gets its own Apps Script project with the current code
   - Test the complete EOY process in the fresh copy

3. **Issue Resolution:**
   - Document any issues found during testing
   - Make fixes in the **MASTER** spreadsheet
   - Push changes to MASTER using `clasp push`
   - Delete test copy and create a new one for retesting

!!! warning "Critical"
    Never use old test copies. Each copy has its own script project, and using an old copy will test outdated code, leading to false results and wasted development time.

!!! danger "Clean up copies to avoid orphan script projects"
    Every *Make a copy* duplicates the container-bound script into a new project. Deleting a copy only *trashes* it — the spreadsheet **and its bound script** linger in Drive Trash (≈30 days) until purged. Left unchecked these accumulate and have, in the past, contributed to Google throttling the account.

    After each test cycle, **empty Drive Trash** (<https://drive.google.com/drive/trash>) and verify the Apps Script dashboard (<https://script.google.com/home/projects>) — never removing the live master script. Better still, **reuse a single persistent test copy** (reset its data/properties between runs) rather than creating and deleting a new one each cycle, so no extra script projects are spawned.

### Month Restriction Testing

The EOY process includes month validation that restricts access to June only:

```javascript
// In setupNewYearBudget() and showYearEndHelp()
const currentMonth = getCurrentMonth();
if (currentMonth && currentMonth.month !== 6) {
  // Block access with user-friendly message
  ui.alert("Process Not Available",
           "The 'Start End of Year Process' is only available in June...");
  return;
}
```

**Testing Considerations:**

- **Production:** Process only works in June
- **Development:** You may need to temporarily bypass month checking for testing
- **Test Mode:** Use `testMode` parameters in functions where available

## State Management and Menu System

### EOY State Tracking

The system uses script properties to track EOY progress:

```javascript
// Key properties for state management
- IS_MASTER: "true"/"false" - Whether spreadsheet is the active master
- EOY_SETUP_COMPLETE: "true"/"false" - Whether EOY setup is finished
- EOY_READY_FOR_EOM: "true"/"false" - Intermediate state during setup
- CURRENT_SPREADSHEET_ID: "{id}" - Current spreadsheet identifier
- MASTER_SPREADSHEET_ID: "{id}" - ID of the master spreadsheet
```

### Menu State Logic

The menu system in `onOpen.js` adapts based on these states:

```javascript
// In createBasicMenus()
if (!isMaster && !eoySetupComplete && !eoyReadyForEom) {
  // Fresh copy, pre-Continue: show the EOY setup steps plus the category
  // tools needed to build the new-year budget (the full 🏦 Budget menu is
  // not built in this state).
  periodMenu.addSubMenu(
    ui.createMenu("End of Year Setup")
      .addItem("1. Run Initial EOY Setup", "setupNewYearBudget")
      .addItem("2. Continue EOY Setup", "continueEOYSetup")
      .addItem("3. Finalize EOY Setup", "finalizeEOYSetup")
  );
  periodMenu.addSeparator();
  periodMenu.addSubMenu(buildEOYMaintainCategoriesMenu(ui)); // Maintain Budget ▸ Maintain Categories
}
```

`buildEOYMaintainCategoriesMenu()` returns the same Maintain Categories submenu used in normal mode (add / delete / manage lookups + the Step-by-Step, Safety and Automation guides). It is added **only** in this pre-Continue state. When the user runs `continueEOYSetup()`, that function sets `EOY_READY_FOR_EOM = true` and calls a `forceMenuRefresh` into the `eoyReadyForEom` menu state — which omits the submenu — so the category tools disappear at Continue, mirroring how the End of Month item appears only in the pre-Finalize window.

### State Transitions

1. **Fresh Copy Creation:**
   - `IS_MASTER = false` (imported from master)
   - `EOY_SETUP_COMPLETE = false`
   - `EOY_READY_FOR_EOM = false`
   - Menu shows only EOY setup options

2. **After Initial Setup:**
   - Properties updated to reflect progress
   - Menu options remain EOY-focused

3. **After Finalization:**
   - `IS_MASTER = true`
   - `EOY_SETUP_COMPLETE = true`
   - Menu shows normal operational options

## Technical Implementation Details

### Commitment Validation System

`endOfMonthProcessing()` includes a commitment validation system that offers user choice rather than blocking. Note the `!eoyReadyForEom` guard: during the EOY flow this check is **skipped** — `continueEOYSetup()` sets `EOY_READY_FOR_EOM = true`, so by the time the EOM step runs inside EOY, commitments have already been surfaced up-front by the EOY Warnings dialog in `showYearEndHelp()` / `checkAllBalances()`. The Fix Now / Ignore dialog below therefore only appears during a *normal* monthly End of Month run:

```javascript
// In endOfMonthProcessing() - commitment validation
if (!isDev && !eoyReadyForEom) {
  const commitmentCheck = validateCommitments();
  
  if (!commitmentCheck.isValid) {
    // Show user choice dialog instead of blocking
    const userChoice = ui.alert(
      "⚠️ Outstanding Commitments Warning",
      `The following commitments have not been met for ${monthNames[currentMonth]} ${currentYear}:\n\n` +
        commitmentCheck.issues.join("\n") +
        "\n\n⚠️ WARNING: These commitments are outstanding.\n\n" +
        "Choose your action:\n" +
        "• NO = Fix Now: Address commitments before EOM processing\n" +
        "• YES = Ignore: Proceed with EOM despite outstanding commitments",
      ui.ButtonSet.YES_NO
    );
    
    if (userChoice === ui.Button.NO) {
      // User chose to fix commitments - block EOM
      return;
    }
    // User chose to ignore - continue with EOM
  }
}
```

**Key Features:**

- **Non-blocking Design:** Users can choose to proceed despite outstanding commitments
- **Clear User Interface:** Intuitive button mapping (NO = Fix Now, YES = Ignore)
- **Month/Year Display:** Shows correct month and year from script properties
- **Detailed Issue Reporting:** Lists specific commitment problems for user review

### Improved Dialog System

All warning dialogs in the EOY process now use a draggable, user-friendly interface:

```javascript
// Example of draggable dialog implementation
function showEOYSetupIncompleteDialog(issues) {
  const htmlOutput = HtmlService.createHtmlOutput(`
    <div style="font-family: Arial, sans-serif; padding: 20px;">
      <h3>⚠️ EOY Setup Incomplete</h3>
      <p>The following issues must be resolved before finalization:</p>
      <ul>${issues.map(issue => `<li>${issue}</li>`).join('')}</ul>
      <p>Please address these issues and try again.</p>
    </div>
  `)
  .setWidth(500)
  .setHeight(300);
  
  SpreadsheetApp.getUi().showModelessDialog(htmlOutput, "EOY Setup Incomplete");
}
```

**Benefits:**

- **Better User Experience:** Dialogs can be moved and don't block the interface
- **Consistent Design:** All dialogs follow the same visual pattern
- **Improved Readability:** Better formatting and layout for complex information
- **Non-intrusive:** Users can continue working while reviewing dialog content

### Property Export/Import System

The property management system ensures continuity between master and copy:

```javascript
// Export from master to hidden sheet
function exportPropertiesToSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("_Properties");

  if (!sheet) {
    sheet = ss.insertSheet("_Properties");
    sheet.hideSheet();
  }

  const props = PropertiesService.getScriptProperties().getProperties();
  // Write properties to sheet for copying
}

// Import from hidden sheet in new copy
function importPropertiesFromSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("_Properties");

  if (sheet) {
    // Read properties from sheet and set in new copy
    // Adjust IS_MASTER to false for new copy
  }
}
```

### Verification System

Multiple verification points ensure system integrity:

1. **Sheet Structure Verification** (`validateSheets()`)
   - Verifies all required sheets exist
   - Checks sheet naming conventions
   - Validates critical named ranges

2. **Budget Formula Verification** (`verifyBudgetSetup()`)
   - Checks Annual Budget formulas
   - Validates Maintain Budget structure
   - Ensures proper formula references

3. **Balance Verification** (in `finalizeEOYSetup()`)
   - Banks sheet: "BOOKS BALANCED" indicator = 0
   - Annual Budget: "BUDGET BALANCED" indicator = 0
   - Maintain Budget: Balance indicator = 0

### Start Dates and Distribution Logic

The **Budget Start Dates** table the user edits in Step 3 is the named range **`IncomeStartDatesConfig`** on Maintain Budget — Column E holds the labels, Column F the values. It is read by **label lookup**, not fixed cell addresses, via `findConfigTableCell(label, "startDate")` (defined in `config/namedRanges.js`). This is why the table can grow or shrink: lookups scan the range for a matching label.

!!! warning "User-facing fragility"
    This is the one delicate, fully-manual step in EOY — everything else is scripted. The [Managing the Start Dates](../guides/yearly-tasks/end-of-year/setup.md#managing-the-start-dates) section of the user guide and the in-product *Create New Budget* dialog both warn novices about it. Keep those three places (dialog, setup guide, this section) in sync if the logic changes.

**How a row's distribution path is chosen** (`distributeBudget.js`, `distributeValuesFromRow()`):

- **Frequency ≤ 12** (1, 2, 3, 4, 6, 12) → `distributeWithSimpleMath()`. Even spread, offset by the per-row **Start Mth (Column J)**. **These never read the start-date table.**
- **Frequency > 12** (fortnightly = 26, weekly = 52) → `distributeWithDynamicCalculation()` → `getStartDateForItem(subcategoryName)`. This matches the **subcategory name exactly** against a Column E label (`getStartDateFromConfigTable()`) to find the real first pay-date, then `calculateMonthlyDistributions()` counts pay-days per month.

**Consequences of editing the table:**

- **Removing a row** is harmless unless a fortnightly/weekly category with that exact name is still distributed — in which case `getStartDateForItem()` returns `null` and `distributeWithDynamicCalculation()` throws `"Start date not configured for {name}"` (a clean stop, never a silent wrong result).
- **Adding a source** requires a Column E label matching the subcategory name character-for-character, plus a first pay-date within the budget period.
- **`Budget`, `Budget Period (months)`, and `Shopping Day` must remain** — `Budget` feeds every calculation; `Shopping Day` drives Groceries via `calculateFirstShoppingDate()`. EOY's start-date config dialog reads these defensively (`range ? value : default`), so missing optional rows degrade gracefully rather than crashing.

!!! info "Editing a per-item start date auto-flags the item for re-distribution"
    The config table is an `onEdit` exclusion zone (it returns before the normal auto-routines). But before bowing out, `handleMaintainBudgetEdit()` now calls `unDistributeForConfigStartDateChange()`: editing the date of a **per-item** row (`Pension`, `Wages`, `FTB`, or `Shopping Day` → Groceries) un-checks and reds that item's distributed flag (Column I) via `clearDistributionCheck()` — the same treatment a Budget/Freq/Start-Mth change gets — so a stale spread can't survive a date change. The mapping is `label === subcategory` (with `Shopping Day` → Groceries); the global rows below are skipped on purpose.

!!! info "Global anchors are warning-only protected"
    `Budget` (Budget Start Date) and `Budget Period` are **global** — every item's distribution depends on them — so changing one should only happen during EOY. `protectGlobalStartDateCells()` applies **warning-only** Google Sheets protection to those two cells: a manual edit pops "You're editing a protected cell — continue?" (a deterrent) but never hard-blocks, so EOY and any deliberate override still work, and script-driven `setValue` is unaffected. It runs automatically as the last step of `continueEOYSetup()` (so new yearly copies inherit it), is idempotent, and can be re-run by hand. A hard lock was deliberately rejected — it tends to bite on unforeseen edge cases. This is also why per-item un-distribute leaves the global rows alone.

!!! note "Legacy date files"
    `src/utility/dates/pensionDays.js`, `ftbDays.js` and `flexPayDays.js` are **fully commented-out legacy**. They wrote to the old "Fortnightly Payments mapped to Monthly" table and were superseded by the dynamic distribution above. Don't reintroduce them.

#### Fortnightly / weekly distribution mechanics (`calculateMonthlyDistributions`)

Three rules govern how a fortnightly (26) or weekly (52) item is spread across the 12 fiscal-month buckets. All three were the subject of bug fixes — be careful changing them.

1. **The pay-day interval is fixed by cadence, not derived from the frequency number.** Use 14 days for the fortnightly band (24–28) and 7 days for the weekly band (50–54). **Do not** use `Math.floor(364 / frequency)` for these. The actual pay-day count (26 *or* 27 — see below) is **no longer** written back into the FREQ cell — it once was, which jammed an out-of-range value into the dropdown and, by feeding the corrected number into the next run with a derived interval (`floor(364/27) = 13`), shrank the interval, inflated the count and never converged: the original "needs 27 → 29 → 31 …" runaway. With FREQ never overwritten, that runaway is now structurally impossible.

2. **The schedule is anchored on the item's own start date** (the `startDate` argument), which is the configured first pay-date for income sources, or the first Shopping Day for Groceries (already resolved by `getStartDateForItem()`). It must **not** re-derive the Shopping Day here — doing so made every fortnightly item share the grocery cadence and ignored per-income start dates.

3. **The budget period ends on the last day of the final fiscal month**, computed as `new Date(year, startMonth + budgetPeriod, 0)` — **not** `start + N months − 1 day`. The old formula overshot whenever the Budget Start Date wasn't the 1st: a `06/07` start ran the window to `05/07` next year (five days into the next FY), pulling an extra fortnight into the period, mis-bucketing it into the first month, and setting up a cross-year double-count (that pay-day becomes next year's start date).

!!! note "The 27-pay year is real, and handled informationally"
    A fortnightly schedule lands on **26 or 27** pay-days in a fiscal year (weekly: 52 or 53), depending on calendar alignment — a well-known payroll effect (e.g. a fortnightly income whose first pay-date is exactly 1 July gets 27 pay-days, since `26 × 14 = 364` and the 27th lands on 30 June inclusive).

    When the actual count differs from the nominal cadence, `distributeWithDynamicCalculation()` **changes nothing on the sheet**. It treats the Maintain Budget row as read-only: `F` (cadence) stays the user's valid dropdown choice, `G`/`E` stay as edit-time normalization (`normalizeRow`) settled them, and `D` keeps its reconciliation formula. The settled annual budget is simply spread across all the real pay-days, and any few-cent rounding residue is reconciled by the user at the **Missing** balance (E84) — exactly as for any other normalization. A `notifyExtraPaymentPeriod()` info dialog ("Extra Payment This Year") tells the user; the old `updateMaintainBudgetForActualPayments()` writeback is retained only as a documented deprecated no-op.

    27 is correct **as long as** next year's start date is set to the genuine next pay-day, so nothing is recounted. This is why the user guide stresses that the start date must be an *actual* pay-date.

!!! success "Budget Start Date is auto-advanced (then verified)"
    `setupNewYearBudget()` calls `autoAdvanceBudgetStartDate()` to set the new Budget Start Date to **closing year + 1 year** — the household FY always starts on the same day, so it is deterministic. This closes the date-typo class (the `06/07` mistake that started the fortnightly investigation); the user only **verifies** the pre-filled value. It is anchored on the `PRE_EOY_BUDGET_START` snapshot, making it **idempotent** (re-running Step 1 won't double-advance) and **override-safe** (if the date already differs from the closing-year value it is left alone). Non-destructive on any uncertainty, and **gated to copies only** so it can never touch the live master's current-year date.

    The warn-only "not the 1st" confirm in `continueEOYSetup()` remains as a backstop for a deliberate non-standard period; since auto-advance keeps the same day-of-month, a clean `01/07` baseline stays clean.

!!! success "Closed — income start-date validation is now interval-tight"
    `checkNewYearStartDatesReady()` previously only checked each income start date fell **within the 12-month window**, so a fortnightly source could legally start months in and silently miss early-year payments. It now requires, for **fortnightly/weekly** items, that the first pay-date land **within one pay-interval** of the Budget Start Date (14 / 7 days — cadence read from Maintain Budget Col F; non-cadence items keep the window check). The `continueEOYSetup()` gate already **hard-blocks** (non-dev) on any issue, and the message states the exact valid range. This catches the three real errors: a left-over last-year date, a typo, and a date set too far in.

    The live green/red highlight (`refreshStartDateValidityHighlights()`) uses the **same** interval rule, so what shows green is exactly what the gate will pass.

!!! warning "Known limitations — start-date validation (deferred, not bugs)"
    Both deliberately deferred (see EOY rehearsal 2026 / one-day-to-live freeze). The **gate remains the safety backstop in every case**; these affect only the convenience layer:

    1. **Mid-year item introductions are not supported by the interval rule.** The "first pay-date within one pay-interval of the Budget Start Date" assumption holds only for items present from the *start* of the budget year. An item genuinely introduced **mid-year** (e.g. a car loan bought in month 5 — you don't budget the months already passed) legitimately has a start date months in, which the interval check would flag **red** / the gate would **block**. Because `refreshStartDateValidityHighlights()` runs on *every* config-table edit year-round (not just during EOY), a mid-year addition would also show a misleading red. A proper fix needs a notion of "introduced part-way through the year" (e.g. an effective-from month) — a real rabbit hole, future work.

    2. **Orphan config rows are not highlighted.** The highlight colours a row only when it finds a matching fortnightly/weekly item in Maintain Budget (to read the cadence). A config start-date row with **no matching item** (or a non-cadence one) is left uncoloured — it is *not* turned red. The validation gate is **not** fooled: for such rows it falls back to the 12-month window check, so a year-early orphan date (e.g. `01/08/2025`) still **blocks** at Continue EOY Setup. Only the visual cue has the gap.

### Manual Master Archiving Process

The archiving system requires **user-initiated action** rather than automatic archiving:

#### What Actually Happens During EOY Finalization

```javascript
// In proceedWithFinalization() - NO automatic archiving occurs
function proceedWithFinalization() {
  // 1. Mark new copy as master
  props.setProperty("IS_MASTER", "true");
  props.setProperty("EOY_SETUP_COMPLETE", "true");
  
  // 2. Show completion dialog with archiving instructions
  const htmlContent = `
    <h3>THEN: Archive Your Old Spreadsheet</h3>
    <p><strong>Go to your old spreadsheet (last year's budget) and archive it:</strong></p>
    <p>Settings → ⚠️ Advanced → Archive This Master</p>
  `;
  
  // 3. User must manually navigate to old master and run archiveThisMaster()
  // NO automatic archiving happens here
}
```

#### User-Initiated Archiving Function

```javascript
function archiveThisMaster() {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const ui = SpreadsheetApp.getUi();
    
    // 1. Get fiscal year for naming
    const fiscalYear = getFiscalYearFromSpreadsheet(ss);
    const currentName = ss.getName();
    const archiveName = `${currentName}_ARCHIVED_FY${fiscalYear.toString().slice(-2)}`;
    
    // 2. Confirm with user
    const confirmResponse = ui.alert(
      "📦 Archive This Master",
      `This will rename to: "${archiveName}" and mark as archived. Continue?`,
      ui.ButtonSet.YES_NO
    );
    
    if (confirmResponse !== ui.Button.YES) return false;
    
    // 3. Create archive metadata sheet
    const archiveSheet = ss.insertSheet("_Archive");
    archiveSheet.hideSheet();
    
    // 4. Update properties to mark as archived
    props.setProperty("IS_MASTER", "false");
    props.setProperty("IS_ARCHIVED", "true");
    props.setProperty("ARCHIVED_DATE", new Date().toISOString());
    
    // 5. Rename the spreadsheet
    ss.rename(archiveName);
    
    return true;
  } catch (error) {
    console.error("Error in archiveThisMaster:", error);
    return false;
  }
}
```

#### Key Technical Points

- **No Automatic Archiving:** The EOY finalization does NOT automatically archive the old master
- **User Control:** Archiving is completely user-initiated via Settings menu
- **Two-Step Process:** EOY finalization + Manual archiving = Complete EOY process
- **Reversible:** `restoreFromArchive()` function can undo the archiving

#### After Finalization: Re-point CLASP and Rename the Script Project

Once the copy has become the new master, two **once-a-year developer housekeeping steps** are needed before you resume development. Neither happens automatically.

**1. Re-point CLASP to the new master's Script ID**

Because the script is *container-bound*, *File → Make a copy* cloned it into a brand-new, independent Script ID. `clasp push` only ever targets the Script ID in `.clasp.json`, so until you update it you are still pushing to **last year's (now archived) master**.

- In the new spreadsheet: **Extensions → Apps Script → ⚙ Project Settings** → copy the **Script ID** (or lift it from the editor URL, between `/projects/` and `/edit`).
- Back up the current config, then swap the ID in `.clasp.json`:

```bash
# From the budget-app repo root
cp .clasp.json ".clasp.json.archived-$(date +%Y%m%d)"   # keeps last year's ID for reference (gitignored)
# then edit .clasp.json and replace "scriptId" with the new master's ID
```

- Verify the link before trusting it — pull into a temp dir and diff against local `src/`:

```bash
rm -rf /tmp/gas-verify && mkdir -p /tmp/gas-verify && cp .clasp.json /tmp/gas-verify/
( cd /tmp/gas-verify && clasp pull )
diff -rq src/ /tmp/gas-verify/src/     # business-logic files should be identical
```

  A cosmetic `appsscript.json` difference is expected (Google reformats the manifest on pull — the OAuth scopes and runtime are unchanged). All `.js` business-logic files should report identical.

**2. Rename the Apps Script project**

The copy inherited **last year's project title**, so the active master and the archived one look identical in the editor — a real footgun. `clasp` has no rename command and the title is not stored in any synced file, so this is a **manual editor step**: open the project, click the title (top-left), and rename it to encode the current budget year, e.g.:

- Active master: `GS Budget App — FY2026-27`
- Archived master: `GS Budget App — FY2025-26 (Archived)`

Encoding the year is deliberate: because the title carries forward on every copy, next year's fresh copy will *still* read `FY2026-27`, which immediately flags it as "rename me to the new year." That turns renaming the copy into a natural, self-reminding annual step, and no two active projects ever share a name.

## Known Technical Limitations

### Print Buttons and the Local Print Subsystem

**Issue:** The "Print Instructions" buttons in the EOY dialogs sometimes do nothing — either the browser print preview never appears, or it appears but pressing **Print** sends nothing to the printer.

**This is NOT a budget-app / Apps Script bug.** It was chased at length during UAT and conclusively ruled out:

- The *same* GAS/HTML code prints fine immediately after a PC reboot and fails later in the same session.
- The button that ultimately fails ("Print" in the screenshot) is **Chrome's own native print dialog** — entirely outside our HTML. By the time that preview is showing, `window.print()` has already done its whole job; everything after is **Chrome → the OS print spooler (CUPS) → the printer driver**.
- The failure is *stateful*: it accumulates during a session and is cleared by a reboot (which restarts both `cupsd` and Chrome). That is the classic signature of a **stuck CUPS print queue**, or less commonly a hung Chrome print-backend process.

**Impact:** Cosmetic/UX only, and **outside the realm of normal user involvement** — a user just needs to know "if Print does nothing, it's your PC's print queue, not the budget; reboot (or restart the print service) and try again." It does not affect any budget data or the EOY process itself.

**Related code (leave as-is):** the `setupNewYearBudget()` dialog carries an `@media print` rule so that *when* it does print, the fixed-height/scrolling layout flows onto one clean page with the footer buttons stripped. That fix is unrelated to the spooler problem but worth keeping.

**Diagnosis & recovery (Manjaro / CUPS):**

```bash
# Healthy baseline looks like: cups active, printer "idle" + "enabled", empty queue
systemctl is-active cups
lpstat -p <PRINTER>     # printer state (e.g. MFC7360N)
lpstat -o               # queued jobs (empty = none stuck)

# Recovery without a full reboot:
cancel -a               # clear stuck jobs
cupsenable <PRINTER>    # re-enable if paused/stopped
cupsaccept <PRINTER>
sudo systemctl restart cups   # restart just the spooler

# Discriminator — is it CUPS or Chrome?
# Press Ctrl+P on any ordinary web page and print to the same printer:
#   - also fails  -> CUPS / printer (use the commands above)
#   - only Sheets fails -> Chrome print process (fully quit & reopen Chrome)
```

### Script Property Isolation

**Issue:** Google Apps Script security model prevents modifying script properties of other spreadsheets.

**Impact:** Archived masters retain `IS_MASTER = true` in their script properties.

**Mitigation Strategies:**

1. **Renamed Title** - Archived spreadsheets have clear "\_ARCHIVED_FY{year}" suffix
2. **Archive Metadata** - Hidden "\_Archive" sheet marks archival status
3. **User Documentation** - Clear guidance to avoid using archived spreadsheets

### Google Authorization User Experience

**Issue:** Google shows intimidating "unsafe" warnings for all custom spreadsheet scripts.

**Impact:** Users may be reluctant to continue authorization due to scary warning language.

**User Experience Challenges:**

- "Google hasn't verified this app" warning appears threatening
- "Go to Budget-YYYY-Scripts (unsafe)" link seems dangerous (the script name matches the copy's name, e.g. `Budget-2026-Scripts`)
- Users may abandon the process thinking something is wrong

**Mitigation Strategies:**

1. **Clear Documentation** - Detailed explanation that warnings are normal
2. **Step-by-Step Instructions** - Specific guidance through each authorization step
3. **Reassurance** - Explicit statements that the process is safe and expected

## Testing and Quality Assurance

### Comprehensive Testing Checklist

#### Before Testing Session
- [ ] All changes pushed to MASTER spreadsheet
- [ ] Old test copies deleted
- [ ] Fresh copy created from MASTER
- [ ] Test environment prepared

#### During Testing - Step 1 (Initial Setup)
- [ ] Month restriction working (if testing in non-June month)
- [ ] Help dialog displays correctly with documentation links
- [ ] Property export completes successfully
- [ ] New copy creation process works
- [ ] Menu system shows only EOY options in new copy

#### During Testing - Step 2 (Initial Setup & Budget Build)
- [ ] Authorization works (OK → Advanced → Go to Budget-YYYY-Scripts → Select all → Continue)
- [ ] Verification, Timezone, and "New Year Budget Setup" dialogs complete
- [ ] Maintain Budget ▸ Maintain Categories is available during the build window (incl. 📋 Step-by-Step Instructions)
- [ ] Manual budget build works (start dates Col F, amount + frequency, Distribute to Annual Budget)
- [ ] Budget balance validation works
- [ ] Continue setup runs; start-date guard blocks if dates are unset; Maintain Categories disappears after Continue

#### During Testing - Step 3 (Finalization)
- [ ] Final verification checks function properly
- [ ] Master archiving completes without errors
- [ ] New copy marked as master successfully
- [ ] Menu system updates to normal operational mode
- [ ] All transaction sheets properly cleared
- [ ] Commitment validation dialogs work correctly
- [ ] User choice options (Fix Now vs Ignore) function properly

#### Post-Testing Verification
- [ ] Master functionality works in new spreadsheet
- [ ] Archived master properly renamed and marked
- [ ] Historical data preserved in archived master
- [ ] No script errors in new master
- [ ] Documentation links work correctly

### Testing Functions

Several helper functions support testing:

```javascript
// Test archiving without affecting production
function testArchiveMaster() {
  const currentId = SpreadsheetApp.getActiveSpreadsheet().getId();
  return archiveLegacyMaster(currentId, true); // testMode = true
}

// Test EOY process with safety checks
function testEOYProcess() {
  console.log("Starting EOY test process...");
  return setupNewYearBudget(true); // testMode = true
}

// Safe refresh function for testing
function runRefreshSafely() {
  try {
    SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Annual Budget");
    // Additional safety checks
  } catch (error) {
    console.error("Refresh safety check failed:", error);
  }
}
```

## Performance Considerations

### Optimization Strategies

1. **Minimal Sheet Operations:**
   - Batch range operations where possible
   - Avoid excessive individual cell operations
   - Use getValues()/setValues() for bulk operations

2. **Property Management:**
   - Cache frequently accessed properties
   - Minimize property service calls
   - Use batch property operations

3. **Verification Efficiency:**
   - Combine multiple checks into single functions
   - Early exit on validation failures
   - Provide specific error messages for quick resolution

### Resource Management

```javascript
// Example of efficient batch operations
function updateMonthlyHeaders() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                             .getSheetByName("Annual Budget");

  // Get all headers in one operation
  const headerRange = sheet.getRange(1, 1, 1, sheet.getLastColumn());
  const headers = headerRange.getValues()[0];

  // Process headers in memory
  const updatedHeaders = headers.map(header => {
    // Update logic here
    return processHeader(header);
  });

  // Write all headers back in one operation
  headerRange.setValues([updatedHeaders]);
}
```

## Future Enhancement Opportunities

### Planned Improvements

1. **Enhanced Pre-EOY Validation:**
   - Automatic verification of balance requirements
   - Account reconciliation status checking
   - Data integrity validation before process start

2. **Improved Error Recovery:**
   - Process checkpoint system for resuming interrupted operations
   - Better error messages with specific resolution steps
   - Automatic retry mechanisms for transient failures

3. **Advanced State Management:**
   - More granular progress tracking
   - Session persistence across browser refreshes
   - Better handling of concurrent user access

### Technical Debt Reduction

1. **Script Property Limitation Resolution:**
   - Research Google Workspace APIs for property management
   - Implement alternative master tracking systems
   - Develop more robust archiving mechanisms

2. **Code Organization:**
   - Modularize large functions for better maintainability
   - Implement consistent error handling patterns
   - Add comprehensive inline documentation

3. **Testing Infrastructure:**
   - Automated testing framework for EOY process
   - Mock data generation for consistent testing
   - Performance benchmarking tools

## Security and Access Considerations

### Permission Requirements

The EOY process requires specific permissions:

- **Script execution** in both master and new copy
- **Spreadsheet access** for reading/writing operations
- **File creation** for making copies
- **Property management** for state tracking

### Security Best Practices

1. **Property Validation:**
   - Validate all imported properties
   - Sanitize user inputs in configuration dialogs
   - Check property values before using in operations

2. **Error Information Exposure:**
   - Avoid exposing sensitive system information in error messages
   - Log detailed errors for developers without showing to users
   - Provide user-friendly error messages with actionable guidance

3. **State Consistency:**
   - Verify state transitions are atomic where possible
   - Implement rollback mechanisms for critical operations
   - Validate system state before proceeding with operations

This developer guide provides the technical foundation for maintaining and enhancing the EOY process. For implementation details of specific functions, refer to the source code in `src/utility/yearEndBudget.js` and related files.