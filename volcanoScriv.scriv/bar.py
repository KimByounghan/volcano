import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 생성
data = {
    '항목': ['훈련', '동료와 갈등', '인정받지 못함', '업무 부하', '승진'],
    '영향도': [11, 10, 9, 8, 7],
    'HRBP': [31, 11, 65, 14, 137],
    '퇴사조사': [23, 15, 44, 39, 171]
}
df = pd.DataFrame(data)

# 막대 그래프 생성
plt.figure(figsize=(10, 6))
df.set_index('항목').plot(kind='bar')
plt.title('각 항목별 영향도, HRBP, 퇴사조사 비교')
plt.ylabel('수치')
plt.xticks(rotation=45)
plt.show()
