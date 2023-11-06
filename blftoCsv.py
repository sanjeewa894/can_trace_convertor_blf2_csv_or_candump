import can
import csv
import time
import math



def run_convertor(fileName):
	#read cananalyzer trace
    log = can.BLFReader(fileName + ".blf") 
    log = list(log) #create list


	log_output = []

	#set timestamp
	time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log[0].timestamp))
	log_output.append([time, 'Channel', 'CAN / CAN FD', 'Frame Type', 'CAN ID(HEX)', 'DLC', 'Data(HEX)'])
	
	#decode each message in trace file
	for msg in log:
		time_secs = msg.timestamp - log[0].timestamp
		time_secs = '%f' % (time_secs)

		if msg.is_fd:
		    can_fd = 'CAN FD'
		else:
		    can_fd = 'CAN'
		if msg.bitrate_switch:
		    can_fd = can_fd + ': Bitrate Switch'

		if msg.is_error_frame:
		    frame_type = 'Error'
		elif msg.is_remote_frame:
		    frame_type = 'Remote'
		else:
		    frame_type = 'Data'

		if msg.is_extended_id:
		    can_id = '0x{:08X}'.format(msg.arbitration_id)
		else:
		    can_id = '0x{:03X}'.format(msg.arbitration_id)

		data = ''
		for byte in msg.data:
		    data = data + '{:02X}'.format(byte) + ' '

		log_output.append([time_secs, msg.channel, can_fd, frame_type, can_id, msg.dlc, data])


	#open file to write  
   	with open((fileName+"_csvdump.csv"), "w", newline='') as f:
		writer = csv.writer(f, dialect='excel') #excel format
		writer.writerows(log_output) #write to file
    
    print("Completed writting to csv file!!!")

if __name__ == "__main__":
	#check arguments passed when running
    if(len(sys.argv) != 2):
        print("Run with input file name without extension")
        print("\n   Usage: blftoCsv.py <input file name> (Ex: blftoCsv.py traceFile)\n")
    else:
        #get trace file name
        fileName = sys.argv[1]
        #check file exist
        isexist = os.path.exists(fileName+".blf")
        #file not exist
        if(isexist == False):
            print("input file (" + fileName + ") does not exist!")
        else:
            print("Converting.... Please wait!")
            run_convertor(fileName) #convert to log
