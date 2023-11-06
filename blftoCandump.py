import can
import csv
import time
import math
import sys, os


def run_convertor(fileName):
	#read cananalyzer trace
    log = can.BLFReader(fileName + ".blf") 
    log = list(log) #create list

	#open file to write  
    f = open((fileName+"_candump.log"), "w")

	#read each message
    for msg in log:
    	#get time stamp
        time_secs = msg.timestamp;
        #create 6digit time stamp 
        time_secs = '%6f' % (time_secs)

		#get message type
        if msg.is_fd:
            can_fd = 'can_fd'
        else:
            can_fd = 'can'
        #check message flags
        if msg.bitrate_switch:
            can_fd = can_fd + ': Bitrate Switch'

		#check message type
        if msg.is_error_frame:
            frame_type = 'Error'
        elif msg.is_remote_frame:
            frame_type = 'Remote'
        else:
            frame_type = 'Data'

		#set can id baed on id type
        if msg.is_extended_id:
            can_id = '{:08X}'.format(msg.arbitration_id)
        else:
            can_id = '{:03X}'.format(msg.arbitration_id)

		#set data
        data = ''
        for byte in msg.data:
            data = data + '{:02X}'.format(byte)
        
        
        #write data to log file by formating to log
        wstr = "("+str(time_secs)+") "+ str(can_fd) + str(msg.channel) + " " + str(can_id) +"#"+data;
        f.write(wstr)
        f.write("\n")


	#close file writting
    f.close()
    print("Successfully converted!!!")


if __name__ == "__main__":
	#check arguments passed when running
    if(len(sys.argv) != 2):
        print("Run with input file name without extension")
        print("\n   Usage: blftoCandump.py <input file name> (Ex: blftoCandump.py traceFile)\n")
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
