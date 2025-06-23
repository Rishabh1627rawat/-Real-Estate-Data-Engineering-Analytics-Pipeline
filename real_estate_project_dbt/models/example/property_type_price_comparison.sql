{{ config(
    database='REAL_ESTATE',
    schema='LISTINGS',
    materialized='table'
) }}

-- Step 1: Get overall average price across all cities
WITH overall_avg_price_cte AS (
    SELECT AVG(PRICE) AS overall_avg_price
    FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED
),

-- Step 2: City-level aggregates (do not use CASE here!)
city_level_aggregates_cte AS (
    SELECT
        CLEAN_CITY_NAME AS CITY_NAME,
        COUNT(PROP_ID) AS TOTAL_LISTINGS,
        AVG(PRICE) AS AVG_PRICE,
        MAX(TOTAL_FLOOR) AS MAX_FLOOR,
        AVG(AGE) AS AVG_AGE
    FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED
    GROUP BY CLEAN_CITY_NAME
)

-- Step 3: Add price category by comparing to overall average
SELECT
    city.*,
    CASE
        WHEN city.AVG_PRICE > overall.overall_avg_price * 1.2 THEN 'Overpriced'
        ELSE 'Fair'
    END AS PRICE_CATEGORY
FROM city_level_aggregates_cte city
CROSS JOIN overall_avg_price_cte overall

