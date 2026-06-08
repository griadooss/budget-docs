---
title: 'Loans & Commitments'
description: 'How to track personal loans and manage budget commitments'
---

# Loans & Commitments

Both of these tools live under **🏦 Budget > Maintain Budget**. They cover two different jobs:

- **💰 Loan Transactions** — review money you have lent to (or been repaid by) other people.
- **📋 Commitment Management** — flag budget items you want the system to check before closing a month or year.

---

## 💰 Loan Transactions

This is a **reporting tool**. It does not create loans — it shows you, per person, what has been lent and repaid, and the resulting balance.

!!! info "How loans are tracked"
    A "loan" is made up of two things:

    1. **A participant** — the person you are lending to or borrowing from. Participants are defined in the **Banks** sheet, in the **LOAN REGISTER** section (the *TO* column).
    2. **Loan transactions** — ordinary entries in your **Cash Flow** sheet that have been categorised as **`LOAN_OUT`** (money you lent out) or **`LOAN_IN`** (money repaid to you), with the participant's name in the **ITEM** column.

    You record loan movements the same way as any other transaction (import or manual entry); the Loan Transactions tool simply gathers them together for review.

### Viewing a participant's loans

1. Click **🏦 Budget > Maintain Budget > 💰 Loan Transactions**.
2. The sidebar opens and lists every participant found in the Loan Register.
3. Click a participant to open their **loan listing dialog**, which shows:
    - Each loan transaction (date, amount, type, description, account, and whether it is reconciled)
    - A **summary**: total lent out, total repaid, and the **balance** (total repaid minus total lent)
4. Use **🔄 Refresh Participant List** if you have just added or removed a participant and don't see the change yet.

!!! note "No participants showing?"
    If the sidebar says *"No loan participants found"*, check the **Banks** sheet **LOAN REGISTER** section — participant names must be present in the *TO* column.

!!! tip
    Because loans rely on the `LOAN_OUT` / `LOAN_IN` categories, make sure each loan transaction is categorised correctly during reconciliation, otherwise it won't appear in the totals.

---

## 📋 Commitment Management

A **commitment** is a budget item you want the system to verify before the End of Month (EOM) and End of Year (EOY) processes — a way of saying *"don't let me close the books until I've actually honoured this."*

Commitments are stored as **`COM` rows in the LookUps sheet**, each tied to a category and subcategory, with an **Active** flag.

### Opening the manager

Click **🏦 Budget > Maintain Budget > 📋 Commitment Management**. A dialog opens listing your existing commitments, with a **+ New** button to add one.

### Creating a commitment

1. Click **+ New**.
2. Fill in the **Commitment Details**:
    - **Category Code** / **Category Name**
    - **Subcategory Code** / **Subcategory Name**
    - **Active** — tick this so the commitment *"will be checked before EOM/EOY"*
3. Click **Create Commitment**.

### Editing or deleting

- Select an existing commitment, change its details, and click **Save Changes**.
- To remove one, select it and click **Delete**.

### What the "Active" flag does

When you run **End of Month** or **End of Year**, the system checks every **active** commitment by comparing its **budgeted amount against the actual amount** for the current month.

- If a commitment has been **met**, processing continues normally.
- If a commitment has **not** been met, it is flagged and you are offered a choice:
    - **Fix Now** — stop and correct the shortfall first, or
    - **Ignore** — proceed anyway.

!!! tip
    Untick **Active** for a commitment you want to keep on record but not enforce for now — it stays in the list but is skipped during EOM/EOY checks.

!!! warning
    Commitment checking only works if the commitment's category and subcategory match real entries in your **Annual Budget**. If you rename a category, update the matching commitment too.

---

## Related

- [Menu Reference](menu-reference.md) — where these items sit in the menus
- [End of Month](../monthly-tasks/end-of-month.md) — when commitment checks run each month
- [End of Year Process Overview](../yearly-tasks/end-of-year/overview.md) — commitment validation during EOY
