merge 
into sample_submission.sample_sdc2 ab
using (
select product_id as key_join, * from sample_submission.sample_stg
union all
select null,a.* from sample_submission.sample_stg a
join sample_submission.sample_sdc2 b on a.product_id=b.product_id
where (a.quantity<>b.quantity and b.expired_date is null)) sub
on sub.key_join=ab.product_id
when matched
and sub.quantity<>ab.quantity then update
set expired_date=current_date()
when not matched
then insert (product_id,product_name, quantity,modified_date,expired_date) 
values (sub.product_id,sub.product_name, sub.quantity,current_date(),null);