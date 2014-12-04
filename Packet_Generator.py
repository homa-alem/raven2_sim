import socket
import struct
import csv
import time
from collections import namedtuple

UDP_IP = "127.0.0.1"
UDP_PORT = 36000
format_ = "<IIIiiiiiiddddddddddddddddddddddddddddddiiiiii"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

u_struct = namedtuple("u_struct", "sequence pactyp version delx0 delx1 dely0 dely1 delz0 delz1 R_l00 R_l01 R_l02 R_l10 R_l11 R_l12 R_l20 R_l21 R_l22 R_r00 R_r01 R_r02 R_r10 R_r11 R_r12 R_r20 R_r21 R_r22 ltheta1 ltheta2 ld3 ltheta4 ltheta5 ltheta6 rtheta1, rtheta2, rd3, rtheta4, rtheta5, rtheta6 buttonstate0 buttonstate1 grasp0 grasp1 surgeon_mode checksum");

csvfile1 = open('/home/homa/Documents/raven_2/left.txt'); 
f_left = csv.reader(csvfile1)
csvfile2 = open('/home/homa/Documents/raven_2/right.txt') 
f_right  = csv.reader(csvfile2)
seq = 0;
#l_line = f_left.next();
#r_line = f_right.next();
#while(1):
for l_line in f_left:
	seq = seq + 1;	
	r_line = f_right.next();
	#print float(l_line[0]);
	#test_msg = struct.pack("f",float(l_line[0]))
	#test_msg = struct.unpack("f",test_msg)
	#print test_msg
        tuple_to_send = u_struct(sequence = seq, 
	                pactyp = 0, 
	                version = 0, 
	                delx0 = int(float(l_line[0])*1000),
			delx1 = int(float(r_line[0])*1000),
	                dely0 = int(float(l_line[1])*1000),
			dely1 = int(float(r_line[1])*1000),
	                delz0 = int(float(l_line[2])*1000),
			delz1 = int(float(r_line[2])*1000),
			R_l00 = float(l_line[3]),
			R_l01 = float(l_line[4]),
			R_l02 = float(l_line[5]),
			R_l10 = float(l_line[6]),
			R_l11 = float(l_line[7]), 
			R_l12 = float(l_line[8]),
          		R_l20 = float(l_line[9]),
			R_l21 = float(l_line[10]),
			R_l22 = float(l_line[11]),
			R_r00 = float(r_line[3]),
			R_r01 = float(r_line[4]), 
			R_r02 = float(r_line[5]),
			R_r10 = float(r_line[6]),
			R_r11 = float(r_line[7]), 
			R_r12 = float(r_line[8]),
          		R_r20 = float(r_line[9]),
			R_r21 = float(r_line[10]),
			R_r22 = float(r_line[11]),
			ltheta1 = float(l_line[12]),
			ltheta2 = float(l_line[13]), 
			ld3 = float(l_line[14]),
			ltheta4 = float(l_line[15]),
			ltheta5 = float(l_line[16]),
			ltheta6 = float(l_line[17]),
			rtheta1 = float(r_line[12]),
			rtheta2 = float(r_line[13]), 
			rd3 = float(r_line[14]),
			rtheta4 = float(r_line[15]),
			rtheta5 = float(r_line[16]),
			rtheta6 = float(r_line[17]),
		        buttonstate0 = 0,
			buttonstate1 = 0, 
		        grasp0 = float(l_line[18]),
	 		grasp1 = float(r_line[18]), 
		        surgeon_mode = 1, 
		        checksum=0);

	MESSAGE = struct.pack(format_,*tuple_to_send._asdict().values());

	print "Packet No. ", seq
	print struct.unpack(format_,MESSAGE);
	print "\n"

	sock = socket.socket(socket.AF_INET, # Internet
		              socket.SOCK_DGRAM) # UDP

	# Send the command to the robot
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

	# Wait for a response from the robot
	#data, addr = sock.recvfrom(1024);
 	time.sleep(0.0001)

