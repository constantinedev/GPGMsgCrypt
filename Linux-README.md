###IF YOU ARE USING LINUX TO EXECUTE THE CODE###<br>
FOLLOWING THIS<br>

1. Install Pyhton3.x and API by following command<br>
sudo apt install python3 python3-dev<br>
pip3 install -U -r request.txt --user<br>

2. If you wanna to begin One File One more step... install pyinstaller<br>
sudo apt install pyinstaller pywin32-ctypes<br>
2.1 Export To One File<br>
pyinstaller -wF UI.py -n MsgCryptTools --clean<br>

3. Execute from the terminal<br>
3.1 the output should in the direct dit<br>
So under the GPGMsgCrypt Folder and cd to dist<br>
cd GPGMsgCrypt/dist<br>
./MsgCryptTools<br>

***If you have any problem with PyInstaller<br>
Check the PyInstaller issues with <a href='https://pyinstaller.readthedocs.io/en/stable/installation.html'>PyInstaller</a>
