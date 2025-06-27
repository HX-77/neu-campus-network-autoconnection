# NEU校园网开机自连接

## 环境配置

前期要求：

    conda环境(anaconda/miniconda)

打开终端，配置编程环境：
    
    conda deactivate

    conda env create -f environment.yaml -n 'your_env'

下载webdriver（以edge为例）：

    注意！！driver的版本和浏览器版本严格对应，自行查看浏览器的版本

    作者的edge版本为 123.0.2420.65 (正式版本) (64 位) ，则driver版本为123.0.2420.65 x64


    网址： https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/?form=MA13LH

    解压找到 **msedgedriver.exe**，重命名为*MicrosoftWebDriver.exe*, 复制到python.exe同路径下。（虚拟环境位于：C:\path\of\your\anaconda\envs\your\env）

## .py, .bat 修改

### .py修改

    修改为自己的校园网账户

    username.send_keys("your_username")

    password.send_keys("your_password")

### .bat 修改

    修改为conda的安装路径，以及Autoconn.py的保存路径
    
    call C:\path\of\your\anaconda\Scripts\activate.bat autoconn
    
    python C:\path\of\your\file\Autoconn.py
    
    call C:\path\of\your\anaconda\Scripts\deactivate.bat

## 开机自启动

    Win + R

    输入：shell:Common Startup， 打开‘启动’文件夹

    将.bat文件移入文件夹中

## 备注

        如果要修改启动文件夹中的.bat，只能在复制到桌面或其他无需管理员权限的位置，修改完后覆盖掉原来的.bat。