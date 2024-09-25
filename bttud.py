import numpy as np
import pandas as pd
import math

c = pd.read_csv('D:/Ngọc Anh/Python/bt coreelation cov/Advertising.csv')
cot2 = c['Newspaper']
cot1 = c['TV']
cot3 = c['Radio']
cot4 = c['Sales']

print(c)

# Tính hiệp phương sai giữa TV và Newspaper
hiepphuongsai = cot1.cov(cot2)
print('Hiệp phương sai TV và Newspaper:', hiepphuongsai)

# Tính phương sai của từng cột
phuongsaitungcot1 = cot1.var()
phuongsaitungcot2 = cot2.var()
print('Phương sai cột TV:', phuongsaitungcot1)
print('Phương sai cột Newspaper:', phuongsaitungcot2)

# Hệ số tương quan Pearson giữa TV và Newspaper
pearson = cot1.corr(cot2)
print('Hệ số tương quan Pearson giữa TV và Newspaper:', pearson)

# Tính góc giữa hai biến (radian và độ)
radian = math.acos(pearson)
print('Góc giữa TV và Newspaper (radian):', radian)

# Chuyển đổi từ radian sang độ
degree = math.degrees(radian)
print('Góc giữa TV và Newspaper (độ):', degree)
