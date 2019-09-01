#Replace is mainly to create generic quires in bigdata scripts
#Example
qurey="select * from $table   where dataset_id=$dataset_id "
qu1=qurey.replace('$table','emp').replace('$dataset_id','123')
print(qu1)
#output :select * from emp   where dataset_id=123 
qurey="select * from $table   where dataset_name='$dataset_name' "
qu1=qurey.replace('$table','emp').replace('$dataset_name','healthstats')
print(qu1)