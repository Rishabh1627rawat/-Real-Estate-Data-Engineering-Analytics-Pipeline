
  create or replace   view REAL_ESTATE.LISTINGS.my_second_dbt_model
  
   as (
    -- Use the `ref` function to select from other models

select *
from REAL_ESTATE.LISTINGS.my_first_dbt_model
where id = 1
  );

