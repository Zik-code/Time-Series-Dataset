# Time-Series-Dataset
&emsp;&emsp;这里存放一些时序数据异常检测的常用数据集，包含原始数据文件和经过预处理后的文件。
预处理后的文件统一为train.npy,test.npy,labels.npy,通过运行脚本查看处理后的文件信息 

 ```python
processecd_data/dataset/.npy
```
&emsp;&emsp;像这样运行脚本查看处理后的文件信息 。
<img width="1446" height="522" alt="image" src="https://github.com/user-attachments/assets/c69a379a-995d-4297-97b8-cb09fbed8c28" />

## SMD
**服务器机器数据集(Server Machine Dataset)**
[数据集链接](https://github.com/NetManAIOps/OmniAnomaly) 

&emsp;&emsp;SMD是从一家大型互联网公司获得的数据集，收集28个不同机器的数据，总的时间周期为五周。数据集被均等分为训练集和测试集，并且各包含28个实体，每个实体包含了38个维度，其中训练集数据有708,405个样本，测试集有708,420个样本（1416825），训练数据集中的异常由专家标记，最后选择28个实体的平均分数作为最终的异常得分。
28个机器五周的数据，时间间隔1min，（五周总共有50400分钟，意味着每台机器要检测50401次，总共28台机器，则总共检测50401×28 = 1411228次）每个机器有38个特征。训练集和测试集的数据比例为1:1，适用于无监督异常检测模型。用SMD数据集跑模型的时候，28个机器的数据需要分开训练。
#### 原文件
&emsp;&emsp;28个机器分成了三组。（第一组有8个，第二组有9个，第三组10个）文件命名：machine-x-y.txt。第x组的第y个机器的特征。
每一个machine-x-y代表一个具体的机器，
原文件一共四个文件夹。分别是train，test，test_label，interpretation_label。
machine-1-1.txt,红圈中即38个维度。
包含了CPU相关指标，内存相关指标，磁盘I/O指标，系统交换指标，TCP相关，UDP协议相关。
其中的八个维度信息如图。
 
<img width="820" height="410" alt="image" src="https://github.com/user-attachments/assets/6788b3b3-9751-430a-ac8b-bb337aa2fe56" />
<img width="865" height="267" alt="image" src="https://github.com/user-attachments/assets/16626ce4-d327-43b0-beed-2e7caa9c344e" />


* train：训练数据集，无标签。
* test：测试数据集，有标签。
* test_label：测试集的便签，0代表正常，1代表异常。
<img width="667" height="418" alt="image" src="https://github.com/user-attachments/assets/26ba550f-9a98-43a2-961b-fc8e4f85558a" />

 
* interpretation_label：对于测试集中的异常数据，哪几个数据特征造成了最终的异常,只要有一个特征异常，本次测量就为异常，已验证interpretation_label中的异常区间和label中的异常值为1匹配，如下图右边的interpretation_label 中的392-416中的12,15特征异常，对应左边label中的392-416行值为1。
 <img width="865" height="495" alt="image" src="https://github.com/user-attachments/assets/e9f97ead-b5fc-40a7-bedd-64fd5fbc42ed" />

#### 预处理后的文件
训练集一共708405条数据，测试集一共708420条数据。预处理的文件放在了processed_data/SMD文件夹下。
处理后的文件命名：machine-x-y_train.npy ，machine-x-y_test.npy

## SMAP & MSL
1. SMAP: 土壤湿度主动被动卫星(Soil Moisture Active Passive satellite)
2. MSL: 火星科学实验室流浪者(Mars Science Laboratory rover)
   
&emsp;&emsp;SMAP和MSL代表两个不同的产生遥测流的航天器，两个数据集分开
* SMAP有55个channel（实体），每个channel有25个维度
* MSL有27个channel（实体），每个channel有55个维度
  
SMAP训练集不含异常数据，训练集的异常数据都由专家打上了异常标签。已验证SMAP包含了562,800个样本，训练集135183，测试集427617。其中异常样本所占比率为 13.13%。 

MSL训练集不含异常数据，训练集的异常数据都由专家打上了异常标签。MSL 的样本总共有 132,046 个，训练集58317，测试集73729，异常样本占比为 10.72%。 

下表是异常序列以及异常比例的展示。 

 <img width="722" height="269" alt="image" src="https://github.com/user-attachments/assets/b325a766-9991-42d9-9dfc-9e966dc62529" />

#### 原文件
MSL数据集与SMAP数据集在一个文件夹data下。
labeled_anomalies.csv的列信息：
* &nbsp;&nbsp;chan_id：匿名通道 ID - 第一个字母代表通道的性质（P = 功率，R = 辐射等），对应于train和test中对应名字的numpy文件。
* &nbsp;&nbsp;Spacecraft：生成遥测流的航天器。MSL or SMAP。
* &nbsp;&nbsp;anomaly_sequences：流中真实异常的开始和结束索引，对应test中chan_id文件中的index为此范围的为异常序列。
* &nbsp;&nbsp;Class：异常分类。Point or contextual。
* &nbsp;&nbsp;num_values：每个流中遥测值的数量，对应chan_id的test文件的时间戳数量。

#### 预处理后的文件
&emsp;&emsp;预处理后的数据集放在了SMAP目录下。为了后续工作能更好的开展，也有将55个channel的数据分开的数据集。
训练和测试数据的列名：
## WADI
**水分配系统数据集(Water Distribution，WaDi)** 

&emsp;&emsp;WADI 数据集在iTrust官网申请数据集，申请通过后会向你的邮箱发送Google网盘链接。 
[数据集链接](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)

&emsp;&emsp;由Singapore University of Technology and Design收集。来自123个传感器和执行器的数据，一共127个特征。时间间隔1s。
一共运行16天，14天正常运行，2天遭到了15次攻击。异常情景是被攻击的时间收集的传感器数据。 

&emsp;&emsp;WADI有新和旧两个数据集，分别是WADI.A1_9 Oct 2017（旧）和WADI.A2_19 Nov 2019（新）。这是因为由于工厂在运行过程中的某些时段不稳定，需要删除受影响的读数，在2019 年 12 月 19 日删除了受影响的读数，上传了新的数据文件WADI_14days_new.csv（在WADI.A2_19 Nov 2019文件夹下）。 

* &nbsp;&nbsp;WADI.A2_19 Nov 2019训练集一共有784570条数据，测试集一共172800条数据。
* &nbsp;&nbsp;WADI.A1_9 Oct 2017训练集一共有1209600条数据，测试集一共172800条数据。

攻击场景：源自研究团队开发的攻击模型。攻击模型将CPS的意图空间(the intent space)视为攻击模型。两天内发起了15次攻击。
#### 原文件
WADI.A1_9 Oct 2017这个文件夹下有三个文件，分别是table_WADI、WADI_14days.csv和WADI_attackdata.csv。
* &nbsp;&nbsp;table_WADI：记录了被攻击的时间段。
* &nbsp;&nbsp;WADI_14days.csv：14天正常运行（训练集）。
* &nbsp;&nbsp;WADI_attackdata.csv：2天15次攻击（测试集）。
(784571, 130) (172803, 131) (1209601, 130) (172801, 130)
WADI.A2_19 Nov 2019这个文件夹下有三个文件，分别是table_WADI、WADI_14days_new.csv和WADI_attackdataLABLE.csv。
table_WADI：记录了被攻击的时间段。
WADI_14days_new.csv：14天正常运行（训练集），工厂在运行过程中的某些时段不稳定，删除了受影响的读数。
WADI_attackdataLABLE.csv：2天15次攻击（测试集）。

#### 预处理后的文件
训练集一共有784570条数据，测试集一共172800条数据。使用的是WADI.A2_19 Nov 2019（新）标准。
训练集 (784571, 128)  测试集  (172803, 129)
128= 127 特征数据 + 1时间数据 
129= 127特征数据 + 1 标签 + 1时间数据 


## MSDS
**用于人工智能分析的多源分布式系统数据(Multi-Source Distributed System data，MSDS)**
出处：
Sasho Nedelkoski, Jasmin Bogatinovski, Ajay Kumar Mandapati, Soeren Becker, Jorge Cardoso, and Odej Kao. 2020. Multi-source distributed system data for AI-powered analytics. In European Conference on Service-Oriented and Cloud Computing. Springer, 161-176.
近年来，人们对IT运营人工智能 (AIOps) 的兴趣日益浓厚。该领域利用来自 IT 系统、大数据平台和机器学习的监控数据来自动化分布式系统的各种运营和维护 (O&M) 任务。
MSDS多源/多模式数据集由运行复杂分布式系统 (Openstack) 产生的分布式跟踪、应用程序日志和指标组成。
这个数据集是专门为人工智能操作建立的，包括自动异常检测、根本原因分析和补救。
#### 原文件
5个不同的日志系统组成，取日志中的两个指标，将它们组合到一起变成多源数据集，特征为10。
3.预处理后的文件
处理后的训练集为29286，测试集也为29286。10个特征。

## NAB
&emsp;&emsp;NAB数据集是Numenta公司开源的用于评估流式时序异常检测算法的公开数据集。它由超过50个带label的真实世界和人工时间序列数据文件组成，包含了很多数据集，主要包含交通，广告点击率，机器等数据可以只取其中的部分用于研究，比如,TranAD模型中使用的是其中的realADExchage（在线点击率）数据。

&emsp;&emsp;[数据集链接](https://github.com/numenta/NAB/tree/master/data)

&emsp;&emsp;详情请看：[官方文档](https://github.com/numenta/NAB/blob/master/data/README.md)

<img width="865" height="228" alt="image" src="https://github.com/user-attachments/assets/2b1914d4-0c82-466a-adef-c8a10a994f42" />

 
&emsp;&emsp;打开一个数据的格式。所有的数据已经标准化，都是两列，一列是timestamp，另外一列是value值。
 
<img width="865" height="498" alt="image" src="https://github.com/user-attachments/assets/e45c4585-d0c1-429b-a2d9-b983515bc41b" />

&emsp;&emsp;label数据在：https://github.com/numenta/NAB/tree/master/labels/raw，格式如下，保存格式是json
<img width="865" height="299" alt="image" src="https://github.com/user-attachments/assets/543df85f-cbef-4c14-955a-fd730f762b37" />
 
&emsp;&emsp;label中key是文件名，value是一个list，里面包含异常的点的timestamp。
<img width="865" height="708" alt="image" src="https://github.com/user-attachments/assets/b6040bbb-81ec-4d20-b4d1-dc44564b7ae8" />

 

