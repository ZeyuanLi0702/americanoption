#!/usr/bin/env python
# coding: utf-8

# In[10]:


from AmericanOptionSolver import AmericanOptionSolver
from QDplus import QDplus, OptionType

import time


def run_test(l, m, n, p, r, q, sigma, S, K, T):
    # 初始化AmericanOptionSolver
    solver = AmericanOptionSolver(r, q, sigma, K, T, OptionType.Put)  # 或者OptionType.Call
    solver.assign_par(l, m, n, p)

    # 记录开始时间
    start_time = time.time()

    # 计算期权价格
    price = solver.solve(0.0, S)

    # 计算结束时间和运行时间
    end_time = time.time()
    cpu_seconds = end_time - start_time

    return price, cpu_seconds

# 测试参数
r = q = 0.05  # 无风险利率和股息率
sigma = 0.25 # 波动率
S = K = 100  # 标的资产价格和行权价格
T = 1        # 到期时间

test_parameters = [
    (5, 1, 4, 15),
    (7, 2, 5, 20),
    (11, 2, 5, 31),
    (15, 2, 6, 41),
    (15, 3, 7, 41),
    (25, 4, 9, 51),
    (25, 5, 12, 61),
    (25, 6, 15, 61),
    (35, 8, 16, 81),
    (51, 8, 24, 101),
    (65, 8, 32, 101)
]

results = []

for l, m, n, p in test_parameters:
    start_time = time.time()
    price, iterations = run_test(l, m, n, p, r, q, sigma, S, K, T)
    end_time = time.time()
    results.append({
        "l": l,
        "m": m,
        "n": n,
        "price": price,
        "iterations": iterations,
        "cpu_time": end_time - start_time
    })


print(results)


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

output_data = [
    (5, 1, 4, 15, 1, 0.7342391316003458),
    (7, 2, 5, 20, 2, 0.448186704555209),
    (11, 2, 5, 31, 2, 0.44818827297345065),
    (15, 2, 6, 41, 2, 0.48652182951539935),
    (15, 3, 7, 41, 3, 0.2796265464351056),
    (25, 4, 9, 51, 4, 0.16446457125128155),
    (25, 5, 12, 61, 5, 0.09712515258112954),
    (25, 6, 15, 61, 6, 0.05515069376942521),
    (35, 8, 16, 81, 8, 0.014540485601843074),
    (51, 8, 24, 101, 8, 0.020452333710689392),
    (65, 8, 32, 101, 8, 0.017744356687812376)
]

df = pd.DataFrame(output_data, columns=['l', 'm', 'n', 'p', 'iterations', 'final_error'])

plt.figure(figsize=(10, 6))

# 绘制迭代次数
plt.subplot(1, 2, 1)
plt.scatter(df['l'], df['iterations'], color='blue')
plt.title('Iterations vs l')
plt.xlabel('l')
plt.ylabel('Iterations')

# 绘制最终错误
plt.subplot(1, 2, 2)
plt.scatter(df['l'], df['final_error'], color='red')
plt.title('Final Error vs l')
plt.xlabel('l')
plt.ylabel('Final Error')

plt.tight_layout()
plt.show()


# In[30]:


from itertools import product

# 定义参数范围
l_values = range(10, 60, 5)  
m_values = range(2, 10)        
n_values = range(5, 20)      
p_values = range(20, 120, 5) 

# 生成所有可能的组合
all_combinations = list(product(l_values, m_values, n_values, p_values))

# 随机选择500组组合
import random
random.seed(0)  # 可以设置一个种子值以便重现结果
selected_combinations = random.sample(all_combinations, 500)


results = []
for l, m, n, p in selected_combinations:
    solver = AmericanOptionSolver(r, q, sigma, K, T, OptionType.Put)
    solver.assign_par(l, m, n, p)
    solver.iter_tol = 1e-5
    solver.max_iters = 100
    solver.solve(0.0, S)
    steps = len(solver.iter_records)  # 获取迭代步骤数
    final_error = solver.iter_records[-1] if solver.iter_records else None
    results.append((l, m, n, p, steps))
import pandas as pd

df = pd.DataFrame(results, columns=['l', 'm', 'n', 'p', 'Steps to Convergence'])





# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='l', y='Steps to Convergence', hue='n', style='m')
plt.title('Convergence Steps for Custom Parameter Sets')
plt.show()


# In[33]:


print(df)


# In[32]:


df.describe()
correlation_matrix = df.corr()
print(correlation_matrix)


# In[29]:


import statsmodels.api as sm

# 以 l, m, n, p 为自变量，收敛步数为因变量进行回归分析
X = df[['l', 'm', 'n', 'p']]
y = df['Steps to Convergence']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[ ]:




