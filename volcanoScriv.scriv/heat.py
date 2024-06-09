import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 프레임 생성
data = {
    '항목': ['훈련', '동료와 갈등', '인정받지 못함', '업무 부하', '승진'],
    '영향도': [11, 10, 9, 8, 7],
    'HRBP': [31, 11, 65, 14, 137],
    '퇴사조사': [23, 15, 44, 39, 171]
}
df = pd.DataFrame(data)

# 히트맵 생성
plt.figure(figsize=(8, 6))
sns.heatmap(df.set_index('항목').corr(), annot=True, cmap='coolwarm')
plt.title('항목 간 상관관계 히트맵')
plt.show()
