# Sales Data — Cleaning & Analysis

**Source:** `sales_data_sample.csv` | **Records:** 2,823 | **Columns:** 25 | **Period:** 2003–2005

---

## Cleaning Steps

| Step | Action |
|------|--------|
| Column names | Stripped, lowercased, spaces → underscores |
| Duplicates | Checked — 0 found |
| `orderdate` | Parsed to datetime, reformatted to `DD-MM-YYYY` |
| `addressline2` | 2,521 nulls → `N/A` |
| `state` | 1,486 nulls → `N/A` |
| `territory` | USA nulls → `NA`, others → `Unknown` (1,074 total) |
| `postalcode` | 76 nulls → `N/A`, cast to string |
| String cols | Stripped whitespace: `status`, `productline`, `dealsize`, `country`, `city`, `customername` |
| Int cols | `ordernumber`, `quantityordered`, `orderlinenumber`, `msrp`, `qtr_id`, `month_id`, `year_id` → `Int64` |
| Float cols | `priceeach`, `sales` → `float64` |
| Final check | `assert nulls == 0` ✅ |

---

## Findings

### Revenue Overview
- **Total Revenue:** $10,032,628.85
- **Avg Order Value:** $3,553.89

### By Year
| Year | Revenue | Share |
|------|---------|-------|
| 2003 | $3,516,979 | 35.1% |
| 2004 | $4,724,162 | 47.1% ← peak |
| 2005 (partial) | $1,791,486 | 17.9% |

### By Product Line
| Product Line | Revenue | Share |
|---|---|---|
| Classic Cars | $3,919,615 | 39.1% |
| Vintage Cars | $1,903,150 | 19.0% |
| Motorcycles | $1,166,388 | 11.6% |
| Trucks and Buses | $1,127,789 | 11.2% |
| Planes | $975,003 | 9.7% |
| Ships | $714,437 | 7.1% |
| Trains | $226,243 | 2.3% |

### By Deal Size
| Size | Orders | Revenue |
|------|--------|---------|
| Large | 157 (5.6%) | $1,302,119 |
| Medium | 1,384 (49.0%) | $6,087,432 |
| Small | 1,282 (45.4%) | $2,643,077 |

### Order Status
| Status | Count |
|--------|-------|
| Shipped | 2,617 (92.7%) |
| Cancelled | 60 (2.1%) |
| Resolved | 47 (1.7%) |
| On Hold | 44 (1.6%) |
| In Process | 41 (1.5%) |
| Disputed | 14 (0.5%) |

### Top 5 Countries (by orders)
| Country | Orders |
|---------|--------|
| USA | 112 |
| France | 37 |
| Spain | 36 |
| Australia | 19 |
| UK | 13 |

### Top 5 Customers (by revenue)
| Customer | Revenue |
|----------|---------|
| Euro Shopping Channel | $912,294 |
| Mini Gifts Distributors Ltd. | $654,858 |
| Australian Collectors, Co. | $200,995 |
| Muscle Machine Inc | $197,736 |
| La Rochelle Gifts | $180,124 |

---

## Quick Notes
- Classic Cars = 39% of total revenue, clear top line
- 2004 best year; 2005 data is partial
- 92.7% shipped — fulfillment is solid
- Euro Shopping Channel alone = ~9% of all revenue
- Large deals are rare (5.6%) but highest value per order (~$8,294 avg)
