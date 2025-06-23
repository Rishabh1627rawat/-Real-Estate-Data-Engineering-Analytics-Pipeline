-- Use the `ref` function to select from other models

select *
from REAL_ESTATE.LISTINGS.my_first_dbt_model
where id = 1