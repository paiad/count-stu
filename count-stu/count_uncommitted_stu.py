# 统计未提交的学生的信息，并生成未提交学生的表格
import pandas as pd

# 全部显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

stu_info = pd.read_csv('csv/stu_info.csv')
deliver_stu = pd.read_csv('csv/deliver_stu.csv')

# 解：
# 取唯一值，避免重复提交的问题
list_do = list(deliver_stu['stu_id'].unique())
list_stu = list(stu_info['stu_id'])
# 已提交人员名单
list_true_deliver = []
for ele in list_do:
    if ele in list_stu:
        list_true_deliver.append(ele)
    else:
        print(
            f"未在学生总表中找到该学号对应的学生信息：{ele}-{deliver_stu.loc[deliver_stu['stu_id'] == ele, 'stu_name'].values[0]}")
        raise ValueError("错误的提交！！！")

# 未提交人员名单
undo_stu = list(set(list_stu) - set(list_true_deliver))

stu_name = []
for stu in undo_stu:
    stu_name.append(stu_info.loc[stu_info['stu_id'] == stu, 'stu_name'].values[0])

dict1 = {'stu_id': undo_stu, 'stu_name': stu_name}

print("未提交人员名单：")
for d in dict1['stu_name']:
    print(d)

print("========================================")
print("已提交人员数目：", len(list_do))
print("========================================")
print("未提交人员数目：", len(undo_stu))


df = pd.DataFrame(dict1)
df.index += 1
df.to_excel('./学生统计/uncommitted_stu.xlsx', index=True)
