import numpy as np
import matplotlib.pyplot as plt
#
# 시뮬레이션 파라미터 설정
#
Fs = 100
Ts = 1/Fs
Ns = 300

# X(시간축) 값
x0 = np.arange(0,Ns)*Ts

y1t = (1.0)*np.sin(2*np.pi*1*x0)
y2t = (1/2)*np.sin(2*np.pi*2*x0)
y3t = (1/3)*np.sin(2*np.pi*3*x0)

y0t = 0
for i in range(1,11):
    y0t = y0t + (1/i)*np.sin(2*np.pi*i*x0)

plt.subplot(4,1,1); plt.plot(x0, y0t,'b'); plt.ylim(-2,2); plt.grid()
plt.ylabel('x1(t)')
plt.subplot(4,1,2); plt.plot(x0, y1t, 'b'); plt.ylim(-2,2); plt.grid()
plt.ylabel('x2(t)')
plt.subplot(4,1,3); plt.plot(x0, y2t, 'b'); plt.ylim(-2,2); plt.grid()
plt.ylabel('x3(t)')
plt.subplot(4,1,4); plt.plot(x0, y3t, 'b'); plt.ylim(-2,2); plt.grid()
plt.ylabel('x4(t)')

plt.show()