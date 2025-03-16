# 统计提交的学生的信息
import os
import pandas as pd

# 需要统计的学生目录
data = pd.read_csv('./csv/path.csv')
folder_path = str(data['path'].iloc[0])

deliver_stu = {
    'stu_id': [],  # 学号
    'stu_name': []  # 姓名
}

# 解构提交的文件名
for file_name in os.listdir(folder_path):
    info = file_name.split(".")[0]
    s = info.split('-')
    stu_id = s[0]
    stu_name = s[1]
    deliver_stu['stu_id'].append(stu_id)
    deliver_stu['stu_name'].append(stu_name)

df = pd.DataFrame(deliver_stu)
for k, v in deliver_stu.items():
    if k == 'stu_name':
        print(v)

df.to_csv('./csv/deliver_stu.csv', index=False)
