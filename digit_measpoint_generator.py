from sys import set_coroutine_origin_tracking_depth
import pandas as pd
import numpy as np
from tabulate import tabulate

#s = "{:,.2f}".format(my_num)
def create_table(pos_x,pos_y):
    sp_tx = pos_x
    sp_ty = pos_y
    sp_target_z = 0.0025
    sp_return_z = 0.0
    sp_target_F = 0.02
    sp_hold_time = 250
    sp_speed_up = 0.0001
    sp_speed_down = 0.001
    sp_push_up = 0
    sp_pause = 0
    tss_x = 0.001
    tss_y = -0.002
    tss_tx = 0
    tss_ty = 0
    force_max = 0.2
    force_inc = 0.005
    target_F = np.arange(0, force_max+force_inc, force_inc, dtype=float)
    target_F [0] = 0.0000001

    Sp_tx = np.full((len(target_F),1),sp_tx)
    Sp_ty = np.full((len(target_F),1),sp_ty)
    Sp_target_z = np.full((len(target_F),1),sp_target_z)
    Sp_return_z = np.full((len(target_F),1),sp_return_z)
    Sp_target_F = target_F
    Sp_hold_time = np.full((len(target_F),1),sp_hold_time)
    Sp_speed_up = np.full((len(target_F),1),sp_speed_up)
    Sp_speed_down = np.full((len(target_F),1),sp_speed_down)
    Sp_push_up = np.full((len(target_F),1),sp_push_up)
    Sp_pause = np.full((len(target_F),1),sp_pause)
    Tss_x = np.full((len(target_F),1),tss_x)
    Tss_y = np.full((len(target_F),1),tss_y)
    Tss_tx = np.full((len(target_F),1),tss_tx)
    Tss_ty = np.full((len(target_F),1),tss_ty)
    DataMatrix = np.column_stack((Sp_tx,Sp_ty, Sp_target_z, Sp_return_z,Sp_target_F,Sp_hold_time,Sp_speed_up,Sp_speed_down,Sp_push_up, Sp_pause,Tss_x,Tss_y,Tss_tx,Tss_ty))
    data = pd.DataFrame(DataMatrix)
    #print(data)
    return data

num_points = 5
d = np.arange(1, (num_points+1), 1, dtype=int) / 1000
angles_deg = np.arange(0, 360, 9 )
angles_rad = angles_deg * np.pi/180

sinY = np.sin(angles_rad)
cosX = np.cos(angles_rad)


all_data = pd.DataFrame()
data = pd.DataFrame()
for i in range(num_points):
    #print(f'd[i]{d[i]}\n')
    x = d[i] * cosX
    y = d[i] * sinY
    for j in range(len(x)):
        data = create_table(x[j],y[j])
        all_data = pd.concat([all_data, data],ignore_index=True)

#print(tabulate(all_data, headers = 'keys', tablefmt = 'psql'))
all_data.to_csv('CharacterizationTest.txt', header=None, index=None, sep='\t')
