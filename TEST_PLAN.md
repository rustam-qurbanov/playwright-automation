# Sauce Demo Test Plan

This document outlines the comprehensive test plan for the Sauce Demo UI automation framework. Scenarios are prioritized from most critical (Core Flows) to less critical edge cases.

### Test ID Legend:
* **AUTH-** (Authentication) — тесты на логин/логаут
* **E2E-** (End-to-End) — полные сквозные пути
* **CART-** (Cart) — всё что связано с корзиной
* **CHK-** (Checkout) — форма оформления заказа и расчеты
* **INV-** (Inventory) — витрина товаров и сортировка
* **SYS-** (System) — системные проверки (бургер-меню, футер)

> **📊 Automation Status:** 5 / 17 scenarios automated (~29%)

## 🔴 Priority 1: Critical Core Flows (Smoke)
These tests verify that the fundamental purpose of the application works. If these fail, the application is fundamentally broken.

- [x] **[AUTH-01] Successful Login:** User can log in with valid credentials (`standard_user`).
- [x] **[E2E-01] End-to-End Checkout:** User can add an item to the cart, proceed through checkout steps, and successfully place an order.

## 🟠 Priority 2: Authentication & Security
Tests validating access control and session management.

- [x] **[AUTH-02] Invalid Credentials:** User sees an error when logging in with incorrect username/password.
- [ ] **[AUTH-03] Locked Out User:** User sees a specific "locked out" error when logging in with `locked_out_user`.
- [ ] **[AUTH-04] Logout Flow:** Logged-in user can successfully log out via the burger menu and is redirected to the login page.
- [ ] **[AUTH-05] Protected Routes:** User cannot access the `/inventory.html` page directly without logging in first.

## 🟡 Priority 3: Cart Logic & State Management
Tests validating the core shopping cart mechanics.

- [x] **[CART-01] Cart Badge Update:** Adding an item updates the cart badge counter to 1.
- [ ] **[CART-02] Add Multiple Items:** Adding multiple different items updates the cart badge and cart page list correctly.
- [ ] **[CART-03] Remove from Inventory:** User can remove an added item directly from the Inventory page (button changes from Add to Remove).
- [ ] **[CART-04] Remove from Cart:** User can remove an item from the Cart page, and the cart becomes empty.
- [ ] **[CART-05] State Persistence:** Cart items persist even if the user refreshes the page (simulating real browser usage).

## 🔵 Priority 4: Checkout Validations & Calculations
Tests validating form logic, mathematical calculations, and edge cases in the checkout process.

- [x] **[CHK-01] Checkout Form Validation:** User sees errors if First Name, Last Name, or Zip Code are left empty on the checkout info page.
- [ ] **[CHK-02] Total Price Calculation:** The "Item total" on the overview page equals the exact mathematical sum of all items in the cart.
- [ ] **[CHK-03] Tax Calculation:** The total sum correctly includes the 8% (or whatever rate is specified) tax rate.

## 🟣 Priority 5: Inventory Sorting & Product Details
Tests validating the product catalog functionality.

- [ ] **[INV-01] Sorting - Price (Low to High):** Products are correctly ordered by price ascending.
- [ ] **[INV-02] Sorting - Price (High to Low):** Products are correctly ordered by price descending.
- [ ] **[INV-03] Sorting - Name (Z to A):** Products are correctly ordered in reverse alphabetical order.
- [ ] **[INV-04] Product Details Match:** Clicking a product opens its detail page, and the name, description, and price exactly match what was on the inventory page.

## ⚪ Priority 6: Extra / Menu Options
Tests for secondary application features.

- [ ] **[SYS-01] Reset App State:** Clicking "Reset App State" in the burger menu clears the cart and resets all "Remove" buttons back to "Add to cart".
- [ ] **[SYS-02] Social Media Links:** Footer links correctly point to Sauce Labs Twitter, Facebook, and LinkedIn pages.
