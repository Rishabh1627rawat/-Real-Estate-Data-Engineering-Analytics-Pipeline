
  
    

create or replace transient table REAL_ESTATE.LISTINGS_LISTINGS.city_level_aggregates
    

    
    as (


WITH city_levels AS (
    SELECT CLEAN_CITY_NAME AS CITY_NAME,
    COUNT(PROP_ID) AS TOTAL_LISTINGS,
    AVG(PRICE) AS AVG_PRICE,
    MAX(TOTAL_FLOOR) AS MAX_FLOOR,
    AVG(AGE) AS AVG_AGE
    FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED
    GROUP BY CLEAN_CITY_NAME
)

SELECT * FROM city_levels
    )
;


  