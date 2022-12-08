import Messages
import CarmenMessage
from CarmenMessage import FlexRayMessage
import CarmenInterpreter
from CarmenLogging import log
import PySimpleGUI27 as sg
import sys
import MessageSpecLoader
import Package_1_2_Data
import Package_3_4_Data
import time


window = None
Id1 = 0
x = 0
message = []
#For Package 1 and 2
RSSI_Min = ['127','127','127','127']
RSSI_Max = ['0','0','0','0']
RSSI_Avg = ['0.0','0.0','0.0','0.0']
RSSI_Last = ['0.0','0.0','0.0','0.0']
SNR_Min = ['127','127','127','127']
SNR_Max = ['0','0','0','0']
SNR_Avg = ['0.0','0.0','0.0','0.0']
SNR_Last = ['0.0','0.0','0.0','0.0']
FrmCnt = ['0','0','0','0']    
PalCounter_mem = ['0','0','0','0']
ExpBlkCnt = ['0','0','0','0']     
ExpFrmCnt = ['0','0','0','0']       
BlkCnt = ['0','0','0','0']          
Pressure = ['-1','-1','-1','-1']
Temperature = ['-52','-52','-52','-52']
Supplier = ['0','0','0','0']
PalState = ['0','0','0','0']
PalTxTrig = ['0','0','0','0']
Ausbeute_Blk = ['0','0','0','0']
Ausbeute_Frms = ['0','0','0','0']
NoiseArr = ['0','0','0']
UTyreId = [0x0,0x0,0x0,0x0]
#For Package 3 and 4
DRSSI_Min = ['127','127','127','127']
DRSSI_Max = ['0','0','0','0']
DRSSI_Avg = ['0.0','0.0','0.0','0.0']
DRSSI_Last = ['0.0','0.0','0.0','0.0']
DSNR_Min = ['127','127','127','127']
DSNR_Max = ['0','0','0','0']
DSNR_Avg = ['0.0','0.0','0.0','0.0']
DSNR_Last = ['0.0','0.0','0.0','0.0']
DFrmCnt = ['0','0','0','0']    
DPalCounter_mem = ['0','0','0','0']
DExpBlkCnt = ['0','0','0','0']     
DExpFrmCnt = ['0','0','0','0']       
DBlkCnt = ['0','0','0','0']          
DPressure = ['-1','-1','-1','-1']
DTemperature = ['-52','-52','-52','-52']
DSupplier = ['0','0','0','0']
DPalState = ['0','0','0','0']
DPalTxTrig = ['0','0','0','0']
DAusbeute_Blk = ['0','0','0','0']
DAusbeute_Frms = ['0','0','0','0']
DNoiseArr = ['0','0','0']
DUTyreId = [0x0,0x0,0x0,0x0]
TyreName = ['VL','VR','RL','RR']

#*******************************************************************************************************************************************#  
# def Variables defintion END 
# def OutputSystemVariables_Pk_1_2() function START
# ......Read the information from the Package 3 & 4
#*******************************************************************************************************************************************#
def OutputSystemVariables_Pk_1_2():

    #Print Tyre Id in Hex
    UTyreId[0] = Package_1_2_Data.UserTyreId[0]
    UTyreId[1] = Package_1_2_Data.UserTyreId[1]
    UTyreId[2] = Package_1_2_Data.UserTyreId[2]
    UTyreId[3] = Package_1_2_Data.UserTyreId[3]
    #Update Tyreinfo 1
    if Package_1_2_Data.bPressure[0] != 0 and Package_1_2_Data.bPressure[0] != -1:  
      Pressure[0] = str((Package_1_2_Data.bPressure[0] - 2) * 25)
      Temperature[0] = str(Package_1_2_Data.bTemperature[0] - 52)
      Supplier[0] = str(Package_1_2_Data.bSupplier[0])
      PalState[0] = str(Package_1_2_Data.bPalState[0])  
      PalTxTrig[0] = str(Package_1_2_Data.bPalTxTrig[0])      
      PalCounter_mem[0] = str(Package_1_2_Data.bID_PalCounter_mem[0])
      BlkCnt[0] = str(Package_1_2_Data.bID_BlkCnt[0])
      ExpBlkCnt[0] = str(Package_1_2_Data.bID_ExpBlkCnt[0])
      if ((Package_1_2_Data.bID_BlkCnt[0] > 0) and (Package_1_2_Data.bID_ExpBlkCnt[0] > 0)):
        Ausbeute_Blk[0] = str(round(100 * Package_1_2_Data.bID_BlkCnt[0] / Package_1_2_Data.bID_ExpBlkCnt[0]))
      FrmCnt[0] = str(Package_1_2_Data.bIDTgCnt[0])   
      ExpFrmCnt[0] = str(Package_1_2_Data.bID_ExpFrmCnt[0])  
      #Update Frm Ausbeute
      if ((Package_1_2_Data.bIDTgCnt[0] > 0) and (Package_1_2_Data.bID_ExpFrmCnt[0] > 0)):
        Ausbeute_Frms[0] = str(round(100 * Package_1_2_Data.bIDTgCnt[0] / Package_1_2_Data.bID_ExpFrmCnt[0]))
      RSSI_Last[0] = str(Package_1_2_Data.bID_RSSI_Last[0] / 2.0)
      RSSI_Min[0] = str(Package_1_2_Data.bID_RSSI_Min[0]/2) 
      RSSI_Max[0] = str(Package_1_2_Data.bID_RSSI_Max[0]/2)
      RSSI_Avg[0] = str(round(Package_1_2_Data.dbl_ID_RSSI_Avg[0] / 2 , 1))
      SNR_Last[0] = str(Package_1_2_Data.dbl_ID_SNR_Last[0] / 2.0)
      SNR_Min[0] = str(Package_1_2_Data.bID_SNR_Min[0] / 2)
      SNR_Max[0] = str(Package_1_2_Data.bID_SNR_Max[0] / 2) 
      SNR_Avg[0] = str(round(Package_1_2_Data.dbl_ID_SNR_Avg[0] / 2 , 1))
      
    #Update Tyreinfo 2  
    if Package_1_2_Data.bPressure[1] != 0 and Package_1_2_Data.bPressure[1] != -1: 
      Pressure[1] = str((Package_1_2_Data.bPressure[1] - 2) * 25)  
      Temperature[1] = str(Package_1_2_Data.bTemperature[1] - 52)
      Supplier[1] = str(Package_1_2_Data.bSupplier[1])
      PalState[1] = str(Package_1_2_Data.bPalState[1])  
      PalTxTrig[1] = str(Package_1_2_Data.bPalTxTrig[1]) 
      PalCounter_mem[1] = str(Package_1_2_Data.bID_PalCounter_mem[1])
      BlkCnt[1] = str(Package_1_2_Data.bID_BlkCnt[1])
      ExpBlkCnt[1] = str(Package_1_2_Data.bID_ExpBlkCnt[1])
      if ((Package_1_2_Data.bID_BlkCnt[1] > 0) and (Package_1_2_Data.bID_ExpBlkCnt[1] > 0)):
        Ausbeute_Blk[1] = str(round(100 * Package_1_2_Data.bID_BlkCnt[1] / Package_1_2_Data.bID_ExpBlkCnt[1])) 
      FrmCnt[1] = str(Package_1_2_Data.bIDTgCnt[1])   
      ExpFrmCnt[1] = str(Package_1_2_Data.bID_ExpFrmCnt[1]) 
      #Update Frm Ausbeute 
      if ((Package_1_2_Data.bIDTgCnt[1] > 0) and (Package_1_2_Data.bID_ExpFrmCnt[1] > 0)):
        Ausbeute_Frms[1] = str(round(100 * Package_1_2_Data.bIDTgCnt[1] / Package_1_2_Data.bID_ExpFrmCnt[1]))  
      RSSI_Last[1] = str(Package_1_2_Data.bID_RSSI_Last[1] / 2.0)
      RSSI_Min[1] = str(Package_1_2_Data.bID_RSSI_Min[1]/2)
      RSSI_Max[1] = str(Package_1_2_Data.bID_RSSI_Max[1]/2) 
      RSSI_Avg[1] = str(round(Package_1_2_Data.dbl_ID_RSSI_Avg[1] / 2 , 1)) 
      SNR_Last[1] = str(Package_1_2_Data.dbl_ID_SNR_Last[1] / 2.0)     
      SNR_Min[1] = str(Package_1_2_Data.bID_SNR_Min[1] / 2)
      SNR_Max[1] = str(Package_1_2_Data.bID_SNR_Max[1] / 2)
      SNR_Avg[1] = str(round(Package_1_2_Data.dbl_ID_SNR_Avg[1] / 2 , 1)) 
      
    #Update Tyreinfo 3  
    if Package_1_2_Data.bPressure[2] != 0 and Package_1_2_Data.bPressure[2] != -1: 
      Pressure[2] = str((Package_1_2_Data.bPressure[2] - 2) * 25)
      Temperature[2] = str(Package_1_2_Data.bTemperature[2] - 52)
      Supplier[2] = str(Package_1_2_Data.bSupplier[2])
      PalState[2] = str(Package_1_2_Data.bPalState[2])  
      PalTxTrig[2] = str(Package_1_2_Data.bPalTxTrig[2])
      PalCounter_mem[2] = str(Package_1_2_Data.bID_PalCounter_mem[2])
      BlkCnt[2] = str(Package_1_2_Data.bID_BlkCnt[2])
      ExpBlkCnt[2] = str(Package_1_2_Data.bID_ExpBlkCnt[2])
      if ((Package_1_2_Data.bID_BlkCnt[2] > 0) and (Package_1_2_Data.bID_ExpBlkCnt[2] > 0)):
        Ausbeute_Blk[2] = str(round(100 * Package_1_2_Data.bID_BlkCnt[2] / Package_1_2_Data.bID_ExpBlkCnt[2]))
      FrmCnt[2] = str(Package_1_2_Data.bIDTgCnt[2])  
      ExpFrmCnt[2] = str(Package_1_2_Data.bID_ExpFrmCnt[2])  
      #Update Frm Ausbeute 
      if ((Package_1_2_Data.bIDTgCnt[2] > 0) and (Package_1_2_Data.bID_ExpFrmCnt[2] > 0)):
        Ausbeute_Frms[2] = str(round(100 * Package_1_2_Data.bIDTgCnt[2] / Package_1_2_Data.bID_ExpFrmCnt[2]))  
      RSSI_Last[2] = str(Package_1_2_Data.bID_RSSI_Last[2] / 2.0)
      RSSI_Min[2] = str(Package_1_2_Data.bID_RSSI_Min[2]/2) 
      RSSI_Max[2] = str(Package_1_2_Data.bID_RSSI_Max[2]/2)
      RSSI_Avg[2] = str(round(Package_1_2_Data.dbl_ID_RSSI_Avg[2] / 2 , 1))
      SNR_Last[2] = str(Package_1_2_Data.dbl_ID_SNR_Last[2] / 2.0)
      SNR_Min[2] = str(Package_1_2_Data.bID_SNR_Min[2] / 2)
      SNR_Max[2] = str(Package_1_2_Data.bID_SNR_Max[2] / 2)
      SNR_Avg[2] = str(round(Package_1_2_Data.dbl_ID_SNR_Avg[2] / 2 , 1))
        
    #Update Tyreinfo 4  
    if Package_1_2_Data.bPressure[3] != 0 and Package_1_2_Data.bPressure[3] != -1:
      Pressure[3] = str((Package_1_2_Data.bPressure[3] - 2) * 25)
      Temperature[3] = str(Package_1_2_Data.bTemperature[3] - 52)
      Supplier[3] = str(Package_1_2_Data.bSupplier[3])    
      PalState[3] = str(Package_1_2_Data.bPalState[3]) 
      PalTxTrig[3] = str(Package_1_2_Data.bPalTxTrig[3])   
      PalCounter_mem[3] = str(Package_1_2_Data.bID_PalCounter_mem[3])
      BlkCnt[3] = str(Package_1_2_Data.bID_BlkCnt[3])
      ExpBlkCnt[3] = str(Package_1_2_Data.bID_ExpBlkCnt[3])
      if ((Package_1_2_Data.bID_BlkCnt[3] > 0) and (Package_1_2_Data.bID_ExpBlkCnt[3] > 0)):
        Ausbeute_Blk[3] = str(round(100 * Package_1_2_Data.bID_BlkCnt[3] / Package_1_2_Data.bID_ExpBlkCnt[3]))
      FrmCnt[3] = str(Package_1_2_Data.bIDTgCnt[3]) 
      ExpFrmCnt[3] = str(Package_1_2_Data.bID_ExpFrmCnt[3])
      #Update Frm Ausbeute 
      if ((Package_1_2_Data.bIDTgCnt[3] > 0) and (Package_1_2_Data.bID_ExpFrmCnt[3] > 0)):
        Ausbeute_Frms[3] = str(round(100 * Package_1_2_Data.bIDTgCnt[3] / Package_1_2_Data.bID_ExpFrmCnt[3]))
      RSSI_Last[3] = str(Package_1_2_Data.bID_RSSI_Last[3] / 2.0)
      RSSI_Min[3] = str(Package_1_2_Data.bID_RSSI_Min[3]/2) 
      RSSI_Max[3] = str(Package_1_2_Data.bID_RSSI_Max[3]/2)
      RSSI_Avg[3] = str(round(Package_1_2_Data.dbl_ID_RSSI_Avg[3] / 2 , 1)) 
      SNR_Last[3] = str(Package_1_2_Data.dbl_ID_SNR_Last[3] / 2.0)
      SNR_Min[3] = str(Package_1_2_Data.bID_SNR_Min[3] / 2)
      SNR_Max[3] = str(Package_1_2_Data.bID_SNR_Max[3] / 2) 
      SNR_Avg[3] = str(round(Package_1_2_Data.dbl_ID_SNR_Avg[3] / 2 , 1))    
     
    #Update Noise values 
    NoiseArr[0] = str(Package_1_2_Data.bNoiseArr[0] / 2.0)  #MinNoise
    NoiseArr[1] = str(Package_1_2_Data.bNoiseArr[1] / 2.0)  #MaxNoise
    NoiseArr[2] = str(Package_1_2_Data.bNoiseArr[2] / 2.0)  #AvgNoise
#*******************************************************************************************************************************************#  
# def OutputSystemVariables_Pk_1_2() funtion END 
# def OutputSystemVariables_Pk_3_4() function START
# ......Read the information from the Package 3 & 4
#*******************************************************************************************************************************************#
def OutputSystemVariables_Pk_3_4():

    #Print Tyre Id in Hex
    DUTyreId[0] = Package_3_4_Data.UserTyreId[0]
    DUTyreId[1] = Package_3_4_Data.UserTyreId[1]
    DUTyreId[2] = Package_3_4_Data.UserTyreId[2]
    DUTyreId[3] = Package_3_4_Data.UserTyreId[3]
    #Update Tyreinfo 1
    if Package_3_4_Data.bPressure[0] != 0 and Package_3_4_Data.bPressure[0] != -1:  
      DPressure[0] = str((Package_3_4_Data.bPressure[0] - 2) * 25)
      DTemperature[0] = str(Package_3_4_Data.bTemperature[0] - 52)
      DSupplier[0] = str(Package_3_4_Data.bSupplier[0])
      DPalState[0] = str(Package_3_4_Data.bPalState[0])  
      DPalTxTrig[0] = str(Package_3_4_Data.bPalTxTrig[0])      
      DPalCounter_mem[0] = str(Package_3_4_Data.bID_PalCounter_mem[0])
      DBlkCnt[0] = str(Package_3_4_Data.bID_BlkCnt[0])
      DExpBlkCnt[0] = str(Package_3_4_Data.bID_ExpBlkCnt[0])
      if ((Package_3_4_Data.bID_BlkCnt[0] > 0) and (Package_3_4_Data.bID_ExpBlkCnt[0] > 0)):
        DAusbeute_Blk[0] = str(round(100 * Package_3_4_Data.bID_BlkCnt[0] / Package_3_4_Data.bID_ExpBlkCnt[0]))
      DFrmCnt[0] = str(Package_3_4_Data.bIDTgCnt[0])   
      DExpFrmCnt[0] = str(Package_3_4_Data.bID_ExpFrmCnt[0])  
      #Update Frm Ausbeute
      if ((Package_3_4_Data.bIDTgCnt[0] > 0) and (Package_3_4_Data.bID_ExpFrmCnt[0] > 0)):
        DAusbeute_Frms[0] = str(round(100 * Package_3_4_Data.bIDTgCnt[0] / Package_3_4_Data.bID_ExpFrmCnt[0]))
      DRSSI_Last[0] = str(Package_3_4_Data.bID_RSSI_Last[0] / 2.0)
      DRSSI_Min[0] = str(Package_3_4_Data.bID_RSSI_Min[0]/2) 
      DRSSI_Max[0] = str(Package_3_4_Data.bID_RSSI_Max[0]/2)
      DRSSI_Avg[0] = str(round(Package_3_4_Data.dbl_ID_RSSI_Avg[0] / 2 , 1))
      DSNR_Last[0] = str(Package_3_4_Data.dbl_ID_SNR_Last[0] / 2.0)
      DSNR_Min[0] = str(Package_3_4_Data.bID_SNR_Min[0] / 2)
      DSNR_Max[0] = str(Package_3_4_Data.bID_SNR_Max[0] / 2) 
      DSNR_Avg[0] = str(round(Package_3_4_Data.dbl_ID_SNR_Avg[0] / 2 , 1))
      
    #Update Tyreinfo 2  
    if Package_3_4_Data.bPressure[1] != 0 and Package_3_4_Data.bPressure[1] != -1: 
      DPressure[1] = str((Package_3_4_Data.bPressure[1] - 2) * 25)  
      DTemperature[1] = str(Package_3_4_Data.bTemperature[1] - 52)
      DSupplier[1] = str(Package_3_4_Data.bSupplier[1])
      DPalState[1] = str(Package_3_4_Data.bPalState[1])  
      DPalTxTrig[1] = str(Package_3_4_Data.bPalTxTrig[1]) 
      DPalCounter_mem[1] = str(Package_3_4_Data.bID_PalCounter_mem[1])
      DBlkCnt[1] = str(Package_3_4_Data.bID_BlkCnt[1])
      DExpBlkCnt[1] = str(Package_3_4_Data.bID_ExpBlkCnt[1])
      if ((Package_3_4_Data.bID_BlkCnt[1] > 0) and (Package_3_4_Data.bID_ExpBlkCnt[1] > 0)):
        DAusbeute_Blk[1] = str(round(100 * Package_3_4_Data.bID_BlkCnt[1] / Package_3_4_Data.bID_ExpBlkCnt[1])) 
      DFrmCnt[1] = str(Package_3_4_Data.bIDTgCnt[1])   
      DExpFrmCnt[1] = str(Package_3_4_Data.bID_ExpFrmCnt[1]) 
      #Update Frm Ausbeute 
      if ((Package_3_4_Data.bIDTgCnt[1] > 0) and (Package_3_4_Data.bID_ExpFrmCnt[1] > 0)):
        DAusbeute_Frms[1] = str(round(100 * Package_3_4_Data.bIDTgCnt[1] / Package_3_4_Data.bID_ExpFrmCnt[1]))  
      DRSSI_Last[1] = str(Package_3_4_Data.bID_RSSI_Last[1] / 2.0)
      DRSSI_Min[1] = str(Package_3_4_Data.bID_RSSI_Min[1]/2)
      DRSSI_Max[1] = str(Package_3_4_Data.bID_RSSI_Max[1]/2) 
      DRSSI_Avg[1] = str(round(Package_3_4_Data.dbl_ID_RSSI_Avg[1] / 2 , 1)) 
      DSNR_Last[1] = str(Package_3_4_Data.dbl_ID_SNR_Last[1] / 2.0)     
      DSNR_Min[1] = str(Package_3_4_Data.bID_SNR_Min[1] / 2)
      DSNR_Max[1] = str(Package_3_4_Data.bID_SNR_Max[1] / 2)
      DSNR_Avg[1] = str(round(Package_3_4_Data.dbl_ID_SNR_Avg[1] / 2 , 1)) 
      
    #Update Tyreinfo 3  
    if Package_3_4_Data.bPressure[2] != 0 and Package_3_4_Data.bPressure[2] != -1: 
      DPressure[2] = str((Package_3_4_Data.bPressure[2] - 2) * 25)
      DTemperature[2] = str(Package_3_4_Data.bTemperature[2] - 52)
      DSupplier[2] = str(Package_3_4_Data.bSupplier[2])
      DPalState[2] = str(Package_3_4_Data.bPalState[2])  
      DPalTxTrig[2] = str(Package_3_4_Data.bPalTxTrig[2])
      DPalCounter_mem[2] = str(Package_3_4_Data.bID_PalCounter_mem[2])
      DBlkCnt[2] = str(Package_3_4_Data.bID_BlkCnt[2])
      DExpBlkCnt[2] = str(Package_3_4_Data.bID_ExpBlkCnt[2])
      if ((Package_3_4_Data.bID_BlkCnt[2] > 0) and (Package_3_4_Data.bID_ExpBlkCnt[2] > 0)):
        DAusbeute_Blk[2] = str(round(100 * Package_3_4_Data.bID_BlkCnt[2] / Package_3_4_Data.bID_ExpBlkCnt[2]))
      DFrmCnt[2] = str(Package_3_4_Data.bIDTgCnt[2])  
      DExpFrmCnt[2] = str(Package_3_4_Data.bID_ExpFrmCnt[2])  
      #Update Frm Ausbeute 
      if ((Package_3_4_Data.bIDTgCnt[2] > 0) and (Package_3_4_Data.bID_ExpFrmCnt[2] > 0)):
        DAusbeute_Frms[2] = str(round(100 * Package_3_4_Data.bIDTgCnt[2] / Package_3_4_Data.bID_ExpFrmCnt[2]))  
      DRSSI_Last[2] = str(Package_3_4_Data.bID_RSSI_Last[2] / 2.0)
      DRSSI_Min[2] = str(Package_3_4_Data.bID_RSSI_Min[2]/2) 
      DRSSI_Max[2] = str(Package_3_4_Data.bID_RSSI_Max[2]/2)
      DRSSI_Avg[2] = str(round(Package_3_4_Data.dbl_ID_RSSI_Avg[2] / 2 , 1))
      DSNR_Last[2] = str(Package_3_4_Data.dbl_ID_SNR_Last[2] / 2.0)
      DSNR_Min[2] = str(Package_3_4_Data.bID_SNR_Min[2] / 2)
      DSNR_Max[2] = str(Package_3_4_Data.bID_SNR_Max[2] / 2)
      DSNR_Avg[2] = str(round(Package_3_4_Data.dbl_ID_SNR_Avg[2] / 2 , 1))
        
    #Update Tyreinfo 4  
    if Package_3_4_Data.bPressure[3] != 0 and Package_3_4_Data.bPressure[3] != -1:
      DPressure[3] = str((Package_3_4_Data.bPressure[3] - 2) * 25)
      DTemperature[3] = str(Package_3_4_Data.bTemperature[3] - 52)
      DSupplier[3] = str(Package_3_4_Data.bSupplier[3])    
      DPalState[3] = str(Package_3_4_Data.bPalState[3]) 
      DPalTxTrig[3] = str(Package_3_4_Data.bPalTxTrig[3])   
      DPalCounter_mem[3] = str(Package_3_4_Data.bID_PalCounter_mem[3])
      DBlkCnt[3] = str(Package_3_4_Data.bID_BlkCnt[3])
      DExpBlkCnt[3] = str(Package_3_4_Data.bID_ExpBlkCnt[3])
      if ((Package_3_4_Data.bID_BlkCnt[3] > 0) and (Package_3_4_Data.bID_ExpBlkCnt[3] > 0)):
        DAusbeute_Blk[3] = str(round(100 * Package_3_4_Data.bID_BlkCnt[3] / Package_3_4_Data.bID_ExpBlkCnt[3]))
      DFrmCnt[3] = str(Package_3_4_Data.bIDTgCnt[3]) 
      DExpFrmCnt[3] = str(Package_3_4_Data.bID_ExpFrmCnt[3])
      #Update Frm Ausbeute 
      if ((Package_3_4_Data.bIDTgCnt[3] > 0) and (Package_3_4_Data.bID_ExpFrmCnt[3] > 0)):
        DAusbeute_Frms[3] = str(round(100 * Package_3_4_Data.bIDTgCnt[3] / Package_3_4_Data.bID_ExpFrmCnt[3]))
      DRSSI_Last[3] = str(Package_3_4_Data.bID_RSSI_Last[3] / 2.0)
      DRSSI_Min[3] = str(Package_3_4_Data.bID_RSSI_Min[3]/2) 
      DRSSI_Max[3] = str(Package_3_4_Data.bID_RSSI_Max[3]/2)
      DRSSI_Avg[3] = str(round(Package_3_4_Data.dbl_ID_RSSI_Avg[3] / 2 , 1)) 
      DSNR_Last[3] = str(Package_3_4_Data.dbl_ID_SNR_Last[3] / 2.0)
      DSNR_Min[3] = str(Package_3_4_Data.bID_SNR_Min[3] / 2)
      DSNR_Max[3] = str(Package_3_4_Data.bID_SNR_Max[3] / 2) 
      DSNR_Avg[3] = str(round(Package_3_4_Data.dbl_ID_SNR_Avg[3] / 2 , 1))    
     
    #Update Noise values 
    DNoiseArr[0] = str(Package_3_4_Data.bNoiseArr[0] / 2.0)  #MinNoise
    DNoiseArr[1] = str(Package_3_4_Data.bNoiseArr[1] / 2.0)  #MaxNoise
    DNoiseArr[2] = str(Package_3_4_Data.bNoiseArr[2] / 2.0)  #AvgNoise   
    
#*******************************************************************************************************************************************#  
# def OutputSystemVariables_Pk_3_4() funtion END 
# def displayFun() function START
# ......Display the package 1 & 2 information in the GUI
#*******************************************************************************************************************************************#               
def displayFun(i):         
     return [    [ sg.Text(TyreName[i],justification='center',size=(2,1)),
                   sg.Text(UTyreId[i],justification='center',size=(7,1)),
                   sg.Text(Pressure[i],justification='center',size=(4,1)),
                   sg.Text(Temperature[i],justification='center',size=(5,1)),
                   sg.Text(Supplier[i],justification='center',size=(4,1)),
                   sg.Text(PalState[i],justification='center',size=(4,1)),
                   sg.Text(PalTxTrig[i],justification='center',size=(4,1)),
                   sg.Text(PalCounter_mem[i],justification='center',size=(4,1)),
                   sg.Text(BlkCnt[i],justification='center',size=(6,1)),
                   sg.Text(ExpBlkCnt[i],justification='center',size=(7,1)),
                   sg.Text(Ausbeute_Blk[i],justification='center',size=(8,1)),
                   sg.Text(FrmCnt[i],justification='center',size=(9,1)),
                   sg.Text(ExpFrmCnt[i],justification='center',size=(8,1)),
                   sg.Text(Ausbeute_Frms[i],justification='center',size=(11,1)),
                   sg.Text(RSSI_Last[i],justification='center',size=(7,1)),
                   sg.Text(RSSI_Min[i],justification='center',size=(7,1)),
                   sg.Text(RSSI_Max[i],justification='center',size=(8,1)),
                   sg.Text(RSSI_Avg[i],justification='center',size=(7,1)),
                   sg.Text(SNR_Last[i],justification='center',size=(7,1)),
                   sg.Text(SNR_Min[i],justification='center',size=(7,1)),
                   sg.Text(SNR_Max[i],justification='center',size=(7,1)),
                   sg.Text(SNR_Avg[i],justification='center',size=(7,1)) ]                  
            ]  
#*******************************************************************************************************************************************#  
# def displayFun() funtion END 
# def DdisplayFun() function START
# ......Display the package 3 & 4 information in the GUI
#*******************************************************************************************************************************************#               
def DdisplayFun(i):         
     return [    [ sg.Text(TyreName[i],justification='center',size=(2,1)),
                   sg.Text(DUTyreId[i],justification='center',size=(7,1)),
                   sg.Text(DPressure[i],justification='center',size=(4,1)),
                   sg.Text(DTemperature[i],justification='center',size=(5,1)),
                   sg.Text(DSupplier[i],justification='center',size=(4,1)),
                   sg.Text(DPalState[i],justification='center',size=(4,1)),
                   sg.Text(DPalTxTrig[i],justification='center',size=(4,1)),
                   sg.Text(DPalCounter_mem[i],justification='center',size=(4,1)),
                   sg.Text(DBlkCnt[i],justification='center',size=(6,1)),
                   sg.Text(DExpBlkCnt[i],justification='center',size=(7,1)),
                   sg.Text(DAusbeute_Blk[i],justification='center',size=(8,1)),
                   sg.Text(DFrmCnt[i],justification='center',size=(9,1)),
                   sg.Text(DExpFrmCnt[i],justification='center',size=(8,1)),
                   sg.Text(DAusbeute_Frms[i],justification='center',size=(11,1)),
                   sg.Text(DRSSI_Last[i],justification='center',size=(7,1)),
                   sg.Text(DRSSI_Min[i],justification='center',size=(7,1)),
                   sg.Text(DRSSI_Max[i],justification='center',size=(8,1)),
                   sg.Text(DRSSI_Avg[i],justification='center',size=(7,1)),
                   sg.Text(DSNR_Last[i],justification='center',size=(7,1)),
                   sg.Text(DSNR_Min[i],justification='center',size=(7,1)),
                   sg.Text(DSNR_Max[i],justification='center',size=(7,1)),
                   sg.Text(DSNR_Avg[i],justification='center',size=(7,1)) ]                  
            ] 
#*******************************************************************************************************************************************#  
# def DdisplayFun() funtion END 
# def onStart() function START
# ......Open the GUI with initial default values
#*******************************************************************************************************************************************#  
  
def onStart():
    global window
    if not hasattr(sys, 'argv'):
      sys.argv  = ['']

    #Package_1_2_Data.ClearBuffer_Pk_1_2()  
    
    #For Package 1 and 2 information  
    HeadingInfo = [[sg.T('ID-Eingabe          Pres.   Temp.   Supp.   State   Tx Trig   PAL Cnt   BlkCnt   Exp.BlkCnt   Ausbeute_Blk   FrmCnt   Exp.FrmCnt   Ausbeute_Frms   RSSI_Last   RSSI_Min   RSSI_Max   RSSI_Avg   SNR_Last   SNR_Min   SNR_Max   SNR_Avg')]]          
    NoiseInfo = [[sg.T('                                                                    '+'Min Noise(dBm) ' + NoiseArr[0] + '      ' +'MaxNoise(dBm) '+NoiseArr[1]+ '      ' +'AverageNoise(dBm) '+NoiseArr[2])]]
    
    #For Package 3 and 4 information  
    DHeadingInfo = [[sg.T('ID-Eingabe          Pres.   Temp.   Supp.   State   Tx Trig   PAL Cnt   BlkCnt   Exp.BlkCnt   Ausbeute_Blk   FrmCnt   Exp.FrmCnt   Ausbeute_Frms   RSSI_Last   RSSI_Min   RSSI_Max   RSSI_Avg   SNR_Last   SNR_Min   SNR_Max   SNR_Avg')]]          
    DNoiseInfo = [[sg.T('                                                                    '+'Min Noise(dBm) ' + NoiseArr[0] + '      ' +'MaxNoise(dBm) '+NoiseArr[1]+ '      ' +'AverageNoise(dBm) '+NoiseArr[2])]]
    
    layout = [[sg.Frame('Daten FBD-4',HeadingInfo,background_color='DarkGrey')],
               [sg.Frame('',displayFun(0))],
               [sg.Frame('',displayFun(1))],
               [sg.Frame('',displayFun(2))],
               [sg.Frame('',displayFun(3))],            
               [sg.Frame('',NoiseInfo,background_color='grey' )],
               [sg.Frame('Dual Daten FBD-4',DHeadingInfo,background_color='DarkGrey')],
               [sg.Frame('',DdisplayFun(0))],
               [sg.Frame('',DdisplayFun(1))],
               [sg.Frame('',DdisplayFun(2))],
               [sg.Frame('',DdisplayFun(3))],            
               [sg.Frame('',DNoiseInfo,background_color='grey' )]
               ]
    window = sg.Window("Carmen Visualization").Layout(layout).Finalize()
    
#*******************************************************************************************************************************************#  
# def onStart() funtion END 
# def onMessage(msg) function START
# ......Update the GUI based the data from the measurement file
#*******************************************************************************************************************************************#      
def onMessage(msg):
    global window
    global Id1
   
    # Get the Frame from the Carmen log file
    F1 = Messages.CarmenMessageHelper(msg)
    Flex_Frame =  F1.findFrame()  
    FrameData = str(Flex_Frame)  
    # Get the payload from the Carmen log file
    Flex_Payload = CarmenMessage.CarmenMessage.getRawMessage(msg)
    # When Frame is 'RDC_DT_PCKG_1_RDC_DT_PCKG_2' call the Pack12 functions and do the calculation
    if FrameData == 'RDC_DT_PCKG_1_RDC_DT_PCKG_2' :
      del message[:]            #Clear the list before loading new data
      print("RDC_DT_PCKG_1_RDC_DT_PCKG_2")
      print(Flex_Payload)
      for val in Flex_Payload:
         hexval = hex(val)
         message.append(hexval) #add the payload data into message list
      print(message)  
      #Package 1 2 functions    
      Package_1_2_Data.ReadTyreId()
      Package_1_2_Data.fileDataInterpretation(message)  
      Package_1_2_Data.WriteToFile()       
      OutputSystemVariables_Pk_1_2() 
      window.close()
      onStart()
    if FrameData == 'RDCDataPackage3RDCDataPackage4' :
      del message[:]            #Clear the list before loading new data
      print("RDCDataPackage3RDCDataPackage4")
      print(Flex_Payload)
      for val in Flex_Payload:
         hexval = hex(val)
         message.append(hexval) #add the payload data into message list
      print(message)    
      #Package 3 4 functions    
      Package_3_4_Data.ReadTyreId()
      Package_3_4_Data.fileDataInterpretation(message)  
      Package_3_4_Data.WriteToFile()       
      OutputSystemVariables_Pk_3_4()       
      window.close()
      onStart()
     

  
# def onStop():
    # window.close()
    # print("stop") 
PythonScript.register(onStart, "onStart")
PythonScript.register(onMessage, "message", filter="(busid == 358)")
#PythonScript.register(onStop, "onStop")
 
#Im Pythonscript Modul ohne Effekt, aber für das Makro wird es gebraucht
PythonScript.startAnalysisEventBased()
 
# carmen: {"name": "CustomUI.py"}
