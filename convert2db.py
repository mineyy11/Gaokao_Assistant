import os
import pandas as pd
from sqlalchemy import create_engine

# 定义路径
csv_folder = "E:\\project\\Gaokao_Assistant\\data"  # 替换为你的 CSV 文件目录
db_path = "E:\\project\\Gaokao_Assistant\\data\\school.db"             # 输出的 SQLite 文件路径

# 创建 SQLite 引擎
engine = create_engine(f"sqlite:///{db_path}")

# 遍历 CSV 文件
for filename in os.listdir(csv_folder):
    if filename.endswith(".csv"):
        table_name = os.path.splitext(filename)[0]  # 用文件名作为表名
        csv_path = os.path.join(csv_folder, filename)
        
        # 读取 CSV 文件
        df = pd.read_csv(csv_path)
        
        # 写入 SQLite 数据库
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",  # 如果表存在则替换
            index=False          # 不保存 DataFrame 的索引列
        )
        print(f"表 {table_name} 导入成功")

print(f"数据库已生成：{db_path}")