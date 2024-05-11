import numpy as np
import control
import matplotlib.pyplot as plt

num = [0,0,16]  #分子多项式系数
den = [1,5,16]  #分母多项式系数

sys = control.TransferFunction(num,den) #系统传递函数

#可视化
time, response = control.step_response(sys)
plt.figure()
plt.plot(time,response)
plt.title("picture")
plt.xlabel("time(s)")
plt.ylabel("raise")
plt.grid(True)
plt.show()

#动态指标
s = control.step_info(sys)

tr = s['RiseTime']  #上升时间（从10%到90%）
tp = s['PeakTime']  #峰值时间
os = s['Overshoot']    #超调量
ts = s['SettlingTime']  #调节时间

# 打印性能指标
print(f"RiseTime: {tr:.4f} s")
print(f"PeakTime: {tp:.4f} s")
print(f"Overshoot: {os:.4f} %")
print(f"SettlingTime: {ts:.4f} s")
