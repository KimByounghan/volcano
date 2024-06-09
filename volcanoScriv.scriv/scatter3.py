import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 윈도우 폰트 경로 예시 (맑은 고딕)
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터 프레임 생성
data = {
    '항목': ['훈련', '동료와 갈등', '인정받지 못함', '업무 부하', '승진', '금여', '업무 형태', '진로 변경', '통근', '전환 배치', '질병'],
    '영향도': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'HRBP': [31, 11, 65, 14, 137, 16, 128, 18, 31, 105, 9],
    '퇴사조사': [23, 15, 44, 39, 171, 24, 78, 30, 22, 37, 21]
}
df = pd.DataFrame(data)

# 산점도 생성
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='영향도', y='퇴사조사', hue='항목', s=100)
plt.title('영향도와 퇴사조사 간의 관계')
plt.xlabel('영향도')
plt.ylabel('퇴사조사')
plt.show()
