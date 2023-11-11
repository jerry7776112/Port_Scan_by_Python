## 專案名稱: Cyber Security Tool Port Scan by Python

### 參考檔案:**[Port_Scan_by_Python.pdf](https://github.com/jerry7776112/Port_Scan_by_Python/blob/main/Port_Scan_by_Python.pdf)**

### Introduction:
Port掃描可以定義為一種監視技術，用於定位特定主機上可用的開放Port。 網路管理員、滲透測試人員或駭客都可以使用此技術。 可根據需要配置Port掃描器，以從目標系統獲取更多的資訊。
##### 執行port掃描可獲得的資訊:
* 目標系統Port的資訊。
* 每個Port上執行的服務資訊。
* 目標主機的作業系統和 MAC 位址的資訊。

##### Port範圍
TCP/IP 協定由 TCP 和 UDP 兩個協定所組成。 兩種協定都有 0 到 65535 的Port。 65535個Port可以分為以下三個範圍：
* 系統常用的Port：從 0 到 1023
* 使用者或註冊相關的Port：從 1024 到 49151
* 動態或私有的Port：全部 > 49151

##### threading 多執行緒處理
Python 在執行時，通常是採用**同步**的任務處理模式，也就是說一個任務完成後才會接下去執行第二個任務，然而 Python 的標準函式**threading**採用**執行緒**的方式，運用多個**執行緒**，在同一時間內同時執行多個任務為，稱為**非同步**。

#### 實作
* Port Scan by Python
* Network Concept(Port)
* Python-threading

#### Usage
1.  ```python portScanner.py ```
2.  ```portScanner_threaded.py``` (increasing efficiency)
