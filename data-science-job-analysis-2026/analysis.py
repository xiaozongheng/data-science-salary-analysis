import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# 读取数据（注意修改为你的实际路径）
df = pd.read_csv(r"D:\xuexiziliao\GKS\数据处理与分析实践\qcwyxm\salaries.csv")

print("数据量:", len(df))
print(df.head())
print("\n列名:", df.columns.tolist())

# ---------- 技能关键词提取 ----------
skill_dict = {
    'python': ['python', 'pyspark'],
    'sql': ['sql', 'postgresql', 'mysql'],
    'tableau': ['tableau'],
    'power bi': ['power bi', 'powerbi'],
    'hadoop': ['hadoop', 'hdfs'],
    'spark': ['spark', 'apache spark'],
    'aws': ['aws', 'amazon web services'],
    'azure': ['azure'],
    'excel': ['excel'],
    'machine learning': ['machine learning', 'ml'],
    'deep learning': ['deep learning', 'dl', 'tensorflow', 'keras'],
    'scikit-learn': ['scikit-learn', 'sklearn'],
    'java': ['java'],
    'scala': ['scala'],
    'c++': ['c++', 'cpp'],
    'r': ['r language'],
}

def extract_skills(title):
    if pd.isna(title):
        return []
    title_lower = str(title).lower()
    found = []
    for skill, keywords in skill_dict.items():
        if any(k in title_lower for k in keywords):
            found.append(skill)
    return found

df['skills'] = df['job_title'].apply(extract_skills)
all_skills = [skill for sublist in df['skills'] for skill in sublist]
skill_counts = Counter(all_skills)
top_skills = skill_counts.most_common(10)
print("\nTop 10 Skills:", top_skills)

# ---------- 薪资分布 ----------
plt.figure(figsize=(10,5))
plt.hist(df['salary_in_usd'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Global Data Science Salaries Distribution (USD)')
plt.xlabel('Annual Salary (USD)')
plt.ylabel('Number of Jobs')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('salary_distribution.png')
plt.show()

# ---------- 词云 ----------
skills_text = ' '.join(all_skills)
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(skills_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Top Skills Word Cloud', fontsize=16)
plt.tight_layout()
plt.savefig('skills_wordcloud.png')
plt.show()

# ---------- 结论 ----------
print("\n" + "="*50)
print("核心分析结论：")
print(f"1. 数据量：{len(df)} 条全球数据科学岗位记录")
print(f"2. 需求量最高的技能：{', '.join([skill for skill, _ in top_skills[:5]])}")
print(f"3. 平均薪资：${df['salary_in_usd'].mean():,.0f} USD")
print(f"4. 中位数薪资：${df['salary_in_usd'].median():,.0f} USD")
print("5. 根据分析，简历已强化 Python/SQL/Tableau 等高频技能")
print("="*50)