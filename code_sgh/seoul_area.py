import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:\Python_project\malgun.ttf' 
font_name = fm.FontProperties(fname=font_path).get_name()

# matplotlib에 한글 폰트로 등록
plt.rc('font', family=font_name)

# CSV 파일 읽기
df = pd.read_csv('C:\Python_project\서울 권역별 월강수량.csv')

# 그래프 데이터 추출
months = df['월']
도심 = df['도심권']
동북 = df['동북권']
서북 = df['서북권']
서남 = df['서남권']
동남 = df['동남권']

# 꺽은선 그래프 생성
plt.plot(months, 도심, label='도심권')
plt.plot(months, 동북, label='동북권')
plt.plot(months, 서북, label='서북권')
plt.plot(months, 서남, label='서남권')
plt.plot(months, 동남, label='동남권')

# 격자 표시
plt.grid(True)

# 그래프 제목과 축 제목 설정
plt.title('서울시 권역별 평균 강수량')
plt.xlabel('2022년')
plt.ylabel('단위(mm)')

# 범례 표시
plt.legend()

# 그래프 출력
plt.show()
