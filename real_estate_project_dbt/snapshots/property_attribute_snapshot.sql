{% snapshot property_attribute_snapshots %}

{{
  config(
    target_schema='LISTINGS',
    target_name='property_attribute_snapshots',
    unique_key='PROP_ID',
    strategy='check',
    check_cols=['PRICE', 'AGE', 'PRICE_PER_UNIT_AREA', 'PRICE_SQFT']
  )
}}

SELECT *
FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED

{% endsnapshot %}
