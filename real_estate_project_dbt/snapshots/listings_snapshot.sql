{% snapshot listings_snapshots %}
{{config(
    target_schema='LISTNGS',
    unique_key='PROP_ID',
    strategy='check',
    check_cols=['PRICE']
)}}


SELECT * FROM REAL_ESTATE.LISTINGS.LISTINGS_CLEANED

{% endsnapshot %}