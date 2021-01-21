import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

acc_df = pd.read_csv('data/acc.csv').drop(['Timestamp'], axis=1)
gyro_df = pd.read_csv('data/gyro.csv').drop(['Timestamp'], axis=1)

acc_x = np.array(acc_df['X'])
acc_y = np.array(acc_df['Y'])
acc_z = np.array(acc_df['Z'])
acc_time = np.array(acc_df['Milliseconds'])

gyro_x = np.array(gyro_df['X'])
gyro_y = np.array(gyro_df['Y'])
gyro_z = np.array(gyro_df['Z'])
gyro_time = np.array(gyro_df['Milliseconds'])


acc_angle = -np.arctan(np.divide(acc_x, np.add(np.square(acc_y), np.square(acc_z))))


fig, axs = plt.subplots(3)
fig.suptitle('IMU data')
axs[0].plot(acc_time, acc_x, label='acc. X data')
axs[0].plot(acc_time, acc_y, label='acc. Y data')
axs[0].plot(acc_time, acc_z, label='acc. Z data')
axs[0].legend()
axs[0].set_ylabel('Acc ($m/s^2$)')

axs[1].plot(gyro_time, gyro_x, label='gyro. X data')
axs[1].plot(gyro_time, gyro_y, label='gyro. Y data')
axs[1].plot(gyro_time, gyro_z, label='gyro. Z data')
axs[1].legend()
axs[1].set_ylabel('Gyro (degree/s)')
plt.xlabel('Time (ms)')

axs[2].plot(acc_time, acc_angle, label='Filter data')
axs[2].legend()
axs[2].set_ylabel('Angle (rad)')
plt.xlabel('Time (ms)')
plt.show()
