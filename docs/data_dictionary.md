# Retail Intelligence Analytics - Data Dictionary

> **Source:** `data_audit.ipynb`. Column names, pandas dtypes, row counts and quality-check results below are transcribed from executed notebook outputs. Descriptions are interpretations of column names, not independently verified dataset documentation.

## 1. Dataset inventory

| Dataset | Rows | Columns | Missing cells | Exact duplicate rows |
|---|---:|---:|---:|---:|
| `transactions` | 100,000 | 16 | 0 | 0 |
| `products` | 500 | 9 | 0 | 0 |
| `supplier_costs` | 998 | 12 | 0 | 0 |
| `price_history` | 18,000 | 12 | 0 | 0 |
| `inventory` | 500 | 7 | 0 | 0 |
| `returns` | 7,126 | 8 | 0 | 0 |
| `customers` | 8,000 | 11 | 0 | 0 |
| `marketing_spend` | 216 | 13 | 0 | 0 |

**Total:** 126,340 records across eight datasets; 88 columns in total (counting columns separately in each table). Found no missing cells or fully duplicated rows in the loaded CSVs. 

## 2. Field definitions and inferred grains

**Observed type** means the pandas dtype reported by the notebook; `str` denotes text, including unparsed dates and alphanumeric identifiers. 

### transactions.csv

- **Purpose:** Transaction-level sales activity.
- **Proposed grain:** One row per transaction_id (candidate; uniqueness verified).
- **Primary key:** transaction_id (verified unique and non-null).

| Column | Observed pandas type | Business description |
|---|---|---|
| `transaction_id` | `str` | Transaction identifier |
| `customer_id` | `str` | Customer identifier; links to customers |
| `product_id` | `str` | Product identifier; links to products |
| `date` | `str` | Transaction date |
| `quantity` | `int64` | Units purchased in the transaction |
| `unit_price_usd` | `float64` | Recorded unit selling price in USD |
| `discount_pct` | `float64` | Recorded discount fraction (0–1 scale observed in transactions) |
| `revenue_usd` | `float64` | Recorded transaction revenue in USD |
| `cost_usd` | `float64` | Recorded transaction cost in USD |
| `profit_usd` | `float64` | Recorded transaction profit in USD |
| `shipping_cost_usd` | `float64` | Recorded shipping cost in USD |
| `channel` | `str` | Sales or marketing channel label (context dependent) |
| `payment_method` | `str` | Payment method used |
| `status` | `str` | Transaction status |
| `country` | `str` | Country label |
| `category` | `str` | Product category label |

### products.csv

- **Purpose:** Product master catalogue.
- **Proposed grain:** One row per product_id (verified).
- **Primary key:** product_id (verified unique and non-null).

| Column | Observed pandas type | Business description |
|---|---|---|
| `product_id` | `str` | Product identifier; links to products |
| `name` | `str` | Product name |
| `category` | `str` | Product category label |
| `brand` | `str` | Product brand |
| `unit_price_usd` | `float64` | Recorded unit selling price in USD |
| `unit_cost_usd` | `float64` | Recorded unit product or supplier cost in USD |
| `weight_kg` | `float64` | Product weight in kilograms |
| `is_active` | `bool` | Whether product is marked active |
| `launch_date` | `str` | Product launch date |

### supplier_costs.csv

- **Purpose:** Supplier purchasing costs and operational characteristics by product.
- **Proposed grain:** One row per product–supplier offering (candidate; not verified).
- **Primary key:** Candidate: (product_id, supplier_name); verify uniqueness.

| Column | Observed pandas type | Business description |
|---|---|---|
| `product_id` | `str` | Product identifier; links to products |
| `category` | `str` | Product category label |
| `supplier_name` | `str` | Supplier name |
| `supplier_rank` | `int64` | Supplier ranking value; ranking definition not verified |
| `unit_cost_usd` | `float64` | Recorded unit product or supplier cost in USD |
| `ordering_cost_usd` | `float64` | Recorded ordering cost in USD |
| `annual_holding_cost_usd` | `float64` | Recorded annual inventory holding cost in USD |
| `holding_cost_pct` | `float64` | Recorded holding-cost fraction or rate; scale to verify |
| `lead_time_days` | `int64` | Supplier lead time in days |
| `min_order_qty` | `int64` | Minimum order quantity |
| `reliability_score` | `float64` | Supplier reliability score; scale and definition to verify |
| `is_primary` | `bool` | Whether supplier is designated primary |

### price_history.csv

- **Purpose:** Monthly product pricing, competitor prices and sales indicators.
- **Proposed grain:** One row per product and year_month (candidate; not verified).
- **Primary key:** Candidate: (product_id, year_month); verify uniqueness.

| Column | Observed pandas type | Business description |
|---|---|---|
| `product_id` | `str` | Product identifier; links to products |
| `category` | `str` | Product category label |
| `year_month` | `str` | Year-month period; source stored as text |
| `listed_price_usd` | `float64` | Recorded listed selling price in USD |
| `base_price_usd` | `float64` | Recorded baseline price in USD |
| `competitor_price_usd` | `float64` | Recorded competitor price in USD |
| `price_index` | `float64` | Recorded relative price index; calculation to verify |
| `is_promotional` | `bool` | Whether price period is marked promotional |
| `price_elasticity` | `float64` | Recorded price elasticity measure; estimation method not verified |
| `units_sold` | `int64` | Recorded units sold in the period |
| `revenue_usd` | `float64` | Recorded transaction revenue in USD |
| `margin_pct` | `float64` | Recorded margin fraction or percentage; scale to verify |

### inventory.csv

- **Purpose:** Product stock levels and replenishment settings.
- **Proposed grain:** One row per product (candidate; not verified).
- **Primary key:** Candidate: product_id; verify uniqueness.

| Column | Observed pandas type | Business description |
|---|---|---|
| `product_id` | `str` | Product identifier; links to products |
| `category` | `str` | Product category label |
| `stock_units` | `int64` | Available stock units |
| `reorder_point` | `int64` | Stock threshold for reordering |
| `warehouse_location` | `str` | Warehouse or storage location label |
| `last_restock_date` | `str` | Date of last restock |
| `supplier_lead_days` | `int64` | Supplier lead time in days for inventory planning |

### returns.csv

- **Purpose:** Returned transactions and refund details.
- **Proposed grain:** One row per return_id (candidate; not verified).
- **Primary key:** Candidate: return_id; verify uniqueness.

| Column | Observed pandas type | Business description |
|---|---|---|
| `return_id` | `str` | Return record identifier |
| `transaction_id` | `str` | Transaction identifier |
| `customer_id` | `str` | Customer identifier; links to customers |
| `product_id` | `str` | Product identifier; links to products |
| `return_date` | `str` | Return date |
| `reason` | `str` | Reason for return |
| `refund_amount_usd` | `float64` | Refund amount in USD |
| `restocked` | `bool` | Whether returned item was restocked |

### customers.csv

- **Purpose:** Customer master records and attributes.
- **Proposed grain:** One row per customer_id (verified).
- **Primary key:** customer_id (verified unique and non-null).

| Column | Observed pandas type | Business description |
|---|---|---|
| `customer_id` | `str` | Customer identifier; links to customers |
| `first_name` | `str` | Customer first name (personal data) |
| `last_name` | `str` | Customer last name (personal data) |
| `country` | `str` | Country label |
| `currency` | `str` | Customer currency code or label |
| `age` | `int64` | Customer age in years |
| `gender` | `str` | Recorded gender category; definition not verified |
| `registration_date` | `str` | Customer registration date |
| `is_premium` | `bool` | Whether customer has premium status |
| `email_verified` | `bool` | Whether email is marked verified |
| `email` | `str` | Customer email address (personal data) |

### marketing_spend.csv

- **Purpose:** Monthly marketing performance by acquisition channel.
- **Proposed grain:** One row per year_month and channel (candidate; not verified).
- **Primary key:** Candidate: (year_month, channel); verify uniqueness.

| Column | Observed pandas type | Business description |
|---|---|---|
| `year_month` | `str` | Year-month period; source stored as text |
| `channel` | `str` | Sales or marketing channel label (context dependent) |
| `spend_usd` | `float64` | Marketing spend in USD |
| `impressions` | `int64` | Recorded advertising impressions |
| `clicks` | `int64` | Recorded advertising clicks |
| `ctr` | `float64` | Recorded click-through rate; scale to verify |
| `actual_orders` | `int64` | Recorded attributed orders |
| `actual_customers` | `int64` | Recorded attributed customers |
| `actual_revenue_usd` | `float64` | Recorded attributed revenue in USD |
| `roas` | `float64` | Recorded return on advertising spend; definition to verify |
| `cac_usd` | `float64` | Recorded customer acquisition cost in USD |
| `cost_per_order_usd` | `float64` | Recorded marketing cost per order in USD |
| `month_multiplier` | `float64` | Recorded monthly multiplier; definition to verify |

## 3. Relationships and candidate keys

| Source | Target | Join field(s) | Audit status |
|---|---|---|
| `transactions` | `products` | `product_id` | Verified: 0 unmatched transaction product IDs |
| `transactions` | `customers` | `customer_id` | Verified: 0 unmatched transaction customer IDs |
| `supplier_costs` | `products` | `product_id` | Expected relationship; not checked in notebook |
| `price_history` | `products` | `product_id` | Expected relationship; not checked in notebook |
| `inventory` | `products` | `product_id` | Expected relationship; not checked in notebook |
| `returns` | `transactions` | `transaction_id` | Expected relationship; not checked in notebook |
| `returns` | `customers` | `customer_id` | Expected relationship; not checked in notebook |
| `returns` | `products` | `product_id` | Expected relationship; not checked in notebook |
| `marketing_spend` | transactions/channel reporting | `year_month`, `channel` (possible) | No row-level FK established; attribution rules need verification |

**Confirmed primary-key candidates:** `transactions.transaction_id`, `products.product_id`, `customers.customer_id` are each unique and contain no missing values.

## 4. Data-quality audit results

| Check | Notebook finding | Interpretation |
|---|---|---|
| File presence | All 8 expected CSVs found | Passed |
| CSV loading | All 8 loaded successfully | Passed |
| Missing cells | 0 in every dataset | Passed for pandas null detection |
| Fully duplicate rows | 0 in every dataset | Passed for exact-row duplicates |
| `transaction_id` uniqueness / non-null | Unique: True; missing: 0 | Passed |
| `product_id` uniqueness / non-null in products | Unique: True; missing: 0 | Passed |
| `customer_id` uniqueness / non-null in customers | Unique: True; missing: 0 | Passed |
| Transaction → product reference | 0 unknown products | Passed |
| Transaction → customer reference | 0 unknown customers | Passed |
| Dates, cross-table category consistency, financial reconciliation | Not tested | Pending |
| Other table keys and foreign-key references | Not tested | Pending |

### Transaction financial field ranges

| Field | Minimum | Maximum |
|---|---:|---:|
| `quantity` | 1 | 10 |
| `unit_price_usd` | 8.06 | 1191.59 |
| `discount_pct` | 0.0 | 0.25 |
| `revenue_usd` | 6.45 | 11915.9 |
| `cost_usd` | 4.58 | 8936.9 |
| `profit_usd` | -0.03 | 2979.0 |

**Observation:** Transaction `profit_usd` has a negative minimum (-0.03), so at least one record shows a loss. The notebook did not count negative-profit transactions or establish why they occur. The `discount_pct` observed range suggests a fractional scale (0–0.25).

## 5. Audit provenance

- Notebook: `data_audit.ipynb`.
- Dataset inventory exported by notebook to `data/exports/dataset_inventory.csv`.
- Findings reflect the notebook outputs at the time of execution; no direct independent inspection of the raw CSV files was performed for this document.
