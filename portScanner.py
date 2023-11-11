import socket
import time

startTime = time.time()


if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')

   t_IP = socket.gethostbyname(target) # 將主機名稱轉換成ipv4地址
   print ('Starting scan on host: ', t_IP)

# 掃描常見的端口
   for i in range(50, 500): #可自行更改
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     conn = s.connect_ex((t_IP, i))

     if(conn == 0) :
        print ('Port %d: OPEN' % (i,))
        s.close()
print('Time taken:', time.time() - startTime)
