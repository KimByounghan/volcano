import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 프레임 생성
data = {'항목': ['훈련', '동료와 갈등', '인정받지 못함', '업무 부하', '승진'],
        '영향도': [11, 10, 9, 8, 7],
        'HRBP': [31, 11, 65, 14, 137],
        '퇴사조사': [23, 15, 44, 39, 171]}

df = pd.DataFrame(data)

# 막대 그래프 생성
plt.figure(figsize=(10, 6))
df.set_index('항목').plot(kind='bar')
plt.title('각 항목별 영향도, HRBP, 퇴사조사 비교')
plt.ylabel('수치')
plt.show()

# 히트맵 생성
plt.figure(figsize=(8, 6))
sns.heatmap(df.set_index('항목').corr(), annot=True, cmap='coolwarm')
plt.title('항목 간 상관관계 히트맵')
plt.show()

# 산점도 생성
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='영향도', y='퇴사조사', hue='항목', s=100)
plt.title('영향도와 퇴사조사 간의 관계')
plt.xlabel('영향도')
plt.ylabel('퇴사조사')
plt.show()
