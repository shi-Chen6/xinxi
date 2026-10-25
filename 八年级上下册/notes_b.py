# -*- coding: utf-8 -*-
# 八年级备考知识笔记 —— 第三单元、第四单元（第11课~第20课）
# 数据来源：教材《义务教育信息科技课程教学指南·物联网实践与探索（八年级全一册）》及各课配套课件

NOTES_B = [
    {
        "module": "第三单元：简单物联功能实践",
        "desc": "物联系统包括感知层、网络层和应用层，本单元聚焦应用层的功能实现，遵循物联网“大场景、小应用”的特点，以实践探究的方式解决真实问题。本单元围绕“物联门锁”这一典型应用展开，先认识身边的物联系统与三层结构，再依次实现刷卡开锁、门铃远程通知、远程控制开锁和刷脸开锁四个核心功能。学习中要重点体会物联系统中的“反馈”与“控制”，掌握在物联网服务平台上读取、发送、接收和使用数据的方法。通过实践，进一步理解物联网、大数据与人工智能之间的关系，感受万物互联为生活带来的便捷与影响。",
        "lessons": [
            {
                "id": "L11",
                "title": "第11课 物联系统细分解",
                "knowledge": '''
<h3>一、什么是物联系统</h3>
<p>生活中的物联系统大多由<strong>终端设备、传感器、网络和软件</strong>组成，它们相互连接和交互，共同实现<strong>数据采集、传输、处理和控制</strong>等功能。</p>
<ul>
  <li>常见的物联系统：物联公交站牌、共享单车、物联家居、物联停车、物联门锁等。</li>
  <li>物联网是<strong>互联网的延伸</strong>，把“人与人相连”扩展为“万物相连”。</li>
</ul>

<h3>二、典型案例：物联公交站牌系统</h3>
<p>公交车上搭载<strong>北斗车载定位终端、加速度传感器</strong>等多个传感器和通信设备，实时感知公交车的<strong>位置、运行状态（速度）</strong>等数据并传输给服务器，服务器对数据进行分析处理，实现<strong>车辆定位、路线规划、到站提醒</strong>等应用功能。</p>
<p><strong>“到站提醒”功能的工作过程（必背）：</strong></p>
<ol>
  <li>北斗车载定位终端、加速度传感器等采集公交车的位置、运行速度等数据；</li>
  <li>通信设备通过网络把数据传送给服务器；</li>
  <li>服务器分析处理后，把结果发送给公交站牌进行可视化呈现。</li>
</ol>

<h3>三、物联系统的三层结构</h3>
<p>人们通常把物联系统划分为三层：<strong>感知层、网络层、应用层</strong>。可以形象地把它们比作人体的器官。</p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>层次</th><th>人体类比</th><th>主要功能</th><th>典型设备／技术</th></tr>
  <tr>
    <td><strong>感知层</strong>（基础层）</td><td>感觉器官（眼、耳）</td>
    <td>从物理环境中<strong>采集数据</strong>，并对数据进行<strong>简单处理</strong>，以便后续传输。是物联系统的基础，起<strong>决定性作用</strong></td>
    <td>温湿度传感器、光敏传感器、摄像头、RFID读卡器、按键传感器、北斗定位终端</td>
  </tr>
  <tr>
    <td><strong>网络层</strong></td><td>神经中枢系统</td>
    <td>实现互联互通，把感知层采集到的数据<strong>安全、可靠地传输</strong>到应用层</td>
    <td>Wi-Fi、蓝牙、3G/4G/5G、NB-IoT（窄带物联网）、有线网络、MQTT协议</td>
  </tr>
  <tr>
    <td><strong>应用层</strong>（最顶层）</td><td>大脑</td>
    <td>通过云计算平台进行信息处理，对数据进行<strong>计算、处理、分析挖掘</strong>，并据此实现对现实世界的<strong>实时控制、精确管理</strong></td>
    <td>物联网服务平台、数据分析软件、手机应用软件、可视化大屏</td>
  </tr>
</table>
<p><strong>数据流主线：</strong>采集数据 → 传输数据 → 处理和呈现数据，正好一一对应<strong>感知层 → 网络层 → 应用层</strong>。</p>
<p><em>说明：物联网仍在不断发展，也有观点把物联系统划分为感知层、网络层、平台层和应用层，还有观点把执行器归入应用层。这些都是帮助理解万物互联原理的“支架”，不必纠结细节。</em></p>

<h3>四、分解物联门锁系统的核心功能</h3>
<p>物联门锁是物联系统的典型应用，可分解为<strong>四个相对完整的核心功能</strong>：刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁。每个功能的实现都离不开软硬件的支持。</p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>功能</th><th>感知层</th><th>网络层</th><th>应用层</th></tr>
  <tr><td>刷卡开锁</td><td>采集门禁卡数据</td><td>需要网络传输数据</td><td>门禁卡校验通过后，控制开锁</td></tr>
  <tr><td>门铃远程通知</td><td>采集门铃按下的状态数据</td><td>需要网络传输数据</td><td>向用户通知反馈</td></tr>
  <tr><td>远程控制开锁</td><td>获取开锁指令</td><td>需要网络传输数据</td><td>发送开锁指令，控制开锁</td></tr>
  <tr><td>刷脸开锁</td><td>采集、识别、匹配人脸数据</td><td>需要网络传输数据</td><td>人脸匹配后，控制开锁</td></tr>
</table>

<h3>五、从结构角度归纳物联门锁</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>物联系统结构</th><th>功能描述</th></tr>
  <tr><td>应用层</td><td>刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁等功能</td></tr>
  <tr><td>网络层</td><td>连接网络，传输数据，实现设备间的数据交互</td></tr>
  <tr><td>感知层</td><td>摄像头、门铃（按键）、读卡器等，采集并处理人脸数据、门铃状态数据等</td></tr>
</table>
<p><strong>物联家居举例：</strong>感知层采集家居环境的温度、湿度、光照强度等数据 → 网络层传输 → 应用层处理后通过执行器作用于现实世界（如控制空调、除湿器、灯光）。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">物联系统的组成</strong>：终端设备、传感器、网络和软件。</li>
  <li><strong style="color:#c0392b;">三层结构名称必须写全写准</strong>：<strong style="color:#c0392b;">感知层、网络层、应用层</strong>（顺序由下到上，不要写成“采集层”“传输层”）。</li>
  <li><strong style="color:#c0392b;">感知层是物联系统的基础</strong>，在物联系统中起<strong style="color:#c0392b;">决定性作用</strong>；负责<strong style="color:#c0392b;">从物理环境中采集数据</strong>并作简单处理。</li>
  <li><strong style="color:#c0392b;">网络层负责“安全、可靠地传输”数据</strong>，如同<strong style="color:#c0392b;">神经中枢系统</strong>；常见技术有 <strong style="color:#c0392b;">Wi-Fi、3G/4G/5G、NB-IoT</strong>。</li>
  <li><strong style="color:#c0392b;">应用层位于最顶层</strong>，如同<strong style="color:#c0392b;">大脑</strong>，通过<strong style="color:#c0392b;">云计算平台</strong>进行信息处理，实现<strong style="color:#c0392b;">实时控制、精确管理</strong>。</li>
  <li><strong style="color:#c0392b;">数据流主线</strong>：<strong style="color:#c0392b;">采集数据—传输数据—处理和呈现数据</strong>，与三层一一对应，这是描述任何物联系统工作过程的“万能模板”。</li>
  <li>物联公交站牌用到的传感器：<strong style="color:#c0392b;">北斗车载定位终端、加速度传感器</strong>；采集的数据是<strong style="color:#c0392b;">位置、运行速度（运行状态）</strong>。</li>
  <li>物联门锁可分解为<strong style="color:#c0392b;">刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁</strong>四个核心功能，常考“填三层表格”。</li>
  <li><strong style="color:#c0392b;">物联网是互联网的延伸</strong>，这是选择题常见表述。</li>
</ul>
<h3>答题模板</h3>
<p>凡是问“某物联系统某功能的工作过程”，一律按三段式作答：<br>
①（感知层）用<strong style="color:#c0392b;">××传感器</strong>采集<strong style="color:#c0392b;">××数据</strong>；<br>
②（网络层）通过<strong style="color:#c0392b;">网络</strong>把数据传输给<strong style="color:#c0392b;">服务器／物联网服务平台</strong>；<br>
③（应用层）服务器<strong style="color:#c0392b;">分析处理</strong>后，把结果反馈给<strong style="color:#c0392b;">执行器／终端</strong>，实现××功能。</p>
''',
                "difficulty": '''
<h3>易混辨析一：感知层 vs 网络层 vs 应用层</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>感知层</th><th>网络层</th><th>应用层</th></tr>
  <tr><td>核心动词</td><td>“采”（采集）</td><td>“传”（传输）</td><td>“算”（处理、分析、控制）</td></tr>
  <tr><td>位置</td><td>最底层（基础）</td><td>中间层（桥梁）</td><td>最顶层</td></tr>
  <tr><td>是否处理数据</td><td>只做<strong>简单处理</strong>（如格式转换），便于传输</td><td>一般不处理，只负责搬运</td><td>做<strong>复杂的计算、分析和挖掘</strong></td></tr>
  <tr><td>常见误判</td><td>误把摄像头“识别人脸”整体算作感知层——采集属感知层，复杂识别属应用层</td><td>误认为网络层会“判断身份”</td><td>误认为应用层就是“手机App界面”，其实核心是数据处理</td></tr>
</table>

<h3>易混辨析二：物联网 vs 互联网</h3>
<ul>
  <li>互联网连接的主要是<strong>人与人、人与信息</strong>；物联网连接的是<strong>物与物、人与物</strong>。</li>
  <li>物联网<strong>建立在互联网之上</strong>，是互联网的延伸和扩展，网络层大量复用互联网技术（如 TCP/IP）。</li>
</ul>

<h3>难点解析：为什么说“感知层起决定性作用”？</h3>
<p>因为数据是物联系统的“原料”。感知层采不到数据、或采到的数据不准确，后面的传输、分析、控制都失去意义（“垃圾进，垃圾出”）。所以感知层是<strong>基础</strong>，起决定性作用。注意：这不等于说感知层“最重要、最复杂”，最复杂的处理仍在应用层。</p>

<h3>难点解析：执行器归哪一层？</h3>
<p>教材说明：不同观点有分歧，有的把执行器归入<strong>应用层</strong>（因为它执行应用层下达的控制指令），有的单列。<strong>考试时按题干给的框架填写</strong>，若无特别说明，把“执行开锁”“显示通知”这类动作写进<strong>应用层</strong>。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>人体三比喻口诀</strong>：<strong>感知是耳目，网络是神经，应用是大脑</strong>。</li>
  <li><strong>三字诀</strong>：<strong>采 → 传 → 算</strong>（采集、传输、计算）。</li>
  <li><strong>门锁四功能口诀</strong>：<strong>卡、铃、控、脸</strong>（刷卡开锁、门铃通知、远程控制、刷脸开锁）。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>请说出物联系统的三层结构，并简述每一层的主要功能。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>感知层</strong>：物联系统的基础，起决定性作用，如同人的感觉器官，负责从物理环境中采集数据并作简单处理，便于后续传输。</li>
  <li><strong>网络层</strong>：如同人的神经中枢系统，负责实现互联互通，把感知层采集的数据安全、可靠地传输到应用层。</li>
  <li><strong>应用层</strong>：位于最顶层，如同人的大脑，通过云计算平台对数据进行计算、处理和分析挖掘，并根据结果实现对现实世界的实时控制和精确管理。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>请描述物联公交站牌系统“到站提醒”功能的工作过程。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>公交车上的北斗车载定位终端、加速度传感器等采集公交车的位置、运行速度等数据（感知层）；</li>
  <li>通信设备通过网络把这些数据传输给服务器（网络层）；</li>
  <li>服务器对数据进行分析处理，计算出到站时间等结果（应用层）；</li>
  <li>把处理结果发送给公交站牌进行可视化呈现，实现到站提醒。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>请从三层结构的角度，分析物联门锁“刷脸开锁”功能的实现。</p>
<p><strong>答案要点：</strong></p>
<ul>
  <li><strong>感知层</strong>：用摄像头采集人脸图像数据，进行人脸识别与匹配。</li>
  <li><strong>网络层</strong>：通过网络（如 Wi-Fi、MQTT 服务器）把识别结果数据传输出去。</li>
  <li><strong>应用层</strong>：判断人脸是否与人脸库匹配，匹配成功后发出指令控制门锁（舵机）打开。</li>
</ul>
'''
            },
            {
                "id": "L12",
                "title": "第12课 刷卡开锁易实现",
                "knowledge": '''
<h3>一、为什么要用刷卡开锁</h3>
<p>传统机械锁只能用钥匙开锁，钥匙<strong>容易被复制</strong>，<strong>丢失后可能要更换锁体</strong>。把门锁与 <strong>RFID（射频识别）</strong> 技术结合后，感应卡就有了钥匙的功能，而且还能对“钥匙”进行统一管理（挂失、注销、绑定身份）。</p>

<h3>二、RFID 门锁系统的组成与工作过程</h3>
<p><strong>组成：</strong>内置<strong>电子标签</strong>的门禁卡、<strong>读卡器</strong>、<strong>控制模块</strong>、<strong>锁体</strong>。</p>
<p><strong>工作过程（必背）：</strong></p>
<ol>
  <li>门禁卡靠近读卡器；</li>
  <li>存储在电子标签中的数据被读卡器<strong>自动读出</strong>；</li>
  <li>数据被发送至<strong>控制模块</strong>；</li>
  <li>控制模块<strong>判断数据正确</strong>（编号在合法名单中）后；</li>
  <li>控制<strong>打开门锁</strong>。</li>
</ol>
<p>可以概括为三个阶段：<strong>外部数据的获取（输入）→ 数据的内部处理（计算）→ 结果的呈现（输出）</strong>。</p>
<p>课件中的流程表述：采集身份数据 → 获取身份数据 → 判断身份 → 发送开锁指令 → 接收指令开锁。</p>

<h3>三、刷卡开锁功能分析（三模块）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>模块</th><th>硬件</th><th>实现思路</th></tr>
  <tr><td><strong>输入模块</strong></td><td>电子标签、RFID读卡器</td><td>读取电子标签的编号</td></tr>
  <tr><td><strong>计算模块</strong></td><td>主控板</td><td>用<strong>列表</strong>存储电子标签编号，判断编号是否在列表中</td></tr>
  <tr><td><strong>输出模块</strong></td><td>舵机（模拟门锁）</td><td>模拟打开门锁</td></tr>
</table>

<h3>四、认识舵机</h3>
<ul>
  <li>舵机是一种<strong>位置（角度）调节的驱动器</strong>，属于<strong>执行器（输出设备）</strong>。</li>
  <li>常见舵机可调节角度为 <strong>0°～180°</strong>。</li>
  <li>在本课中用舵机的转动来<strong>模拟门锁的开／关动作</strong>。</li>
</ul>
<p><strong>控制舵机转动的主要代码：</strong></p>
<pre>import time
from educore import servo
sv = servo(1)          # 将舵机连接到1号接口
sv.angle(180)          # 控制舵机转到180°位置（模拟开锁）
time.sleep(2)          # 等待2 s
sv.angle(0)            # 控制舵机转回起始位置（模拟关锁）</pre>

<h3>五、设计算法并实现刷卡开锁</h3>
<p><strong>算法思想：</strong>把合法的电子标签编码作为用户身份数据<strong>存储在列表中</strong>；当读取到的门禁卡编码<strong>在列表中</strong>时，执行开锁动作。</p>
<p><strong>模拟刷卡开锁的主要代码：</strong></p>
<pre>sn_list = ["53152396", "53152018"]        # 用列表存储合法电子标签编号
while True:
    rf = scan_rfid.scanning()             # 尝试识别电子标签
    sn = rf.serial_number()               # 获取电子标签编号
    if sn in sn_list:                     # 判断编号是否在列表中
        servo(1).angle(180)               # 控制舵机转动，模拟开锁
        time.sleep(1.5)
        servo(1).angle(0)</pre>

<h3>六、实践操作步骤</h3>
<ol>
  <li>正确连接计算机、主控板、RFID读卡器和舵机；</li>
  <li>修改程序列表中的电子标签编号（换成自己卡片的编号）；</li>
  <li>把程序<strong>烧录</strong>到主控板中；</li>
  <li>刷卡<strong>验证</strong>开锁功能。</li>
</ol>
<p><strong>功能实现的一般流程（本单元通用）：</strong>功能分析 → 硬件搭建 → 编程实现 → 测试验证。</p>

<h3>七、编码的唯一性与拓展</h3>
<p>每张门禁卡内电子标签的编号是<strong>唯一</strong>的，因此可以用它来<strong>标识用户身份</strong>。小区常把门禁卡编号与业主身份数据<strong>关联</strong>，实现人员精准管理。<br>
拓展做法：用<strong>字典</strong>存储“电子标签编号—用户姓名”，二者<strong>一一对应</strong>，开锁的同时在显示屏上显示用户姓名。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">RFID门锁系统的组成</strong>：内置<strong style="color:#c0392b;">电子标签的门禁卡、读卡器、控制模块、锁体</strong>（四样，容易漏写“锁体”）。</li>
  <li><strong style="color:#c0392b;">工作过程五步</strong>：靠近读卡器 → 自动读出标签数据 → 发送到控制模块 → 判断数据正确 → 控制开锁。</li>
  <li><strong style="color:#c0392b;">三模块划分</strong>：输入模块（<strong style="color:#c0392b;">电子标签、RFID读卡器</strong>）、计算模块（<strong style="color:#c0392b;">主控板</strong>）、输出模块（<strong style="color:#c0392b;">舵机</strong>）——常考“填表”。</li>
  <li>舵机是<strong style="color:#c0392b;">位置（角度）调节的驱动器</strong>，常见调节角度 <strong style="color:#c0392b;">0°～180°</strong>，属于<strong style="color:#c0392b;">执行器／输出设备</strong>。</li>
  <li>控制舵机的关键语句：<strong style="color:#c0392b;">servo(1).angle(180)</strong>；<strong style="color:#c0392b;">time.sleep()</strong> 用于保持一段时间。</li>
  <li>判断身份的关键语句：<strong style="color:#c0392b;">if sn in sn_list:</strong>——考“in 运算符判断元素是否在列表中”。</li>
  <li><strong style="color:#c0392b;">电子标签编码具有唯一性</strong>，可用来标识用户身份，这是刷卡开锁能识别“谁”的根本原因。</li>
  <li>存储“编号—姓名”的对应关系要用<strong style="color:#c0392b;">字典</strong>（键值对一一对应），只存合法编号用<strong style="color:#c0392b;">列表</strong>。</li>
  <li>功能实现流程：<strong style="color:#c0392b;">功能分析—硬件搭建—编程实现—测试验证</strong>。</li>
  <li>刷卡开锁属于<strong style="color:#c0392b;">本地校验</strong>，主要体现“输入—计算—输出”的<strong style="color:#c0392b;">过程与控制</strong>思想。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：列表 vs 字典</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>列表 list</th><th>字典 dict</th></tr>
  <tr><td>写法</td><td>["53152396", "53152018"]</td><td>{"53152396": "小华", "53152018": "小智"}</td></tr>
  <tr><td>存的内容</td><td>一组<strong>并列</strong>的数据</td><td>一组<strong>键值对</strong>，键与值<strong>一一对应</strong></td></tr>
  <tr><td>本课用途</td><td>存合法门禁卡编号，只判断“在不在”</td><td>存“编号—姓名”，开锁时还能显示姓名</td></tr>
  <tr><td>判断方式</td><td>if sn in sn_list</td><td>if sn in sn_dict，再用 sn_dict[sn] 取姓名</td></tr>
</table>

<h3>易混辨析二：RFID门锁 vs 普通机械锁</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>普通机械锁</th><th>RFID门锁</th></tr>
  <tr><td>开锁凭证</td><td>金属钥匙（物理形状）</td><td>门禁卡中的<strong>电子标签编号</strong>（数据）</td></tr>
  <tr><td>识别方式</td><td>机械结构配合</td><td><strong>非接触式</strong>射频识别，自动读取</td></tr>
  <tr><td>能否管理</td><td>不能，丢失需换锁</td><td>能，可<strong>挂失、注销、增删</strong>合法名单</td></tr>
  <tr><td>能否记录</td><td>不能</td><td>可记录开锁时间、人员，实现精准管理</td></tr>
</table>

<h3>易混辨析三：“输入／计算／输出”三模块 vs “感知／网络／应用”三层</h3>
<ul>
  <li><strong>三层结构</strong>是从<strong>整个物联系统的体系架构</strong>角度划分的（第11课）。</li>
  <li><strong>三模块</strong>是从<strong>一个具体功能的实现流程</strong>角度划分的（第12～15课）。</li>
  <li>大致对应关系：输入模块≈感知层，计算模块≈应用层（判断决策），输出模块≈执行反馈。<strong>但不是严格等同</strong>，答题时看题目问的是“层”还是“模块”。</li>
</ul>

<h3>难点解析：刷卡开锁为什么对网络要求最低？</h3>
<p>因为编号的合法性判断是在<strong>主控板本地</strong>完成的（列表就存在主控板程序里），不需要把数据发到远程服务器再等回复。所以本课没有用到 MQTT。而第13～15课的功能都需要<strong>跨设备通信</strong>，才必须借助 MQTT 服务器中转。</p>

<h3>记忆技巧</h3>
<ul>
  <li>RFID门锁组成口诀：<strong>卡（含标签）、读（读卡器）、控（控制模块）、锁（锁体）</strong>。</li>
  <li>工作过程口诀：<strong>靠近—读出—发送—判断—开锁</strong>。</li>
  <li>三模块口诀：<strong>读卡器管“读”，主控板管“判”，舵机管“开”</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>请描述 RFID 门锁系统的工作过程。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>RFID门锁系统由内置电子标签的门禁卡、读卡器、控制模块和锁体等组成；</li>
  <li>门禁卡靠近读卡器时，存储在电子标签中的数据被读卡器自动读出；</li>
  <li>读卡器把读到的编号数据发送给控制模块；</li>
  <li>控制模块把该编号与预先存储的合法编号进行比对，判断数据是否正确；</li>
  <li>判断正确（有开锁权限）后，发送开锁指令，控制打开门锁；不正确则不开锁。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>在模拟刷卡开锁的程序中，为什么要用列表存储电子标签编号？程序是如何判断一张卡是否合法的？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>一个门禁系统通常有<strong>多个</strong>合法用户，用列表可以方便地把多张卡的编号<strong>集中存储和管理</strong>，增删用户只需修改列表；</li>
  <li>由于<strong>电子标签编码具有唯一性</strong>，编号可以直接代表某位用户的身份；</li>
  <li>程序先用 rf.serial_number() 读取当前卡的编号 sn，再用 <strong>if sn in sn_list</strong> 判断该编号是否在合法列表中；</li>
  <li>如果在列表中，就控制舵机转动模拟开锁；如果不在，则不执行开锁动作。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>小区要实现“刷卡时在显示屏上显示业主姓名”，程序应如何改进？为什么？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>把原来的<strong>列表</strong>改为<strong>字典</strong>，用“电子标签编号”作为键，“业主姓名”作为值，二者一一对应；</li>
  <li>刷卡读到编号后，先判断该编号是否是字典中的键；</li>
  <li>若是，则通过键取出对应的姓名，用显示屏（如 oled.print）显示，同时控制舵机开锁；</li>
  <li>这样做利用了<strong>标签编号的唯一性</strong>，把卡与业主身份数据关联起来，可实现对进入小区人员的精准管理。</li>
</ol>
'''
            },
            {
                "id": "L13",
                "title": "第13课 门铃通知即时到",
                "knowledge": '''
<h3>一、认识物联系统中的反馈</h3>
<p><strong>反馈的定义（必背）：</strong>在物联系统中，<strong>反馈就是针对现实世界采取行动的过程</strong>。可用于反馈的设备被称为<strong>输出设备（执行器）</strong>。</p>
<ul>
  <li>通过反馈，人们可以了解物联系统中的数据是<strong>如何被利用</strong>的。</li>
  <li>从某种意义上看，<strong>物品的反馈能力决定了它的价值</strong>。</li>
  <li>常见输出设备：显示屏（OLED）、蜂鸣器、RGB灯、舵机、电机、智能终端等。</li>
</ul>

<h3>二、反馈的两种主要方式</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>方式</th><th>含义</th><th>举例</th></tr>
  <tr><td><strong>可视化反馈</strong></td><td>用户通过智能终端的屏幕查看物联网服务提供的各种信息，进而作出决策</td><td>规划行程、实时导航指引、推荐附近停车场、数据监测大屏</td></tr>
  <tr><td><strong>通知反馈</strong></td><td>系统实时检测物品状态，并通知相应设备，设备按预先设定的规则提醒用户</td><td>有人按门铃时，把“有人按门铃”的信息传到智能终端，以声音、文字消息等形式提醒</td></tr>
</table>
<p><em>具体采用哪种反馈方式，取决于物品被用来做什么。</em></p>
<p><strong>门铃系统中的两种反馈：</strong>①有人按门铃时屋内响铃，是一种反馈；②物联门铃把“门铃被按下”的数据实时传输到用户智能终端并提醒，也是一种反馈（远程通知反馈）。</p>

<h3>三、“门铃按、通知到”的工作过程</h3>
<ul>
  <li><strong>触发条件：</strong>门铃（按键传感器）被按下。</li>
  <li><strong>通信方式：</strong>远程通知使用 <strong>MQTT</strong>（发布／订阅）。</li>
  <li><strong>输出设备：</strong>用户终端（主控板显示屏），显示通知内容。</li>
</ul>
<p><strong>工作过程（必背）：</strong></p>
<ol>
  <li><strong>家中门铃端：</strong>门铃被按下 → 获取按键状态数据 → 通过网络<strong>发布</strong>至 MQTT 服务器的主题；</li>
  <li><strong>用户终端：</strong>从该主题<strong>订阅／接收</strong>数据 → 终端显示“有人按门铃”通知。</li>
</ol>

<h3>四、门铃远程通知功能分析（三模块）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>模块</th><th>硬件</th><th>实现思路</th><th>角色</th></tr>
  <tr><td><strong>输入模块</strong></td><td>主控板、按键传感器</td><td>采集门铃状态数据，并<strong>发布</strong>消息至 MQTT 服务器相应主题</td><td>门铃端（<strong>发布者</strong>）</td></tr>
  <tr><td><strong>计算模块</strong></td><td>具备移动热点功能的计算机</td><td>搭建 MQTT 服务器，设置主题，实现发布与订阅功能</td><td>MQTT服务器（<strong>桥梁／中转</strong>）</td></tr>
  <tr><td><strong>输出模块</strong></td><td>主控板</td><td><strong>订阅</strong> MQTT 服务器相应主题，收到消息后以通知方式提醒用户</td><td>用户端（<strong>订阅者</strong>）</td></tr>
</table>
<p>实现远程通知必须解决<strong>两个关键问题</strong>：①主控板需要<strong>连接网络</strong>；②控制端与被控制端的通信需要<strong>服务器中转</strong>，这里使用 MQTT 服务器，提供设备管理、数据存储及数据处理等功能。</p>

<h3>五、模拟实现步骤</h3>
<p>器材：2个主控板、1个按键传感器、1台具备移动热点功能的计算机（用 SIoT 搭建本地 MQTT 服务器）。</p>
<ol>
  <li><strong>搭建环境：</strong>连接无线网络；搭建本地 MQTT 服务器，获取<strong>服务器地址、端口号、用户名和密码</strong>。</li>
  <li><strong>门铃端（主控板A）：</strong>连接服务器 Wi-Fi → 建立与 MQTT 服务器的连接 → 按键被按下时向主题 <strong>“Door/Bell”</strong> 发送消息 <strong>“有人按门铃”</strong>。</li>
  <li><strong>用户端（主控板B）：</strong>连接 Wi-Fi 与 MQTT 服务器 → <strong>订阅</strong>主题“Door/Bell” → 收到消息时屏幕显示该消息。</li>
  <li><strong>功能测试：</strong>分别烧录程序，按下主控板A的按键传感器，查看主控板B屏幕是否显示“有人按门铃”。</li>
</ol>

<h3>六、主要代码</h3>
<p><strong>门铃端（发布）：</strong></p>
<pre>bt = button(0)                     # 将按键传感器连接到 pin0 接口
while True:
    if bt.status() == 1:           # 如果按键被按下
        mqttclient.publish(topic="Door/Bell", content="有人按门铃")
        time.sleep(5)              # 等待5 s，防止重复发送</pre>
<p><strong>用户端（订阅）：</strong></p>
<pre>def receivedfunction():
    msg = mqttclient.message(topic="Door/Bell")   # 读取主题消息
    if msg == "有人按门铃":                        # 判断收到的消息内容
        oled.print(msg)
        time.sleep(5)
        oled.clear()
# 绑定消息接收事件：主题收到消息时执行 receivedfunction
mqttclient.received(topic="Door/Bell", callback=receivedfunction)</pre>
<p><em>注意：两个设备订阅／发布的<strong>主题名称相同</strong>，但各自的<strong>连接参数（用户名、密码等）不同</strong>。</em></p>

<h3>七、拓展：其他通知方式</h3>
<p>除显示屏外，还可以用<strong>蜂鸣器</strong>发声提醒、用 <strong>RGB灯</strong> 闪烁提醒等，只需更换相应的执行器并修改程序。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">反馈的定义</strong>：在物联系统中，反馈就是<strong style="color:#c0392b;">针对现实世界采取行动的过程</strong>；可用于反馈的设备称为<strong style="color:#c0392b;">输出设备</strong>。</li>
  <li><strong style="color:#c0392b;">反馈的两种方式</strong>：<strong style="color:#c0392b;">可视化反馈</strong>和<strong style="color:#c0392b;">通知反馈</strong>。</li>
  <li><strong style="color:#c0392b;">物品的反馈能力决定了其价值</strong>（常作判断题）。</li>
  <li>门铃远程通知的<strong style="color:#c0392b;">触发条件是“门铃（按键）被按下”</strong>。</li>
  <li>远程通知使用 <strong style="color:#c0392b;">MQTT 协议</strong>，采用<strong style="color:#c0392b;">发布／订阅</strong>模式；门铃端是<strong style="color:#c0392b;">发布者</strong>，用户端是<strong style="color:#c0392b;">订阅者</strong>，MQTT服务器是<strong style="color:#c0392b;">桥梁（中转）</strong>。</li>
  <li>本课主题名：<strong style="color:#c0392b;">Door/Bell</strong>；消息内容：<strong style="color:#c0392b;">“有人按门铃”</strong>。</li>
  <li>三模块硬件：输入模块=<strong style="color:#c0392b;">主控板+按键传感器</strong>；计算模块=<strong style="color:#c0392b;">具备移动热点功能的计算机</strong>；输出模块=<strong style="color:#c0392b;">主控板（显示屏）</strong>。</li>
  <li>搭建 MQTT 服务器后必须获取四项参数：<strong style="color:#c0392b;">服务器地址、端口号、用户名、密码</strong>。</li>
  <li><strong style="color:#c0392b;">time.sleep(5) 的作用是防止重复发送</strong>（按键按住不放会连续触发）——高频问答点。</li>
  <li>关键函数：发布用 <strong style="color:#c0392b;">mqttclient.publish(topic=, content=)</strong>；订阅绑定用 <strong style="color:#c0392b;">mqttclient.received(topic=, callback=)</strong>；取消息用 <strong style="color:#c0392b;">mqttclient.message(topic=)</strong>。</li>
  <li>可替换的通知执行器：<strong style="color:#c0392b;">蜂鸣器、RGB灯、显示屏</strong>。</li>
  <li>信息安全渗透点：<strong style="color:#c0392b;">不要设置过于简单的 Wi-Fi／服务器密码</strong>。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：反馈 vs 控制</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>反馈（第13课）</th><th>控制（第14课）</th></tr>
  <tr><td>定义</td><td>针对现实世界<strong>采取行动</strong>的过程</td><td>基于反馈的数据<strong>调整设备或系统的工作状态</strong></td></tr>
  <tr><td>关注点</td><td>“把结果告诉／作用于现实世界”</td><td>“根据结果去改变设备状态”</td></tr>
  <tr><td>本课例子</td><td>显示屏显示“有人按门铃”</td><td>发送 open 指令让舵机转动开锁</td></tr>
  <tr><td>关系</td><td colspan="2">二者<strong>密不可分</strong>：反馈是控制的<strong>依据和触发条件</strong>，控制是反馈的进一步动作</td></tr>
</table>

<h3>易混辨析二：发布（publish） vs 订阅（subscribe／received）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>发布</th><th>订阅</th></tr>
  <tr><td>谁在做</td><td>数据的<strong>产生方</strong>（门铃端）</td><td>数据的<strong>使用方</strong>（用户端）</td></tr>
  <tr><td>动作</td><td>把消息<strong>发送到</strong>某个主题</td><td>从某个主题<strong>接收</strong>消息</td></tr>
  <tr><td>关键代码</td><td>mqttclient.publish(...)</td><td>mqttclient.received(...) + message(...)</td></tr>
  <tr><td>共同点</td><td colspan="2">必须使用<strong>相同的主题名</strong>（Door/Bell），否则收不到；但连接参数各自独立</td></tr>
</table>

<h3>易混辨析三：本地 MQTT 服务器 vs 在线 MQTT 服务器</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>本地 MQTT 服务器（如 SIoT）</th><th>在线 MQTT 服务器</th></tr>
  <tr><td>访问范围</td><td>一般只能在<strong>同一局域网</strong>内访问</td><td>可通过<strong>公网远程访问</strong>，覆盖范围广</td></tr>
  <tr><td>便捷性</td><td>需自己搭建，课堂内使用方便、不依赖外网</td><td>注册即用，但需要联网和账号</td></tr>
  <tr><td>数据安全性</td><td>数据留在本地，<strong>可控性强</strong></td><td>数据存放在第三方平台，需关注隐私</td></tr>
</table>

<h3>难点解析：为什么两个主控板不能“直接对话”？</h3>
<p>两个主控板通常处在不同位置、不同网络中，彼此不知道对方地址。MQTT 服务器充当<strong>中转桥梁</strong>：发布者只管把消息投递到<strong>主题</strong>这个“信箱”，订阅者只管从同名“信箱”取信。这样发布者和订阅者<strong>互相解耦</strong>，一个发布者的消息还可以被多个订阅者同时接收。</p>

<h3>难点解析：time.sleep(5) 放在哪、为什么</h3>
<p>放在发布语句<strong>之后</strong>。按键按下的瞬间，循环会飞快地执行很多次，若不延时会向服务器<strong>疯狂重复发送</strong>相同消息，既造成数据冗余，又增加服务器压力。延时5秒相当于“一次通知后先冷静一会儿”。</p>

<h3>记忆技巧</h3>
<ul>
  <li>反馈两方式口诀：<strong>“看得见”是可视化，“提醒你”是通知</strong>。</li>
  <li>MQTT 三角色口诀：<strong>发布者投信、服务器管信箱、订阅者取信</strong>。</li>
  <li>主题名记忆：<strong>Bell 是铃（第13课通知）、Lock 是锁（第14课控制）</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>什么是物联系统中的反馈？反馈主要有哪几种方式？请各举一例。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>定义</strong>：在物联系统中，反馈就是针对现实世界采取行动的过程；可用于反馈的设备被称为输出设备（执行器）。</li>
  <li><strong>可视化反馈</strong>：用户通过智能终端屏幕查看物联网服务提供的信息并作出决策。例如导航软件显示实时路况、智慧社区数据监测大屏。</li>
  <li><strong>通知反馈</strong>：系统实时检测物品状态并通知相应设备，设备按预设规则提醒用户。例如有人按门铃时，把“有人按门铃”消息推送到智能终端，以声音或文字提醒。</li>
  <li>具体使用哪种方式，取决于物品被用来做什么；物品的反馈能力在一定程度上决定了它的价值。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>请描述门铃远程通知功能的工作过程，并说明各模块使用的硬件。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>门铃端（输入模块，主控板+按键传感器）</strong>：门铃被按下，主控板采集到按键状态数据，通过网络把消息“有人按门铃”<strong>发布</strong>到 MQTT 服务器的主题“Door/Bell”；</li>
  <li><strong>MQTT服务器（计算模块，具备移动热点功能的计算机）</strong>：负责搭建服务器、设置主题，实现发布与订阅功能，起中转作用；</li>
  <li><strong>用户端（输出模块，主控板）</strong>：<strong>订阅</strong>主题“Door/Bell”，收到消息后在显示屏上显示“有人按门铃”，实现通知反馈；</li>
  <li>整个过程的触发条件是门铃被按下，反馈形式是通知反馈。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>为什么门铃端与用户端之间的通信必须借助 MQTT 服务器？程序中 time.sleep(5) 起什么作用？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>门铃端与用户端是两台相互独立的设备，需要跨网络通信，无法直接建立联系，因此需要<strong>服务器中转</strong>；</li>
  <li>MQTT 服务器提供<strong>设备管理、数据存储及数据处理</strong>等功能，通过“主题”把发布者与订阅者连接起来，实现发布／订阅通信；</li>
  <li>time.sleep(5) 的作用是<strong>等待5秒、防止重复发送</strong>。因为循环执行速度很快，按键被按住时会连续触发发送，造成消息重复和数据冗余，延时可以避免这一问题。</li>
</ol>
'''
            },
            {
                "id": "L14",
                "title": "第14课 远程控制更便捷",
                "knowledge": '''
<h3>一、认识物联系统中的控制</h3>
<p><strong>控制的定义（必背）：</strong>物联系统中的<strong>反馈与控制密不可分</strong>，<strong>控制是基于反馈的数据调整设备或者系统的工作状态</strong>。</p>
<p><strong>案例：火车站验票（人脸识别闸机）系统</strong></p>
<ol>
  <li>乘客在闸机上刷身份证并注视摄像头，系统<strong>采集乘客的身份数据</strong>；</li>
  <li>通过网络传输到<strong>验票服务器</strong>；</li>
  <li>服务器<strong>分析</strong>后作出是否允许通过的<strong>决策</strong>，<strong>反馈</strong>给闸机系统；</li>
  <li>闸机系统根据反馈数据<strong>判断是否打开闸机</strong>（控制）。</li>
</ol>
<p>可概括为：<strong>采集身份数据 — 分析处理 — 反馈结果 — 打开闸机</strong>。可见<strong>反馈是控制的触发条件</strong>。</p>

<h3>二、控制的两种类型</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>类型</th><th>定义</th><th>是否需要人参与</th><th>举例</th></tr>
  <tr>
    <td><strong>人工控制</strong></td>
    <td>由人直接或间接利用计算机、智能终端等联网设备<strong>发送指令</strong>，实现对远程设备的控制</td>
    <td><strong>需要</strong>人全程／直接参与</td>
    <td>用手机启动扫地机器人、设置开启和清洁模式；用燃气烧水时人观察并关火；本课的远程控制开锁</td>
  </tr>
  <tr>
    <td><strong>自动控制</strong></td>
    <td>物联系统对采集到的数据进行分析处理，根据<strong>设定的控制规则</strong>把决策反馈给设备，<strong>无须人直接干预</strong>就能控制设备运转</td>
    <td><strong>不需要</strong>人直接参与</td>
    <td>扫地机器人启动后感知环境数据、自主规划路线、避开障碍清扫；自动灌溉；自动报警</td>
  </tr>
</table>

<h3>三、远程控制开锁的实现过程</h3>
<p>本课采用<strong>人工（手动）控制</strong>方式实现对门锁的控制。</p>
<ol>
  <li>搭建 MQTT 服务器，设置主题，实现发布与订阅；</li>
  <li>门锁端<strong>订阅</strong>开锁指令主题；</li>
  <li>用户端<strong>按键触发</strong>，向主题<strong>发布</strong>开锁指令；</li>
  <li>门锁端收到指令后<strong>控制开锁</strong>（舵机转动）。</li>
</ol>

<h3>四、远程控制开锁功能分析（三模块）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>模块</th><th>硬件</th><th>实现思路</th><th>角色</th></tr>
  <tr><td><strong>输入模块</strong></td><td>主控板、按键传感器</td><td>采集按键状态数据，并<strong>发布</strong>消息至 MQTT 服务器相应主题</td><td><strong>用户端</strong>（发布者）</td></tr>
  <tr><td><strong>计算模块</strong></td><td>具备移动热点功能的计算机</td><td>搭建 MQTT 服务器，设置主题，实现发布与订阅功能</td><td>物联网服务平台</td></tr>
  <tr><td><strong>输出模块</strong></td><td>主控板、<strong>舵机</strong></td><td><strong>订阅</strong> MQTT 服务器相应主题，收到消息后<strong>控制舵机转动</strong></td><td><strong>门锁端</strong>（订阅者）</td></tr>
</table>
<p>本课主题名：<strong>“Door/Lock”</strong>；消息内容：<strong>“open”</strong>。</p>

<h3>五、主要代码</h3>
<p><strong>用户端（发布开锁指令）：</strong></p>
<pre>bt = button(1)                     # 将按键传感器连接到 Pin1 接口
while True:
    if bt.status() == 1:           # 如果按键被按下
        mqttclient.publish(topic="Door/Lock", content="open")
        time.sleep(5)              # 等待5 s，防止重复发送</pre>
<p><strong>门锁端（订阅并控制舵机）：</strong></p>
<pre>def open():                        # 定义开锁函数，控制舵机转动模拟开锁
    servo(1).angle(180)
    time.sleep(1.5)
    servo(1).angle(0)

def receivedfunction():
    msg = mqttclient.message(topic="Door/Lock")
    if msg == "open":              # 判断消息内容是否为 open
        open()                     # 调用开锁函数

mqttclient.received(topic="Door/Lock", callback=receivedfunction)</pre>
<p><em>判断语句 if msg == "open" 非常关键：如果不加判断，主题收到<strong>任何</strong>消息舵机都会转动，存在被误触发甚至被恶意开锁的隐患。</em></p>

<h3>六、实验与调试要点</h3>
<ul>
  <li>需要 <strong>2个主控板</strong>、1个按键传感器、1个舵机、1台具备移动热点功能的计算机，建议小组合作完成。</li>
  <li>若舵机没有反应，可在 MQTT 服务器中直接向主题“Door/Lock”发送“open”，观察舵机是否转动，以此逐步排查故障（是发布端问题还是订阅端问题）。</li>
</ul>

<h3>七、安全隐患与思考</h3>
<ul>
  <li><strong>数据公开传输：</strong>指令以明文形式发布在主题上，容易被他人查看或伪造。</li>
  <li><strong>认证机制缺失：</strong>任何知道主题名并能连上服务器的人都能发送“open”，就能打开别人的锁。</li>
  <li><strong>改进思路：</strong>加强身份认证（用户名／密码）、对数据加密、采用<strong>双重身份验证</strong>（如火车站验票系统同时使用身份证和人脸识别）。</li>
</ul>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">控制的定义</strong>：控制是<strong style="color:#c0392b;">基于反馈的数据调整设备或者系统的工作状态</strong>；<strong style="color:#c0392b;">反馈与控制密不可分</strong>。</li>
  <li><strong style="color:#c0392b;">人工控制</strong>：由人直接或间接利用计算机、智能终端等联网设备<strong style="color:#c0392b;">发送指令</strong>实现对远程设备的控制。</li>
  <li><strong style="color:#c0392b;">自动控制</strong>：系统分析处理数据后，按<strong style="color:#c0392b;">设定的控制规则</strong>把决策反馈给设备，<strong style="color:#c0392b;">无须人直接干预</strong>。</li>
  <li>经典判断：用手机启动扫地机器人是<strong style="color:#c0392b;">人工控制</strong>；扫地机器人启动后自主规划路径是<strong style="color:#c0392b;">自动控制</strong>。</li>
  <li>火车站验票系统工作过程：<strong style="color:#c0392b;">采集身份数据—分析处理—反馈结果—打开闸机</strong>；<strong style="color:#c0392b;">反馈是控制闸机是否打开的触发条件</strong>。</li>
  <li>本课主题名 <strong style="color:#c0392b;">Door/Lock</strong>，消息内容 <strong style="color:#c0392b;">“open”</strong>；输入模块是<strong style="color:#c0392b;">用户端</strong>，输出模块是<strong style="color:#c0392b;">门锁端</strong>（与第13课角色相反，易错）。</li>
  <li>输出模块硬件为<strong style="color:#c0392b;">主控板+舵机</strong>（第13课是主控板+显示屏），常考填表区分。</li>
  <li><strong style="color:#c0392b;">if msg == "open" 判断语句的作用</strong>：避免收到任意消息就开锁，提高安全性——高频简答点。</li>
  <li>安全隐患答题词：<strong style="color:#c0392b;">数据公开（明文）传输、认证机制缺失、指令可被伪造</strong>；改进：<strong style="color:#c0392b;">身份认证、数据加密、双重身份验证</strong>。</li>
  <li>本课采用的是<strong style="color:#c0392b;">人工（手动）控制</strong>方式，不是自动控制。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：人工控制 vs 自动控制</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>人工控制</th><th>自动控制</th></tr>
  <tr><td>指令来源</td><td><strong>人</strong>发送指令</td><td><strong>系统</strong>按预设规则／算法自行决策</td></tr>
  <tr><td>人是否参与</td><td>全程或关键环节需要人参与</td><td>无须人直接干预</td></tr>
  <tr><td>判断关键词</td><td>“用手机／App／按钮…去操作”</td><td>“检测到…就自动…”“根据规则自动…”</td></tr>
  <tr><td>本册举例</td><td>远程控制开锁、手动控制灌溉、用燃气烧水时人观察关火</td><td>自动灌溉（第20课）、扫地机器人自主规划路线、烟雾报警自动制动</td></tr>
</table>

<h3>易混辨析二：反馈 vs 控制</h3>
<ul>
  <li><strong>反馈</strong>回答“系统<strong>告诉／作用于</strong>现实世界什么”，如显示“有人按门铃”。</li>
  <li><strong>控制</strong>回答“系统<strong>让设备怎么改变状态</strong>”，如让舵机转动开锁、让水泵启动。</li>
  <li><strong>关系</strong>：先有数据与反馈，再有基于反馈的控制；反馈是控制的<strong>依据和触发条件</strong>，控制是反馈的落地执行。二者密不可分。</li>
</ul>

<h3>易混辨析三：第13课 vs 第14课（角色互换，最易错）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>第13课 门铃远程通知</th><th>第14课 远程控制开锁</th></tr>
  <tr><td>数据流向</td><td>家 → 用户（把状态<strong>告诉</strong>用户）</td><td>用户 → 家（把指令<strong>下达</strong>给门锁）</td></tr>
  <tr><td>输入模块是谁</td><td><strong>门铃端</strong></td><td><strong>用户端</strong></td></tr>
  <tr><td>输出模块是谁</td><td><strong>用户端</strong>（主控板显示屏）</td><td><strong>门锁端</strong>（主控板+舵机）</td></tr>
  <tr><td>主题名</td><td>Door/Bell</td><td>Door/Lock</td></tr>
  <tr><td>消息内容</td><td>“有人按门铃”</td><td>“open”</td></tr>
  <tr><td>体现的概念</td><td><strong>反馈</strong>（通知反馈）</td><td><strong>控制</strong>（人工控制）</td></tr>
</table>

<h3>易混辨析四：开环控制 vs 闭环（反馈）控制</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>开环控制</th><th>闭环（反馈）控制</th></tr>
  <tr><td>有无反馈</td><td><strong>没有</strong>把结果送回去比较</td><td><strong>有</strong>，把采集到的数据送回参与决策</td></tr>
  <tr><td>能否自我调整</td><td>不能，按固定指令执行到底</td><td>能，根据数据不断调整设备状态</td></tr>
  <tr><td>举例</td><td>定时5秒后关灯，不管房间实际亮度</td><td>验票闸机根据识别结果决定是否开闸；自动灌溉根据土壤湿度决定是否浇水</td></tr>
</table>

<h3>难点解析：为什么“加不加判断语句”是安全问题？</h3>
<p>若门锁端写成“只要收到消息就调用 open()”，那么任何人（包括邻组同学、恶意用户）只要能向该主题发送<strong>任意内容</strong>，门就会打开。加上 if msg == "open" 至少限定了<strong>指令格式</strong>。但这仍不够安全——指令是<strong>明文公开</strong>的，别人抓到“open”就能复制，所以真正的系统还需要身份认证与加密。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>控制口诀</strong>：<strong>人发指令是人工，规则自跑是自动</strong>。</li>
  <li><strong>反馈控制关系</strong>：<strong>反馈是“因”，控制是“果”；无反馈不成控制</strong>。</li>
  <li><strong>两课对比</strong>：<strong>Bell 往外报信（反馈），Lock 往里下令（控制）</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>物联系统中反馈与控制是什么关系？请结合火车站验票系统说明。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>反馈与控制<strong>密不可分</strong>：控制是<strong>基于反馈的数据</strong>调整设备或系统的工作状态，反馈是控制的依据和触发条件；</li>
  <li>验票系统中，乘客刷身份证并注视摄像头，系统<strong>采集身份数据</strong>；</li>
  <li>数据经网络传输到验票服务器，服务器<strong>分析处理</strong>后作出是否允许通过的决策，并把结果<strong>反馈</strong>给闸机系统；</li>
  <li>闸机系统根据反馈数据<strong>判断并控制</strong>闸机是否打开，这就是基于反馈的控制。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>什么是人工控制？什么是自动控制？请以扫地机器人为例加以说明。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>人工控制</strong>：由人直接或间接利用计算机、智能终端等联网设备发送指令，实现对远程设备的控制；</li>
  <li><strong>自动控制</strong>：物联系统对采集的数据进行分析处理，根据设定的控制规则把决策反馈给设备，无须人直接干预就能控制设备运转；</li>
  <li>用智能终端（手机）启动家里的扫地机器人、设置清洁模式，属于<strong>人工控制</strong>；</li>
  <li>扫地机器人启动后，依靠传感器感知周围环境数据，自主规划清扫路径、避开障碍，属于<strong>自动控制</strong>。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>本课实现的远程控制开锁系统存在哪些安全隐患？可以怎样改进？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>数据公开传输</strong>：开锁指令“open”以明文形式发布在 MQTT 主题上，容易被截获或查看；</li>
  <li><strong>认证机制缺失</strong>：只要知道服务器地址和主题名就能发布“open”，任何人都可能打开门锁，指令容易被伪造和重复利用；</li>
  <li><strong>缺少身份核验</strong>：系统只判断消息内容，不判断“是谁发的”；</li>
  <li><strong>改进措施</strong>：为设备设置<strong>用户名和密码</strong>进行身份认证、避免使用简单密码；对传输数据进行<strong>加密</strong>；采用<strong>双重身份验证</strong>（如火车站验票同时使用身份证和人脸识别）；增加操作日志与异常提醒。</li>
</ol>
'''
            },
            {
                "id": "L15",
                "title": "第15课 面容钥匙显智能",
                "knowledge": '''
<h3>一、认识人脸识别</h3>
<p><strong>定义（必背）：</strong>人脸识别是<strong>基于人的脸部特征数据进行身份识别</strong>的一种<strong>生物识别技术</strong>。把“人脸”当作钥匙实现开锁，通常称为<strong>刷脸开锁（面容钥匙）</strong>。</p>

<h3>二、人是怎样认出一张脸的（类比）</h3>
<ol>
  <li>眼睛<strong>捕捉</strong>到人脸图像信息，传给大脑；</li>
  <li>大脑对人脸图像进行<strong>分析</strong>，提取人脸的<strong>局部特征</strong>（眉毛、眼睛、鼻子、嘴等）和<strong>整体轮廓</strong>；</li>
  <li>与<strong>记忆中的人脸特征进行匹配</strong>，识别出人脸的身份。</li>
</ol>
<p>可以用“描述同桌五官特征”的小游戏体会：眉毛（浓密／稀疏）、眼睛（双眼皮／单眼皮）、鼻子（高鼻梁／鹰钩鼻）、嘴（厚嘴唇／薄嘴唇）、脸型（圆脸／方脸／瓜子脸）。</p>

<h3>三、机器识别人脸的基本过程（核心考点）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>步骤</th><th>做什么</th><th>形象说法</th></tr>
  <tr><td><strong>①人脸检测（人脸定位）</strong></td><td>对输入的图像进行人脸检测，<strong>找到并框出人脸</strong></td><td><strong>看得到</strong></td></tr>
  <tr><td><strong>②特征提取（特征分析）</strong></td><td>使用<strong>算法提取</strong>人脸图像中的<strong>特征点</strong>，不仅能识别出人的表情、年龄等</td><td><strong>看得懂</strong></td></tr>
  <tr><td><strong>③人脸匹配（身份识别）</strong></td><td>根据<strong>预先设置的匹配算法和条件</strong>，与人脸库比对，判断输入人脸的身份</td><td><strong>认得出</strong></td></tr>
</table>
<p>一个完整的人脸识别系统要求计算机能够完成上述<strong>三步</strong>，从而保证采集到的人脸图像能够被<strong>看得到、看得懂和认得出</strong>。</p>

<h3>四、利用摄像头实现人脸识别</h3>
<p>只需给计算机配备普通摄像头，就可以利用<strong>网页版人脸识别平台</strong>体验人脸采集和人脸识别。</p>
<ol>
  <li>运行人脸识别平台；</li>
  <li>选择<strong>人脸匹配</strong>模块，通过摄像头拍摄或上传图片的方式<strong>添加人脸库</strong>；</li>
  <li>将面部对准摄像头，观察是否匹配。</li>
</ol>
<p><em>注意：不同人脸识别平台的操作有所不同；也可使用人工智能摄像头替代“普通摄像头+网页平台”的方案。</em></p>

<h3>五、刷脸开锁功能分析（三模块）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>模块</th><th>硬件</th><th>实现思路</th></tr>
  <tr><td><strong>输入模块</strong></td><td><strong>摄像头</strong></td><td>采集人脸数据，进行<strong>人脸识别</strong>后，<strong>发布</strong>消息至 MQTT 服务器相应主题</td></tr>
  <tr><td><strong>计算模块</strong></td><td>具备移动热点功能的计算机</td><td>搭建 MQTT 服务器，设置主题，实现发布与订阅功能</td></tr>
  <tr><td><strong>输出模块</strong></td><td>主控板、<strong>舵机</strong></td><td><strong>订阅</strong> MQTT 服务器相应主题，收到消息后<strong>控制舵机转动</strong></td></tr>
</table>
<p><strong>实现效果：</strong>通过摄像头采集小华的人脸数据，物联系统确认是小华后，舵机转动（门锁打开）。</p>

<h3>六、模拟实现步骤</h3>
<p>器材：1个主控板、1个摄像头、1个舵机、1台具备移动热点功能的计算机。</p>
<ol>
  <li><strong>设置无线网络</strong>；</li>
  <li><strong>搭建 MQTT 服务器</strong>，建立项目并<strong>设置主题</strong>，记录系统自动生成的<strong>设备ID、用户名和密码</strong>；</li>
  <li>登录<strong>人脸识别平台</strong>，在 MQTT 设置中填写<strong>主题、设备ID、用户名、密码，以及服务器的 IP 地址和端口</strong>；</li>
  <li>启动 web 版摄像头页面，<strong>采集人脸到人脸库中</strong>；</li>
  <li>补充完善程序 → 把程序<strong>烧录</strong>到主控板 → <strong>测试验证</strong>。</li>
</ol>

<h3>七、主要代码</h3>
<pre>def open():                              # 定义开锁函数
    servo(1).angle(180)
    time.sleep(1.5)
    servo(1).angle(0)

def receivedfunction():
    msg = mqttclient.message(topic="主题ID")
    if ujson.loads(msg)["status"] == 1:  # 识别到人脸库中的人脸
        open()                           # 控制舵机转动，模拟开锁

mqttclient.received(topic="主题ID", callback=receivedfunction)</pre>
<p><em>要点：人脸识别平台把识别结果以 <strong>JSON</strong> 格式发布到主题；主控板用 <strong>ujson.loads()</strong> 把 JSON 字符串解析为字典，再取出 <strong>status</strong> 字段判断是否匹配成功（1 表示识别到人脸库中的人脸）。</em></p>

<h3>八、发展趋势与安全提醒</h3>
<ul>
  <li>门锁的发展：<strong>钥匙开锁 → 刷卡开锁 → 远程门铃通知 → 远程控制开锁 → 刷脸开锁</strong>，越来越智能，体现了<strong>物联网、大数据与人工智能</strong>的融合。</li>
  <li><strong>隐私安全：</strong>人脸、指纹、掌纹等属于<strong>生物特征数据</strong>，一旦泄露<strong>无法像密码那样更改</strong>。要高度警惕任何收集生物特征数据的场景，不随意提供个人面部等数据；对索要人脸识别权限的应用软件或小程序，应<strong>阅读了解授权采集生物特征数据的合同条款</strong>。</li>
  <li><strong>拓展应用：</strong>物联考勤系统——摄像头识别人脸后，通过 MQTT 把学生学号实时推送到教师端设备，教师端用字典存“人脸ID—学生姓名”，显示“某某已签到”。</li>
</ul>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">人脸识别的定义</strong>：基于人的<strong style="color:#c0392b;">脸部特征数据</strong>进行<strong style="color:#c0392b;">身份识别</strong>的一种<strong style="color:#c0392b;">生物识别技术</strong>。</li>
  <li><strong style="color:#c0392b;">机器识别人脸的三个步骤</strong>：<strong style="color:#c0392b;">人脸检测（定位）→ 特征提取（分析）→ 人脸匹配（识别身份）</strong>，对应<strong style="color:#c0392b;">看得到、看得懂、认得出</strong>——最高频考点。</li>
  <li>人识别人脸的三步：<strong style="color:#c0392b;">眼睛捕捉图像 → 大脑提取局部特征和整体轮廓 → 与记忆匹配</strong>。</li>
  <li>刷脸开锁三模块：输入模块=<strong style="color:#c0392b;">摄像头</strong>；计算模块=<strong style="color:#c0392b;">具备移动热点功能的计算机（MQTT服务器）</strong>；输出模块=<strong style="color:#c0392b;">主控板+舵机</strong>。</li>
  <li>人脸识别平台 MQTT 设置需填：<strong style="color:#c0392b;">主题、设备ID、用户名、密码、服务器IP地址和端口</strong>。</li>
  <li>代码要点：<strong style="color:#c0392b;">ujson.loads(msg)["status"] == 1</strong> 表示识别到人脸库中的人脸；识别结果以 <strong style="color:#c0392b;">JSON</strong> 格式传输。</li>
  <li>使用前必须先<strong style="color:#c0392b;">采集人脸到人脸库</strong>，否则无法匹配（“先入库，后识别”）。</li>
  <li><strong style="color:#c0392b;">生物特征数据一旦泄露无法更改</strong>，要警惕收集人脸、指纹、掌纹的场景，注意阅读授权条款——高频价值观／安全考点。</li>
  <li>门锁演进顺序：<strong style="color:#c0392b;">钥匙 → 刷卡 → 远程通知 → 远程控制 → 刷脸</strong>，体现物联系统的<strong style="color:#c0392b;">智能化发展趋势</strong>。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：人脸检测 vs 人脸识别</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>人脸检测</th><th>人脸识别</th></tr>
  <tr><td>解决的问题</td><td><strong>“有没有脸、脸在哪”</strong></td><td><strong>“这张脸是谁”</strong></td></tr>
  <tr><td>输出结果</td><td>框出人脸的位置</td><td>身份判断结果（是／不是某人）</td></tr>
  <tr><td>所处阶段</td><td>第一步（看得到）</td><td>第三步（认得出），需先完成检测和特征提取</td></tr>
  <tr><td>典型场景</td><td>相机自动对焦人脸</td><td>刷脸开锁、刷脸考勤、验票闸机</td></tr>
</table>

<h3>易混辨析二：刷脸开锁 vs 刷卡开锁</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>刷卡开锁（第12课）</th><th>刷脸开锁（第15课）</th></tr>
  <tr><td>身份凭证</td><td>门禁卡内<strong>电子标签编号</strong>（身外之物）</td><td><strong>人脸特征数据</strong>（生物特征，人本身）</td></tr>
  <tr><td>输入设备</td><td>RFID读卡器</td><td>摄像头</td></tr>
  <tr><td>判断方式</td><td>编号是否在<strong>列表</strong>中（精确比对）</td><td>特征是否与<strong>人脸库</strong>匹配（算法比对）</td></tr>
  <tr><td>是否需要联网</td><td>本课方案<strong>本地</strong>判断即可</td><td>需要 MQTT 服务器转发识别结果</td></tr>
  <tr><td>优点</td><td>成本低、稳定、判断简单</td><td>无须携带物品、更便捷，防止卡片转借</td></tr>
  <tr><td>不足</td><td>卡片可能<strong>丢失、转借、被复制</strong></td><td>受光线、角度、遮挡影响；存在<strong>隐私泄露</strong>风险</td></tr>
</table>

<h3>易混辨析三：三课的“三模块”对比（本单元综合大表）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>功能</th><th>输入模块</th><th>计算模块</th><th>输出模块</th></tr>
  <tr><td>刷卡开锁（L12）</td><td>电子标签、RFID读卡器</td><td>主控板（本地判断）</td><td>舵机</td></tr>
  <tr><td>门铃远程通知（L13）</td><td>主控板+按键传感器</td><td>计算机（MQTT服务器）</td><td>主控板（显示屏）</td></tr>
  <tr><td>远程控制开锁（L14）</td><td>主控板+按键传感器</td><td>计算机（MQTT服务器）</td><td>主控板+舵机</td></tr>
  <tr><td>刷脸开锁（L15）</td><td><strong>摄像头</strong></td><td>计算机（MQTT服务器）</td><td>主控板+舵机</td></tr>
</table>

<h3>难点解析：为什么代码里要用 ujson.loads()？</h3>
<p>人脸识别平台发布到主题的消息是一段 <strong>JSON 格式的字符串</strong>（里面包含 status 等多个字段）。字符串不能直接取字段，必须先用 <strong>ujson.loads()</strong> 把它<strong>解析为字典</strong>，才能用 ["status"] 取出识别结果。这与第17课解析天气 API 数据的方法完全一致，是本册的通用技能。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>三步口诀</strong>：<strong>找脸（检测）→ 取点（特征）→ 对号（匹配）</strong>，即<strong>看得到、看得懂、认得出</strong>。</li>
  <li><strong>输入设备记忆</strong>：卡靠<strong>读卡器</strong>，铃靠<strong>按键</strong>，脸靠<strong>摄像头</strong>。</li>
  <li><strong>安全提醒记忆</strong>：<strong>密码丢了能换，脸丢了换不了</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>什么是人脸识别技术？请描述机器识别人脸的基本过程。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>定义</strong>：人脸识别是基于人的脸部特征数据进行身份识别的一种生物识别技术。</li>
  <li><strong>第一步 人脸检测（定位）</strong>：系统对输入的图像进行人脸检测，找到并框出人脸——保证“<strong>看得到</strong>”。</li>
  <li><strong>第二步 特征提取（分析）</strong>：使用算法提取人脸图像中的特征点，如眉毛、眼睛、鼻子、嘴等局部特征和整体轮廓，还可识别表情、年龄等——保证“<strong>看得懂</strong>”。</li>
  <li><strong>第三步 人脸匹配（身份识别）</strong>：根据预先设置的匹配算法和条件，把提取的特征与人脸库中的数据比对，判断输入人脸的身份——保证“<strong>认得出</strong>”。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>请分析刷脸开锁功能的三个模块，并说明各模块使用的硬件与作用。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>输入模块——摄像头</strong>：采集人脸数据，进行人脸识别，并把识别结果发布到 MQTT 服务器相应主题；</li>
  <li><strong>计算模块——具备移动热点功能的计算机</strong>：搭建 MQTT 服务器，设置主题，实现发布与订阅功能，起中转作用；</li>
  <li><strong>输出模块——主控板和舵机</strong>：订阅 MQTT 服务器相应主题，收到消息后判断识别状态，若匹配成功则控制舵机转动，模拟门锁打开；</li>
  <li>使用前需要先通过摄像头或上传图片把人脸采集到<strong>人脸库</strong>中，识别时才能完成匹配。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>与刷卡开锁相比，刷脸开锁有哪些优点？使用人脸识别技术时应注意什么？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>优点</strong>：人脸是人自身的生物特征，<strong>无须携带门禁卡</strong>，不会丢失或被转借，使用更便捷；识别过程非接触、速度快，安全性和用户体验更好；便于与考勤、访客管理等系统结合。</li>
  <li><strong>不足</strong>：识别效果会受光线、角度、遮挡等影响；对设备和算法要求较高。</li>
  <li><strong>安全注意</strong>：人脸属于<strong>生物特征数据</strong>，泄露后无法像密码一样更改；要高度警惕收集人脸、指纹、掌纹等数据的场景，不随意向他人或不明应用提供这类数据；对索要人脸识别权限的应用软件或小程序，应认真阅读并了解授权采集生物特征数据的合同条款。</li>
</ol>
'''
            }
        ]
    },
    {
        "module": "第四单元：简易物联系统实践",
        "desc": "在上一单元“简单物联功能实践”的基础上，本单元内容更加综合，要求从物联系统的<strong>整体</strong>出发进行分析和规划，学会设计较为完整的简易物联系统。物联系统的工作过程，本质上是通过<strong>感知外部环境</strong>，并经过<strong>数据传输、存储、处理</strong>，最终<strong>反馈到外部环境</strong>的过程。本单元围绕“简易物联花盆系统”这一项目展开：先划分功能模块、确定功能需求，再依次完成数据采集与传输、数据分析与处理、数据可视化呈现，最后基于数据设计算法实现反馈与控制，并进行系统整合与调试。实践难度较前三个单元略大，实施时应<strong>先分别实现各模块功能，再集成为完整系统</strong>。",
        "lessons": [
            {
                "id": "L16",
                "title": "第16课 模块功能先划分",
                "knowledge": '''
<h3>一、物联系统的工作环节</h3>
<p>物联系统会根据<strong>任务目标</strong>，采集周围环境数据，对数据进行传输、存储、分析处理，再设计算法，通过执行器对现实世界采取行动。<strong>不同的物联系统在功能、软硬件组成上各有不同，但工作环节类似。</strong></p>
<p><strong>四个工作环节（必背，注意顺序）：</strong></p>
<ol>
  <li><strong>采集数据</strong></li>
  <li><strong>传输与存储数据</strong></li>
  <li><strong>分析处理数据</strong></li>
  <li><strong>反馈与控制</strong></li>
</ol>
<p><strong>示例：共享单车系统的工作环节</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>物联系统</th><th>采集数据</th><th>传输与存储数据</th><th>分析处理数据</th><th>反馈与控制</th></tr>
  <tr><td>共享单车</td><td>位置传感器采集单车位置数据</td><td>通过<strong>窄带物联网（NB-IoT）</strong>传输单车位置数据</td><td>计算单车的具体位置</td><td>用户扫码（认证）后开锁</td></tr>
</table>

<h3>二、确定物联系统的功能需求</h3>
<p>搭建物联系统前，首先要<strong>明确系统建设的目标</strong>——期望用该系统达到什么目的、解决什么问题，进而得出需要实现的功能。</p>
<p><strong>项目情境：</strong>学校种植了绿色植物，为了解校园不同区域的实时环境状况，决定搭建<strong>物联花盆系统</strong>。</p>
<p><strong>物联花盆系统功能需求表（必背）：</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>环节</th><th>功能描述</th></tr>
  <tr><td>采集数据</td><td>可实时获取<strong>温度、土壤湿度、光照强度</strong>等数据；可通过网络获取<strong>天气预报</strong>数据</td></tr>
  <tr><td>传输与存储数据</td><td>可通过网络将数据传输给<strong>物联网服务平台</strong></td></tr>
  <tr><td>分析处理数据</td><td>可从物联网服务平台获取<strong>历史数据</strong>；可对数据进行初步分析处理，得到简单的<strong>数据统计结果和可视化图表</strong></td></tr>
  <tr><td>反馈与控制</td><td>可<strong>动态显示土壤湿度</strong>情况；可根据温度、土壤湿度、天气预报数据，实现<strong>自动灌溉</strong></td></tr>
</table>

<h3>三、各环节的实现方案（可行性评估）</h3>
<ol>
  <li><strong>采集数据：</strong>根据任务确定要采集的环境数据，再根据使用场景选择合适的传感器。空气温度、土壤湿度、光照强度分别用<strong>温湿度传感器、土壤湿度传感器、光敏传感器</strong>；天气预报数据通过 <strong>API</strong> 获取。</li>
  <li><strong>传输与存储数据：</strong>通过网络把数据传输并存储在<strong>物联网服务平台</strong>。</li>
  <li><strong>分析处理数据：</strong>从平台获取<strong>历史数据</strong>，进行简单分析处理，得到统计结果和<strong>可视化图表</strong>。</li>
  <li><strong>反馈与控制：</strong>根据土壤湿度、天气预报等数据<strong>设计算法</strong>实现自动灌溉（如土壤湿度大不灌溉；湿度小且预报次日下雨不灌溉；光照强度大时适当提高土壤湿度设定值）。</li>
</ol>

<h3>四、划分物联系统的功能模块</h3>
<p>为了<strong>降低难度</strong>，需要把物联系统分解为多个功能模块，并明确每个模块负责的任务以及模块之间的关系。<strong>物联花盆系统可分为四个功能模块（必背）：</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>功能模块</th><th>组成</th><th>负责的任务</th></tr>
  <tr><td><strong>环境感知模块</strong></td><td>传感器 + 主控板</td><td>传感器负责采集环境数据；主控板接收传感器数据，并通过网络通信模块发送到服务平台模块</td></tr>
  <tr><td><strong>网络通信模块</strong></td><td>主控板的联网功能／网络设备</td><td>实现数据通信：把传感器数据发送到服务平台；把服务平台数据和互联网上的天气预报数据传给主控板</td></tr>
  <tr><td><strong>服务平台模块</strong></td><td>物联网服务平台（在线／本地 MQTT 服务器）</td><td>负责数据的<strong>汇总、存储、处理</strong>；存储环境数据、将环境数据可视化、实现手动控制灌溉</td></tr>
  <tr><td><strong>执行模块</strong></td><td>主控板 + 执行器</td><td>执行器根据主控板发出的指令产生相应动作（如 LED 灯亮灭、电机启动或关闭、水泵灌溉），实现物联系统对现实世界的<strong>反馈</strong></td></tr>
</table>
<p><strong>重要提示：</strong>有些设备会<strong>同时属于多个模块</strong>。例如物联花盆系统中的<strong>主控板</strong>，既是环境感知模块的一部分，也是执行模块的一部分，同时因为提供联网功能，还是网络通信模块的一部分。</p>

<h3>五、网络通信方式的选择</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>系统类型</th><th>通信方式</th><th>原因</th></tr>
  <tr><td>共享单车等<strong>地域分布广</strong>的系统</td><td>移动通信网络（如窄带物联网）</td><td>覆盖范围大，随时随地联网</td></tr>
  <tr><td>物联家居等<strong>区域较小</strong>的系统</td><td>蓝牙等近距离无线通信技术</td><td>距离近、功耗低、成本低</td></tr>
  <tr><td>火灾自动报警系统</td><td>多采用<strong>有线传输</strong></td><td>保证数据传输的<strong>可靠性</strong></td></tr>
</table>

<h3>六、拓展案例分析</h3>
<p><strong>1. 高铁烟雾报警系统（按四环节）：</strong>各车厢内的<strong>烟雾报警器（传感器）</strong>负责环境数据采集 → 通过有线或无线方式<strong>传输数据</strong> → <strong>服务器</strong>负责分析处理数据 → 报警使列车<strong>紧急制动</strong>并通知列车长和司机，实现反馈与控制。</p>
<p><strong>2. 物联公交系统（按四模块）：</strong>环境感知模块——利用北斗车载定位终端等获得实时位置；网络通信模块——通过窄带物联网连接互联网；服务平台模块——公交公司数据中心部署的物联网服务平台；执行模块——智能终端应用软件查询公交车位置。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">物联系统的四个工作环节</strong>：<strong style="color:#c0392b;">采集数据 → 传输与存储数据 → 分析处理数据 → 反馈与控制</strong>（顺序不能乱，常考填空／排序）。</li>
  <li><strong style="color:#c0392b;">不同物联系统功能与软硬件不同，但工作环节类似</strong>——常作判断题。</li>
  <li><strong style="color:#c0392b;">物联花盆系统的四个功能模块</strong>：<strong style="color:#c0392b;">环境感知模块、网络通信模块、服务平台模块、执行模块</strong>——最高频考点。</li>
  <li>环境感知模块由<strong style="color:#c0392b;">传感器和主控板</strong>组成；执行模块包括<strong style="color:#c0392b;">主控板和执行器</strong>。</li>
  <li><strong style="color:#c0392b;">执行器的作用</strong>：根据主控板发出的指令<strong style="color:#c0392b;">产生相应的动作</strong>（LED灯亮灭、电机启停等），实现物联系统对现实世界的<strong style="color:#c0392b;">反馈</strong>。</li>
  <li>服务平台模块负责数据的<strong style="color:#c0392b;">汇总、存储、处理</strong>，还负责<strong style="color:#c0392b;">可视化</strong>和<strong style="color:#c0392b;">手动控制灌溉</strong>。</li>
  <li>物联花盆需采集：<strong style="color:#c0392b;">温度、土壤湿度、光照强度</strong>（传感器）+ <strong style="color:#c0392b;">天气预报</strong>（网络API）。</li>
  <li><strong style="color:#c0392b;">主控板同时属于三个模块</strong>（环境感知、网络通信、执行）——易错高频点。</li>
  <li>通信方式选择：广域用<strong style="color:#c0392b;">移动通信网络／窄带物联网</strong>；小范围用<strong style="color:#c0392b;">蓝牙</strong>；高可靠性场合用<strong style="color:#c0392b;">有线传输</strong>。</li>
  <li>划分模块的目的：<strong style="color:#c0392b;">降低难度</strong>，明确各模块任务和相互关系，便于分别实现后再集成。</li>
  <li>数据可视化<strong style="color:#c0392b;">也可以看作一种反馈方式</strong>，因此可归入执行模块。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：工作环节 vs 功能模块</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>四个工作环节</th><th>四个功能模块</th></tr>
  <tr><td>划分角度</td><td>按<strong>做事的先后过程</strong>（时间／流程）</td><td>按<strong>承担任务的软硬件组合</strong>（结构）</td></tr>
  <tr><td>内容</td><td>采集数据、传输与存储数据、分析处理数据、反馈与控制</td><td>环境感知模块、网络通信模块、服务平台模块、执行模块</td></tr>
  <tr><td>回答什么问题</td><td>“系统<strong>先做什么、后做什么</strong>”</td><td>“<strong>谁</strong>来做这件事、用什么硬件”</td></tr>
  <tr><td>对应关系</td><td colspan="2">采集↔环境感知模块；传输与存储↔网络通信模块+服务平台模块；分析处理↔服务平台模块；反馈与控制↔执行模块</td></tr>
</table>

<h3>易混辨析二：三层结构（第三单元） vs 四模块（第四单元）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>三层结构</th><th>大致对应的功能模块</th></tr>
  <tr><td>感知层</td><td>环境感知模块</td></tr>
  <tr><td>网络层</td><td>网络通信模块</td></tr>
  <tr><td>应用层</td><td>服务平台模块 + 执行模块</td></tr>
</table>
<p><strong>注意：</strong>三层结构是<strong>通用的体系架构</strong>，四模块是<strong>针对具体项目</strong>的划分，二者只是大致对应，答题时要按题目要求的框架作答。</p>

<h3>易混辨析三：环境感知模块 ≠ 只有传感器</h3>
<p>环境感知模块由<strong>传感器和主控板共同组成</strong>：传感器负责“采”，主控板负责“收并转发”。只写“传感器”会丢分。同理，执行模块也是<strong>主控板+执行器</strong>，不是只有执行器。</p>

<h3>难点解析：为什么一个主控板会横跨三个模块？</h3>
<p>因为模块是按<strong>功能</strong>划分而不是按<strong>物理设备</strong>划分的。主控板同时承担了三件事：①接收传感器数据（环境感知）；②通过 Wi-Fi 联网收发数据（网络通信）；③驱动水泵、显示屏等执行器（执行）。所以同一块硬件可以出现在多个模块中。这正说明<strong>模块划分是逻辑上的分工，不是物理上的切割</strong>。</p>

<h3>难点解析：数据可视化算反馈吗？</h3>
<p>算。教材指出：对于一些主要用于数据采集及呈现的物联系统，<strong>对数据进行可视化呈现也是一种反馈方式</strong>，因此也可以把数据可视化功能归于执行模块。判断依据是——它是否<strong>作用于现实世界／让用户获知并作出决策</strong>。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>四环节口诀</strong>：<strong>采 → 传（存）→ 析 → 控</strong>。</li>
  <li><strong>四模块口诀</strong>：<strong>感、通、台、行</strong>（环境感知、网络通信、服务平台、执行）。</li>
  <li><strong>模块与环节对应</strong>：<strong>感管采、通管传、台管析、行管控</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>物联系统的一般工作环节有哪些？请以共享单车为例说明。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>物联系统的工作环节一般包括四步：<strong>采集数据 → 传输与存储数据 → 分析处理数据 → 反馈与控制</strong>；不同的物联系统在功能和软硬件组成上各有不同，但工作环节类似。</li>
  <li><strong>采集数据</strong>：共享单车用位置传感器采集单车的位置数据；</li>
  <li><strong>传输与存储数据</strong>：通过窄带物联网把位置数据传输到服务平台；</li>
  <li><strong>分析处理数据</strong>：服务器计算出单车的具体位置；</li>
  <li><strong>反馈与控制</strong>：用户扫码认证通过后，系统控制车锁打开。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>物联花盆系统可以划分为哪几个功能模块？各模块由什么组成、负责什么任务？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>环境感知模块</strong>：由传感器和主控板组成。传感器采集温度、土壤湿度、光照强度等环境数据，主控板接收数据并通过网络通信模块发送出去。</li>
  <li><strong>网络通信模块</strong>：负责实现数据通信，把主控板获取的传感器数据发送到服务平台模块，并把服务平台数据和互联网上的天气预报数据传输给主控板。</li>
  <li><strong>服务平台模块</strong>：负责数据的汇总、存储和处理，实现环境数据的存储、可视化以及手动控制灌溉。</li>
  <li><strong>执行模块</strong>：由主控板和执行器组成，执行器根据主控板发出的指令产生相应动作（如显示屏显示、水泵电机启动灌溉），实现系统对现实世界的反馈。</li>
  <li>补充：主控板同时属于环境感知、网络通信和执行三个模块。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>高铁上安装了烟雾报警系统，任何区域有烟雾，列车长和司机都能第一时间收到报警信息。请结合物联系统的工作环节，说说每个环节可能使用了哪些硬件。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>采集数据</strong>：各车厢内设置的<strong>烟雾报警器（烟雾传感器）</strong>负责采集环境中的烟雾浓度数据；</li>
  <li><strong>传输与存储数据</strong>：通过<strong>有线或无线网络</strong>把数据传输到列车的数据服务器并存储；</li>
  <li><strong>分析处理数据</strong>：<strong>服务器</strong>对烟雾数据进行分析处理，判断是否超过报警阈值；</li>
  <li><strong>反馈与控制</strong>：通过<strong>报警器（蜂鸣器）、显示终端</strong>向列车长和司机推送报警信息，必要时使列车<strong>紧急制动</strong>，实现对现实世界的反馈与控制。</li>
</ol>
'''
            },
            {
                "id": "L17",
                "title": "第17课 物联数据需采集",
                "knowledge": '''
<h3>一、数据是物联系统的基础</h3>
<p>要搭建一个物联系统，<strong>首先要实现数据的采集与传输</strong>。</p>
<p><strong>物联网数据的来源（必背）：</strong></p>
<ul>
  <li><strong>传感器采集</strong>的数据（主要来源）；</li>
  <li><strong>互联网</strong>中的数据（通过 API 获取，如天气预报）（主要来源）；</li>
  <li>用户<strong>输入</strong>的数据；</li>
  <li>物联系统在<strong>运行过程中自行产生</strong>的数据。</li>
</ul>

<h3>二、利用传感器获取数据</h3>
<p>获取不同的环境数据需要不同的传感器。物联花盆系统项目需要<strong>三种传感器</strong>：</p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>传感器</th><th>采集的数据</th><th>输出信号类型</th></tr>
  <tr><td><strong>温湿度传感器</strong></td><td>空气温度、空气湿度</td><td><strong>数字信号</strong></td></tr>
  <tr><td><strong>土壤湿度传感器</strong></td><td>土壤湿度</td><td><strong>模拟信号</strong></td></tr>
  <tr><td><strong>光敏传感器</strong></td><td>光照强度</td><td><strong>模拟信号</strong></td></tr>
</table>
<p><em>当前主流主控板的每个引脚都具备读取模拟信号和数字信号的能力，因此只需在主控板或扩展板上找任意3个接口分别与三个传感器的数据接口相连。</em></p>

<h3>三、从互联网获取数据（API）</h3>
<p>互联网上有很多<strong>公共数据监测网站</strong>和免费的<strong>天气预报 API</strong> 供人们调用。访问官方网站获取的数据更可靠。</p>
<p><strong>调用 API 的主要代码：</strong></p>
<pre>city_code = "CH010100"        # 城市编号，CH010100 表示北京
key = "API密钥"
res = urequests.get("http://api.yytianqi.com/forecast7d?city=" + city_code + "&key=" + key)   # 发起网络请求
if res.status_code == 200:                       # 200 表示请求成功
    data = ujson.loads(res.text)                 # 把 JSON 字符串转换为字典
    tq1 = data["data"]["list"][0]["tq1"]
    tq2 = data["data"]["list"][0]["tq2"]
    tq = tq1 + "-" + tq2                         # 例如 “多云-晴”
    oled.print(tq)</pre>
<p><strong>关键要素：</strong>①<strong>城市编号</strong>（不同城市不同，必须准确）；②<strong>API 密钥（key）</strong>；③<strong>URL 与参数</strong>；④返回的 <strong>status_code 为 200 表示成功</strong>。</p>

<h3>四、认识 JSON 数据格式</h3>
<ul>
  <li>通过 Web 协议交换的数据格式中，具有代表性的是 <strong>XML</strong> 和 <strong>JSON</strong>。</li>
  <li><strong>XML</strong> 格式比 JSON 更容易理解，但<strong>字符数较多、数据量较大</strong>；<strong>JSON</strong> 比 XML <strong>字符数少、数据量小</strong>。</li>
  <li>通过 <strong>ujson.loads()／json.loads()</strong> 方法，可以把 JSON 字符串<strong>转换为字典结构</strong>。</li>
  <li>天气接口返回结果整体是一个<strong>字典</strong>；其中 <strong>data 键</strong>包含主要的天气预报数据；data 中的 <strong>list 键</strong>是一个<strong>列表</strong>，分别存储当天和第二天的天气预报。这体现了<strong>字典与列表的嵌套</strong>。</li>
</ul>

<h3>五、配置物联网服务平台</h3>
<p>主控板实时读取传感器数据，整理后发送到物联网服务平台，好处是：可在平台<strong>实时看到环境数据</strong>，方便<strong>汇总来自不同采集端的数据</strong>，也为后续<strong>数据分析</strong>提供便利。可以搭建<strong>本地 MQTT 服务器</strong>，也可以使用<strong>在线 MQTT 服务器</strong>。</p>
<p><strong>配置三要点（必背）：</strong></p>
<ol>
  <li><strong>使用不同的主题存储不同的数据。</strong>物联花盆系统可按<strong>温度、光照强度、土壤湿度</strong>添加 <strong>3 个主题</strong>。</li>
  <li><strong>按项目需求添加设备。</strong>考虑数据安全性，接入设备需<strong>身份认证</strong>；根据终端设备数量添加，并与主控板一一对应，平台会为每个主控板分配<strong>用户名和密码</strong>。</li>
  <li><strong>记录主题ID、设备ID、用户名和密码。</strong>运行时：主控板通过<strong>用户名和密码</strong>进行身份验证后连接 MQTT 服务器；通过<strong>主题ID</strong>识别对应主题，实现发布和订阅；通过<strong>设备ID</strong>识别不同的主控板。</li>
</ol>

<h3>六、实现数据的传输与存储</h3>
<p><strong>数据传输核心流程图（必背顺序）：</strong>连接无线网络 → 连接物联网服务平台 → 获取传感器数据 → 发送到对应主题 → 暂停30 s（循环）。</p>
<p><strong>数据传输的主要代码：</strong></p>
<pre>while True:
    temp, _ = dht(0).read()                # 从Pin0接口传感器读取空气温度值
    hum = pin(1).read_analog()             # 从Pin1接口传感器读取土壤湿度值
    lgt = light(2).read()                  # 从Pin2接口传感器读取光照强度值
    mqttclient.publish(topic="温度主题ID", content=str(temp))
    mqttclient.publish(topic="光照主题ID", content=str(lgt))
    mqttclient.publish(topic="湿度主题ID", content=str(hum))
    time.sleep(30)                         # 每隔30 s上报一次数据</pre>
<p><strong>两点注意：</strong>①考虑 MQTT 服务器压力，每次上报要留<strong>时间间隔</strong>（本例 30 s）；②有些传感器读到的数据还需<strong>计算处理</strong>后才能得到结果。数据采集时间较长时，建议为主控板<strong>外接电源</strong>供电。</p>

<h3>七、三个实践思考问题及解决办法</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>问题</th><th>解决办法</th></tr>
  <tr><td>如何实时查看主控板的运行状态？</td><td>每次采集数据时用 <strong>oled.print()</strong> 把数据值显示出来；若数值在变化，说明主控板运行正常</td></tr>
  <tr><td>多种数据放在一个主题里，如何区分？</td><td>把多个数据进行<strong>字符串拼接</strong>并加<strong>分隔符</strong>，如温度20、光照1500、湿度500 发送为 <strong>“20-1500-500”</strong>；后续处理时用 <strong>split()</strong> 分割还原</td></tr>
  <tr><td>如何减少数据冗余（数据变化时才上传）？</td><td>在程序中添加<strong>临时变量</strong>：新读取的数据与临时变量<strong>不同</strong>时才上传，并把临时变量<strong>更新</strong>为新值；相同则说明无变化，无须上传</td></tr>
</table>

<h3>八、本地 MQTT 服务器 vs 在线 MQTT 服务器</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>角度</th><th>本地 MQTT 服务器</th><th>在线 MQTT 服务器</th></tr>
  <tr><td>覆盖范围</td><td>一般只能在<strong>同一局域网</strong>内访问</td><td>一般可通过<strong>公网远程访问</strong></td></tr>
  <tr><td>便捷性</td><td>需自行搭建、配置；课堂内使用方便，不依赖外网</td><td>注册后即可使用，无须自建，但依赖网络与账号</td></tr>
  <tr><td>数据安全性</td><td>数据保存在本地，自主可控</td><td>数据存放在第三方平台，需关注隐私与账号安全</td></tr>
</table>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">数据是物联系统的基础</strong>；搭建物联系统<strong style="color:#c0392b;">首先要实现数据的采集与传输</strong>。</li>
  <li><strong style="color:#c0392b;">物联网数据的四类来源</strong>：<strong style="color:#c0392b;">传感器采集、互联网（API）、用户输入、系统运行自行产生</strong>（前两类是主要来源）。</li>
  <li>物联花盆系统的三种传感器：<strong style="color:#c0392b;">温湿度传感器（温度）、土壤湿度传感器（土壤湿度）、光敏传感器（光照强度）</strong>；天气预报靠<strong style="color:#c0392b;">API</strong>。</li>
  <li>信号类型：<strong style="color:#c0392b;">温湿度传感器输出数字信号</strong>，<strong style="color:#c0392b;">土壤湿度传感器和光敏传感器输出模拟信号</strong>。</li>
  <li>API 调用四要素：<strong style="color:#c0392b;">城市编号、API密钥、URL与参数、status_code==200 表示请求成功</strong>。</li>
  <li><strong style="color:#c0392b;">JSON 与 XML 比较</strong>：XML 更易理解但<strong style="color:#c0392b;">字符多、数据量大</strong>；JSON <strong style="color:#c0392b;">字符少、数据量小</strong>。</li>
  <li><strong style="color:#c0392b;">ujson.loads() 把 JSON 字符串转换为字典结构</strong>；返回数据是<strong style="color:#c0392b;">字典与列表的嵌套</strong>（data 键 → list 列表 → 第0项为当天）。</li>
  <li>平台配置：按<strong style="color:#c0392b;">温度、光照强度、土壤湿度添加3个主题</strong>；接入设备需<strong style="color:#c0392b;">身份认证</strong>；必须记录<strong style="color:#c0392b;">主题ID、设备ID、用户名、密码</strong>。</li>
  <li>三个ID的作用：<strong style="color:#c0392b;">用户名密码用于身份验证连接服务器，主题ID用于识别主题实现发布订阅，设备ID用于识别不同主控板</strong>。</li>
  <li>数据传输核心流程：<strong style="color:#c0392b;">连接无线网络 → 连接物联网服务平台 → 获取传感器数据 → 发送到对应主题 → 暂停30 s</strong>。</li>
  <li><strong style="color:#c0392b;">time.sleep(30) 的作用：留出上报间隔，减轻 MQTT 服务器压力</strong>。</li>
  <li>多数据合并到一个主题用<strong style="color:#c0392b;">字符串拼接+分隔符</strong>，处理时用 <strong style="color:#c0392b;">split()</strong> 分割。</li>
  <li>减少数据冗余用<strong style="color:#c0392b;">临时变量比较法</strong>：数据变化时才上传。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：模拟信号 vs 数字信号</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>模拟信号</th><th>数字信号</th></tr>
  <tr><td>取值特点</td><td><strong>连续变化</strong>的量</td><td>离散的、已编码的数值</td></tr>
  <tr><td>本课传感器</td><td><strong>土壤湿度传感器、光敏传感器</strong></td><td><strong>温湿度传感器</strong></td></tr>
  <tr><td>读取方法</td><td>pin(1).read_analog()</td><td>dht(0).read()</td></tr>
  <tr><td>提示</td><td colspan="2">当前主流主控板的每个引脚<strong>都能读取模拟和数字信号</strong>，接线时任选3个接口即可</td></tr>
</table>

<h3>易混辨析二：JSON vs XML</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>JSON</th><th>XML</th></tr>
  <tr><td>可读性</td><td>较好</td><td><strong>更容易理解</strong></td></tr>
  <tr><td>体积</td><td><strong>字符数少、数据量小</strong></td><td>字符数多、数据量大</td></tr>
  <tr><td>解析后</td><td>可直接转换为<strong>字典</strong>结构，便于程序取值</td><td>需专门的解析方法</td></tr>
  <tr><td>物联网中</td><td>更常用（省流量、省带宽）</td><td>相对少用</td></tr>
</table>

<h3>易混辨析三：主题ID vs 设备ID vs 用户名密码</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>标识</th><th>识别的对象</th><th>作用</th></tr>
  <tr><td><strong>用户名、密码</strong></td><td>接入者的<strong>身份</strong></td><td>身份验证，通过后才允许连接 MQTT 服务器</td></tr>
  <tr><td><strong>主题ID</strong></td><td><strong>数据的“信箱”</strong></td><td>识别对应主题，实现发布和订阅</td></tr>
  <tr><td><strong>设备ID</strong></td><td><strong>具体哪一块主控板</strong></td><td>区分不同的采集终端；第18课分组分析时按 clientId 分组正是用它</td></tr>
</table>
<p><strong>易错提醒：</strong>多个设备有多个设备ID、用户名和密码，<strong>不能混用</strong>，否则会验证失败。</p>

<h3>易混辨析四：本地 MQTT 服务器 vs 在线 MQTT 服务器</h3>
<ul>
  <li><strong>覆盖范围</strong>：本地只能局域网访问；在线可公网远程访问（在线胜）。</li>
  <li><strong>便捷性</strong>：本地需自建但课堂内不依赖外网；在线注册即用但依赖网络（各有优势）。</li>
  <li><strong>数据安全性</strong>：本地数据自主可控（本地胜）；在线数据在第三方平台，需关注隐私。</li>
</ul>

<h3>难点解析：为什么要“数据变化时才上传”？</h3>
<p>温度、土壤湿度等环境数据<strong>变化缓慢</strong>，若每30秒都上传，会产生大量<strong>重复、冗余</strong>的记录，浪费存储空间和网络流量，也增加服务器压力。用<strong>临时变量</strong>保存上一次的值，只有新值与它<strong>不同</strong>时才发布并更新临时变量，就能大幅减少无效数据。</p>

<h3>难点解析：多个数据挤在一个主题怎么办？</h3>
<p>做法：发送前<strong>拼接成一个字符串</strong>并用分隔符隔开，如 <code>"20-1500-500"</code>；接收／处理时用 <strong>split("-")</strong> 切成列表，再按顺序取出温度、光照强度、湿度。<strong>关键是发送端和接收端必须约定好顺序和分隔符</strong>。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>三传感器口诀</strong>：<strong>温湿测空气、土壤测水分、光敏测亮度</strong>。</li>
  <li><strong>流程口诀</strong>：<strong>连网 → 连台 → 读数 → 发送 → 等待</strong>。</li>
  <li><strong>三ID口诀</strong>：<strong>用户名密码认“人”，主题ID认“信箱”，设备ID认“板子”</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>结合身边的物联网案例，说一说物联网的数据来源有哪些。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>传感器采集的数据</strong>：这是最主要的来源，如物联花盆用温湿度传感器、土壤湿度传感器、光敏传感器采集环境数据，共享单车用位置传感器采集位置数据。</li>
  <li><strong>互联网中的数据</strong>：通过 API 调用公共数据，如调用天气预报 API 获取当地天气数据。</li>
  <li><strong>用户输入的数据</strong>：如用户在应用软件中设置的参数、手动录入的信息。</li>
  <li><strong>物联系统运行过程中自行产生的数据</strong>：如设备的运行日志、状态记录等。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>在物联花盆系统中，环境数据变化缓慢。为了减少数据冗余，希望只有在数据发生变化时才上传，应该怎样实现？为什么每次上报还要加 time.sleep(30)？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>在程序中添加<strong>临时变量</strong>，用来保存上一次上传的数据值；</li>
  <li>每次读取传感器后，把<strong>新读取的数据与临时变量比较</strong>；</li>
  <li>若<strong>不同</strong>，说明数据发生了变化，则上传新数据，并把临时变量<strong>更新</strong>为新读取的值；若<strong>相同</strong>，说明没有变化，无须上传；</li>
  <li>time.sleep(30) 的作用是让每次上报之间留出<strong>时间间隔</strong>，避免频繁上传，<strong>减轻 MQTT 服务器的压力</strong>，同时也减少不必要的数据存储和网络消耗。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>请从便捷性、覆盖范围、数据安全性三个角度，比较本地 MQTT 服务器和在线 MQTT 服务器的优缺点。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>覆盖范围</strong>：本地 MQTT 服务器一般只能在<strong>同一局域网</strong>内访问，范围有限；在线 MQTT 服务器一般可以通过<strong>公网远程访问</strong>，覆盖范围广。</li>
  <li><strong>便捷性</strong>：本地服务器需要自己搭建和配置，但在课堂或家庭环境中使用方便、不依赖外网；在线服务器注册后即可使用，无须自建，但必须联网且依赖平台账号。</li>
  <li><strong>数据安全性</strong>：本地服务器的数据保存在本地，<strong>自主可控</strong>，隐私性较好；在线服务器的数据存放在第三方平台，存在隐私和账号安全方面的风险。</li>
  <li><strong>结论</strong>：应根据实际需求选择——需要远程访问、长期存储和后续分析时可选在线服务器；对数据隐私要求高、只在局域网内使用时可选本地服务器。</li>
</ol>
'''
            },
            {
                "id": "L18",
                "title": "第18课 数据分析与处理",
                "knowledge": '''
<h3>一、为什么要分析处理数据</h3>
<p>物联网服务平台只是把数据<strong>汇集</strong>在一起，而数据往往需要<strong>被加工和处理之后才能产生价值</strong>。</p>

<h3>二、常见的数据处理工具</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>阶段</th><th>代表工具</th></tr>
  <tr><td>早期（传统工具）</td><td><strong>算盘</strong>、机械式计算机（<strong>差分机</strong>）、<strong>计算器</strong></td></tr>
  <tr><td>现代（计算机工具）</td><td><strong>电子计算机</strong>；电子表格软件（如《WPS 表格》）；专用数据分析软件（<strong>FineBI、Hadoop</strong>）</td></tr>
  <tr><td>编程工具</td><td>Python 中的 <strong>pandas、numpy</strong> 等数据处理模块</td></tr>
</table>
<p><strong>电子计算机的意义：</strong>与算盘、滑尺等只能实现单一功能的传统工具不同，电子计算机通过<strong>“存储程序、程序执行”</strong>的模式，展现了<strong>通用性和自动化</strong>的优势。</p>
<p><strong>处理数据的两种方式：</strong>①使用常见的数据处理工具（如电子表格软件）；②<strong>借助编程工具</strong>处理数据。</p>
<p><em>安装方法：在命令提示符中输入 pip install pandas 和 pip install numpy。</em></p>

<h3>三、从物联网服务平台获取数据（两种方式）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>方式</th><th>操作步骤</th><th>适用场景</th></tr>
  <tr><td><strong>以数据文件形式下载</strong></td><td>①登录服务平台；②进入相应的<strong>主题管理页面</strong>；③在<strong>查看详情</strong>页面点击下载</td><td>用<strong>电子表格软件</strong>处理，操作直观</td></tr>
  <tr><td><strong>通过 API 调用</strong></td><td>①<strong>参阅说明文档</strong>；②确定 API 的 <strong>URL</strong>；③传入相关参数后<strong>发起网络请求</strong>；④获取并处理返回数据</td><td>可实现<strong>自动获取</strong>，便于编程处理</td></tr>
</table>
<p><strong>通过 API 调用数据的主要代码：</strong></p>
<pre>import requests
user  = "填写物联网服务平台账号"
psd   = "填写密码"
topic = "填写主题ID"
res = requests.get("填写物联网服务平台接口网址" + "/?user=" + user + "&psd=" + psd + "&topic=" + topic)
if res.status_code == 200:      # 200 为 http 请求成功的响应值
    print(res.text)</pre>
<p><em>注意：不同在线 MQTT 服务器的 API 使用方法有差异，<strong>使用前必须参阅相关说明文档</strong>。</em></p>

<h3>四、数据整理与常见异常处理</h3>
<p><strong>1. 数据整理：</strong>把从 API 获取的数据整理并转换为适合编程处理的格式，如 <strong>DataFrame</strong> 类型。</p>
<pre>data = json.loads(res.text)              # 解析返回数据
df = pd.DataFrame(data["result"])        # 整理为 DataFrame 格式</pre>
<p><strong>2. 原始数据常见的三类问题及处理方法（必背）：</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>问题</th><th>含义</th><th>处理方法</th></tr>
  <tr><td><strong>数据缺失</strong></td><td>有些数据没有被记录下来，形成空的字段</td><td>根据实际情况处理，如<strong>填充前后数据的平均值</strong></td></tr>
  <tr><td><strong>数据重复</strong></td><td>同样的数据被记录了多次</td><td>完全重复的可<strong>删除其中一条</strong>；若重复记录互有缺失，需<strong>补全后保留较完整</strong>的记录</td></tr>
  <tr><td><strong>数据格式错误</strong></td><td><strong>单位不一致、数据类型不一致</strong></td><td>统一单位与类型。如身高数据大多是2以下小数，出现三位数说明单位不一致；编号大多用阿拉伯数字，个别用中文数字说明类型不一致</td></tr>
</table>

<h3>五、用 pandas 分析物联花盆数据（四个实例）</h3>
<p><strong>① 数据整理 → DataFrame</strong>（见上）。</p>
<p><strong>② 最高温度与最低温度——排序（sort_values）</strong></p>
<pre>df1 = df.sort_values("valueMsg")          # 对温度数值所在列进行升序排序
print("最高温度:", df1.tail(1))            # 获取最后一行（即最大值）
print("最低温度:", df1.head(1))            # 获取第一行（即最小值）</pre>
<p><strong>③ 光照强度与光照时间——筛选</strong></p>
<pre>df_c  = df2[df2["clientId"] == "光照主题ID"]      # 按设备 clientId 筛选
light = df_c[df_c["valueMsg"] >= 1000]           # 再筛选光照强度≥1000 的数据
print(light)</pre>
<p><em>pandas 支持多条件筛选：用 <strong>&</strong> 表示“与”，用 <strong>|</strong> 表示“或”。</em></p>
<p><strong>④ 土壤湿度——分组求平均（groupby + mean）</strong></p>
<pre>mean = df3.groupby("clientId")["valueMsg"].mean()   # 按设备ID分组后求各组平均值
print(mean)</pre>

<h3>六、常用的数据分析方法（必背三种）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>方法</th><th>含义</th><th>本项目中的例子</th></tr>
  <tr><td><strong>统计分析法</strong></td><td>通过求一组数据的<strong>最大值、最小值、平均值</strong>等方式进行分析处理</td><td>对温度数据求最高温度和最低温度</td></tr>
  <tr><td><strong>对比分析法</strong></td><td>通过对<strong>不同数据的对比</strong>分析其异同</td><td>对不同区域的温度（或二氧化碳浓度）数据进行对比</td></tr>
  <tr><td><strong>分组分析法</strong></td><td>将数据<strong>根据某个条件分成若干组</strong>，再对数据进行统计和对比分析</td><td>先根据设备ID（clientId）分组，再求每组土壤湿度平均值</td></tr>
</table>

<h3>七、编程处理数据的优势</h3>
<p>虽然电子表格软件也可以进行数据分析处理，但通过<strong>编程能高效处理大量数据</strong>，并实现<strong>更为直观的数据可视化</strong>，还便于<strong>自动化、重复执行</strong>。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">物联网服务平台只负责汇集数据，数据要经过加工处理才能产生价值</strong>。</li>
  <li>数据处理工具演变：<strong style="color:#c0392b;">算盘 → 机械式计算机（差分机）→ 计算器 → 电子计算机</strong>；电子计算机的优势在于<strong style="color:#c0392b;">“存储程序、程序执行”带来的通用性和自动化</strong>。</li>
  <li>常见工具：电子表格软件（<strong style="color:#c0392b;">WPS表格</strong>）、专用软件（<strong style="color:#c0392b;">FineBI、Hadoop</strong>）、编程模块（<strong style="color:#c0392b;">pandas、numpy</strong>）。</li>
  <li><strong style="color:#c0392b;">从平台获取数据的两种方式</strong>：<strong style="color:#c0392b;">以数据文件形式下载</strong>、<strong style="color:#c0392b;">通过 API 调用</strong>。</li>
  <li>下载步骤：<strong style="color:#c0392b;">登录平台 → 进入主题管理页面 → 查看详情页点击下载</strong>。</li>
  <li>API 调用步骤：<strong style="color:#c0392b;">参阅说明文档 → 确定URL → 传入参数发起请求 → 调用数据</strong>；<strong style="color:#c0392b;">status_code == 200 表示请求成功</strong>。</li>
  <li><strong style="color:#c0392b;">DataFrame</strong> 是 pandas 中适合编程处理的表格型数据格式，用 <strong style="color:#c0392b;">pd.DataFrame()</strong> 创建。</li>
  <li>关键方法：<strong style="color:#c0392b;">sort_values() 排序、head(1) 取第一行（最小）、tail(1) 取最后一行（最大）、groupby() 分组、mean() 求平均</strong>。</li>
  <li>筛选多条件：<strong style="color:#c0392b;">& 表示“与”，| 表示“或”</strong>。</li>
  <li><strong style="color:#c0392b;">三种数据分析方法</strong>：<strong style="color:#c0392b;">统计分析法、对比分析法、分组分析法</strong>——最高频考点，要能举例。</li>
  <li><strong style="color:#c0392b;">数据异常三类</strong>：<strong style="color:#c0392b;">数据缺失、数据重复、数据格式错误（单位不一致、类型不一致）</strong>及其处理方法。</li>
  <li>编程处理数据相比电子表格的优势：<strong style="color:#c0392b;">高效处理大量数据、可自动化重复执行、可视化更直观</strong>。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：三种数据分析方法</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>方法</th><th>关键动作</th><th>判断口诀</th><th>典型函数</th></tr>
  <tr><td><strong>统计分析法</strong></td><td>求最大值、最小值、平均值等</td><td>看到“<strong>最高／最低／平均／总数</strong>”</td><td>sort_values + head/tail、mean()</td></tr>
  <tr><td><strong>对比分析法</strong></td><td>把不同对象的数据放在一起比较异同</td><td>看到“<strong>比较／哪个更…／异同</strong>”</td><td>并列展示、绘图对比</td></tr>
  <tr><td><strong>分组分析法</strong></td><td><strong>先分组，再统计或对比</strong></td><td>看到“<strong>按…分别／每个…的</strong>”</td><td>groupby() + mean()</td></tr>
</table>
<p><strong>易错点：</strong>分组分析法常与统计分析法<strong>结合使用</strong>（先 groupby 再 mean），但题目若强调“按设备／区域<strong>分别</strong>求”，答案应写<strong>分组分析法</strong>。</p>

<h3>易混辨析二：head() vs tail()（升序排序后）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>函数</th><th>取的位置</th><th>升序排序后对应</th></tr>
  <tr><td>head(1)</td><td>第一行</td><td><strong>最小值</strong>（最低温度）</td></tr>
  <tr><td>tail(1)</td><td>最后一行</td><td><strong>最大值</strong>（最高温度）</td></tr>
</table>
<p><strong>易错提醒：</strong>“head 是头 = 最高温度”是<strong>错误</strong>联想。sort_values 默认<strong>升序</strong>，所以头部是最小值。</p>

<h3>易混辨析三：数据文件下载 vs API 调用</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>数据文件下载</th><th>API 调用</th></tr>
  <tr><td>操作方式</td><td>手动点击下载</td><td>编程自动获取</td></tr>
  <tr><td>后续处理</td><td>常用电子表格软件</td><td>用 pandas 等编程处理</td></tr>
  <tr><td>优点</td><td>直观、简单、门槛低</td><td>可<strong>自动化、可重复</strong>，适合大量／持续更新的数据</td></tr>
  <tr><td>不足</td><td>每次都要手动操作，难以自动更新</td><td>需参阅文档、编写代码，不同平台差异大</td></tr>
</table>

<h3>易混辨析四：结构化数据 vs 非结构化数据（拓展）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>结构化数据</th><th>非结构化数据</th></tr>
  <tr><td>组织形式</td><td>有固定的<strong>行列／字段</strong>结构，可用表格表示</td><td>没有固定结构</td></tr>
  <tr><td>举例</td><td>物联网平台导出的温度记录表、DataFrame、电子表格</td><td>图片、音频、视频、自由文本</td></tr>
  <tr><td>处理方式</td><td>可直接用 pandas、电子表格软件统计分析</td><td>通常要先<strong>提取特征</strong>或转换后才能分析（如人脸图像先提特征点）</td></tr>
</table>
<p>本课处理的物联环境数据（clientId、valueMsg、createdAt 等字段）属于<strong>结构化数据</strong>，所以能直接转成 DataFrame 分析。</p>

<h3>难点解析：为什么要先 groupby("clientId")？</h3>
<p>因为从服务器取回的土壤湿度表中，<strong>混合了所有花盆（所有设备）</strong>采集的数据。如果直接求平均，得到的是“所有花盆的总平均”，看不出各个位置的差异。先按 <strong>clientId（设备ID）分组</strong>，再用 ["valueMsg"] 选中数值列、用 mean() 求平均，才能得到<strong>每个花盆各自的平均湿度</strong>，从而比较哪个位置更适合植物生长。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>三分析法口诀</strong>：<strong>统（算数值）、对（比异同）、分（先分组）</strong>。</li>
  <li><strong>数据清洗口诀</strong>：<strong>缺（补平均）、重（删或补全）、错（统一单位类型）</strong>。</li>
  <li><strong>排序口诀</strong>：<strong>升序排，头最小，尾最大</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>常用的数据分析方法有哪几种？请结合物联花盆系统各举一例。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>统计分析法</strong>：通过求一组数据的最大值、最小值、平均值等方式进行分析处理。例如对采集到的温度数据排序，求出最高温度和最低温度。</li>
  <li><strong>对比分析法</strong>：通过对不同数据的对比来分析其异同。例如把不同区域花盆的温度或土壤湿度数据进行对比，找出环境差异。</li>
  <li><strong>分组分析法</strong>：将数据根据某个条件分成若干组，再对数据进行统计和对比分析。例如先根据设备ID（clientId）对土壤湿度数据分组，再用 mean() 求出每个花盆的平均湿度。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>从物联网服务平台获取数据有哪两种方式？各自的操作要点是什么？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>以数据文件形式下载</strong>：登录服务平台 → 进入相应的主题管理页面 → 在查看详情页面点击下载；下载后可用电子表格软件处理，操作直观简单。</li>
  <li><strong>通过 API 调用</strong>：先参阅平台的说明文档 → 确定 API 的 URL → 传入用户名、密码、主题ID 等参数后发起网络请求 → 判断 status_code 是否为 200（成功）→ 获取并解析返回的数据。</li>
  <li>注意：不同在线 MQTT 服务器的 API 使用方法有差异，使用前必须查阅相关说明文档。</li>
  <li>API 方式的优势是可以<strong>自动获取</strong>数据，便于编程处理和重复执行。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>物联系统采集到的原始数据可能存在哪些问题？应如何处理？为什么说用编程处理数据比只用电子表格软件更好？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>数据缺失</strong>：有些数据没有被记录，形成空字段；可根据实际情况处理，如用前后数据的平均值填充。</li>
  <li><strong>数据重复</strong>：同样的数据被记录多次；完全重复的可删除其中一条，若重复记录互有缺失则补全后保留较完整的记录。</li>
  <li><strong>数据格式错误</strong>：主要是单位不一致、数据类型不一致；需要统一单位和数据类型。</li>
  <li><strong>编程处理的优势</strong>：能<strong>高效处理大量数据</strong>，可以自动、重复地执行同一套处理流程，并能借助绘图库实现<strong>更为直观的数据可视化</strong>；电子表格软件虽然直观，但面对海量数据时效率低、难以自动化。</li>
</ol>
'''
            },
            {
                "id": "L19",
                "title": "第19课 数据呈现可视化",
                "knowledge": '''
<h3>一、为什么需要数据可视化</h3>
<p>只对数据作统计分析，虽然能粗略了解数据特征，但<strong>不能充分利用其价值</strong>。例如从最大值、最小值和平均值很难看出温度<strong>变化的趋势</strong>；大量数据也让人觉得枯燥、难懂。这时就需要借助<strong>数据可视化</strong>直观地呈现数据。</p>
<p><strong>定义：</strong>数据可视化是一种把<strong>数据转化为图表、图形</strong>的手段，能把大量数据转化为<strong>易于理解的图像</strong>。</p>

<h3>二、数据可视化的作用（必背）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>作用</th><th>说明</th><th>举例</th></tr>
  <tr><td><strong>1. 发现数据异常</strong></td><td>更容易<strong>识别并定位</strong>数据中存在的异常</td><td>对温度数据可视化后，直观发现13:00左右数据异常</td></tr>
  <tr><td><strong>2. 了解整体概况</strong></td><td>方便、直观地了解物联系统的<strong>整体概况</strong>，提供全局视图</td><td>智慧社区数据监测大屏，帮助工作人员及时了解社区概况</td></tr>
  <tr><td><strong>3. 发现趋势变化</strong></td><td>展示历史数据，帮助理解<strong>数据变化情况</strong>，助力<strong>预测未来趋势</strong></td><td>航班软件显示近期起降时间，可判断该航班大概率会晚点</td></tr>
  <tr><td><strong>4. 方便交流共享、支持分析决策</strong></td><td>把复杂数据和分析结果转化为易理解、吸引人的形式，让决策者更快更准地理解数据含义</td><td>各类数据报告、图表汇报</td></tr>
</table>
<p><em>此外还能强化记忆和理解、促进深入探索（交互式可视化）、激发创新思维。</em></p>

<h3>三、常见的数据可视化方式（必背）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>方式</th><th>用途</th><th>常见图表</th><th>举例</th></tr>
  <tr><td><strong>趋势可视化</strong></td><td>描绘数据<strong>随时间的变化趋势</strong></td><td><strong>折线图、柱形图</strong>（像素图）</td><td>一天中的温度变化趋势图</td></tr>
  <tr><td><strong>比例可视化</strong></td><td>显示不同部分<strong>所占整体的比例关系</strong></td><td><strong>饼图、环形图</strong></td><td>各类天气天数占比</td></tr>
  <tr><td><strong>分布可视化</strong></td><td>展示数据的<strong>分布规律</strong>；与地图结合可表示<strong>地理位置分布</strong></td><td><strong>散点图</strong>、散点图+地图</td><td>共享单车App查询附近空闲单车位置</td></tr>
  <tr><td><strong>标签云</strong></td><td>直观展示一段<strong>文本数据中的高频词</strong>，<strong>词频越高字体越大</strong></td><td>标签云</td><td>不读全文即可大致了解课文重点内容</td></tr>
</table>
<p><strong>中文文本生成标签云的一般步骤：</strong><strong>分词 → 词频统计 → 生成标签云</strong>。分词是根据中文词典并结合上下文语境对文本进行词语分割；词频统计是通过算法统计不同词语出现的频率。</p>

<h3>四、实现数据可视化的工具</h3>
<ul>
  <li>很多<strong>物联网服务平台</strong>自带数据可视化功能；</li>
  <li><strong>电子表格软件</strong>（如《WPS 表格》）也可以生成图表；</li>
  <li>编程处理数据时可利用<strong>绘图库</strong>：<strong>matplotlib</strong> 是 Python 中常用的图表生成模块；<strong>ECharts</strong> 是常用在网页上的数据可视化图表库。</li>
</ul>
<p><strong>重要前提：在对数据进行可视化前，要先明确数据可视化的目的。</strong></p>

<h3>五、用 Python 绘制温度变化趋势图（三步）</h3>
<p><strong>1. 准备数据：</strong>时间数据作为横坐标保存到变量 X，对应温度数据作为纵坐标保存到变量 Y。</p>
<p><strong>2. 设置画布和标题：</strong>图表大小由画布决定，用 <strong>plt.figure(figsize=(宽,高))</strong> 指定；用 <strong>plt.title()</strong> 设置标题。</p>
<p><strong>3. 绘制图表并显示：</strong>不同类型图表的绘图函数不同。</p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>函数</th><th>作用</th></tr>
  <tr><td><strong>plt.plot()</strong></td><td>绘制<strong>折线图</strong></td></tr>
  <tr><td><strong>plt.scatter()</strong></td><td>绘制<strong>散点图</strong></td></tr>
  <tr><td><strong>plt.bar()</strong></td><td>绘制<strong>柱形图</strong></td></tr>
  <tr><td><strong>plt.show()</strong></td><td>把图表<strong>显示</strong>出来</td></tr>
</table>
<p><strong>主要代码：</strong></p>
<pre>import matplotlib.pyplot as plt        # 导入绘图模块
X = df["createdAt"]                    # 以 createdAt 列为横坐标数据
Y = df["valueMsg"]                     # 以 valueMsg 列为纵坐标数据
plt.figure(figsize=(8, 6))             # 设置画布尺寸
plt.title("Temperature")               # 设置图表标题
plt.plot(X, Y)                         # 绘制折线图
plt.show()                             # 显示图表</pre>
<p><strong>补充要点：</strong></p>
<ul>
  <li><strong>figsize</strong> 接收一个含两个元素的元组，第一个是<strong>宽度</strong>，第二个是<strong>高度</strong>，单位是<strong>英寸</strong>；默认分辨率约 <strong>100 像素/英寸（DPI）</strong>，因此 figsize=(8,6) 对应 <strong>800×600 像素</strong>。</li>
  <li>若 matplotlib 要<strong>显示中文</strong>，需先下载中文字库文件（如 SimHei.ttf）放到项目目录，并添加：<br>
  <code>from matplotlib import rcParams</code><br><code>rcParams["font.sans-serif"] = ["SimHei"]</code></li>
  <li>还可通过 xtick、ytick 设置坐标轴格式，通过 plot() 的 <strong>color</strong> 参数设置线条颜色，实现个性化图表。</li>
</ul>

<h3>六、选图原则</h3>
<p>要<strong>根据实际要展示的数据关系</strong>选择合适的可视化图表：看<strong>随时间的变化</strong>用折线图；看<strong>各类之间的多少比较</strong>用柱形图；看<strong>占整体的比例</strong>用饼图／环形图；看<strong>分布</strong>用散点图（可与地图结合）；看<strong>文本高频词</strong>用标签云。</p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">数据可视化的定义</strong>：把<strong style="color:#c0392b;">数据转化为图表、图形</strong>的手段。</li>
  <li><strong style="color:#c0392b;">数据可视化的作用（三大核心）</strong>：<strong style="color:#c0392b;">发现数据异常、了解整体概况、发现趋势变化</strong>；此外还有<strong style="color:#c0392b;">方便交流共享、支持分析决策</strong>。</li>
  <li><strong style="color:#c0392b;">四种可视化方式与对应图表</strong>：趋势可视化—<strong style="color:#c0392b;">折线图、柱形图</strong>；比例可视化—<strong style="color:#c0392b;">饼图、环形图</strong>；分布可视化—<strong style="color:#c0392b;">散点图（+地图）</strong>；<strong style="color:#c0392b;">标签云</strong>—文本高频词。</li>
  <li><strong style="color:#c0392b;">标签云：词频越高，字体越大</strong>；制作步骤<strong style="color:#c0392b;">分词 → 词频统计 → 生成标签云</strong>。</li>
  <li>绘图工具：<strong style="color:#c0392b;">matplotlib（Python 常用图表生成模块）</strong>、<strong style="color:#c0392b;">ECharts（常用在网页上的图表库）</strong>。</li>
  <li><strong style="color:#c0392b;">绘图三步</strong>：<strong style="color:#c0392b;">准备数据 → 设置画布和标题 → 绘制图表并显示</strong>。</li>
  <li>函数对应：<strong style="color:#c0392b;">plt.plot() 折线图、plt.scatter() 散点图、plt.bar() 柱形图、plt.title() 标题、plt.figure(figsize=) 画布、plt.show() 显示</strong>——高频填空。</li>
  <li><strong style="color:#c0392b;">figsize 单位是英寸</strong>，元组第一个是宽、第二个是高；默认 <strong style="color:#c0392b;">100 DPI</strong>，figsize=(8,6) 即 <strong style="color:#c0392b;">800×600 像素</strong>。</li>
  <li>matplotlib 显示中文需要<strong style="color:#c0392b;">中文字库（如 SimHei）并设置 rcParams</strong>。</li>
  <li><strong style="color:#c0392b;">可视化前要先明确数据可视化的目的</strong>；要根据<strong style="color:#c0392b;">数据关系</strong>选择合适图表。</li>
  <li>温度随时间变化 → 用<strong style="color:#c0392b;">折线图</strong>（最常考的选图判断）。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：四种可视化方式如何选</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>要展示的关系</th><th>选用方式</th><th>图表</th><th>题干关键词</th></tr>
  <tr><td>随<strong>时间</strong>怎么变</td><td>趋势可视化</td><td>折线图（首选）、柱形图</td><td>“变化趋势”“一天中”“近一周”</td></tr>
  <tr><td>各部分<strong>占整体</strong>多少</td><td>比例可视化</td><td>饼图、环形图</td><td>“占比”“百分比”“构成”</td></tr>
  <tr><td>数据<strong>散布</strong>在哪</td><td>分布可视化</td><td>散点图、散点图+地图</td><td>“分布”“位置”“附近”</td></tr>
  <tr><td>文本中<strong>哪些词多</strong></td><td>标签云</td><td>标签云</td><td>“高频词”“关键词”“主题”</td></tr>
</table>
<p><strong>易错点：</strong>折线图与柱形图都能表现趋势，但<strong>折线图更强调连续变化</strong>（如温度曲线），<strong>柱形图更强调各项数值的比较</strong>（如各区域平均湿度对比）。</p>

<h3>易混辨析二：matplotlib 三个函数别混</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>函数</th><th>管什么</th><th>典型写法</th></tr>
  <tr><td>plt.figure(figsize=(8,6))</td><td>管<strong>画布大小</strong></td><td>先设置，后绘图</td></tr>
  <tr><td>plt.title("Temperature")</td><td>管<strong>图表标题</strong></td><td>字符串参数</td></tr>
  <tr><td>plt.plot(X, Y)</td><td>管<strong>画什么图</strong>（折线）</td><td>传入横、纵坐标数据</td></tr>
  <tr><td>plt.show()</td><td>管<strong>显示出来</strong></td><td>最后一步，不写就看不到图</td></tr>
</table>

<h3>易混辨析三：数据分析 vs 数据可视化</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>数据分析（第18课）</th><th>数据可视化（第19课）</th></tr>
  <tr><td>输出形式</td><td>数值结果（最大值、平均值等）</td><td>图表、图形</td></tr>
  <tr><td>擅长</td><td>精确的量化结论</td><td>直观呈现<strong>趋势、异常、比例、分布</strong></td></tr>
  <tr><td>局限</td><td>很难看出“变化趋势”，数据多时枯燥难懂</td><td>不能替代精确计算</td></tr>
  <tr><td>关系</td><td colspan="2">可视化是数据分析处理的<strong>重要内容和延伸</strong>，二者结合才能充分发挥数据价值</td></tr>
</table>

<h3>难点解析：figsize=(8,6) 到底多大？</h3>
<p>figsize 接收一个<strong>元组</strong>，第一个元素是<strong>宽</strong>，第二个是<strong>高</strong>，单位为<strong>英寸</strong>。每英寸对应的像素数由分辨率决定，matplotlib 默认约 <strong>100 DPI</strong>，所以 (8,6) 生成的图形约为 <strong>800×600 像素</strong>。<strong>易错点：不要把 8 和 6 当成像素。</strong></p>

<h3>难点解析：为什么中文会变成方框？</h3>
<p>matplotlib 默认字体不包含中文字符。解决办法：下载中文字库文件（如 SimHei.ttf）放入项目目录，并通过 rcParams["font.sans-serif"] = ["SimHei"] 指定字体。这也是教材代码中标题写成英文 "Temperature" 的原因。</p>

<h3>记忆技巧</h3>
<ul>
  <li><strong>作用口诀</strong>：<strong>找异常、看全局、看趋势、好沟通</strong>。</li>
  <li><strong>选图口诀</strong>：<strong>趋势折线、比例饼图、分布散点、词多云图</strong>。</li>
  <li><strong>函数口诀</strong>：<strong>plot 是线、bar 是柱、scatter 是点、show 才看见</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>数据可视化有哪些作用？请各举一例说明。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>发现数据异常</strong>：通过可视化更容易识别并定位数据中的异常。例如对温度数据作折线图后，可以直观发现13:00左右的数据出现异常。</li>
  <li><strong>了解整体概况</strong>：能方便、直观地了解物联系统的整体情况。例如智慧社区的数据监测大屏，帮助社区工作人员及时掌握社区概况。</li>
  <li><strong>发现趋势变化</strong>：能展示历史数据、帮助理解数据变化并预测未来趋势。例如航班服务软件显示近期起降时间，可以判断该航班近期是否容易晚点。</li>
  <li><strong>方便交流共享、支持分析决策</strong>：把复杂数据和分析结果转化为易于理解的形式，让决策者更快速、准确地理解数据背后的意义。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>常见的数据可视化方式有哪几类？下列情形分别适合用哪种图表，并说明理由。<br>
①展示教室一天中温度的变化；②展示一周中晴、阴、雨天数的占比；③展示附近共享单车的位置；④展示一篇课文中的高频词。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>常见方式包括<strong>趋势可视化、比例可视化、分布可视化</strong>，此外还有<strong>标签云</strong>。</li>
  <li>①用<strong>折线图</strong>（趋势可视化）：温度是随时间连续变化的数据，折线图能清晰描绘变化趋势。</li>
  <li>②用<strong>饼图或环形图</strong>（比例可视化）：需要显示各类天气在整体中所占的比例关系。</li>
  <li>③用<strong>散点图与地图结合</strong>（分布可视化）：能表示数据在地理位置上的分布情况。</li>
  <li>④用<strong>标签云</strong>：能直观展示文本中的高频词，词频越高字体越大，不用读全文也能了解重点内容。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>请简述利用 Python 的 matplotlib 绘制温度变化趋势图的主要步骤及对应函数。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>明确目的</strong>：先确定要展示温度随时间的变化趋势，因此选择折线图。</li>
  <li><strong>准备数据</strong>：把时间数据作为横坐标保存到变量 X（如 df["createdAt"]），把对应的温度数据作为纵坐标保存到变量 Y（如 df["valueMsg"]）。</li>
  <li><strong>设置画布和标题</strong>：用 <strong>plt.figure(figsize=(8,6))</strong> 指定画布大小（单位为英寸，约合800×600像素），用 <strong>plt.title("Temperature")</strong> 设置标题。</li>
  <li><strong>绘制并显示图表</strong>：用 <strong>plt.plot(X, Y)</strong> 绘制折线图（若绘散点图用 plt.scatter()，柱形图用 plt.bar()），最后用 <strong>plt.show()</strong> 把图表显示出来。</li>
  <li>补充：若图表标题或标签需要显示中文，需下载 SimHei 等中文字库并设置 rcParams["font.sans-serif"]。</li>
</ol>
'''
            },
            {
                "id": "L20",
                "title": "第20课 反馈控制有算法",
                "knowledge": '''
<h3>一、数据、算法、反馈、执行器的关系（必背）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>要素</th><th>含义／定位</th></tr>
  <tr><td><strong>数据</strong></td><td><strong>设计算法的依据</strong></td></tr>
  <tr><td><strong>算法</strong></td><td>根据<strong>一定的规则</strong>产生的结果（作出决策）</td></tr>
  <tr><td><strong>反馈</strong></td><td>物联系统<strong>作用于外部环境</strong>的过程</td></tr>
  <tr><td><strong>执行器</strong></td><td><strong>反馈的载体</strong>，都是<strong>输出设备</strong></td></tr>
</table>
<p><strong>物联系统中的反馈与控制是基于算法实现的。</strong>反馈不局限于控制电机、舵机运动，<strong>点亮指示灯、让蜂鸣器发声也属于反馈</strong>。</p>

<h3>二、根据数据分析结果设计算法</h3>
<p>物联花盆系统要实现<strong>自动灌溉</strong>，需要在对<strong>温度、土壤湿度、光照强度和天气预报</strong>数据分析的基础上设计算法。可以通过<strong>设计表格</strong>来规划灌溉条件。</p>
<p><strong>第一步：确定阈值。</strong>根据前面数据分析中获得的土壤在干燥、适中、湿润时的传感器数据（取平均值），确定合适的土壤湿度<strong>上限值和下限值</strong>。教材示例：</p>
<pre>hum_max = 3000      # 土壤湿度上限值
hum_min = 2000      # 土壤湿度下限值</pre>
<p><strong>第二步：列举条件与决策（初步）。</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>条件</th><th>决策</th></tr>
  <tr><td>土壤湿度大于上限值</td><td>不灌溉</td></tr>
  <tr><td>土壤湿度小于下限值</td><td>灌溉</td></tr>
  <tr><td>土壤湿度介于上下限值之间，且天气预报下雨</td><td>不灌溉</td></tr>
  <tr><td>土壤湿度介于上下限值之间，且天气预报不下雨</td><td>灌溉</td></tr>
  <tr><td>土壤湿度介于上下限值之间，且光照强度大</td><td>提高下限值</td></tr>
</table>
<p><strong>第三步：整理优化（以土壤湿度为首要条件分类）。</strong></p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>条件（土壤湿度）</th><th>附加条件</th><th>决策</th></tr>
  <tr><td>大于上限值</td><td>—</td><td><strong>不灌溉</strong></td></tr>
  <tr><td rowspan="4">大于下限值且小于等于上限值</td><td>天气预报下雨</td><td><strong>不灌溉</strong></td></tr>
  <tr><td>天气预报不下雨</td><td><strong>灌溉</strong></td></tr>
  <tr><td>光照强度大</td><td><strong>提高下限值</strong></td></tr>
  <tr><td>光照强度小</td><td><strong>恢复下限值</strong></td></tr>
  <tr><td>小于下限值</td><td>—</td><td><strong>灌溉</strong></td></tr>
</table>
<p><strong>第四步：形成数据决策程序（使用分支结构嵌套）。</strong></p>
<pre>if hum &gt; hum_max:                       # 土壤湿度大于上限值
    oled.print("不灌溉")
elif hum &gt; hum_min:                     # 介于上下限值之间
    if "雨" in tq[0] or "雨" in tq[1]:   # 天气预报有雨
        oled.print("不灌溉")
    else:
        oled.print("灌溉")
    if lgt &gt; 1200:                      # 光照强度大，提高下限值
        hum_min = 2500
    else:                               # 光照强度小，恢复下限值
        hum_min = 2000
else:                                   # 土壤湿度低于下限值
    oled.print("灌溉")</pre>
<p><em>数据决策是一个<strong>反复判断、执行</strong>的过程，因此这部分代码需要放在<strong>循环结构</strong>中。</em></p>

<h3>三、控制执行器</h3>
<p>物联花盆系统中，<strong>反馈与控制就是“显示土壤湿度情况”和“实现自动灌溉”</strong>，对应的执行器分别是<strong>显示屏</strong>和<strong>直流电机水泵</strong>。</p>
<p><strong>1. 实时显示土壤湿度值：</strong></p>
<pre>oled.print("土壤湿度:" + str(hum))</pre>
<p><strong>2. 实现自动灌溉（水泵接主控板 M1 口，灌溉5 s）：</strong></p>
<pre>M1 = parrot(parrot.M1)      # 将电机连接到 M1 口
M1.speed(100)               # 让连接水泵的电机运转
time.sleep(5)               # 持续 5 s
M1.speed(0)                 # 让电机停止运转</pre>
<p><strong>硬件原理提示：</strong>主控板<strong>引脚只能输出小电流</strong>的电信号，而<strong>直流电机耗电较高</strong>，难以由引脚直接驱动。有些主控板<strong>内置了直流电机驱动芯片</strong>并设有电机输出接口（如 M1、M2），把直流小水泵接到电机输出接口上即可直接驱动。</p>

<h3>四、对系统进行整合</h3>
<p>实现各功能模块并测试后，把所有模块<strong>集成</strong>为一个简易物联灌溉系统。</p>
<p><strong>核心流程（必背顺序）：</strong>连接无线网络 → 连接物联网服务平台 → 获取传感器数据 → 获取 API 数据 → 通过物联网服务平台上传数据 → 判断“是否需要灌溉” → 若“是”则控制水泵灌溉，若“否”则跳过 → 循环。</p>
<p><strong>程序结构技巧：</strong>把主程序代码写在 <strong>while True</strong> 无限循环中，并在最后通过 <strong>time.sleep()</strong> 控制等待时间。<br>
<strong>好处：</strong>让主控板每执行完一次功能后<strong>等待一段时间</strong>再执行，可以<strong>减少数据通信和数据存储</strong>，减轻服务器压力，也降低设备功耗。<br>
<strong>局限：</strong>在任务比较繁杂的场景中，用 time.sleep() 让主控板“干等”会<strong>造成资源浪费</strong>；有些主控板支持<strong>定时器</strong>功能，可以把代码放入定时器框架中定时执行。</p>

<h3>五、系统调试与测试</h3>
<p>项目投入使用前必须进行调试：一方面<strong>对比功能需求进行测试</strong>，另一方面让物联系统<strong>整体运行</strong>，测试是否存在问题。</p>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>测试类型</th><th>测试内容</th></tr>
  <tr><td><strong>硬件检查</strong></td><td>通电前仔细检查所有连线，确保<strong>连接正确</strong>；注意不要接错电源正负极，否则可能导致电路损坏或烧毁；检查传感器、执行器连接是否正确、有无物理损伤</td></tr>
  <tr><td><strong>网络测试</strong></td><td>确保系统内所有设备都能<strong>顺畅连接到网络</strong>，测试设备之间的通信连通性，以及设备与云服务或服务器连接的<strong>稳定性</strong></td></tr>
  <tr><td><strong>动态测试</strong></td><td>通过<strong>模拟实际操作条件</strong>测试系统整体功能，如模拟温度变化、光照强度变化等，测试<strong>触发条件的响应</strong>，确保系统稳定工作并按预期响应</td></tr>
</table>
<p><strong>整合时的注意事项：</strong>硬件方面要考虑<strong>引脚是否够用、供电能力是否充足</strong>；软件方面要考虑<strong>主控板的系统资源和程序结构</strong>（如无限循环可能影响网络通信等功能）。</p>

<h3>六、探索功能扩展（三个方向）</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>扩展方向</th><th>具体做法</th></tr>
  <tr><td><strong>1. 从系统功能上扩展</strong></td><td>①利用<strong>红外热释电传感器</strong>感知是否有人在附近活动，上传数据并分析，了解主人对植物的关心程度；②增加<strong>人工智能摄像头</strong>，自动识别植物种类并设置不同的湿度参数</td></tr>
  <tr><td><strong>2. 从人机交互上扩展</strong></td><td>①编写<strong>网页端程序</strong>，方便查看各个花盆终端的实时数据；②增加<strong>手动灌溉控制按钮</strong>，更灵活地控制灌溉</td></tr>
  <tr><td><strong>3. 从数据处理与可视化上扩展</strong></td><td>在网页端增加<strong>数据图表</strong>，直观分析花盆环境数据，进一步探索环境数据对绿植生长的影响</td></tr>
</table>
<p><em>设计物联系统时还要考虑后续扩展需求：硬件上<strong>预留引脚</strong>连接更多传感器和执行器；软件上设计<strong>合理的程序框架</strong>，方便扩展功能。例如可在土壤湿度过低时用 LED 灯或蜂鸣器发出报警信息。</em></p>
''',
                "exam": '''
<h3>高频考点清单</h3>
<ul>
  <li><strong style="color:#c0392b;">四要素关系（必背）</strong>：<strong style="color:#c0392b;">数据是设计算法的依据；算法是根据一定规则产生的结果；反馈是物联系统作用于外部环境的过程；执行器是反馈的载体</strong>。</li>
  <li><strong style="color:#c0392b;">物联系统中的反馈与控制是基于算法实现的</strong>；<strong style="color:#c0392b;">执行器都是输出设备</strong>，点亮指示灯、蜂鸣器发声也属于反馈。</li>
  <li>物联花盆的反馈与控制具体指：<strong style="color:#c0392b;">显示土壤湿度情况</strong>和<strong style="color:#c0392b;">实现自动灌溉</strong>，对应执行器是<strong style="color:#c0392b;">显示屏</strong>和<strong style="color:#c0392b;">直流电机水泵</strong>。</li>
  <li>设计算法的依据是<strong style="color:#c0392b;">温度、土壤湿度、光照强度和天气预报</strong>数据；先确定土壤湿度的<strong style="color:#c0392b;">上限值与下限值</strong>（教材示例 hum_max=3000、hum_min=2000）。</li>
  <li><strong style="color:#c0392b;">优化后的灌溉条件与决策表</strong>（高频填表）：湿度>上限→<strong style="color:#c0392b;">不灌溉</strong>；湿度<下限→<strong style="color:#c0392b;">灌溉</strong>；介于两者之间时——预报下雨→<strong style="color:#c0392b;">不灌溉</strong>，不下雨→<strong style="color:#c0392b;">灌溉</strong>，光照强→<strong style="color:#c0392b;">提高下限值</strong>，光照弱→<strong style="color:#c0392b;">恢复下限值</strong>。</li>
  <li>整理条件的思路：<strong style="color:#c0392b;">先以土壤湿度作为首要条件分三类，再对天气预报和光照强度分类讨论</strong>；程序使用<strong style="color:#c0392b;">分支结构嵌套</strong>，并放在<strong style="color:#c0392b;">循环结构</strong>中。</li>
  <li>水泵控制代码：<strong style="color:#c0392b;">M1.speed(100) 启动 → time.sleep(5) 灌溉5秒 → M1.speed(0) 停止</strong>。</li>
  <li><strong style="color:#c0392b;">引脚只能输出小电流，直流电机耗电高，不能直接由引脚驱动</strong>；需借助主控板<strong style="color:#c0392b;">内置的直流电机驱动芯片和电机输出接口（M1/M2）</strong>。</li>
  <li>系统核心流程：<strong style="color:#c0392b;">连接无线网络 → 连接物联网服务平台 → 获取传感器数据 → 获取API数据 → 上传数据 → 判断是否需要灌溉 → 控制水泵灌溉</strong>。</li>
  <li><strong style="color:#c0392b;">把主程序放在 while True 中并用 time.sleep() 控制等待时间</strong>，好处是<strong style="color:#c0392b;">减少数据通信和数据存储</strong>。</li>
  <li><strong style="color:#c0392b;">系统调试三方面</strong>：<strong style="color:#c0392b;">硬件检查（连接正确）、网络测试（畅通稳定）、动态测试（模拟功能过程、测试触发条件响应）</strong>。</li>
  <li>功能扩展三方向：<strong style="color:#c0392b;">系统功能、人机交互、数据处理与可视化</strong>。</li>
</ul>
''',
                "difficulty": '''
<h3>易混辨析一：数据、算法、反馈、执行器</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>要素</th><th>一句话定位</th><th>物联花盆中的对应</th></tr>
  <tr><td>数据</td><td>算法的<strong>依据</strong>（原料）</td><td>土壤湿度值、光照强度、天气预报</td></tr>
  <tr><td>算法</td><td>按<strong>规则</strong>作出决策（大脑）</td><td>灌溉条件与决策的分支判断</td></tr>
  <tr><td>反馈</td><td>作用于<strong>外部环境</strong>的过程（行动）</td><td>显示土壤湿度、启动灌溉</td></tr>
  <tr><td>执行器</td><td>反馈的<strong>载体</strong>（手脚）</td><td>显示屏、直流电机水泵</td></tr>
</table>
<p><strong>顺序链条：</strong>数据 → 算法 → 决策 → 反馈 → 执行器动作。</p>

<h3>易混辨析二：反馈控制（闭环） vs 开环控制</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>反馈（闭环）控制</th><th>开环控制</th></tr>
  <tr><td>是否采集并使用结果数据</td><td><strong>是</strong>，把传感器数据送回参与判断</td><td><strong>否</strong>，按固定指令执行</td></tr>
  <tr><td>能否自动适应变化</td><td><strong>能</strong>，环境变了决策也会变</td><td>不能</td></tr>
  <tr><td>本课例子</td><td>根据土壤湿度、天气、光照<strong>判断后再决定</strong>是否灌溉</td><td>不看湿度，每天固定时间浇水5秒</td></tr>
  <tr><td>优缺点</td><td>更节水、更智能，但系统更复杂</td><td>简单可靠，但可能过量或不足灌溉</td></tr>
</table>

<h3>易混辨析三：传感器 vs 执行器</h3>
<table border="1" cellspacing="0" cellpadding="6">
  <tr><th>比较点</th><th>传感器</th><th>执行器</th></tr>
  <tr><td>作用</td><td><strong>采集</strong>环境数据（输入）</td><td>产生<strong>动作</strong>、作用于现实世界（输出）</td></tr>
  <tr><td>属于</td><td>输入设备</td><td><strong>输出设备</strong></td></tr>
  <tr><td>本册举例</td><td>温湿度、土壤湿度、光敏、按键、红外热释电传感器</td><td>舵机、水泵电机、显示屏、LED灯、蜂鸣器</td></tr>
  <tr><td>所属模块</td><td>环境感知模块</td><td>执行模块</td></tr>
</table>

<h3>易混辨析四：人工控制 vs 自动控制（在本课的体现）</h3>
<ul>
  <li>物联花盆的<strong>自动灌溉</strong>：系统根据传感器数据和预设算法自行判断并启动水泵，属于<strong>自动控制</strong>。</li>
  <li>在服务平台上点击按钮<strong>手动控制灌溉</strong>（第16课服务平台模块功能、第20课人机交互扩展），属于<strong>人工控制</strong>。</li>
</ul>

<h3>难点解析：为什么条件要“整理优化”？</h3>
<p>初步列举的五个条件<strong>互相交叉</strong>（都与土壤湿度有关），直接写程序会混乱、重复甚至冲突。优化的思路是：<strong>先以土壤湿度这一首要条件把情况分成三类</strong>（大于上限、介于上下限之间、小于下限），<strong>再在“介于之间”这一类内部</strong>对天气预报和光照强度分别讨论。这样条件<strong>互不重叠、覆盖完整</strong>，正好对应 <strong>if / elif / else 的分支嵌套结构</strong>。</p>

<h3>难点解析：“提高下限值”是什么意思？</h3>
<p>光照强度大时，水分蒸发快、植物需水多，因此把土壤湿度的<strong>下限值调高</strong>（如从2000提高到2500），意味着<strong>更容易触发灌溉</strong>，让土壤保持更湿润；光照弱时再<strong>恢复</strong>原来的下限值。这体现了算法可以<strong>根据环境动态调整参数</strong>，而不是死板地用固定阈值。</p>

<h3>难点解析：while True + time.sleep() 的两面性</h3>
<ul>
  <li><strong>好处：</strong>每次执行完等待一段时间再执行，<strong>减少数据通信和数据存储</strong>，减轻服务器压力，节约设备电量。</li>
  <li><strong>问题：</strong>主控板在 sleep 期间什么都不做，任务繁杂时会<strong>浪费系统资源</strong>；无限循环还可能影响网络通信等功能。</li>
  <li><strong>改进：</strong>使用主控板支持的<strong>定时器</strong>功能，把代码放入定时器框架中定时执行。</li>
</ul>

<h3>记忆技巧</h3>
<ul>
  <li><strong>四要素口诀</strong>：<strong>数据是料，算法是脑，反馈是行，执行是手</strong>。</li>
  <li><strong>灌溉决策口诀</strong>：<strong>湿了不浇，干了就浇，不干不湿看天看光</strong>。</li>
  <li><strong>调试口诀</strong>：<strong>先查线（硬件），再通网（网络），后模拟（动态）</strong>。</li>
  <li><strong>扩展口诀</strong>：<strong>加功能、改交互、强可视</strong>。</li>
</ul>
''',
                "qa": '''
<h3>简答题1</h3>
<p><strong>题目：</strong>请说明物联系统中数据、算法、反馈和执行器之间的关系，并结合物联花盆系统举例。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>数据是设计算法的依据</strong>：物联花盆系统采集的土壤湿度、温度、光照强度以及从网络获取的天气预报数据，是设计灌溉算法的基础；</li>
  <li><strong>算法是根据一定规则产生的结果</strong>：依据土壤湿度上下限值、天气预报和光照强度，用分支结构判断是否灌溉，得出决策；</li>
  <li><strong>反馈是物联系统作用于外部环境的过程</strong>：在显示屏上显示土壤湿度、启动水泵灌溉，都是系统对现实世界采取的行动；</li>
  <li><strong>执行器是反馈的载体</strong>：显示屏、直流电机水泵、LED灯、蜂鸣器等都是执行器（输出设备），由它们把决策变成实际动作；</li>
  <li>总的链条是：<strong>采集数据 → 设计算法作出决策 → 通过执行器实现反馈与控制</strong>。</li>
</ol>

<h3>简答题2</h3>
<p><strong>题目：</strong>请设计物联花盆系统自动灌溉的条件与决策，并说明为什么要对条件进行整理优化。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li>先根据数据分析结果确定土壤湿度的<strong>上限值和下限值</strong>（如上限3000、下限2000）；</li>
  <li>决策规则：<br>
  ①土壤湿度<strong>大于上限值</strong> → <strong>不灌溉</strong>；<br>
  ②土壤湿度<strong>小于下限值</strong> → <strong>灌溉</strong>；<br>
  ③土壤湿度<strong>介于上下限值之间</strong>：天气预报<strong>下雨</strong> → 不灌溉；天气预报<strong>不下雨</strong> → 灌溉；<strong>光照强度大</strong> → 提高下限值；<strong>光照强度小</strong> → 恢复下限值。</li>
  <li><strong>整理优化的原因</strong>：初步列举的条件都与土壤湿度有关且互相交叉，直接编程容易重复和冲突；以土壤湿度为首要条件分成三类后再对天气和光照分类讨论，条件<strong>互不重叠、覆盖完整</strong>，正好对应程序中的<strong>分支结构嵌套</strong>，便于实现和理解。</li>
  <li>由于判断需要反复进行，这部分代码要放在<strong>循环结构</strong>中。</li>
</ol>

<h3>简答题3</h3>
<p><strong>题目：</strong>物联系统投入使用前为什么要进行调试？系统调试主要包括哪几个方面？</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>原因</strong>：一方面要<strong>对比功能需求进行测试</strong>，检查各项功能是否都已实现；另一方面要让物联系统<strong>整体运行</strong>，测试模块集成后是否存在问题，确保系统在实际环境中稳定可靠。</li>
  <li><strong>硬件检查</strong>：通电前仔细检查所有连线，确保连接正确；注意电源正负极不能接错，否则可能损坏或烧毁电路；检查传感器、执行器连接是否正确、有无物理损伤。</li>
  <li><strong>网络测试</strong>：确保系统内所有设备都能顺畅连接网络，测试设备之间的通信连通性以及设备与服务器连接的稳定性。</li>
  <li><strong>动态测试</strong>：模拟实际操作条件测试系统整体功能，如模拟温度、光照强度变化，检验触发条件的响应是否符合预期。</li>
</ol>

<h3>简答题4</h3>
<p><strong>题目：</strong>某物联门锁系统检测到门口有人停留时，会自动启动摄像头监控，把画面实时显示在房间内的显示屏上，同时通过蜂鸣器发出提示音，并通过应用软件推送消息通知用户；用户可以通过手机应用软件远程控制门锁。请分析该系统中数据采集、传输和反馈控制是如何实现的，可能用到哪些硬件。</p>
<p><strong>答案要点：</strong></p>
<ol>
  <li><strong>数据采集</strong>：用<strong>红外热释电（人体感应）传感器</strong>检测门口是否有人停留，用<strong>摄像头</strong>采集监控画面数据；</li>
  <li><strong>数据传输</strong>：通过<strong>家庭无线网络（Wi-Fi）</strong>把画面和状态数据传输给主控设备、服务器或用户的手机应用软件；</li>
  <li><strong>分析处理</strong>：系统利用算法判断是否有人停留、是否需要报警和推送；</li>
  <li><strong>反馈与控制</strong>：通过<strong>显示屏</strong>显示监控画面（可视化反馈）、通过<strong>蜂鸣器</strong>发出提示音、通过应用软件<strong>推送消息</strong>通知用户（通知反馈）；用户在手机上发出指令后，<strong>电机／舵机（锁体驱动装置）</strong>执行开锁动作（人工控制）；</li>
  <li><strong>可能用到的硬件</strong>：红外热释电传感器、摄像头、主控板、无线路由器（网络模块）、显示屏、蜂鸣器、电机／舵机、智能手机等。</li>
</ol>
'''
            }
        ]
    }
]
