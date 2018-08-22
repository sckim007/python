# 설치 순서 #
1. Cuda 9.0 Install
<pre>
주소 : https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

cuda_9.0.176_win10.exe		<Base Package>
cuda_9.0.176.1_windows.exe	<Patch Package>
cuda_9.0.176.2_windows.exe	<Patch Package>
cuda_9.0.176.3_windows.exe	<Patch Package>
cuda_9.0.176.4_windows.exe	<Patch Package>
</pre>

2. cudnn 7.2.1.38 설치
<pre>
<b>주소 : https://developer.nvidia.com/rdp/cudnn-download</b>

"I Agree To the Terms of ..." 체크
"Download cuDNN v7.2.1 (August 7, 2018), for CUDA 9.0" 클릭
"cuDNN v7.2.1 Library for Windows 10" 클릭 및  다운로드

<b>압축해제 : cudnn-9.0-windows10-x64-v7.2.1.38.zip</b>

<b>파일 복사</b>
* installpath는 압축해제한 디렉토리 path(cudnn-9.0-windows10-x64-v7.2.1.38)
Copy <installpath>\cuda\bin\cudnn64_7.dll to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin.
Copy <installpath>\cuda\ include\cudnn.h to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include.
Copy <installpath>\cuda\lib\x64\cudnn.lib to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64.
</pre>

3. 시스템 환경변수 확인
<pre>
"내PC" -> "속성" -> "고급시스템설정" -> "환경변수"
"시스템 변수에 아래 값이 설정되어야 함."
...
CUDA_PATH 		C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0
CUDA_PATH_V9_0	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0
...
Path 에 아래 디렉토리가 추가되어야 함.
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\libnvvp
...      
</pre>

4. GPU 확인 : deviceQuery.exe 프로그램을 실행하여 GPU 정보를 확인한다.
<pre>
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\extras\demo_suite>deviceQuery.exe
deviceQuery.exe Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GTX 1080 Ti"
  CUDA Driver Version / Runtime Version          9.0 / 9.0
  CUDA Capability Major/Minor version number:    6.1
  Total amount of global memory:                 11264 MBytes (11811160064 bytes)
  (28) Multiprocessors, (128) CUDA Cores/MP:     3584 CUDA Cores
  GPU Max Clock rate:                            1633 MHz (1.63 GHz)
  Memory Clock rate:                             5505 Mhz
  Memory Bus Width:                              352-bit
  L2 Cache Size:                                 2883584 bytes
...
</pre>

5. Open Hardware Monitor 설치
<pre>
주소 : https://openhardwaremonitor.org/downloads/
</pre>

6. Python 3.6 설치
<pre>
주소 : https://www.python.org/downloads/
</pre>

7. Pycharm 설치
<pre>
주소 : https://www.jetbrains.com/pycharm/download/#section=windows
</pre>

8. Git 설치
<pre>
주소 : https://git-scm.com/download/win
</pre>

9. Pycharm GitHub 연동
<pre>
<b>GitHub 계정 및 프로젝트 생성</b>
</pre>

<pre>
<b>ID/PWD를 이용하여 GitHup 접속</b>
  "File" -> "Setting" -> "Version Control" ->"Git"의 "Path to Git executable" 필드에 "git.exe" Path 설정
    < Path to Git executable : C:\Program Files\Git\cmd\git.exe >
  "File" -> "Setting" -> "Version Control" ->"GitHub"에서
    < GitHub에서 생성한 ID/PWD로 Login 절차 수행 >
</pre>

<pre>
<b>최초 소스 Checkout</b>
  "VCS" -> "Check https://github.com/sckim007/python.githttps://github.com/sckim007/python.gitout from version control" -> "Git"에서 
          < URL : https://github.com/sckim007/python.git 입력 후 Test 버튼 클릭>
          < Clone 버튼을 클릭하여 GitHub 으로부터 소스를 Checkout 받는다 >
</pre>

<pre>
<b>변경 소스 Push/Pull</b>
    "VCS" -> "Update"/"Commit"
    "VCS" -> "Git" -> "Push"/"Pull"
</pre>

10. tensorflow 관련 패키지 설치
<pre>
<b>Pycharm의 "File" -> "Settings" -> "Project" -> "Project Interpreter"에서 설치</b>
  tensorflow 1.8.0 또는 1.10.0
  tensorflow-gpu 1.8.0 또는 1.10.0
  matplotlib 2.2.3
  numpy 1.14.5
  opencv-python 3.4.2.17
</pre>
