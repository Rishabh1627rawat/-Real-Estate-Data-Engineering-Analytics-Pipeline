WITH prices AS(
    SELECT 
        PROP_ID,
        PRICE,
        dbt_valid_from,
        dbt_valid_to,
        ROW_NUMBER() OVER( PARTITION BY PROP_ID ORDER BY dbt_valid_from) AS version
    FROM {{ref ('listings_snapshots')}}
)

SELECT
   a.PROP_ID,
   a.dbt_valid_from AS CURRENT_DATE,
   a.PRICE AS CURRENT_PRICE,
   b.PRICE AS PERVIOUS_PRICE,
   ROUND((a.PRICE -b.PRICE) /NULLIF(b.PRICE, 0),4) AS PRICE_CHANGE_PERCENT
FROM prices a
LEFT JOIN prices B 
  ON a.PROP_ID = b.PROP_ID AND a.version = b.version + 1