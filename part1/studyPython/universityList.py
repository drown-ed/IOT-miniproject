
import pandas as pd

filePath = 'part1/studyPython/university_list_2020.xlsx'
df_excel = pd.read_excel(filePath, engine = 'openpyxl')
df_excel.columns = df_excel.loc[4].tolist()
df_excel = df_excel.drop(index = list(range(0, 5))) # 실제 데이터 이외 행 날리기


print(df_excel.head())
print(df_excel['학교명'].values)
print(df_excel['주소'].values)