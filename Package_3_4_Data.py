# 

# Carmen default imports. Messages is necessary for using message types. log offers methods to write to the protocoll.
#import Messages
#from CarmenLogging import log
import array as myarray


# Enter code here.

#*******************************************************************************************************************************************#  
# Variables definition # START
#*******************************************************************************************************************************************#

bID_RSSI_Min = myarray.array('i',[255, 255, 255, 255])
bID_RSSI_Max = myarray.array('i',[0, 0, 0, 0])
dbl_ID_RSSI_Avg = myarray.array('d',[0.0, 0.0, 0.0, 0.0])
iID_RSSI_Sum = myarray.array('i',[0, 0, 0, 0])

bID_RSSI_Last = myarray.array('i',[0, 0, 0, 0])

bID_SNR_Min = myarray.array('i',[255, 255, 255, 255])

bID_SNR_Max = myarray.array('i',[0, 0, 0, 0])

dbl_ID_SNR_Avg = myarray.array('d',[0.0, 0.0, 0.0, 0.0])

dbl_ID_SNR_Sum = myarray.array('d',[0.0, 0.0, 0.0, 0.0])

dbl_ID_SNR_Last = myarray.array('d',[0.0, 0.0, 0.0, 0.0])

bIDTgCnt = myarray.array('i',[0, 0, 0, 0])            #// speichert die Anzahl der Empfaenge je ID 

bID_PalCounter_mem = myarray.array('i',[0, 0, 0, 0])  #// speichert den letzten wert des PAL-counters je slot zur Erkennung eines neue Blocks...

bID_ExpBlkCnt = myarray.array('i',[0, 0, 0, 0])        #// speichert die Anzahl der erwarteten Bloecke je ID

bID_ExpFrmCnt = myarray.array('i',[0, 0, 0, 0])        #// speichert die Anzahl der erwarteten Frames je ID

bID_BlkCnt = myarray.array('i',[0, 0, 0, 0])           #// speichert die Anzahl der empfangenen Bloecke je ID

dwID = myarray.array('i',[0, 0, 0, 0])

bPressure = myarray.array('i',[0, 0, 0, 0])

bTemperature = myarray.array('i',[0, 0, 0, 0])

bSupplier = myarray.array('i',[0, 0, 0, 0])

bPalState = myarray.array('i',[0, 0, 0, 0])

bPalTxTrig = myarray.array('i',[0, 0, 0, 0])
 
UserTyreId = []

bNoiseArr = myarray.array('d',[0.0, 0.0, 0.0])
x = 0

bMinNoise = 0xff
bMaxNoise = 0x00
dblAvgNoise = 0
bAliveTgCnt = 0 
iSumNoise = 0
dblAvgNoise = 0
dblSNR = 0

#*******************************************************************************************************************************************# 
# Variables definition # END
# def ReadTyreId()function START
# .....Read the Tyre Id from the UserInputFile.txt 
#*******************************************************************************************************************************************#

def ReadTyreId():

	Ftxt = open("UserInputFile.txt", "r")
	while(True):
		#read next line
		locId = Ftxt.readline()
		Id = locId.strip() 
		UserTyreId.append(Id)  
	#if line is empty, you are done with all lines in the file
		if not Id:
			break
	#print(UserTyreId) 
	Ftxt.close()  
#*******************************************************************************************************************************************# 
# def ReadTyreId()function END
# def fileDataInterpretation() funtion START 
# ......Perform the calculation from the Carmen Message#
#*******************************************************************************************************************************************# 
def fileDataInterpretation(Message):
#local variables  
	global dblAvgNoise
	global bAliveTgCnt
	global iSumNoise
	global dblSNR
	global bMinNoise 
	global bMaxNoise   
	#-----------------------------------------------------------------------------------------------#  
	# on frPDU RDC_DT_PCKG_1_RDC_DT_PCKG_2 #
	#Signalwerte aus den Datenbytes des FR-Frames in Variablen uebergeben
	#(Aktion scheint notwendig, da der Signalzugriff bei Frames nicht zuverlaessig funktioniert hat!)
	#-----------------------------------------------------------------------------------------------#  

	#sig_TYR_ID = (((byte_3 << 20) & 0xFF00000) + ((byte_2 << 12) & 0x000FF000) + ((byte_1 << 4) & 0x000000FF0) + ((byte_0 >> 4) & 0x0000000F) ); 
	#Byte_0 convert into int   
	byte_0 = int(Message[0],16)    
	#Byte_1 convert into int     
	byte_1 = int(Message[1],16) 
	#Byte_2 convert into int     
	byte_2 = int(Message[2],16) 
	#Byte_3 convert into int     
	byte_3 = int(Message[3],16) 
  
	sig_TYR_ID = (((byte_3 << 20) & 0xFF00000) + ((byte_2 << 12) & 0x000FF000) + ((byte_1 << 4) & 0x000000FF0) + ((byte_0 >> 4) & 0x0000000F) ); 
    
	sig_RDC_DT_1 = int(Message[4],16)  
	sig_RDC_DT_2 = int(Message[5],16)  
	sig_RDC_DT_3 = int(Message[6],16)  
	sig_RDC_DT_4 = int(Message[7],16)   
	#sig_SUPP_ID from byte 8
	byte_8 = int(Message[8],16)   
	sig_SUPP_ID = (byte_8 >> 4 ) & 0x0f

	sig_PCKG_ID = int(Message[9],16) 
	#sig_RDC_MES_TSTMP = (word) ((this.byte(10) << 8) & 0xFF00) + this.byte(11); 
	byte_10 = int(Message[10],16) 
	byte_11 = int(Message[11],16)   
	TSTMP1 =((byte_10 << 8) & 0xFFFF) 
	TSTMP2 = ((TSTMP1 >> 8 ) + byte_11)
	sig_RDC_MES_TSTMP ='{:04X}'.format(TSTMP2 & ((1 << 16)-1))
    
	sig_RDC_DT_5 = int(Message[12],16) 
	sig_RDC_DT_6 = int(Message[13],16) 
	sig_RDC_DT_7 = int(Message[14],16) 
	sig_RDC_DT_8 = int(Message[15],16)    
	#Determine Tyre Id
	tmpvar = ((sig_SUPP_ID << 28) & 0xF0000000) + sig_TYR_ID;
	tmpvar1 = hex(tmpvar)
	tmpvar2 = str(tmpvar1)
	tmpvar3 = tmpvar2[:-1]
	TYR_ID = tmpvar3[2:]

	#//----------------------------------------------------------------------------------------------------------------------
	#//-----------
	#//-----------   Unterscheidung zwischen Alive TG und Empfang von RDC Telgrammen
	#//-----------
	#//----------------------------------------------------------------------------------------------------------------------  
	#//-----------   => Alive TG
	#//----------------------------------------------------------------------------------------------------------------------
	#//#define cTelTypeAlive             (uint8) 0xFF /* FBD4 alive telegram: PCKG_ID = 255. Supplier and Tyre ID must be 0 */ 
	if ((sig_PCKG_ID == 0xff) and (sig_SUPP_ID == 0x00)) :  
		if sig_RDC_DT_4 > 0 : 
			#Empfangscounter zahlen 
			bAliveTgCnt = bAliveTgCnt + 1  
			#Noise Mittelwert bilden
			iSumNoise += sig_RDC_DT_4 
			if ((iSumNoise > 0) and (bAliveTgCnt > 0)):
				dblAvgNoise = iSumNoise / bAliveTgCnt; 
				#Noise Min und Max bilden
				if (sig_RDC_DT_4 <= bMinNoise):
					bMinNoise = sig_RDC_DT_4 
				if (sig_RDC_DT_4 >= bMaxNoise):
					bMaxNoise = sig_RDC_DT_4
	#//----------------------------------------------------------------------------------------------------------------------             
	#-----------   => RDC Telegramm  
	#//---------------------------------------------------------------------------------------------------------------------- 
	else:
		#RID
		#//#define cTelTypeTyreDOT           (uint8) 0x40 /* No P/T */
		#//#define cTelTypeTyreDIM           (uint8) 0x52 /* No P/T */
		#//#define cTelTypeTyreDataOE1       (uint8) 0xCD /* No P/T */
		#//#define cTelTypeTyreDataOE2       (uint8) 0xCE /* No P/T */
		#//#define cTelTypeTyreStatus        (uint8) 0xCF /* No P/T */ 
		if ((sig_PCKG_ID == 0x40) or (sig_PCKG_ID == 0x52) or (sig_PCKG_ID == 0xCD) or (sig_PCKG_ID == 0xCE) or (sig_PCKG_ID == 0xCF)):  
			#write("PackID = 0x%02X", sig_PCKG_ID);  
			# => hier koennte man noch die RID-Daten speichern.... 
			print("Inside if sig Id ")        
		else:
			#//---------------------------------------------------------------------------------------
			#//------  Telegramm Empfang  
			#//---------------------------------------------------------------------------------------
			#//--------------- telegram types for BMW35up  ---------------
			#//#define cTelTypeContiFP           (uint8) 0x80 /* Loc Sync. Also check supplier id!! */
			#//#define cTelTypeSELPAL            (uint8) 0x03 /* Pal w/o learn bit */
			#//#define cTelTypeSELPAL1           (uint8) 0x23 /* Pal w learn bit   */
			#//#define cTelTypeAK35def           (uint8) 0x00 /* only P/T */
			#//#define cTelTypeAK35defLMA        (uint8) 0x20 /* only P/T */
			#//#define cTelTypeG4Standard        (uint8) 0xA5 /* only P/T */
			#//#define cTelTypeBeruLong          (uint8) 0x88 /* only P/T */
			#//#define cTelTypeBeruMed           (uint8) 0xA0 /* only P/T */        
			#//---------------------------------------------------------------------------------------    
			#print("Inside else")         
			#//ID Slot herausfinden        
			if (TYR_ID == UserTyreId[0]):              #@sysvar::FBD4_Empfang_Panel::ID_0) //(@sysvar::DebugMsg::ECU_ZOM_00_WU_ID & 0x0fffffff))
				#print ("Tyre id is matching with UserTyId 0")          
				bSlot = 0          
			elif (TYR_ID == UserTyreId[1]):      # @sysvar::FBD4_Empfang_Panel::ID_1) //(@sysvar::DebugMsg::ECU_ZOM_01_WU_ID & 0x0fffffff))          
				#print ("Tyre id is matching with UserTyId 1")  
				bSlot = 1          
			elif (TYR_ID == UserTyreId[2]):      # @sysvar::FBD4_Empfang_Panel::ID_2) //(@sysvar::DebugMsg::ECU_ZOM_02_WU_ID & 0x0fffffff))         
				#print ("Tyre id is matching with UserTyId 2")            
				bSlot = 2         
			elif (TYR_ID == UserTyreId[3]):      # @sysvar::FBD4_Empfang_Panel::ID_3) //(@sysvar::DebugMsg::ECU_ZOM_03_WU_ID & 0x0fffffff))          
				#print ("Tyre id is matching with UserTyId 3")  
				bSlot = 3          
			else:          
				bSlot = 0xff;              #// else-Zweig fehlte 31.05.2017 CD&ME                           
			if (bSlot < 4):
				#// Daten speichern...  
				dwID[bSlot] = sig_TYR_ID;                              # //(dword)this.TYR_ID;              
				bPalState[bSlot] = ((sig_RDC_DT_4 >> 5) & 0x07)
				bPalTxTrig[bSlot] = ((sig_RDC_DT_5 >> 6) & 0x03)       
				bSupplier[bSlot] = sig_SUPP_ID
				bPressure[bSlot] = sig_RDC_DT_1
				bTemperature[bSlot] = sig_RDC_DT_2 
            
				#//Telegramm zahlen
				bIDTgCnt[bSlot] = bIDTgCnt[bSlot] + 1 
				if (bIDTgCnt[bSlot] > 1):           #// Beim ersten TG kann man noch nicht bewerten ob ein TG ausgefallen ist, weil man keinen Referenzwert des PAL-Counters hat!!          
					# // Erwartete Telegramme ermitteln
					bPalCounter = (sig_RDC_DT_4 & 0x1F)           
					# // Ueberlauf Pal Counter beruecksichtigen ==> + 31  
					if (bPalCounter != bID_PalCounter_mem[bSlot]):
						bID_BlkCnt[bSlot] = bID_BlkCnt[bSlot] + 1    
						# // Ueberlauf Pal Counter beruecksichtigen ==> + 31  
					if (bPalCounter < bID_PalCounter_mem[bSlot]):
						bPalCounter = bPalCounter + 31            
					# // Differenz des PAL-Counters seit dem letzten TG ergibt die Anzahl an erwarteten TG
					bID_ExpBlkCnt[bSlot] = bID_ExpBlkCnt[bSlot] + bPalCounter - bID_PalCounter_mem[bSlot]
					# //Aus der Anzahl der erwarteten Bloecke die Abzahl erwarteter Frames ableiten
					bID_ExpFrmCnt[bSlot] = bID_ExpBlkCnt[bSlot] * 3
				else:        
					# //  erstes TG => erwartung 1 Blk, 1 Frame
					bID_ExpBlkCnt[bSlot] = 1
					bID_BlkCnt[bSlot] = 1
					bID_ExpFrmCnt[bSlot] = 1  
				#// alten Counterwert sichern         
				bID_PalCounter_mem[bSlot] = (sig_RDC_DT_4 & 0x1F)  
				#// letze RSSI Werte sichern  
				bID_RSSI_Last[bSlot] = sig_RDC_DT_7
				# //Rssi Minwert bilden              
				if (sig_RDC_DT_7 <= bID_RSSI_Min[bSlot]):
					bID_RSSI_Min[bSlot] = sig_RDC_DT_7       
				# //Rssi Maxwert bilden          
				if (sig_RDC_DT_7 >= bID_RSSI_Max[bSlot]):
					bID_RSSI_Max[bSlot] = sig_RDC_DT_7           
				#  //Rssi Mittelwert bilden         
				iID_RSSI_Sum[bSlot] = iID_RSSI_Sum[bSlot] + sig_RDC_DT_7         
				# // write("RSSI Avg => iID_RSSI_Sum = %d ; bIDTgCnt = %d", iID_RSSI_Sum[bSlot], bIDTgCnt[bSlot]);
				if ((iID_RSSI_Sum[bSlot] > 0) and ( bIDTgCnt[bSlot] > 0)): 
					dbl_ID_RSSI_Avg[bSlot] = iID_RSSI_Sum[bSlot] / bIDTgCnt[bSlot]          
				# //SNR bilden
				if (dblAvgNoise < sig_RDC_DT_7):         #// if-Abfrage erganzt zur Vermeidung eines Ueberlaufs 31.05.2017 CD&ME
					dblSNR = sig_RDC_DT_7 - dblAvgNoise
					#// letze SNR Werte sichern  
					dbl_ID_SNR_Last[bSlot] = dblSNR
					#//SNR Minwert bilden
					if (dblSNR <= bID_SNR_Min[bSlot]):
						bID_SNR_Min[bSlot] = dblSNR
					#//SNR Maxwert bilden
					if (dblSNR >= bID_SNR_Max[bSlot]):
						bID_SNR_Max[bSlot] = dblSNR
					#//SNR Mittelwert bilden
					dbl_ID_SNR_Sum[bSlot] = dbl_ID_SNR_Sum[bSlot] + dblSNR        
					if ((dbl_ID_SNR_Sum[bSlot] > 0) and (bIDTgCnt[bSlot] > 0 )):
						dbl_ID_SNR_Avg[bSlot] = dbl_ID_SNR_Sum[bSlot] / bIDTgCnt[bSlot]
	bNoiseArr[0] = bMinNoise
	bNoiseArr[1] = bMaxNoise
	bNoiseArr[2] = dblAvgNoise
  
#*******************************************************************************************************************************************# 
# def fileDataInterpretation()function END
# def WriteToFile() funtion START 
# ......Open the file in write mode and write the data into file
#*******************************************************************************************************************************************#     

def WriteToFile():
	ID_0_Ausbeute = 0
	ID_1_Ausbeute = 0
	ID_2_Ausbeute = 0
	ID_3_Ausbeute = 0

	ID_0_Ausbeute_Frms = 0
	ID_1_Ausbeute_Frms = 0
	ID_2_Ausbeute_Frms = 0
	ID_3_Ausbeute_Frms = 0
  
  
	Fwr = open("OutputFile_Dual_Daten_FBD.txt", "w")  
	Fwr.write("//****************************************************//\n") 
	Fwr.write("Daten Dual-FBD \n")       
	Fwr.write("//****************************************************//\n")  
  
	#Update Min RSSI values
	Fwr.write("//Update Min RSSI values\n")    
	Fwr.write("ID_0_RSSI_Min " + str(bID_RSSI_Min[0] / 2) + "\n")
	Fwr.write("ID_1_RSSI_Min " + str(bID_RSSI_Min[1] / 2)+ "\n") 
	Fwr.write("ID_2_RSSI_Min " + str(bID_RSSI_Min[2] / 2)+ "\n") 
	Fwr.write("ID_3_RSSI_Min " + str(bID_RSSI_Min[3] / 2)+ "\n")  
	Fwr.write("\n")               
	#Update Max RSSI values
	Fwr.write("//Update Max RSSI values\n") 
	Fwr.write("ID_0_RSSI_Max " + str(bID_RSSI_Max[0] / 2)+ "\n")
	Fwr.write("ID_1_RSSI_Max " + str(bID_RSSI_Max[1] / 2)+ "\n") 
	Fwr.write("ID_2_RSSI_Max " + str(bID_RSSI_Max[2] / 2)+ "\n") 
	Fwr.write("ID_3_RSSI_Max " + str(bID_RSSI_Max[3] / 2)+ "\n")               
	Fwr.write("\n") 
	#Update Avg RSSI values
	Fwr.write("//Update Avg RSSI values\n")     
	Fwr.write("ID_0_RSSI_Avg " + str(round(dbl_ID_RSSI_Avg[0] / 2.0 , 1))+ "\n")
	Fwr.write("ID_1_RSSI_Avg " + str(round(dbl_ID_RSSI_Avg[1] / 2.0 , 1))+ "\n") 
	Fwr.write("ID_2_RSSI_Avg " + str(round(dbl_ID_RSSI_Avg[2] / 2.0 , 1))+ "\n") 
	Fwr.write("ID_3_RSSI_Avg " + str(round(dbl_ID_RSSI_Avg[3] / 2.0 , 1))+ "\n")               
	Fwr.write("\n")               
	#Update Last RSSI values
	Fwr.write("//Update Last RSSI values\n")     
	Fwr.write("ID_0_RSSI_Last_Blk " + str(bID_RSSI_Last[0] / 2.0)+ "\n")
	Fwr.write("ID_1_RSSI_Last_Blk " + str(bID_RSSI_Last[1] / 2.0)+ "\n") 
	Fwr.write("ID_2_RSSI_Last_Blk " + str(bID_RSSI_Last[2] / 2.0)+ "\n") 
	Fwr.write("ID_3_RSSI_Last_Blk " + str(bID_RSSI_Last[3] / 2.0)+ "\n")               
	Fwr.write("\n")               
	#Update Min SNR Values
	Fwr.write("//Update Min SNR Values\n")     
	Fwr.write("ID_0_SNR_Min " + str(bID_SNR_Min[0] / 2)+ "\n")
	Fwr.write("ID_1_SNR_Min " + str(bID_SNR_Min[1] / 2)+ "\n") 
	Fwr.write("ID_2_SNR_Min " + str(bID_SNR_Min[2] / 2)+ "\n") 
	Fwr.write("ID_3_SNR_Min " + str(bID_SNR_Min[3] / 2)+ "\n")               
	Fwr.write("\n")   
	#Update Max SNR Values
	Fwr.write("//Update Max SNR Values\n")     
	Fwr.write("ID_0_SNR_Max " + str(bID_SNR_Max[0] / 2)+ "\n")
	Fwr.write("ID_0_SNR_Max " + str(bID_SNR_Max[1] / 2)+ "\n") 
	Fwr.write("ID_0_SNR_Max " + str(bID_SNR_Max[2] / 2)+ "\n") 
	Fwr.write("ID_0_SNR_Max " + str(bID_SNR_Max[3] / 2)+ "\n")               
	Fwr.write("\n")  
	#Update Avg SNR values
	Fwr.write("//Update Avg SNR values\n")     
	Fwr.write("ID_0_SNR_Avg " + str(round(dbl_ID_SNR_Avg[0] / 2.0 , 1))+ "\n")
	Fwr.write("ID_1_SNR_Avg " + str(round(dbl_ID_SNR_Avg[1] / 2.0 , 1))+ "\n") 
	Fwr.write("ID_2_SNR_Avg " + str(round(dbl_ID_SNR_Avg[2] / 2.0 , 1))+ "\n")
	Fwr.write("ID_3_SNR_Avg " + str(round(dbl_ID_SNR_Avg[3] / 2.0 , 1))+ "\n")               
	Fwr.write("\n")     
	#Update Last SNR values 
	Fwr.write("//Update Last SNR values \n")     
	Fwr.write("ID_0_SNR_Last_Blk " + str(dbl_ID_SNR_Last[0] / 2.0)+ "\n")
	Fwr.write("ID_1_SNR_Last_Blk " + str(dbl_ID_SNR_Last[1] / 2.0)+ "\n") 
	Fwr.write("ID_2_SNR_Last_Blk " + str(dbl_ID_SNR_Last[2] / 2.0)+ "\n") 
	Fwr.write("ID_3_SNR_Last_Blk " + str(dbl_ID_SNR_Last[3] / 2.0)+ "\n")               
	Fwr.write("\n")     
	#Update Noise values 
	Fwr.write("//Update Noise values \n")     
	Fwr.write("Noise_Minimum " + str(bMinNoise / 2.0)+ "\n")
	Fwr.write("Noise_Maximum " + str(bMaxNoise / 2.0)+ "\n") 
	Fwr.write("Noise_Average " + str(dblAvgNoise / 2.0)+ "\n") 
	Fwr.write("Noise_Average_Raw " + str(dblAvgNoise)+ "\n")               
	Fwr.write("\n")     
	#Update Blk cnt
	Fwr.write("//Update Blk cnt \n")     
	Fwr.write("ID_0_Blks " + str(bID_BlkCnt[0] )+ "\n")
	Fwr.write("ID_1_Blks " + str(bID_BlkCnt[1])+ "\n") 
	Fwr.write("ID_2_Blks " + str(bID_BlkCnt[2])+ "\n") 
	Fwr.write("ID_3_Blks " + str(bID_BlkCnt[3])+ "\n")                
	Fwr.write("\n")
	#Update Exp Blks
	Fwr.write("//Update Exp Blks  \n")     
	Fwr.write("ID_0_Blks_Exp " + str(bID_ExpBlkCnt[0])+ "\n")
	Fwr.write("ID_1_Blks_Exp " + str(bID_ExpBlkCnt[1])+ "\n") 
	Fwr.write("ID_2_Blks_Exp " + str(bID_ExpBlkCnt[2])+ "\n") 
	Fwr.write("ID_3_Blks_Exp " + str(bID_ExpBlkCnt[3])+ "\n")                
	Fwr.write("\n")  
	#Update Blk Ausbeute
	Fwr.write("//Update Blk Ausbeute  \n")     
	if ((bID_BlkCnt[0] > 0) and (bID_ExpBlkCnt[0] > 0)):
		ID_0_Ausbeute = round(100 * bID_BlkCnt[0] / bID_ExpBlkCnt[0])
	if ((bID_BlkCnt[1] > 0) and (bID_ExpBlkCnt[1] > 0)):
		ID_1_Ausbeute = round(100 * bID_BlkCnt[1] / bID_ExpBlkCnt[1])      
	if ((bID_BlkCnt[2] > 0) and (bID_ExpBlkCnt[2] > 0)):
		ID_2_Ausbeute = round(100 * bID_BlkCnt[2] / bID_ExpBlkCnt[2])
	if ((bID_BlkCnt[3] > 0) and (bID_ExpBlkCnt[3] > 0)):
		ID_3_Ausbeute = round(100 * bID_BlkCnt[3] / bID_ExpBlkCnt[3])      
	Fwr.write("ID_0_Ausbeute " + str(ID_0_Ausbeute)+ "\n") 
	Fwr.write("ID_1_Ausbeute " + str(ID_1_Ausbeute)+ "\n")     
	Fwr.write("ID_2_Ausbeute " + str(ID_2_Ausbeute)+ "\n") 
	Fwr.write("ID_3_Ausbeute " + str(ID_3_Ausbeute)+ "\n")       
	Fwr.write("\n") 
	#Update Frm cnt
	Fwr.write("//Update Frm cnt \n")     
	Fwr.write("ID_0_Frms " + str(bIDTgCnt[0] )+ "\n")
	Fwr.write("ID_1_Frms " + str(bIDTgCnt[1] )+ "\n")    
	Fwr.write("ID_2_Frms " + str(bIDTgCnt[2] )+ "\n")
	Fwr.write("ID_3_Frms " + str(bIDTgCnt[3] )+ "\n")
	Fwr.write("\n")     
	#Update Exp Frm
	Fwr.write("//Update Exp Frm  \n")     
	Fwr.write("ID_0_Frms_Exp " + str(bID_ExpFrmCnt[0])+ "\n")    
	Fwr.write("ID_1_Frms_Exp " + str(bID_ExpFrmCnt[1])+ "\n")  
	Fwr.write("ID_2_Frms_Exp " + str(bID_ExpFrmCnt[2])+ "\n")  
	Fwr.write("ID_3_Frms_Exp " + str(bID_ExpFrmCnt[3])+ "\n") 
	Fwr.write("\n")     
	#Update Frm Ausbeute
	Fwr.write("//Update Frm Ausbeute  \n")     
	if ((bIDTgCnt[0] > 0) and (bID_ExpFrmCnt[0] > 0)):
		ID_0_Ausbeute_Frms = round(100 * bIDTgCnt[0] / bID_ExpFrmCnt[0])
	if ((bIDTgCnt[1] > 0) and (bID_ExpFrmCnt[1] > 0)):
		ID_1_Ausbeute_Frms = round(100 * bIDTgCnt[1] / bID_ExpFrmCnt[1])
	if ((bIDTgCnt[2] > 0) and (bID_ExpFrmCnt[2] > 0)):
		ID_2_Ausbeute_Frms = round(100 * bIDTgCnt[2] / bID_ExpFrmCnt[2])      
	if ((bIDTgCnt[3] > 0) and (bID_ExpFrmCnt[3] > 0)):
		ID_3_Ausbeute_Frms = round(100 * bIDTgCnt[3] / bID_ExpFrmCnt[3])
	Fwr.write("ID_0_Ausbeute_Frms " + str(ID_0_Ausbeute_Frms)+ "\n") 
	Fwr.write("ID_1_Ausbeute_Frms " + str(ID_1_Ausbeute_Frms)+ "\n") 
	Fwr.write("ID_2_Ausbeute_Frms " + str(ID_2_Ausbeute_Frms)+ "\n") 
	Fwr.write("ID_3_Ausbeute_Frms " + str(ID_3_Ausbeute_Frms)+ "\n")     
	Fwr.write("\n") 
	#Update Pressure
	Fwr.write("//Update Pressure \n")   
	Fwr.write("ID_0_Pressure " + str((bPressure[0] - 2) * 25 )+ "\n") 
	Fwr.write("ID_1_Pressure " + str((bPressure[1] - 2) * 25 )+ "\n") 
	Fwr.write("ID_2_Pressure " + str((bPressure[2] - 2) * 25 )+ "\n") 
	Fwr.write("ID_3_Pressure " + str((bPressure[3] - 2) * 25 )+ "\n")     
	Fwr.write("\n") 
	#Update Temperature
	Fwr.write("//Update Temperature \n")   
	Fwr.write("ID_0_Temperature " + str(bTemperature[0] - 52)+ "\n")   
	Fwr.write("ID_1_Temperature " + str(bTemperature[1] - 52)+ "\n")  
	Fwr.write("ID_2_Temperature " + str(bTemperature[2] - 52)+ "\n")  
	Fwr.write("ID_3_Temperature " + str(bTemperature[3] - 52)+ "\n")  
	Fwr.write("\n")     
	#Update Supplier
	Fwr.write("//Update Supplier \n")   
	Fwr.write("ID_0_Supplier " + str(bSupplier[0])+ "\n")     
	Fwr.write("ID_1_Supplier " + str(bSupplier[1])+ "\n")  
	Fwr.write("ID_2_Supplier " + str(bSupplier[2])+ "\n")  
	Fwr.write("ID_3_Supplier " + str(bSupplier[3])+ "\n")  
	Fwr.write("\n")     
	#Update PAL BasicState
	Fwr.write("//Update PAL BasicState \n")   
	Fwr.write("ID_0_PAL_BasicState " + str(bPalState[0])+ "\n") 
	Fwr.write("ID_1_PAL_BasicState " + str(bPalState[1])+ "\n") 
	Fwr.write("ID_2_PAL_BasicState " + str(bPalState[2])+ "\n")     
	Fwr.write("ID_3_PAL_BasicState " + str(bPalState[3])+ "\n") 
	Fwr.write("\n")
	#Update PAL Counter
	Fwr.write("//Update PAL Counter \n")   
	Fwr.write("ID_0_PAL_Counter " + str(bID_PalCounter_mem[0])+ "\n")    
	Fwr.write("ID_1_PAL_Counter " + str(bID_PalCounter_mem[1])+ "\n")     
	Fwr.write("ID_2_PAL_Counter " + str(bID_PalCounter_mem[2])+ "\n")     
	Fwr.write("ID_3_PAL_Counter " + str(bID_PalCounter_mem[3])+ "\n")     
	Fwr.write("\n")  
	#Update PAL TxTrig
	Fwr.write("//Update PAL TxTrig \n")   
	Fwr.write("ID_0_PAL_TxTrig " + str(bPalTxTrig[0])+ "\n") 
	Fwr.write("ID_1_PAL_TxTrig " + str(bPalTxTrig[1])+ "\n") 
	Fwr.write("ID_2_PAL_TxTrig " + str(bPalTxTrig[2])+ "\n") 
	Fwr.write("ID_3_PAL_TxTrig " + str(bPalTxTrig[3])+ "\n")     
	Fwr.write("\n")     
       
#*******************************************************************************************************************************************#  
# def WriteToFile() function END 
#*******************************************************************************************************************************************#         

#*******************************************************************************************************************************************#  
# Code Ends here # 
#*******************************************************************************************************************************************#  


#Starts event based trace analysis in macros, please do not remove.
#PythonScript.startAnalysisEventBased()
# carmen: {"name": "Package_3_4_Data.py"}
