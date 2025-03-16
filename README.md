**使用说明：**

1. 修改 csv 文件中 path 文件地址，将自己收集作业的`文件夹`目录地址导入到 path.csv 中。📂  
> 格式：</br>
> path</br>
> C:/Users/XXXX/XXXX/WPS云盘/Word收集

2. 将学生总名单填入到 stu_info.csv 中，第一列为学号，第二列为姓名。📋  
```python
# 将学生总名单填入到stu_info.csv中，这里可以用老师所给的excel导出另外的csv格式的文件
```
> 格式：</br>
> stu_id,stu_name</br>
> 2225xxxxxx,李四</br>
> 2226xxxxxx,张三</br>
> 2227xxxxxx,李四</br>

3. 执行并启动 paiad.py 文件。🚀  
4. 保存生成的 uncommitted_stu.xlsx 文件(文件位于`学生统计`文件夹中)。✅  
> 注意一定要保证总学生姓名列表(stu_info.csv)不出错，本程序执行正确！！！⚠️
