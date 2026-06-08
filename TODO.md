# Documentation Backlog

Low-priority enhancements for the Budget Docs manual. Nothing here is broken —
these are optional improvements to pick up when time allows.

## Enhancements

- [ ] **Add screenshots of the EOY dialogs.**
  The manual is currently text-only (the only image is the decorative
  `docs/images/balance.svg` on the home page). The End of Year dialogs were
  reworked in the app in 2026 (guidance text, print button, sticky footers,
  theming — budget-app commit `e4fd07d`), and visuals would help users follow
  the multi-step EOY process.

  **How to do it:**
  1. Capture the EOY dialogs from the live spreadsheet as PNGs.
  2. Drop them in `docs/images/` (e.g. `eoy-step1.png`, `eoy-step2.png`).
  3. Embed them in the relevant pages under
     `docs/guides/yearly-tasks/end-of-year/` with descriptive captions.

  *Note: capturing the screenshots must be done by hand from the Google Sheet —
  it can't be automated from this repo.*
