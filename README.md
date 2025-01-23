Hoopla audiobook Downloader will let you download audiobooks (maybe even videos) from Hoopla Digital. Source (https://github.com/jo1gi/audiobook-dl/issues/70)

1. download and install the latest python (i used 3.13.1)

2. Open a command prompt/powershell in the directory hoopladownloaderng\Scripts and type 'pip install requests', 'pip install xmltodict', 'pip install pycryptodome', 'pip install pyperclip' 
or Install the requirements all at once by running `pip install -r requirements.txt` 

3. Run RUNME.bat [Image 4]
	3.1 You will be asked to enter 'dt-custom-data'. 
		  3.1.1 Go to hoopla with google chrome and borrow an audiobook. 
		  3.1.2 Click the Play or Resume button to start playing the content [see Image 1]. Then Immediately right-click inside Hoopla webpage and click Inspect. (then pause the audio because all we needed (to capture
            with Chrome's Inspect tool) were those first few moment of network activity after you started playing your hoopla content). Next go to Network tab. [see Image 2]
		  3.1.3 Copy and paste the value of the dt-custom-data request header on the POST request to https://lic.drmtoday.com/license-proxy-widevine/cenc/. [see Image 3 and Image 4]
	3.2 You will be asked to enter URL of the Audiobook https://www.hoopladigital.com/audiobook/the-man-who-disappeared-america-franz-kafka/16233840
	
5. if every runs smoothly you should find the audiobook in ..\hoopladownloaderng\FINISHED


![Image 1](https://github.com/user-attachments/assets/9fc0d82d-afc4-4c74-8f15-17ffe2fcd38a)
Image 1
![Image 2](https://github.com/user-attachments/assets/d51d89c8-c0da-4276-91fa-429544e2b90a)
Image 2
![Image 3](https://github.com/user-attachments/assets/15523c18-dc68-4f28-8a70-d74430d7b4e0)
Image 3
![Image 4](https://github.com/user-attachments/assets/8b09606d-302d-4cb4-b26a-7c52d6b66e66)
Image 4
