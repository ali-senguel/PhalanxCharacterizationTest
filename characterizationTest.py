from sys import set_coroutine_origin_tracking_depth
import pandas as pd
import numpy as np
from tabulate import tabulate


sp_tx = 0.0
sp_ty = 0.0
sp_target_z = 1.0
sp_return_z = 0.0
sp_target_F = 0.02
sp_hold_time = 500
sp_speed_up = 0.1
sp_speed_down = 0.1
sp_push_up = 0.5
sp_pause = 1000
tss_x = 0
tss_y = 0
tss_tx = 90
tss_ty = 90

num_points = 25

d = np.arange(1, (num_points+1), 1, dtype=int)
angles_deg = np.arange(0, 360, 9 )
angles_rad = angles_deg * np.pi/180

sinY = np.sin(angles_rad)
cosX = np.cos(angles_rad)



Sp_tx = np.full((len(angles_rad),1),sp_tx)
Sp_ty = np.full((len(angles_rad),1),sp_ty)
Sp_target_z = np.full((len(angles_rad),1),sp_target_z)
Sp_return_z = np.full((len(angles_rad),1),sp_return_z)
Sp_target_F = np.full((len(angles_rad),1),sp_target_F)
Sp_hold_time = np.full((len(angles_rad),1),sp_hold_time)
Sp_speed_up = np.full((len(angles_rad),1),sp_speed_up)
Sp_speed_down = np.full((len(angles_rad),1),sp_speed_down)
Sp_push_up = np.full((len(angles_rad),1),sp_push_up)
Sp_pause = np.full((len(angles_rad),1),sp_pause)
#tss_x = d[0] * cosX
#tss_y = d[0] * sinY
#Tss_x = np.array(tss_x)
#Tss_y = np.array(tss_y)
Tss_tx = np.full((len(angles_rad),1),tss_tx)
Tss_ty = np.full((len(angles_rad),1),tss_ty)


all_data = pd.DataFrame()
data = pd.DataFrame()
for i in range(num_points):
    #print(f'd[i]{d[i]}\n')
    tss_x = d[i] * cosX
    tss_y = d[i] * sinY
    Tss_x = np.array(tss_x)
    Tss_y = np.array(tss_y)
    DataMatrix = np.column_stack((Sp_tx,Sp_ty, Sp_target_z, Sp_return_z,Sp_target_F,Sp_hold_time,Sp_speed_up,Sp_speed_down,Sp_push_up, Sp_pause,Tss_x,Tss_y,Tss_tx,Tss_ty))
    data = pd.DataFrame(DataMatrix)
    all_data = pd.concat([all_data, data],ignore_index=True)

#print(tabulate(all_data, headers = 'keys', tablefmt = 'psql'))
all_data.to_excel('CharacterizationTest.xlsx')


#DataMatrix = np.column_stack((Sp_tx,Sp_ty, Sp_target_z, Sp_return_z,Sp_target_F,Sp_hold_time,Sp_speed_up,Sp_speed_down,Sp_push_up, Sp_pause,Tss_x,Tss_y,Tss_tx,Tss_ty))
#print(DataMatrix.shape)
#df = pd.DataFrame(DataMatrix)
#df.to_excel('CharacterizationTest.xlsx')
#print(tabulate(df, headers = 'keys', tablefmt = 'psql'))