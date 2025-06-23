
      begin;
    merge into "REAL_ESTATE"."LISTINGS"."PROPERTY_ATTRIBUTE_SNAPSHOTS" as DBT_INTERNAL_DEST
    using "REAL_ESTATE"."LISTINGS"."PROPERTY_ATTRIBUTE_SNAPSHOTS__dbt_tmp" as DBT_INTERNAL_SOURCE
    on DBT_INTERNAL_SOURCE.dbt_scd_id = DBT_INTERNAL_DEST.dbt_scd_id

    when matched
     
       and DBT_INTERNAL_DEST.dbt_valid_to is null
     
     and DBT_INTERNAL_SOURCE.dbt_change_type in ('update', 'delete')
        then update
        set dbt_valid_to = DBT_INTERNAL_SOURCE.dbt_valid_to

    when not matched
     and DBT_INTERNAL_SOURCE.dbt_change_type = 'insert'
        then insert ("PROP_ID", "PROPERTY_TYPE", "CITY", "PRICE", "PRICE_PER_UNIT_AREA", "BEDROOM_NUM", "AGE", "TOTAL_FLOOR", "PRICE_SQFT", "CLEAN_CITY_NAME", "DBT_UPDATED_AT", "DBT_VALID_FROM", "DBT_VALID_TO", "DBT_SCD_ID")
        values ("PROP_ID", "PROPERTY_TYPE", "CITY", "PRICE", "PRICE_PER_UNIT_AREA", "BEDROOM_NUM", "AGE", "TOTAL_FLOOR", "PRICE_SQFT", "CLEAN_CITY_NAME", "DBT_UPDATED_AT", "DBT_VALID_FROM", "DBT_VALID_TO", "DBT_SCD_ID")

;
    commit;
  