### 对于pip、conda、anaconda和miniconda的区别。
- conda是一个包和环境管理工具，它不仅能管理包，还能隔离和管理不同python版本的环境。类似管理nodejs环境的nvm工具。

- anaconda和miniconda都是conda的一种发行版。只是包含的包不同。

- anaconda包含了conda、python等180多个科学包及其依赖项，体格比较大。但很多东西你未必用到，所以才有mini版。

- miniconda是最小的conda安装环境，只有conda+python+pip+zlib和一些其他常用的包，体格非常迷你。

- pip也叫包管理器，和conda的区别是，pip只管理python的包，而conda可以安装所有语言的包。而且conda可以管理python环境，pip不行。

`注意：miniconda所有的操作命令皆在命令行中完成，没有GUI界面。而anaconda是有界面的。`

### 1.安装miniconda
- 下载地址：https://docs.conda.io/en/latest/miniconda.html 
- 安装完成后，打开命令行，输入conda list，如果能正常显示安装的包，则安装成功。
- 如果显示conda不是内部或外部命令，则需要配置环境变量。将miniconda安装目录下的Scripts文件夹添加到环境变量中即可。
- 如果显示conda不是内部或外部命令，也没有将Scripts文件夹添加到环境变量中，可以在命令行中输入完整的路径，如：C:\Users\zhang\Miniconda3\Scripts\conda list


```
创建和管理环境：

conda create --name myenv：创建一个名为myenv的新环境。
conda env list：列出所有已创建的环境。
conda activate myenv：激活名为myenv的环境。
conda deactivate：退出当前环境，返回到基础环境。

conda env remove --name <环境名称>    # 删除指定的环境


安装和管理软件包：

conda install numpy：在当前环境中安装NumPy。
conda install pandas=1.2.3：在当前环境中安装指定版本的Pandas。
conda update numpy：在当前环境中更新NumPy到最新版本。
conda remove numpy：从当前环境中移除NumPy。
conda list：列出当前环境中已安装的所有软件包。
导出和导入环境：

conda env export > environment.yaml：将当前环境导出为YAML文件。
conda env create --file environment.yaml：根据YAML文件创建环境。
```
![pycharm使用miniconda.png](../10010-image/pycharm使用miniconda.png)
![miniconda配置001.png](../10010-image/miniconda配置001.png)

