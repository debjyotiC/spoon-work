import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

alpha = 0.9

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

dt = (gyro_df['Milliseconds'][1] - gyro_df['Milliseconds'][0]) * pow(10, -3)
acc_angle = np.arctan(np.divide(acc_x, np.add(np.square(acc_y), np.square(acc_z))))
angle = np.degrees((1 / alpha) * ((1 - alpha) * gyro_x * dt + alpha * acc_angle))


# save data
values = {'Time': acc_time, 'Acc_x': acc_x, 'Acc_y': acc_y, 'Acc_z': acc_z, 'Gyro_x': gyro_x, 'Gyro_y': gyro_y,
          'Gyro_z': gyro_z, 'Filter_angle': angle}
df_w = pd.DataFrame(values, columns=['Time', 'Acc_x', 'Acc_y', 'Acc_z', 'Gyro_x', 'Gyro_y', 'Gyro_z', 'Filter_angle'])
df_w.to_csv("data/final-data.csv", index=None, header=True)


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

axs[2].plot(acc_time, angle, color='red', label=f'Filter data with dt={dt}')
axs[2].legend()
axs[2].set_ylabel('Angle (degree)')
plt.xlabel('Time (ms)')
plt.show()
