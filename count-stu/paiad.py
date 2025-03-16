# @Software  :PyCharm
# @Author    : ad
# @File      : paiad.py
# @Time      : 2024-10-12 17:12
import subprocess

# 运行 committed_to_csv.py
print("正在统计已提交的人数信息...")
subprocess.run(["python", "committed_to_csv.py"])

# 运行 count_uncommitted_stu.py
print("\n\n正在生成未提交的人数信息...")
subprocess.run(["python", "count_uncommitted_stu.py"])

print("'未上交学生名单————uncommitted_stu.xlsx' 文件生成完成！！！")
