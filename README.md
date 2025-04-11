# MigrationDowntimeAnalysis
A client-server python script for VM migration downtime analysis. 

## For Memory Denial of Service reproduction
Please refer to Appendix section of the paper: Zhang, T., Zhang, Y., & Lee, R. B. (2017, April). Dos attacks on your memory in cloud. In Proceedings of the 2017 ACM on Asia Conference on Computer and Communications Security (pp. 253-265). Available at: https://dl.acm.org/doi/10.1145/3052973.3052978, which presents the implementation of _memDoS_ attack. 

## For using MQTT benchmark
Please follow the instructions at: https://github.com/krylovsk/mqtt-benchmark

## For VM Migration downtime analysis

First, adjust the UDP_IP variable in clientDwt.py to the IP address of VM that will be monitored. 
For unstable connections, adjust sock.settimeout to avoid excessive timeout entries in the server_time.txt file. 

Then, import the serverDwt.py file to your VM. 
Run the server using python3.  

``
python3 serverDwt.py
``

From your external client, run the clientDwt.py.

``
python3 clientDwt.py
``

The client software will generate a output file: server_time.txt with the data obtained from the server. 
Filter the file for the "timeout" word to find the downtime occurence. 


