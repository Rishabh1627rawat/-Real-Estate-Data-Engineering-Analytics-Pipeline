
  
    

create or replace transient table REAL_ESTATE.LISTINGS_LISTINGS.property_distribution
    

    
    as (

WITH city_percentiles AS (
    SELECT
        CLEAN_CITY_NAME,
        PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY PRICE) AS P90_PRICE
    FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED
    GROUP BY CLEAN_CITY_NAME
),

flagged_listings AS (
    SELECT
        l.*,
        c.P90_PRICE,
        CASE
            WHEN l.PRICE > c.P90_PRICE THEN TRUE
            ELSE FALSE
        END AS IS_LUXURY
    FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED AS l
    JOIN city_percentiles AS c 
        ON l.CLEAN_CITY_NAME = c.CLEAN_CITY_NAME
)

SELECT * FROM flagged_listings
    )
;


  