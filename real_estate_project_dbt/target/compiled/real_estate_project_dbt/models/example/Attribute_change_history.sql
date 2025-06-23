SELECT
  PROP_ID,
  dbt_valid_from,
  dbt_valid_to,
  PRICE,
  AGE,
  PRICE_PER_UNIT_AREA,
  PRICE_SQFT,
  ROW_NUMBER() OVER (PARTITION BY PROP_ID ORDER BY dbt_valid_from) AS version_number
FROM REAL_ESTATE.LISTINGS.property_attribute_snapshots