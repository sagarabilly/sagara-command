
# Sagara System Monitor

A quick simple Python code that shows your system status like cpu, memory, and so on.  
  
## Features
- Displays system summary, including hostname, IP, MAC address, platform details, and processor information.
- Provides memory, CPU, and disk usage statistics.
- Shows network activity and system uptime.
- Fetches kernel information.
- Load average status monitoring.

## Usage
You can run `sysmon.py` with different command-line arguments to retrieve specific system details:

```sh
python sysmon.py --info         # Shows system information summary
python sysmon.py --memory       # Displays memory status
python sysmon.py --cpu          # Shows CPU usage details
python sysmon.py --disk         # Displays disk usage information
python sysmon.py --boot         # Shows system uptime
python sysmon.py --loadaverage  # Displays load average
python sysmon.py --network      # Shows network activity
python sysmon.py --kernel       # Retrieves kernel information
```

If you have added the entire repository "sagara-command" to your environment variable (read the main README.md), you can simply use:  

```sh
sysmon --info
sysmon --memory
sysmon --cpu
sysmon --disk
sysmon --boot
sysmon --loadaverage
sysmon --network
sysmon --kernel
```  

or use the short flag, for example:  
```sh
sysmon -imcdb
```  

## Contributions
Of course, feel free to modify and any contribution will be appreciated.  
