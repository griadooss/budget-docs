---
title: 'Categorizing Transactions'
description: 'How to categorize transactions and manage categories'
---

# Categorizing Transactions

This guide covers how to categorize transactions and manage the category system in your budget.

## Overview

Categorization is the process of assigning transactions to specific income or expense categories. This helps you track spending patterns, analyze budget performance, and generate meaningful reports.

## Category System

### Structure
The category system uses a two-level hierarchy:

=== "Main Categories"

    - High-level classifications
    - Income vs Expense types
    - Examples: Food, Transport, Salary

=== "Subcategories"

    - Detailed breakdowns
    - More specific classifications
    - Examples: Groceries, Fuel, Wages

### Category Types

=== "Income Categories"

    - **INC prefix** - Income categories
    - **Green color coding** - Visual identification
    - **Examples:** Salary, Gifts, Investment Income

=== "Expense Categories"

    - **EXP prefix** - Expense categories
    - **Red color coding** - Visual identification
    - **Examples:** Food, Transport, Utilities

## Managing Categories

### Access Category Manager
1. Open your budget spreadsheet
2. Click **⚙️ Settings > Sheet Settings > Manage Categories**
3. The Category Manager will open in a new window

### Adding New Categories

1. **Click "Add Category"** - In the Category Manager
2. **Enter category name** - Use clear, descriptive names
3. **Select category type** - Income or Expense
4. **Click "Save"** - Category is added to the system

### Editing Categories
1. **Select category** - Click on the category in the list
2. **Click "Edit"** - Opens edit dialog
3. **Modify name** - Update category name as needed
4. **Save changes** - Click "Save" to update

### Activating/Deactivating Categories
1. **Select category** - Click on the category in the list
2. **Toggle status** - Click "Activate" or "Deactivate"
3. **Confirm change** - Status updates immediately

### Adding Subcategories
1. **Select main category** - Click on the parent category
2. **Click "Add Sub-category"** - In the subcategory panel
3. **Enter subcategory name** - Use specific, descriptive names
4. **Save subcategory** - Click "Save" to add

## Categorizing Transactions

### During Reconciliation
1. **Open Reconciliation Dashboard** - 🏦 Budget > Reconciliation Dashboard
2. **Select transaction** - Click on unmatched transaction
3. **Click "Add to Cash Flow"** - Opens categorization dialog
4. **Choose category** - Select from dropdown menu
5. **Select subcategory** - Choose specific subcategory
6. **Add description** - Modify transaction description
7. **Save transaction** - Click "Add Transaction"

### Manual Entry
1. **Open Import Tool** - 🏦 Budget > Import Bank Transactions
2. **Switch to Manual tab** - Click "Manual Entry"
3. **Fill transaction details** - Date, amount, description
4. **Select category** - Choose from dropdown
5. **Add to pending list** - Click "Add Transaction"
6. **Process all** - Click "Process All" when done

### Split Transactions
1. **Identify split** - Look for blue highlighted groups
2. **Click "Find Match"** - Locate bank transaction
3. **Add splits** - Click "Add Split" for each part
4. **Assign categories** - Different category for each split
5. **Verify total** - Ensure splits equal bank amount
6. **Save splits** - Click "Save Split Transactions"

## Category Best Practices

### Naming Conventions
- **Use clear names** - Avoid abbreviations
- **Be consistent** - Use same names throughout
- **Be specific** - "Groceries" not just "Food"
- **Use hierarchy** - Main category + subcategory

### Organization Tips
- **Group related items** - Keep similar categories together
- **Use subcategories** - Break down main categories
- **Regular cleanup** - Remove unused categories
- **Standardize names** - Use consistent terminology

### Common Categories

=== "Income Categories"

    - **Salary/Wages** - Regular employment income
    - **Investment Income** - Dividends, interest
    - **Gifts** - Cash gifts, presents
    - **Other Income** - Miscellaneous income

=== "Expense Categories"

    - **Food & Dining** - Groceries, restaurants
    - **Transport** - Fuel, public transport
    - **Utilities** - Electricity, water, gas
    - **Entertainment** - Movies, hobbies
    - **Shopping** - Clothing, household items
    - **Healthcare** - Medical expenses

## Category Management

### Active vs Inactive
- **Active categories** - Available for selection
- **Inactive categories** - Hidden from dropdowns
- **Toggle status** - Activate/deactivate as needed
- **Historical data** - Inactive categories preserve history

### Category Hierarchy
- **Main categories** - High-level classifications
- **Subcategories** - Detailed breakdowns
- **Consistent structure** - Maintain hierarchy
- **Easy navigation** - Clear organization

### Bulk Operations
- **Sync ACTIVE flags** - Synchronize category status
- **Validate ACTIVE flags** - Check for inconsistencies
- **Bulk distribute** - Distribute budget values

## Troubleshooting

### Common Issues

??? warning "Category Not Found"
    **Problem:** Category not in dropdown

    **Solution:**

    - Check if category is active
    - Verify category type (Income/Expense)
    - Refresh the dropdown

??? warning "Wrong Category Type"
    **Problem:** Income category for expense transaction

    **Solution:**

    - Select correct category type
    - Check transaction type setting
    - Verify category assignment

??? warning "Missing Subcategories"
    **Problem:** No subcategories available

    **Solution:**

    - Add subcategories to main category
    - Check if main category is active
    - Verify subcategory status

??? warning "Category Manager Issues"
    **Problem:** Can't access category manager

    **Solution:**

    - Check menu permissions
    - Verify spreadsheet access
    - Try refreshing the page

## Advanced Features

### Category Statistics
- **Usage tracking** - Monitor category usage
- **Budget analysis** - Compare actual vs budget
- **Trend analysis** - Track spending patterns
- **Report generation** - Category-based reports

### Import Templates
- **Save mappings** - Store category assignments
- **Auto-categorization** - Based on transaction descriptions
- **Template management** - Edit and update templates

### Bulk Operations
- **Category updates** - Modify multiple categories
- **Status changes** - Activate/deactivate in bulk
- **Data migration** - Move categories between systems

## Best Practices

!!! tip "Best Practices"
    - Use consistent category names
    - Create meaningful subcategories
    - Regularly review and clean up categories
    - Use active categories only
    - Maintain category hierarchy
    - Document category purposes

## Next Steps

After categorizing:

1. **Review categorization** - Check for consistency
2. **Update categories** - Add new categories as needed
3. **Generate reports** - Analyze spending patterns
4. **Adjust budget** - Update budget based on categories

!!! note
    For detailed budget management, see the [Budget Management Guide](../user-manual/basic-operations.md).