# 八年级信息科技 第三单元、第四单元 练习题数据（L11-L20，共10课，每课20题，合计200题）
# 变量名：Q34
# 每课题型配比：10 单选(single) + 4 判断(tf) + 3 多选(multi) + 3 简答(short)
# answer 规则：单选/判断用数字下标 0/1/2/3（判断 0=错误 1=正确）；多选为数字下标数组；简答 options=[""]，answer 为要点字符串。

Q34 = [
    # ===================== 第11课 物联系统细分解（第三单元） =====================
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "物联系统中把整体功能分解后，通常划分为哪三层结构？",
        "options": ["感知层、网络层、应用层", "输入层、计算层、输出层", "采集层、传输层、控制层", "硬件层、软件层、服务层"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联系统分为感知层、网络层、应用层三层结构。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层采集数据，网络层传输数据，应用层处理分析并实现控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>记忆“感知—网络—应用”三段式即可排除其他干扰项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知采、网络传、应用管。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "在物联系统的三层结构中，负责从物理环境中采集数据、起决定性作用是哪一层？",
        "options": ["感知层", "网络层", "应用层", "传输层"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>感知层负责从物理环境中采集数据，在物联网中起着决定性的作用，是物联网的基础。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层通过摄像头、传感器等采集现实世界的数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采集数据、起决定性作用、是基础”均指向感知层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知是根基，采数它第一。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "物联系统中，负责将感知层采集到的数据安全、可靠地传输到进行处理和分析的是哪一层？",
        "options": ["感知层", "网络层", "应用层", "控制层"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络层负责将感知层采集到的数据安全、可靠地传输到进行处理和分析。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>网络层连接网络、传输数据，实现设备间的数据交互。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“传输”关键词对应网络层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网络管传输。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "物联系统中，对数据进行处理和分析、实现对物理世界的实时控制和精确管理的是哪一层？",
        "options": ["感知层", "网络层", "应用层", "采集层"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>应用层对数据进行处理和分析，实现对物理世界的实时控制、精确管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>刷卡开锁、门铃通知、远程控制、刷脸开锁等功能都在应用层实现。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“处理分析、控制管理”指向应用层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>应用做决策，控制靠它来。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "下列关于物联门锁核心功能的描述，哪一项不属于教材列出的四个相对完整应用场景？",
        "options": ["刷卡开锁", "门铃远程通知", "远程控制开锁", "机械钥匙开锁"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材列出的物联门锁核心功能为刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁，不含传统机械钥匙开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联门锁强调智能化联网功能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>机械钥匙是非联网的传统方式，属于干扰项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>刷、铃、远、脸四功能。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "在公交站牌“到站提醒”功能中，北斗车载定位终端、加速度传感器属于物联系统哪一层？",
        "options": ["感知层", "网络层", "应用层", "传输层"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>北斗车载定位终端、加速度传感器用于采集位置、运行速度等数据，属于感知层。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器是感知层的核心设备。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采集位置/速度数据”对应感知层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感器在感知层。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "公交站牌到站提醒中，传感器采集的数据“通过网络传送给服务器”这一过程属于哪一层？",
        "options": ["感知层", "网络层", "应用层", "处理层"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据通过网络传送给服务器，属于网络层的传输功能。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>网络层负责数据传输与设备间交互。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>“网络传送”是网络层标志。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传送靠网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "公交站牌中，服务器分析处理后把结果发送给站牌进行可视化呈现，这属于哪一层？",
        "options": ["感知层", "网络层", "应用层", "采集层"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>服务器分析处理并可视化呈现，属于应用层的数据处理与分析功能。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>应用层完成分析、处理、呈现与控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“分析处理、可视化呈现”是应用层特征。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>呈现归应用。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "在物联系统三层结构中，被称为“物联网的基础”并且“起着决定性作用”的是？",
        "options": ["感知层", "网络层", "应用层", "互联网层"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>感知层在物联网中起着决定性的作用，是物联网的基础。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>没有感知层采集数据，后续传输与分析都无从谈起。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>题干“基础、决定性”明确指向感知层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知是地基。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "single",
        "stem": "下列哪一项体现了物联系统“应用层”的功能？",
        "options": ["摄像头采集人脸数据", "RFID读卡器读取标签", "刷脸开锁功能实现", "传感器采集温度"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>刷脸开锁功能实现属于应用层对数据的处理与控制；其余三项均为感知层采集。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>应用层实现具体智能功能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>识别“功能实现”而非“数据采集”即为应用层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>功能实现看应用。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "tf",
        "stem": "物联系统由感知层、网络层、应用层三层结构组成。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联系统通常划分为感知层、网络层、应用层三层。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三层结构是最基础的物联系统模型。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材定义一致选“正确”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>三层记心间。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "tf",
        "stem": "网络层负责对数据进行处理和分析，实现对物理世界的实时控制。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。对数据进行处理、分析并实现实时控制的是应用层，网络层只负责传输数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>各层分工不同，勿混淆。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“处理分析、控制”属于应用层，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>处理归应用，别赖网络层。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "tf",
        "stem": "感知层在物联网中起着决定性的作用，是物联网的基础。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材明确指出感知层在物联网中起着决定性作用，是物联网的基础。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层采集物理环境数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材原话一致选“正确”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知是基础。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "tf",
        "stem": "物联门锁只能实现刷卡开锁这一种功能。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。物联门锁可实现刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁等多种功能。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联门锁功能丰富多样。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能”过于绝对，明显错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>功能多又全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "multi",
        "stem": "教材中物联门锁系统可以分解为哪些相对完整的应用场景功能？（多选）",
        "options": ["刷卡开锁", "门铃远程通知", "远程控制开锁", "刷脸开锁"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个均为教材列出的物联门锁核心功能，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>核心功能：刷卡开锁、门铃远程通知、远程控制开锁、刷脸开锁。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐一对照教材四功能，无干扰项则全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>刷铃远脸四功能。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "multi",
        "stem": "下列哪些设备/作用属于物联系统的感知层？（多选）",
        "options": ["摄像头采集人脸数据", "门铃采集状态数据", "服务器分析处理数据", "数据通过网络传输"],
        "answer": [0, 1],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>摄像头采集人脸、门铃采集状态均为感知层采集数据；服务器分析属应用层，网络传输属网络层。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层由传感器完成数据采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>抓“采集”二字，排除分析、传输项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采集归感知。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "multi",
        "stem": "关于物联系统三层结构，下列说法正确的有哪些？（多选）",
        "options": ["感知层负责采集数据", "网络层负责传输数据", "应用层负责处理分析和控制", "应用层负责采集物理环境数据"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>感知层采集、网络层传输、应用层处理分析控制均正确；应用层不负责采集，采集是感知层的职责。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三层职责需严格区分。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“应用层采集”这一错项，其余全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>各层各司职。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "short",
        "stem": "简述物联系统的三层结构及其各自的主要作用。",
        "options": [""],
        "answer": "物联系统分为三层：①感知层——负责从物理环境中采集数据，是物联网的基础，起决定性作用（如摄像头、各类传感器）；②网络层——负责将感知层采集到的数据安全、可靠地传输到进行处理和分析，实现设备间数据交互；③应用层——对数据进行处理和分析，实现对物理世界的实时控制与精确管理（如刷卡开锁、门铃通知、远程控制、刷脸开锁等功能）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三层即感知层、网络层、应用层，分别承担采集、传输、处理控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是物联系统最基础的架构模型。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>围绕“采集—传输—处理控制”三词展开作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知采、网络传、应用管。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "short",
        "stem": "物联门锁系统可以分解为哪几个相对完整的应用场景功能？",
        "options": [""],
        "answer": "物联门锁可分为四个相对完整的应用场景功能：①刷卡开锁；②门铃远程通知；③远程控制开锁；④刷脸开锁。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个核心功能即刷卡、门铃通知、远程控制、刷脸。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是后续各课逐一实现的功能模块。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按教材列表逐条写出即可。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>刷铃远脸。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 11,
        "lessonTitle": "物联系统细分解",
        "type": "short",
        "stem": "以公交站牌“到站提醒”为例，说明该功能的工作过程。",
        "options": [""],
        "answer": "工作过程：①北斗车载定位终端、加速度传感器等采集位置、运行速度等数据（感知层）；②通过网络将采集的数据传送给服务器（网络层）；③服务器分析处理后，将结果发送给公交站牌进行可视化呈现（应用层），从而实现到站提醒。",
        "analysis": '<strong style="color:#1e88e5;">🎯 答案解析：</strong>按“采集—传输—分析呈现”三段描述。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>用真实案例理解三层协作。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>对应三层各写一句即可。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传现。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第11课 物联系统细分解'
    },

    # ===================== 第12课 刷卡开锁易实现（第三单元） =====================
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "在刷卡开锁功能中，负责读取电子标签中编号的模块是？",
        "options": ["输入模块", "计算模块", "输出模块", "网络模块"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输入模块由电子标签、RFID读卡器组成，负责读取电子标签中的编号。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入模块采集身份数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“读取编号”是输入采集，属输入模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>读卡输入先。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "RFID技术的中文全称是？",
        "options": ["射频识别", "近场通信", "蓝牙通信", "远程控制"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>RFID是radio frequency identification的缩写，中文为“射频识别”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>RFID通过无线电信号识别特定目标并读写数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>RFID=射频识别，是教材明确定义。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID射频识别。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "下列关于RFID特点的描述，正确的是？",
        "options": ["通过机械接触读取数据", "通过无线电信号识别目标，无须机械或光学接触", "只能在10厘米内使用", "必须联网才能识别"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>RFID是一种无线通信技术，通过无线电信号识别特定目标并读写相关数据，无须识别系统与特定目标之间建立机械或光学接触。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>非接触式识别是RFID的核心特点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>抓“无线电信号、无须接触”关键词。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>无线非接触。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "刷卡开锁功能中，判断是否可以开锁的关键依据是？",
        "options": ["读卡器是否通电", "电子标签编号是否在存储列表中", "舵机是否转动", "网络是否连接"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主控板用列表存储电子标签编号，判断编号是否在列表中，若在列表中则执行开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>编号匹配是身份校验的核心。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“是否在列表中”是开锁触发条件。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>列表查编号。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "在刷卡开锁模拟系统中，用来模拟打开门锁的硬件是？",
        "options": ["RFID读卡器", "舵机", "按键传感器", "摄像头"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>舵机（模拟门锁）在计算模块中用于模拟打开门锁的动作。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>舵机是一种位置（角度）调节的驱动器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“模拟开锁动作”对应舵机。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>舵机转开锁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "舵机作为一种位置（角度）调节的驱动器，其常见可调节角度范围是？",
        "options": ["0°到90°", "0°到180°", "0°到360°", "−90°到90°"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>舵机常见可调节角度为0°到180°。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>舵机通过角度变化模拟门锁开合。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材明确给出0°到180°。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>舵机0到180。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "刷卡开锁功能的工作流程，第一步是？",
        "options": ["采集身份数据", "判断身份", "发送开锁指令", "接收指令开锁"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>工作流程为：采集身份数据→获取身份数据→判断身份→发送开锁指令→接收指令开锁，第一步是采集身份数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>流程始于数据采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>任何识别流程都从“采集”开始。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>先采集后判断。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "用列表存储电子标签编号并进行判断比对，这属于哪个模块的功能？",
        "options": ["输入模块（电子标签、RFID读卡器）", "计算模块（主控板）", "输出模块（舵机）", "网络模块"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>计算模块由主控板担任，用列表存储电子标签编号并判断编号是否在列表中。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>主控板完成身份校验逻辑。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“存储、判断”是计算逻辑，属计算模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>主控做判断。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "门禁系统中将门禁卡和业主身份数据关联，利用的是电子标签编码的什么特性？",
        "options": ["可复制性", "唯一性", "可变性", "通用性"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用标签编号的唯一性来标识用户身份，实现精准管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>每个电子标签编码唯一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“标识身份”靠唯一性。<br><br><strong style="color:#e67e22;">🧠 预警：</strong>唯一才可靠。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "single",
        "stem": "将刷卡开锁程序烧录到主控板之前，需要完成的关键步骤是？",
        "options": ["修改程序列表中的电子标签编号", "直接烧录即可", "断开所有硬件连接", "删除判断逻辑"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>实现步骤为：连接硬件→修改程序列表中的电子标签编号→烧录到主控板→验证刷卡开锁功能。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>烧录前必须先配置正确的标签编号。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>烧录前准备工作是修改编号。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>改号再烧录。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "tf",
        "stem": "RFID读卡器属于输入模块，负责读取电子标签中的编号。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。输入模块由电子标签、RFID读卡器组成，用于读取电子标签中的编号。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入模块完成身份数据采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与模块划分一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>读卡即输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "tf",
        "stem": "舵机是一种用于采集环境数据的传感器。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。舵机是位置（角度）调节的驱动器（执行器），用于模拟打开门锁，不是采集数据的传感器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>舵机属于输出/执行设备。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>舵机执行动作而非采集，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>舵机是执行。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "tf",
        "stem": "电子标签编码具有唯一性，可用于标识用户身份。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。门禁系统正是利用标签编号的唯一性来标识用户身份，实现精准管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>唯一性是身份关联的基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>编号唯一性。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "tf",
        "stem": "刷卡开锁只需读取电子标签即可，无需判断编号是否在列表中。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。必须先判断电子标签编号是否在存储列表中，只有编号匹配才执行开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>身份校验依赖列表匹配。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“无需判断”违背开锁逻辑，明显错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>不判不开锁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "multi",
        "stem": "刷卡开锁功能的模块及对应硬件包括以下哪些？（多选）",
        "options": ["输入模块：电子标签、RFID读卡器", "计算模块：主控板", "计算模块：舵机（模拟门锁）", "加速度传感器"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输入模块（电子标签、RFID读卡器）、计算模块（主控板）、计算模块（舵机模拟门锁）均属刷卡开锁系统；加速度传感器是公交站牌案例中的设备，不在此系统。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>注意舵机在教材中归入计算模块（执行开锁）。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除无关的加速度传感器即可。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>标签读卡主控舵。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "multi",
        "stem": "刷卡开锁功能的工作过程包括以下哪些环节？（多选）",
        "options": ["采集身份数据", "获取身份数据", "判断身份", "发送开锁指令"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>流程为采集身份数据→获取身份数据→判断身份→发送开锁指令→接收指令开锁，前四项均在列，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>完整流程五步，本题覆盖前四步。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为流程组成部分，无干扰项则全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采获取判发。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "multi",
        "stem": "模拟实现刷卡开锁功能的一般步骤包括？（多选）",
        "options": ["正确连接计算机、主控板、RFID读卡器和舵机", "修改程序列表中的电子标签编号", "把程序烧录到主控板中", "验证刷卡开锁功能"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四步均为教材给出的实现步骤：连接硬件、修改编号、烧录程序、验证功能。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>按步骤操作才能完成功能验证。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为正确步骤，全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>连改烧验。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "short",
        "stem": "简述刷卡开锁功能的工作流程。",
        "options": [""],
        "answer": "刷卡开锁工作流程为：①采集身份数据（RFID读卡器读取电子标签）；②获取身份数据（得到标签编号）；③判断身份（主控板用列表存储编号，判断读取的编号是否在列表中）；④若匹配则发送开锁指令；⑤接收指令开锁（舵机转动模拟打开门锁）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>按“采集—获取—判断—发送—接收开锁”五步描述。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>体现系统中的过程与控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>结合模块功能逐环节写出。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采获取判发开。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "short",
        "stem": "物联门锁刷卡开锁系统中，输入模块、计算模块分别由哪些硬件组成，各完成什么功能？",
        "options": [""],
        "answer": "①输入模块：由电子标签、RFID读卡器组成，负责读取电子标签中的编号（采集身份数据）；②计算模块：由主控板组成，用列表存储电子标签编号，判断编号是否在列表中（身份校验）；并由舵机模拟打开门锁（模拟开锁动作）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输入采集编号，主控板判断，舵机执行。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>模块划分对应硬件与功能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“硬件+功能”两要素作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>读卡采集、主控判断、舵机执行。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 12,
        "lessonTitle": "刷卡开锁易实现",
        "type": "short",
        "stem": "在实现小区门禁精准管理时，为什么可以利用电子标签编号的唯一性来标识用户身份？",
        "options": [""],
        "answer": "因为每个电子标签的编码具有唯一性，相当于每张卡有独一无二的“身份证号”。将门禁卡与业主身份数据关联后，系统只需判断读到的编号是否在授权列表中，即可精准识别业主身份，从而实现进入小区人员的精准管理。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>唯一性使每张卡可唯一对应一人，便于身份校验与管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>编号唯一性=身份唯一标识。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从“唯一对应、便于校验”角度作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>一卡一身份。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第12课 刷卡开锁易实现'
    },

    # ===================== 第13课 门铃通知即时到（第三单元） =====================
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "在物联系统中，用于反馈、显示通知内容的设备被称为？",
        "options": ["输入设备", "输出设备", "传感器", "传输设备"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用于反馈的设备被称为输出设备，用户终端是输出设备，可显示通知内容。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈即针对现实世界采取行动，由输出设备完成。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“显示通知”是反馈，对应输出设备。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈靠输出。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "在物联系统中，“反馈”指的是？",
        "options": ["采集环境数据的过程", "针对现实世界采取行动的过程", "传输数据的过程", "存储数据的过程"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>反馈就是针对现实世界采取行动的过程，可用于反馈的设备是输出设备。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈让系统对现实世界产生作用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采取行动”是反馈本质。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈即行动。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "门铃远程通知功能通常使用哪种通信协议来实现数据的发布与订阅？",
        "options": ["HTTP", "MQTT", "RFID", "NFC"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>远程通知可使用MQTT协议实现发布与订阅。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT是基于TCP/IP的轻量级发布/订阅协议。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>门铃通知依赖MQTT的发布订阅机制。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>通知用MQTT。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "在“门铃按、通知到”的工作过程中，门铃按下起到的作用是？",
        "options": ["输出结果", "触发条件", "数据分析", "网络传输"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>门铃按下是触发条件，触发后续的数据采集、发布与通知。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>触发条件启动整个流程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“按下”是启动事件的触发条件。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按下即触发。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "门铃远程通知功能中，按键传感器所属的功能模块是？",
        "options": ["输入模块", "计算模块", "输出模块", "网络模块"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输入模块由主控板、按键传感器组成，负责采集门铃状态数据并发布至MQTT服务器相应主题。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>按键传感器采集触发状态。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采集状态”属输入模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键是输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "门铃通知功能中，搭建MQTT服务器（计算模块）通常使用的硬件是？",
        "options": ["具备移动热点功能的计算机", "按键传感器", "舵机", "摄像头"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>计算模块由具备移动热点功能的计算机担任，负责搭建本地MQTT服务器、设置主题、实现发布与订阅。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>计算机作为服务平台中枢。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>MQTT服务器运行在带热点的计算机上。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>电脑搭MQTT。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "门铃端采集到按键状态后，将消息发布到哪里？",
        "options": ["直接显示在门铃上", "MQTT服务器相应主题", "本地硬盘", "互联网任意网站"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>门铃端（输入模块）采集按键状态数据后，将其发布至MQTT服务器相应主题。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>发布/订阅基于主题。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“发布”动作指向MQTT主题。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>发布到主题。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "用户终端接收到“有人按门铃”通知并显示出来，这体现了物联系统的？",
        "options": ["数据采集", "网络传输", "输出（反馈）", "身份验证"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用户终端显示通知内容，是系统对现实世界采取行动的反馈，由输出设备完成。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>通知显示属于输出/反馈环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“显示通知”即反馈输出。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>显示即反馈。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "除了用显示屏显示通知，教材还提到可以用哪些执行器来通知用户？",
        "options": ["蜂鸣器、RGB灯传感器", "按键传感器", "主控板", "RFID读卡器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>除显示屏外，还可采用蜂鸣器、RGB灯传感器等执行器实现通知。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>多种输出设备可承担反馈。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>蜂鸣器、RGB灯是典型输出执行器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>蜂鸣RGB也可通知。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "single",
        "stem": "门铃通知功能中，订阅MQTT主题并在收到数据后以通知形式提醒用户的是？",
        "options": ["输入模块（按键传感器）", "计算模块（计算机）", "输出模块（主控板）", "传感器"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输出模块由主控板担任，订阅MQTT服务器相应主题，收到数据后以通知形式提醒用户。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输出模块完成反馈动作。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“订阅并提醒”是输出模块职责。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>输出来提醒。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "tf",
        "stem": "在物联系统中，反馈就是针对现实世界采取行动的过程。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材定义反馈为针对现实世界采取行动的过程。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈由输出设备实施。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材定义一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈即行动。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "tf",
        "stem": "MQTT协议可用于门铃通知中的数据发布与订阅传输。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。门铃远程通知使用MQTT实现发布与订阅。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT是轻量级发布/订阅协议。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT发布订阅。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "tf",
        "stem": "门铃通知功能中，按键传感器属于输出模块。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。按键传感器属于输入模块，负责采集门铃状态数据，不是输出模块。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>采集=输入，显示=输出。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>传感器采集属输入，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键是输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "tf",
        "stem": "用户终端显示通知内容，说明它是输入设备。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。显示通知是反馈，用户终端是输出设备，而非输入设备。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输出设备用于反馈。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“显示=反馈=输出”，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>显示即输出。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "multi",
        "stem": "门铃远程通知功能由哪些功能模块组成？（多选）",
        "options": ["输入模块", "计算模块", "输出模块", "存储模块"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>门铃通知由输入模块（按键传感器+主控板）、计算模块（带热点计算机+MQTT服务器）、输出模块（主控板）组成；教材未单列“存储模块”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入—计算—输出三模块协作。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除无关项，选前三。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>输入输出计算。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "multi",
        "stem": "模拟实现门铃远程通知功能，正确的步骤包括？（多选）",
        "options": ["连接无线网络", "搭建本地MQTT服务器，获取地址、端口、用户名和密码", "门铃端按键按下时发送“有人按门铃”消息", "用户端接收并显示通知"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四步均为教材给出的实现步骤：连接无线网、搭建MQTT服务器、门铃端发送消息、用户端接收显示。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>完整覆盖发布端与订阅端。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为正确步骤，全选。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>勿漏任一端。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "multi",
        "stem": "可用于门铃通知的“输出/执行器”有哪些？（多选）",
        "options": ["显示屏", "蜂鸣器", "RGB灯传感器", "按键传感器"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>显示屏、蜂鸣器、RGB灯传感器都可作为输出设备通知用户；按键传感器是输入设备，不在此列。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈由多种输出执行器承担。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除输入设备按键传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>屏蜂灯皆反馈。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "short",
        "stem": "简述门铃远程通知功能的工作过程。",
        "options": [""],
        "answer": "工作过程：①家中门铃端——门铃按下（触发条件），获取按键状态数据，通过网络发布至MQTT服务器相应主题；②用户终端（输出设备）——从主题中接收数据，终端显示“有人按门铃”通知，实现对用户的反馈。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>按“门铃按下→发布主题→订阅接收→显示通知”描述。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>体现发布/订阅与反馈。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>分门铃端与用户端两步写。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按发收显。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "short",
        "stem": "门铃远程通知功能的输入模块、计算模块、输出模块分别由哪些硬件组成？",
        "options": [""],
        "answer": "①输入模块：主控板、按键传感器——采集门铃状态数据，并发布至MQTT服务器相应主题；②计算模块：具备移动热点功能的计算机——搭建MQTT服务器，设置主题，实现发布与订阅；③输出模块：主控板——订阅MQTT服务器相应主题，收到数据后以通知形式提醒用户。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三模块硬件与功能逐一对应。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入采集、计算中转、输出反馈。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“模块=硬件+功能”结构作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>键采、脑转、板显。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 13,
        "lessonTitle": "门铃通知即时到",
        "type": "short",
        "stem": "什么是物联系统中的“反馈”？请结合门铃通知举例说明。",
        "options": [""],
        "answer": "反馈是指物联系统针对现实世界采取行动的过程，由输出设备完成。例如门铃通知中，用户端的显示屏（输出设备）收到MQTT主题消息后显示“有人按门铃”的通知，就是对“门铃被按下”这一事件在现实世界中采取的行动（反馈），让用户及时得知有人到访。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>反馈=对现实采取行动，输出设备执行。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈是物联系统关键特征。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先下定义再结合门铃实例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈即行动。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第13课 门铃通知即时到'
    },

    # ===================== 第14课 远程控制更便捷（第三单元） =====================
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "在远程控制开锁功能中，作为“用户端”发起控制指令的是哪个模块？",
        "options": ["输入模块", "计算模块", "输出模块", "网络模块"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材明确：输入模块是用户端，输出模块是门锁端。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>用户端发送指令属输入。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“用户端、发指令”对应输入模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>用户是输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "在远程控制开锁功能中，作为“门锁端”接收指令并执行开锁的是哪个模块？",
        "options": ["输入模块", "计算模块", "输出模块", "传输模块"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材明确：输出模块是门锁端，接收指令后控制舵机转动开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>门锁端执行动作属输出。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“门锁端、执行开锁”对应输出模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>门锁是输出。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "物联系统中，控制是指什么？",
        "options": ["采集环境数据", "基于反馈的数据调整设备或系统的工作状态", "存储历史数据", "显示通知内容"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>控制是基于反馈的数据调整设备或系统的工作状态，反馈与控制密不可分。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>控制依赖反馈数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“调整工作状态”是控制定义。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>控制调状态。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "通过发送指令实现对远程设备的控制，这属于？",
        "options": ["人工控制", "自动控制", "反馈控制", "数据采集"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>人工控制即通过发送指令实现对远程设备的控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>远程开锁属于人工控制实例。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“发送指令”关键词指向人工控制。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>指令属人工。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "根据设定的控制规则，由系统自动控制设备运转，这属于？",
        "options": ["人工控制", "自动控制", "远程通知", "数据采集"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>自动控制是根据设定的控制规则，由系统控制设备运转，如扫地机器人。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>自动运转无需人实时指令。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“设定规则、系统自动”对应自动控制。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>规则属自动。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "远程控制开锁中，门锁端收到消息后控制哪个硬件转动以实现开锁？",
        "options": ["蜂鸣器", "舵机", "按键传感器", "RGB灯"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输出模块由主控板、舵机组成，订阅主题收到消息后控制舵机转动开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>舵机模拟门锁开合。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“转动开锁”对应舵机。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>舵机转开锁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "远程控制开锁功能中，用户端与门锁端之间进行消息传递所使用的通信协议是？",
        "options": ["RFID", "MQTT（主题 Door/Lock）", "NFC", "蓝牙"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>远程控制开锁使用MQTT，用户端发布、门锁端订阅同一主题（如 Door/Lock）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT发布/订阅实现远程控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>远程控制依赖MQTT主题通信。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>Door/Lock走MQTT。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "远程控制开锁的用户端按下按键后，通常向主题发布的消息内容是？",
        "options": ["close", "open", "hello", "bell"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用户端采集按键状态，若按下则发布MQTT主题消息“open”表示开锁指令。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>“open”即开启指令。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>开锁指令对应“open”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按下发open。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "远程控制开锁中，作为计算模块、负责搭建MQTT服务器的是？",
        "options": ["具备移动热点功能的计算机", "按键传感器", "舵机", "摄像头"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>计算模块由具备移动热点功能的计算机担任，负责搭建MQTT服务器、设置主题、实现发布与订阅。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>计算机充当服务平台。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>MQTT服务器运行在带热点计算机上。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>电脑搭服务器。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "single",
        "stem": "下列例子中，属于“自动控制”的是？",
        "options": ["用户手机远程按下按键开锁", "火车站验票系统按规则自动验票", "用户发送指令开灯", "用户订阅门铃通知"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>自动控制按设定规则由系统运转，如扫地机器人、火车站验票系统；其余均为人工发送指令的控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>自动=规则驱动，人工=指令驱动。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“按规则自动”是自动控制标志。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>规则自动跑。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "tf",
        "stem": "物联系统中的反馈与控制密不可分，控制是基于反馈的数据调整设备的工作状态。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材指出反馈与控制密不可分，控制基于反馈的数据调整设备/系统工作状态。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈是控制的前提。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈控相依。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "tf",
        "stem": "远程控制开锁功能中，用户端是输出模块。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。教材明确用户端是输入模块（发送指令），门锁端才是输出模块。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>用户端发指令=输入。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“用户端”非输出，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>用户是输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "tf",
        "stem": "人工控制是指通过发送指令，实现对远程设备的控制。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。人工控制即通过发送指令实现远程设备控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>远程开锁是人工控制实例。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材定义一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>指令即人工。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "tf",
        "stem": "远程控制开锁只能由系统自动完成，不能由人工控制。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。远程控制开锁是人工控制的典型例子，由用户发送“open”指令实现，并非只能自动完成。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>本课重点就是人工远程控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能自动”违背本课内容，明显错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>远程靠人工。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "multi",
        "stem": "远程控制开锁功能包含哪些功能模块？（多选）",
        "options": ["输入模块（用户端）", "计算模块（MQTT服务器）", "输出模块（门锁端）", "存储模块"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>包含输入模块（用户端，主控板+按键传感器）、计算模块（带热点计算机，MQTT服务器）、输出模块（门锁端，主控板+舵机）；教材未单列存储模块。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入—计算—输出三模块。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除无关项，选前三。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>用户计算门锁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "multi",
        "stem": "远程控制开锁的工作过程环节包括？（多选）",
        "options": ["搭建MQTT服务器并设置主题，实现发布与订阅", "门锁端订阅开锁指令", "用户端按键触发，发布开锁指令", "门锁端控制开锁"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四步均为教材流程：搭建MQTT与主题、订阅指令、按键触发发布指令、控制开锁，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>完整覆盖通信与控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为正确环节，全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>搭订发控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "multi",
        "stem": "关于人工控制与自动控制，下列说法正确的有哪些？（多选）",
        "options": ["人工控制通过发送指令实现对远程设备的控制", "自动控制根据设定的控制规则由系统运转", "扫地机器人按设定规则清扫属于自动控制", "自动控制需要人实时发出每一条指令"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>前三项正确；自动控制按规则运转，不需要人实时发每条指令，故第四项错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>人工靠指令，自动靠规则。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“实时发指令”错项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>人指自规。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "short",
        "stem": "什么是物联系统中的“控制”？反馈与控制有什么关系？",
        "options": [""],
        "answer": "控制是指基于反馈的数据调整设备或系统的工作状态。反馈与控制密不可分：反馈为控制提供数据依据，控制则依据反馈数据对设备或系统进行调整，从而实现对现实世界的干预。例如火车站验票系统、扫地机器人都体现了反馈与控制的结合。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>控制基于反馈数据调整状态，两者紧密相依。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈是控制的前提。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先定义控制，再说二者关系。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>反馈控相依。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "short",
        "stem": "简述远程控制开锁功能的工作过程。",
        "options": [""],
        "answer": "工作过程：①搭建MQTT服务器，设置主题（如 Door/Lock），实现发布与订阅；②门锁端（输出模块）订阅开锁指令主题；③用户端（输入模块）按键触发，若按下则发布“open”消息；④门锁端收到消息后控制舵机转动，实现开锁。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>按“搭服务器→订阅→触发发布→控制开锁”四步。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>体现远程人工控制闭环。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>分用户端与门锁端描述。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>搭订发控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 14,
        "lessonTitle": "远程控制更便捷",
        "type": "short",
        "stem": "区分“人工控制”与“自动控制”，并各举一个教材中的例子。",
        "options": [""],
        "answer": "人工控制：通过发送指令实现对远程设备的控制，例如本课的远程控制开锁（用户按下按键发送“open”指令）。自动控制：根据设定的控制规则，由系统控制设备运转，例如家里的扫地机器人（设定规则后自动规划路线、避开障碍清扫）和火车站验票系统。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>人工=指令驱动，自动=规则驱动，各举教材例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>两类控制区别在触发方式。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>给出定义+对应实例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>人指自规。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第14课 远程控制更便捷'
    },

    # ===================== 第15课 面容钥匙显智能（第三单元） =====================
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "人脸识别技术属于下列哪一类识别技术？",
        "options": ["射频识别技术", "生物识别技术", "近场通信技术", "条码识别技术"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>人脸识别是基于人的脸部特征数据进行身份识别的一种生物识别技术。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>生物识别包括人脸、指纹等。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“脸部特征”对应生物识别。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>人脸属生物。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "人脸识别是基于什么数据进行身份识别的？",
        "options": ["声音数据", "脸部特征数据", "指纹数据", "电子标签数据"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>人脸识别基于人的脸部特征数据进行身份识别。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>脸部特征是识别依据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>题干“人脸”直接对应脸部特征。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>看脸识人。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "机器识别人脸的第一步是？",
        "options": ["提取五官特征", "采集人脸图像信息", "与人脸库匹配", "分析整体轮廓"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>机器识别人脸第一步是采集人脸图像信息（相当于人眼捕捉图像传给大脑）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>识别流程始于图像采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>任何识别都先“采集图像”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>先采图。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "人脸识别中提取的“局部特征”主要包括以下哪些部位？",
        "options": ["眉毛、眼睛、鼻子、嘴", "手、脚、臂、腿", "心脏、肺、肝、肾", "键盘、鼠标、屏幕、主机"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>机器提取人脸局部特征包括眉毛、眼睛、鼻子、嘴等，以及整体轮廓。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>五官特征用于区分身份。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“人脸局部特征”指向五官。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>眉眼鼻嘴。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "机器识别人脸时，“和记忆中的人脸特征进行匹配，识别出身份”是第几步？",
        "options": ["第一步", "第二步", "第三步", "第四步"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>完整的人脸识别三步为：①采集图像；②分析提取特征；③与记忆中特征匹配识别身份，故匹配是第三步。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>匹配识别是最后一步。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“匹配识别”在流程末尾。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采提匹。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "在刷脸开锁功能中，负责采集人脸数据并进行人脸识别的是？",
        "options": ["输入模块（摄像头）", "计算模块（计算机）", "输出模块（舵机）", "网络模块"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输入模块由摄像头组成，负责采集人脸数据、进行人脸识别后发布消息至MQTT主题。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>摄像头完成采集与识别。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采集人脸”对应输入模块（摄像头）。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>摄像即输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "刷脸开锁中，订阅MQTT主题、收到消息后控制舵机转动的是？",
        "options": ["输入模块（摄像头）", "计算模块（计算机）", "输出模块（主控板、舵机）", "传感器"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>输出模块由主控板、舵机组成，订阅MQTT主题，收到消息后控制舵机转动开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输出模块执行开锁动作。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“控制舵机转动”是输出模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>舵机属输出。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "人脸识别要保证采集到的人脸图像能够被“看得见、看得懂、认得出”，其中“认得出”对应的是？",
        "options": ["采集图像", "提取与分析特征", "与人脸库匹配并识别身份", "网络传输"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>“看得见”=采集图像，“看得懂”=分析提取特征，“认得出”=与人脸库匹配识别身份。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三步对应三句话。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“认得出”即匹配识别。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>见懂认。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "使用人脸识别平台模拟刷脸开锁时，首先需要做的准备是？",
        "options": ["直接控制舵机转动", "运行人脸识别平台并添加人脸库", "断开网络连接", "删除摄像头驱动"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>实验步骤：运行人脸识别平台→选择人脸匹配模块、添加人脸库→对准摄像头观察匹配。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>先建人脸库才能匹配。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“首先”是运行平台加人脸库。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>先建库再比。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "single",
        "stem": "相比刷卡开锁，刷脸开锁的主要优势在于？",
        "options": ["成本更低", "提供独一无二的生物特征，更安全便捷", "不需要任何计算设备", "速度更慢"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>人脸识别提供基于脸部生物特征身份识别，更加安全、便捷，无需携带卡片。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>生物特征难以伪造、随身可用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“生物特征、安全便捷”是优势。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>刷脸更安全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "tf",
        "stem": "人脸识别是基于人的脸部特征数据进行身份识别的一种生物识别技术。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材原话定义人脸识别为生物识别技术。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>脸部特征是识别依据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>人脸属生物。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "tf",
        "stem": "一个完整的人脸识别系统要求计算机能够进行三步：采集图像、提取特征、匹配识别。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。三步即采集人脸图像、分析提取特征、与存储特征匹配识别身份。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三步流程是识别核心。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采提匹。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "tf",
        "stem": "刷脸开锁中，摄像头属于输出模块。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。摄像头属于输入模块，负责采集人脸数据并进行人脸识别，不是输出模块。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>采集=输入。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>摄像头采集属输入，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>摄像即输入。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "tf",
        "stem": "人脸识别只需要采集图像，不需要与人脸库匹配也能识别身份。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。人脸识别必须与人脸库（记忆中的特征）进行匹配才能识别身份，仅采集图像无法确认“是谁”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>匹配是识别关键。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不需要匹配”违背三步流程，明显错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>不配比不了。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "multi",
        "stem": "机器识别人脸的基本过程包括以下哪些步骤？（多选）",
        "options": ["采集人脸图像信息", "分析并提取人脸局部特征与整体轮廓", "与人脸库中的特征进行匹配识别身份", "直接播放语音播报"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三步为采集图像、分析提取特征（眉毛眼睛鼻子嘴及轮廓）、匹配识别；语音播报不在基本识别步骤内。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>识别核心是采提匹。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“语音播报”这一输出动作。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采提匹。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "multi",
        "stem": "刷脸开锁功能包含哪些功能模块？（多选）",
        "options": ["输入模块（摄像头）", "计算模块（带热点计算机、MQTT服务器）", "输出模块（主控板、舵机）", "存储模块（硬盘）"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>包含输入模块（摄像头）、计算模块（带热点计算机）、输出模块（主控板、舵机）；教材未单列“存储模块（硬盘）”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入—计算—输出三模块。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除无关项，选前三。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>摄像脑舵。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "multi",
        "stem": "人脸识别中需要提取的特征包括以下哪些？（多选）",
        "options": ["眉毛", "眼睛", "鼻子", "嘴"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材列举机器提取局部特征包括眉毛、眼睛、鼻子、嘴等，以及整体轮廓，四者全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>五官均为识别特征。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为五官特征，无干扰项则全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>眉眼鼻嘴。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "short",
        "stem": "简述机器识别人脸的基本过程（三步）。",
        "options": [""],
        "answer": "机器识别人脸的基本过程为三步：①采集人脸图像信息（相当于人眼捕捉图像）；②分析图像，提取人脸的局部特征（眉毛、眼睛、鼻子、嘴等）和整体轮廓；③将提取的特征与记忆（人脸库）中的人脸特征进行匹配，从而识别出人脸的身份。即“看得见、看得懂、认得出”。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三步：采集、提取特征、匹配识别。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>对应“见懂认”。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按三步骤顺序展开。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采提匹。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "short",
        "stem": "刷脸开锁功能中，输入、计算、输出模块分别由哪些硬件组成？",
        "options": [""],
        "answer": "①输入模块：摄像头——采集人脸数据，进行人脸识别后，发布消息至MQTT服务器相应主题；②计算模块：具备移动热点功能的计算机——搭建MQTT服务器，设置主题，实现发布与订阅；③输出模块：主控板、舵机——订阅MQTT服务器相应主题，收到消息后控制舵机转动，实现开锁。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三模块硬件与功能逐一对应。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>输入采集、计算中转、输出执行。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“模块=硬件+功能”结构作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>摄像脑舵。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },
    {
        "module": "第三单元 简单物联功能实践",
        "lesson": 15,
        "lessonTitle": "面容钥匙显智能",
        "type": "short",
        "stem": "为什么说人脸识别技术让门锁更安全、便捷？",
        "options": [""],
        "answer": "因为人脸识别基于每个人独一无二的脸部生物特征进行身份识别，难以复制或冒用，安全性高于传统钥匙或卡片；同时用户无需携带任何实体钥匙或卡片，刷脸即可开锁，使用更为便捷，为人们提供更安全、便捷的生活体验，也代表了物联系统智能化的发展趋势。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>从生物特征唯一性与免携带两方面说明。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>生物识别优势明显。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>围绕“安全（唯一）+便捷（免带）”作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>唯一又免带。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第三单元/第15课 面容钥匙显智能'
    },

    # ===================== 第16课 模块功能先划分（第四单元） =====================
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "不同物联系统的工作环节虽然各有不同，但一般都包含以下哪个不属于共同环节的流程？",
        "options": ["采集环境数据", "传输与存储数据", "分析处理数据", "机械加工制造"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联系统共同工作环节为采集环境数据、传输与存储数据、分析处理数据、反馈与控制；机械加工制造不属于物联系统工作环节。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>四个环节是物联系统共性。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“机械加工”明显不相关。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传析控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆系统中，实时获取温度、土壤湿度、光照强度等数据属于哪个工作环节？",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>实时获取温度、土壤湿度、光照强度等环境数据属于“采集数据”环节。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器完成数据采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“获取…数据”即采集。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>获取数据先。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆系统中，将环境数据通过网络传输给物联网服务平台属于哪个环节？",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>将数据传输给物联网服务平台，属于“传输与存储数据”环节。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>网络传输是此环节核心。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“传输”关键词指向该环节。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传输靠网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆系统中，对数据进行简单分析处理、得到统计结果和可视化图表属于哪个环节？",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>获取历史数据并进行简单分析处理、得到统计结果和可视化图表，属于“分析处理数据”环节。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分析处理生成价值信息。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“分析处理、图表”对应此环节。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>处理出图表。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆系统中，根据温度、土壤湿度、天气预报数据实现自动灌溉属于哪个环节？",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>根据分析结果与天气数据自动灌溉、动态显示土壤湿度，属于“反馈与控制”环节。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈控制作用于现实世界。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“自动灌溉”是反馈控制动作。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>灌溉即控制。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆项目中，负责采集环境数据的功能模块是？",
        "options": ["环境感知模块", "网络通信模块", "服务平台模块", "执行模块"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>环境感知模块负责采集环境数据（传感器采集，主控板接收并通过网络通信发送）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知模块是数据入口。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“采集环境数据”对应环境感知模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知采数据。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆项目中，负责数据的汇总、存储、处理的模块是？",
        "options": ["环境感知模块", "网络通信模块", "服务平台模块", "执行模块"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>服务平台模块负责数据的汇总、存储、处理，并进行可视化与手动控制灌溉。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>服务平台是系统中枢。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“汇总存储处理”对应服务平台模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台管汇总。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆项目中，负责实现数据通信的模块是？",
        "options": ["环境感知模块", "网络通信模块", "服务平台模块", "执行模块"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络通信模块负责实现数据通信，既将传感器数据发往服务平台，也将天气预报数据传输给主控板。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>通信模块双向传输。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“数据通信”对应网络通信模块。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网络管通信。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆项目中，执行模块中的执行器（如LED灯、水泵电机）的主要作用是？",
        "options": ["采集环境数据", "根据主控板指令产生相应动作，实现反馈", "存储历史数据", "分析处理数据"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>执行模块负责反馈与控制，执行器根据主控板发出的指令产生相应动作（如LED灯、水泵电机），实现对现实世界的反馈。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>执行器是反馈的执行者。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“产生动作、反馈”是执行器职责。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>执行出动作。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "single",
        "stem": "物联花盆项目中，传感器采集到的环境数据最终由谁接收并通过网络通信模块发送出去？",
        "options": ["服务器", "主控板", "显示屏", "水泵"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主控板负责接收传感器的数据，并将这些数据通过网络通信模块发送给物联网服务平台。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>主控板是数据汇聚与转发节点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“接收传感器数据并发送”是主控板职责。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>主控来转发。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "tf",
        "stem": "不同的物联系统在功能、软硬件组成上各有不同，但它们的工作环节都类似。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材指出不同物联系统功能、软硬件各有不同，但工作环节都类似（采集、传输存储、分析处理、反馈控制）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>共性在四个工作环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>环节皆相似。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "tf",
        "stem": "物联花盆系统的“执行模块”负责采集环境数据。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。采集环境数据是环境感知模块的职责，执行模块负责反馈与控制（由执行器产生动作）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>采集≠执行。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>采集归感知模块，故判断为错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采集属感知。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "tf",
        "stem": "服务平台模块负责物联花盆系统数据的汇总、存储和处理。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。服务平台模块负责数据的汇总、存储、处理，并可视化、手动控制灌溉。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>平台是数据处理中心。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台管汇总。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "tf",
        "stem": "网络通信模块只负责将传感器数据传到主控板，不负责接收外部数据。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。网络通信模块既将主控板获取的传感器数据发送到服务平台，也将互联网中的天气预报数据传输给主控板，是双向通信。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>通信模块双向传输。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只负责…不负责”与双向传输矛盾，故错。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网络双传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "multi",
        "stem": "物联花盆系统一般包含哪四个工作环节？（多选）",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个共同工作环节：采集数据、传输与存储数据、分析处理数据、反馈与控制，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是物联系统通用流程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>无干扰项，全选四环节。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传析控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "multi",
        "stem": "物联花盆项目可划分为哪些功能模块？（多选）",
        "options": ["环境感知模块", "网络通信模块", "服务平台模块", "执行模块"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>项目划分为环境感知模块、网络通信模块、服务平台模块、执行模块四大模块，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>模块对应四个工作环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>四模块一一对应四环节，全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感网台执。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "multi",
        "stem": "关于执行模块，下列说法正确的有哪些？（多选）",
        "options": ["执行模块负责反馈与控制", "执行模块包含执行器如LED灯、水泵电机", "执行器根据主控板指令产生相应动作", "执行模块负责采集环境数据"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>执行模块负责反馈与控制，由LED灯、水泵电机等执行器根据主控板指令产生动作；采集环境数据是环境感知模块的职责，故第四项错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>执行模块=反馈控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“采集数据”错项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>执行出动作。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "short",
        "stem": "物联系统一般包含哪四个工作环节？请结合物联花盆系统各举一例。",
        "options": [""],
        "answer": "物联系统一般包含四个工作环节：①采集数据——物联花盆实时获取温度、土壤湿度、光照强度等，并可通过网络获取天气预报；②传输与存储数据——将环境数据通过网络传输给物联网服务平台；③分析处理数据——获取历史数据并分析处理，得到统计结果与可视化图表；④反馈与控制——动态显示土壤湿度，并根据温度、土壤湿度、天气预报实现自动灌溉。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节：采集、传输存储、分析处理、反馈控制，各配花盆例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>环节对应模块功能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按四环节顺序逐一举例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传析控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "short",
        "stem": "物联花盆项目可划分成哪些功能模块？各自的主要作用是什么？",
        "options": [""],
        "answer": "可划分为四个功能模块：①环境感知模块——负责采集环境数据（传感器采集，主控板接收并发送）；②网络通信模块——负责实现数据通信（双向传输传感器数据与天气预报数据）；③服务平台模块——负责数据汇总、存储、处理（可视化、手动控制灌溉）；④执行模块——负责反馈与控制（由LED灯、水泵电机等执行器产生动作）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四模块：环境感知、网络通信、服务平台、执行，各说作用。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>模块划分对应工作环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按模块名称+作用结构作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感网台执。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 16,
        "lessonTitle": "模块功能先划分",
        "type": "short",
        "stem": "什么是执行模块？执行器在物联系统中的作用是什么？",
        "options": [""],
        "answer": "执行模块是物联系统中负责反馈与控制的功能模块。执行器（如LED灯、水泵电机等）的主要作用是：根据主控板发出的指令产生相应的动作，从而实现对现实世界的反馈与控制，例如物联花盆中由水泵电机完成自动灌溉。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>执行模块=反馈控制；执行器按指令产生动作。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>执行器是反馈的执行者。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先定义模块，再说执行器作用并举例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>执行出动作。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第16课 模块功能先划分'
    },

    # ===================== 第17课 物联数据需采集（第四单元） =====================
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "物联系统中，数据的主要来源有哪两类？",
        "options": ["传感器采集和互联网数据", "键盘输入和鼠标点击", "打印输出和扫描", "声音和图像"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联系统的数据来源主要有两类：传感器采集和互联网数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知设备+网络资源共同供数。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“传感器+互联网”是教材明确两类。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感加网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "物联花盆项目中，采集温度、湿度、光照需要确定连接哪些传感器？",
        "options": ["温湿度传感器、土壤湿度传感器、光敏传感器", "加速度传感器、陀螺仪、麦克风", "RFID读卡器、NFC模块", "按键传感器、舵机"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材确定连接温湿度传感器、土壤湿度传感器、光敏传感器来采集相应数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>不同传感器对应不同环境量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>温度湿度光照对应题中三种传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿光三感。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "为了获取更可靠的天气预报数据，应当优先访问？",
        "options": ["任意商业网站", "官方网站", "社交媒体", "论坛帖子"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材提示“官网数据更可靠”，应访问官方网站实时查看天气数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>官方数据源权威性高。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“更可靠”指向官网。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>官网更可靠。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "从互联网中获取天气预报数据，常用以下哪种方式？",
        "options": ["手动抄写", "调用免费的天气预报数据API", "直接查看电视", "发送短信"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>互联网中有很多免费的天气预报数据API供人们调用。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>API便于程序自动获取。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“获取天气数据”对应API调用。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>天气用API。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "天气预报数据API通常返回什么格式的数据？",
        "options": ["图片文件", "JSON格式字符串", "音频文件", "Word文档"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>API返回的天气预报数据为JSON数据格式（字符串）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>JSON便于程序解析。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“API返回”常是JSON。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>API返JSON。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "在Python中，将JSON字符串转换为字典结构，应使用？",
        "options": ["json.load( )方法", "print( )函数", "open( )函数", "len( )函数"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过json.load( )方法可以将JSON字符串转换为字典结构。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>字典便于按键值访问数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“JSON转字典”对应json.load。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>json.load转字典。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "天气预报的JSON数据中，list键对应的列表主要用于存储？",
        "options": ["用户账号", "当天和第二天的天气预报", "历史日志", "设备编号"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>list键中的列表存储当天和第二天的天气预报；data键值是主要的天气预报数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>理解JSON结构是解析前提。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“list=当天+第二天”是教材说明。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>list存两天。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "在物联网服务平台中，为物联花盆项目添加主题一般按什么方式添加？",
        "options": ["按温度、光照强度、土壤湿度添加3个主题", "只添加1个总主题", "按日期添加", "按学生姓名添加"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可按温度、光照强度、土壤湿度在物联网服务平台中添加3个主题，并与主控板对应。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分主题便于区分数据类型。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“三类环境量→三个主题”是教材做法。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>三类三主题。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "在物联网服务平台中，为区分不同的终端设备，需要为每个主控板分配？",
        "options": ["颜色和形状", "用户名和密码", "物理地址贴纸", "蓝牙名称"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联网服务平台为每个主控板分配用户名和密码，以便区分与管理设备。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>账号体系区分多设备。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“区分设备”对应用户名密码。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>每板一账号。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "single",
        "stem": "为减少数据冗余，在物联网服务平台上何时才上传新的环境数据较为合理？",
        "options": ["每隔固定的1秒都上传", "检测到温度、湿度、光照等环境数据发生变化时再上传", "只在开机时上传一次", "每天只上传一次"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材提出：在检测到环境数据发生变化时再上传新数据，可减少数据冗余。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>变化上传避免重复存储。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“减少冗余”对应变化时才上传。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>变才上传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "tf",
        "stem": "物联系统的数据采集主要来自传感器采集和互联网数据两个方面。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。数据来源主要包括传感器采集与互联网数据两类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>两类来源互补。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>传感加网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "tf",
        "stem": "JSON格式字符串可以直接当作字典使用，无需任何转换。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。JSON是字符串，需通过json.load( )等方法转换为字典结构后才能方便按键值访问。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>字符串与字典类型不同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“直接当字典”违背转换步骤，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>先转再用。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "tf",
        "stem": "物联网服务平台中，可以为每个主控板分配用户名和密码以区分设备。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。平台为每个主控板分配用户名和密码，与主控板对应，便于区分和管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>账号体系区分设备。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>每板一账号。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "tf",
        "stem": "为了减少数据冗余，应在数据每次固定时间都上传，无需判断变化。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。教材建议检测到环境数据发生变化时再上传新数据，以减少数据冗余，而非无条件频繁上传。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>变化上传更省资源。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“无需判断变化”与减少冗余相悖，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>变才上传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "multi",
        "stem": "物联花盆项目的传感器设备包括以下哪些？（多选）",
        "options": ["温湿度传感器", "土壤湿度传感器", "光敏传感器", "按键传感器"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>项目确定连接温湿度传感器、土壤湿度传感器、光敏传感器；按键传感器属于门铃/远程控制案例，不在花盆采集清单内。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三类传感器对应三类环境量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除按键传感器。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>温湿光三感。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "multi",
        "stem": "关于通过API获取天气预报数据，下列说法正确的有哪些？（多选）",
        "options": ["API通常返回JSON格式数据", "可用json.load( )将JSON字符串转为字典", "list键中列表存储当天和第二天的天气预报", "官网数据不可靠，应使用随意网站"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>前三项正确；官网数据更可靠，故“官网不可靠”错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>理解API与JSON解析流程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“官网不可靠”错项。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>官网更可靠。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "multi",
        "stem": "在物联网服务平台中进行主题与设备管理，正确的做法有哪些？（多选）",
        "options": ["按温度、光照强度、土壤湿度添加3个主题", "为每个主控板分配用户名和密码", "多个数据需在同一主题中注意区分", "无论数据是否变化都持续高频上传"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>前三项正确：分三类主题、每板分配账号、多数据需区分；教材建议变化时才上传以减少冗余，故“无论变化都高频上传”错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>合理管理降低冗余。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“高频无变化上传”错项。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>变才上传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "short",
        "stem": "物联系统的数据来源有哪些？请结合物联花盆项目举例说明。",
        "options": [""],
        "answer": "物联系统的数据来源主要有两类：①传感器采集——如物联花盆通过温湿度传感器、土壤湿度传感器、光敏传感器采集温度、土壤湿度、光照强度等环境数据；②互联网数据——如通过网络获取官方网站提供的天气预报数据。两类数据共同支撑系统分析与应用。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>两类来源：传感器采集+互联网数据，各配花盆例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知与网络共同供数。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>分两类说明并举例。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>传感加网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "short",
        "stem": "什么是API？如何通过API获取天气预报数据并解析JSON？",
        "options": [""],
        "answer": "API（应用程序接口）是预先定义、基于一定协议的软件函数集合，提供不同程序间交互的能力。获取天气预报数据：①调用互联网中免费的天气预报数据API；②API返回JSON格式字符串；③在Python中用json.load( )方法将JSON字符串转换为字典结构，再按data、list等键值提取当天及第二天的天气预报数据。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>先定义API，再说调用→返回JSON→json.load转换→按键提取。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>API+JSON解析流程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“调用—返回—转换—提取”顺序作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>API返JSON，load转字典。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 17,
        "lessonTitle": "物联数据需采集",
        "type": "short",
        "stem": "在物联网服务平台中，应如何为主题和设备进行管理？",
        "options": [""],
        "answer": "管理要点：①按数据类别添加主题——物联花盆项目可按温度、光照强度、土壤湿度添加3个主题，并与各主控板对应；②为每个主控板分配用户名和密码，以区分不同终端设备；③当多个数据放在同一主题时，要在数据中做好区分标识；④为减少数据冗余，应在检测到环境数据发生变化时再上传新数据，而非无变化也频繁上传。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主题分类、设备分配账号、数据区分、变化上传四点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>平台管理最佳实践。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从主题、设备、区分、冗余四方面作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>三类三主题，变才上传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第17课 物联数据需采集'
    },

    # ===================== 第18课 数据分析与处理（第四单元） =====================
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "lesson": 18,
        "type": "single",
        "stem": "下列工具中，不属于教材列举的“早期数据处理工具”的是？",
        "options": ["算盘", "差分机", "主控板", "计算器"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材列举的早期数据处理工具包括算盘、差分机、计算器、计算机；主控板是物联系统的控制硬件，不属于早期数据处理工具。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据处理工具随时代演进。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>主控板明显不属于计算工具。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>算差计计四工具。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "在Python中，提供对表格数据进行快速处理方法、常用于数据处理的模块是？",
        "options": ["pandas", "random", "turtle", "time"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>pandas提供了对表格数据进行快速处理的一系列方法，可提高数据处理效率。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>pandas是数据分析利器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“表格快速处理”对应pandas。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>pandas处理表。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "与pandas常配合、用于数值计算的Python模块是？",
        "options": ["numpy", "json", "os", "math（仅基础）"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材提到可借助pandas、numpy等数据处理模块处理数据，numpy擅长数值计算。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>pandas+numpy组合常见。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“数值计算模块”对应numpy。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>numpy算数值。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "通过数据文件直接下载物联网服务平台的数据后，可用什么软件进行处理？",
        "options": ["电子表格软件", "杀毒软件", "绘图软件", "压缩软件"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>两种下载方式中，通过数据文件直接下载后，可用电子表格软件处理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>表格软件适合查看统计。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“数据文件处理”对应电子表格软件。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>表格处理文件。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "通过API获取数据，一般不需要执行以下哪一步？",
        "options": ["参阅说明文档", "确定API的URL", "传入相关参数后发起网络请求", "购买专用硬件服务器"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>API获取数据步骤为：参阅文档、确定URL、传入参数发起请求；无需购买专用硬件服务器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>API调用是软件层面的事。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“购买硬件服务器”不在此流程。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>API三步取。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "想从数据中快速得到最高温度和最低温度，可以利用什么方法对数据排序？",
        "options": ["sort_values方法", "print方法", "len方法", "open方法"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用sort_values方法对数据进行排序，可快速得到最高和最低温度。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>排序后首尾即极值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“排序求最值”对应sort_values。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>排序用sort_values。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "要找出光照强度大于某个阈值（如1000）的时间段，可使用？",
        "options": ["数据筛选", "数据合并", "数据加密", "数据删除"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过数据筛选找出光照强度大于阈值的数据，从而确定光照时间。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>筛选用于条件提取。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“大于阈值”对应筛选。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>筛选按条件。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "根据不同设备ID求每组土壤湿度的平均值，应使用？",
        "options": ["groupby( )分组后配合mean( )", "sort_values", "print", "json.load"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>groupby( )提供数据分组功能，先按clientId分组，再利用mean( )函数求每组数据的平均值。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分组+聚合是典型分析。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“按设备ID分组求平均”对应groupby+mean。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>分组用groupby。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "对温度求最大值、最小值、平均值，这属于哪种数据分析方法？",
        "options": ["统计分析法", "对比分析法", "分组分析法", "标签分析法"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>统计分析法通过求一组数据的最大值、最小值、平均值等方式进行分析，如温度、湿度的极值与均值。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>统计是基础分析方法。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“最值、平均”对应统计分析法。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>统计看极值。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "single",
        "stem": "对不同区域的二氧化碳浓度数据进行对比，这属于哪种数据分析方法？",
        "options": ["对比分析法", "统计分析法", "分组分析法", "聚类分析法"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>对比分析法通过对不同数据的对比分析其异同，如不同区域二氧化碳浓度对比。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>对比揭示差异。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不同区域对比”对应对比分析法。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>对比看异同。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "tf",
        "stem": "物联系统产生大量数据，早期的数据处理工具已经不能胜任复杂的数据处理任务。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联系统产生大量数据，早期工具（算盘、差分机等）已不能胜任复杂处理，需借助计算机与编程。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据规模推动工具升级。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>早期力不足。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "tf",
        "stem": "在Python中可以使用pandas模块处理从API获取的数据。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材指出可用pandas模块处理数据，提升处理效率。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>pandas适合表格数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>pandas能处理。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "tf",
        "stem": "物联网服务平台的数据只能手动查看，不能下载或编程获取。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。服务平台数据可通过数据文件直接下载，也可通过API调用编程获取数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>两种获取数据方式并存。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能手动”与两种下载方式矛盾，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>文件API两取。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "tf",
        "stem": "分组分析法是指将数据按某个条件分成若干组再统计对比，如按设备ID分组。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。分组分析法先按条件分组再统计对比，如先按设备ID分组再分析各组数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分组便于横向比较。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材定义一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>分组再比对。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "multi",
        "stem": "物联系统处理数据的方式主要包括哪些？（多选）",
        "options": ["使用常见的数据处理工具", "借助pandas、numpy等编程工具", "通过API编程获取数据", "只能靠人工手抄记录"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>处理方式包括使用常见数据处理工具、借助编程工具（pandas/numpy）、通过API编程获取数据；人工手抄不是规范方式，故第四项错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>工具+编程双路径。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“人工手抄”错项。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>工具加编程。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "multi",
        "stem": "数据分析的三种常用方法包括？（多选）",
        "options": ["统计分析法", "对比分析法", "分组分析法", "随机猜测法"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三种方法为统计分析法、对比分析法、分组分析法；随机猜测不是科学方法。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三类方法各有适用场景。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“随机猜测”。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>统对分三法。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "multi",
        "stem": "关于pandas数据处理，下列说法正确的有哪些？（多选）",
        "options": ["pandas提供对表格数据的快速处理方法", "可将数据整理为DataFrame类型", "可用groupby( )分组后配合mean( )求平均", "pandas不能处理从API获取的数据"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>前三项正确：pandas快速处理表格、可转为DataFrame、groupby+mean聚合；pandas正是用于处理API数据的工具，故第四项错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>理解pandas核心能力。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“不能处理API数据”错项。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>pandas全能。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "short",
        "stem": "物联系统中处理数据有哪些方式？",
        "options": [""],
        "answer": "处理方式主要有两类：①使用常见的数据处理工具（如电子表格软件等对数据文件进行处理）；②借助编程工具处理数据——在Python中可用pandas、numpy等模块对数据进行快速处理，也可通过API调用获取数据后再用程序分析。两种数据下载方式配合：数据文件直接下载、通过API编程获取。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>工具+编程两类，配合两种下载方式。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>处理与获取结合。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从“工具、编程、下载方式”展开。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>工具加编程。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "short",
        "stem": "数据分析常用哪三种方法？请各举一例。",
        "options": [""],
        "answer": "三种常用方法：①统计分析法——通过求最大值、最小值、平均值分析，如案例中求温度、湿度的最值与均值；②对比分析法——对比不同数据异同，如对比不同区域的二氧化碳浓度；③分组分析法——按条件分组后再统计对比，如先按设备ID分组，再求各组平均值。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>统、对、分三法各配教材例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三类方法互补。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐法定义+举例。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>统对分三法。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 18,
        "lessonTitle": "数据分析与处理",
        "type": "short",
        "stem": "如何通过API从物联网服务平台获取数据？简述主要步骤。",
        "options": [""],
        "answer": "步骤：①参阅相关说明文档（不同在线MQTT服务器API用法有差异）；②确定API的URL；③传入相关参数（如user、psd、topic等）后发起网络请求；④接收返回的JSON数据，用json.load( )转换为字典或使用pandas整理为DataFrame，再进行后续分析处理。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>文档→URL→参数请求→解析四步。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>API调用标准流程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按教材四步顺序作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>API四步取。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第18课 数据分析与处理'
    },

    # ===================== 第19课 数据呈现可视化（第四单元） =====================
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "对温度数据进行可视化后，直观发现13:00左右的数据有异常，这体现了数据可视化的什么作用？",
        "options": ["发现数据异常", "了解整体概况", "发现趋势变化", "生成标签云"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过数据可视化可以更容易识别并定位数据中存在的异常，如温度数据在13:00异常。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>异常检测是可视化价值之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“发现异常”直接对应作用。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>可视找异常。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "智慧社区数据监测大屏让工作人员及时了解社区概况，体现了数据可视化的什么作用？",
        "options": ["发现数据异常", "了解整体概况", "发现趋势变化", "数据筛选"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据可视化可以让人们方便、直观地了解物联网系统的整体概况，如智慧社区监测大屏。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>概览是可视化的基础价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“了解概况”对应此作用。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>可视看全局。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "通过历史起降时间数据预测航班大概率晚点，体现了数据可视化的什么作用？",
        "options": ["发现数据异常", "了解整体概况", "发现趋势变化", "数据加密"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据可视化可展示历史数据情况，帮助理解变化并助力预测未来趋势，如预测航班晚点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>趋势预测是高级价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“预测趋势”对应发现趋势变化。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>可视看趋势。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "描绘数据随时间的变化趋势，常见的可视化方式属于？",
        "options": ["趋势可视化（折线图、柱形图、像素图）", "比例可视化（饼图、环形图）", "分布可视化（散点图+地图）", "标签云"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>趋势可视化用于描绘数据随时间的变化趋势，常见有折线图、柱形图、像素图等。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>趋势类用折线/柱形。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“随时间变化”对应趋势可视化。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>折线看趋势。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "显示不同部分所占整体的比例关系，常见的可视化方式属于？",
        "options": ["趋势可视化", "比例可视化（饼图、环形图）", "分布可视化", "标签云"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>比例可视化用于显示不同部分所占整体的比例关系，常见有饼图、环形图。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>占比用饼/环形。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“比例关系”对应比例可视化。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>饼图看占比。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "将散点图与地图结合，表示数据在地理位置上的分布情况，这属于？",
        "options": ["趋势可视化", "比例可视化", "分布可视化", "标签云"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>分布可视化可将散点图与地图结合，表示数据在地理位置上的分布，如查询附近空闲单车。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>地理分布用散点+地图。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“地理位置分布”对应分布可视化。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>地图看分布。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "标签云主要用于直观展示什么？",
        "options": ["数值随时间变化", "各部分占比", "文本中的高频词（词频越高字体越大）", "地理位置分布"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>标签云可直观展示一段文本数据中的高频词，词频越高字体越大。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>标签云是文本可视化。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“高频词、字体大小”对应标签云。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>标签看词频。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "在Python中，用于绘制折线图的函数是？",
        "options": ["plt.plot( )", "plt.scatter( )", "plt.bar( )", "plt.title( )"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>plt.plot( )用来绘制折线图；plt.scatter( )画散点图，plt.bar( )画柱形图。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>不同图表对应不同函数。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“折线图”对应plt.plot。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>plot画折线。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "在Python绘图时，用于设置图表标题的函数是？",
        "options": ["plt.figsize( )", "plt.title( )", "plt.plot( )", "plt.show( )"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>plt.title( )用于设置图表标题；plt.figsize( )指定画布大小。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>标题与画布分开设置。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“标题”对应plt.title。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>title设标题。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "single",
        "stem": "在Python中，用于指定画布（图表）大小的函数是？",
        "options": ["plt.figsize( )", "plt.title( )", "plt.scatter( )", "plt.bar( )"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用plt.figsize( )可以指定画布大小，从而控制图表尺寸。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>画布决定整体布局。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“画布大小”对应plt.figsize。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>figsize定大小。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "tf",
        "stem": "数据可视化可以帮助识别并定位数据中存在的异常。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。如对温度数据可视化后可直观发现13:00左右的异常。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>异常检测是作用之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>可视找异常。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "tf",
        "stem": "饼图、环形图常用于显示不同部分占整体的比例关系，属于比例可视化。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。比例可视化常见有饼图、环形图，用于显示占比。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>占比类图表。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>饼环看占比。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "tf",
        "stem": "散点图与地图结合只能表示单一数据，无法表示地理位置分布。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。散点图与地图结合正是用于分布可视化，可表示数据在地理位置上的分布（如附近空闲单车）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分布可视化依赖地图叠加。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能单一”与分布可视化矛盾，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>地图看分布。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "tf",
        "stem": "在Python中，plt.bar( )用于绘制柱形图。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。plt.bar( )用于绘制柱形图；plt.plot( )画折线，plt.scatter( )画散点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>绘图函数各有分工。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>bar画柱形。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "multi",
        "stem": "数据可视化的作用主要包括哪些？（多选）",
        "options": ["发现数据异常", "了解整体概况", "发现趋势变化", "增加数据冗余"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三大作用：发现数据异常、了解整体概况、发现趋势变化；可视化旨在精简呈现而非增加冗余。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>作用对应三类价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“增加冗余”错项。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>异常概况趋势。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "multi",
        "stem": "常见的数据可视化方式包括以下哪些？（多选）",
        "options": ["趋势可视化（折线图、柱形图）", "比例可视化（饼图、环形图）", "分布可视化（散点图+地图）", "标签云"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类方式教材均介绍：趋势、比例、分布可视化与标签云，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>四类覆盖主要场景。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>无干扰项，全选。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>趋比分标四式。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "multi",
        "stem": "关于Python绘图，下列说法正确的有哪些？（多选）",
        "options": ["plt.plot( )绘制折线图", "plt.scatter( )绘制散点图", "plt.bar( )绘制柱形图", "plt.title( )设置图表标题"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个说法均正确：plot折线、scatter散点、bar柱形、title标题。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>绘图函数分工明确。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为教材原话，全选。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>plo散bar题。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "short",
        "stem": "数据可视化有哪些作用？请各举一例。",
        "options": [""],
        "answer": "数据可视化主要有三大作用：①发现数据异常——如对温度数据可视化后直观发现13:00左右数据异常；②了解整体概况——如智慧社区数据监测大屏让工作人员及时了解社区概况；③发现趋势变化——如通过历史起降时间数据预测航班大概率晚点，助力预测未来趋势。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>异常、概况、趋势三作用各配例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>作用体现可视化价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐作用定义+举例。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>异常概况趋势。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "short",
        "stem": "常见的数据可视化方式有哪些？分别适合什么场景？",
        "options": [""],
        "answer": "常见方式：①趋势可视化（折线图、柱形图、像素图）——适合描绘数据随时间的变化趋势；②比例可视化（饼图、环形图）——适合显示不同部分占整体的比例关系；③分布可视化（散点图与地图结合）——适合表示数据在地理位置上的分布（如附近空闲单车）；④标签云——适合展示文本中的高频词，词频越高字体越大。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类方式+适用场景一一对应。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>选对方式是关键。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“方式—场景”结构作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>趋比分标四式。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 19,
        "lessonTitle": "数据呈现可视化",
        "type": "short",
        "stem": "利用Python绘制温度变化趋势图，需要哪些步骤和绘图函数？",
        "options": [""],
        "answer": "步骤：①数据准备——准备横坐标（时间，存入变量X）和纵坐标（温度，存入变量Y）；②设置画布和标题——用plt.figsize( )指定画布大小，用plt.title( )设置标题；③绘制图表并显示——用plt.plot( )绘制折线图（温度趋势），如需散点用plt.scatter( )、柱形用plt.bar( )，最后显示图表。绘制前应先明确可视化的目的。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>准备XY、设画布标题、plot绘制三步。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>绘图流程标准化。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按准备—设置—绘制顺序作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>XY标题plot。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第19课 数据呈现可视化'
    },

    # ===================== 第20课 反馈控制有算法（第四单元） =====================
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆自动灌溉算法设计中，需要依据数据分析确定哪两个关键参数？",
        "options": ["土壤湿度的上限值和下限值", "光照强度的最大最小值", "温度的上下限", "设备编号范围"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>需根据土壤在干燥、适中、湿润时的传感器数据，确定合适的土壤湿度上限值和下限值。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>上下限是灌溉决策边界。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“灌溉”依赖土壤湿度阈值。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>湿度定上下。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆中，当土壤湿度大于上限值时，系统的决策是？",
        "options": ["不灌溉", "灌溉", "提高下限值", "报警"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>土壤湿度大于上限值→不灌溉（土壤已足够湿润）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>过湿无需浇水。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“大于上限、已湿”→不灌溉。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>超上不浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆中，当土壤湿度小于下限值时，系统的决策是？",
        "options": ["不灌溉", "灌溉", "提高下限值", "等待"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>土壤湿度小于下限值→灌溉（土壤过干需补水）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>过干需浇水。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“小于下限、已干”→灌溉。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>低于下限浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "土壤湿度介于上下限之间且天气预报下雨，系统决策是？",
        "options": ["灌溉", "不灌溉", "提高下限值", "开启水泵5秒"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>土壤湿度介于上下限之间且天气预报下雨→不灌溉（雨水会补给，避免过湿）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>结合天气优化决策。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“将下雨”→不必人工灌溉。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>将雨不浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "土壤湿度介于上下限之间且天气预报不下雨，系统决策是？",
        "options": ["不灌溉", "灌溉", "提高下限值", "关闭系统"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>土壤湿度介于上下限之间且天气预报不下雨→灌溉（补充即将缺失的水分）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>不下雨需主动补水。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不下雨”→灌溉。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>无雨则浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆中，实时显示土壤湿度值所使用的执行器是？",
        "options": ["显示屏", "直流电机水泵", "舵机", "蜂鸣器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>反馈与控制中，实时显示土壤湿度情况由显示屏完成。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>显示属反馈输出。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“显示湿度”对应显示屏。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>屏显湿度。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆中实现自动灌溉所使用的执行器是？",
        "options": ["直流电机水泵", "显示屏", "摄像头", "按键传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>实现自动灌溉由直流电机水泵完成，条件满足时电机启动灌溉约5秒。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>水泵是灌溉执行器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“灌溉”对应水泵。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>水泵来灌溉。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆系统投入使用前，下列调试工作中不属于教材要求的是？",
        "options": ["硬件检查", "网络测试", "动态测试", "直接发布到应用商店"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>调试包括硬件检查、网络测试、动态测试；直接发布到应用商店不是本系统调试内容。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三类测试保障正常运行。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“发布商店”不相关。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>硬网动三测。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "物联花盆主程序通常写在什么结构中，并用time.sleep( )控制等待时间？",
        "options": ["while True循环", "if单分支", "for固定次数", "def函数定义"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主程序代码写在while True中，并在最后通过time.sleep( )函数控制等待时间，实现持续循环运行与节奏控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>循环保证系统长期运行。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“持续运行+等待”对应while True。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>永久循环跑。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "single",
        "stem": "为感知是否有人在附近活动以了解主人对植物的关心程度，可扩展使用哪种传感器？",
        "options": ["红外热释电传感器", "光敏传感器", "温湿度传感器", "RFID读卡器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可扩展红外热释电传感器感知是否有人活动，并将数据上传分析，了解主人关心程度。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>功能扩展提升智能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“感知人体活动”对应红外热释电。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>红外感有人。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "tf",
        "stem": "物联花盆自动灌溉需要根据数据分析设计算法，确定土壤湿度的上限值和下限值。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。需基于温度、土壤湿度、光照、天气预报数据设计算法，并确定土壤湿度上下限值。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>阈值驱动决策。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>湿度定上下。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "tf",
        "stem": "土壤湿度大于上限值时，系统应当立刻灌溉。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。土壤湿度大于上限值时应“不灌溉”，过湿无需补水。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>过湿反致伤害。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“大于上限→灌溉”违背决策表，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>超上不浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "tf",
        "stem": "物联花盆的反馈与控制中，显示屏用于显示土壤湿度，直流电机水泵用于自动灌溉。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。控制与执行即显示土壤湿度（显示屏）和实现自动灌溉（直流电机水泵）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>两执行器各司其职。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与教材一致，选正确。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>屏显泵灌。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "tf",
        "stem": "系统调试只需测试功能即可，无需检查硬件连接和网络。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。调试包括硬件检查（连接正确）、网络测试（畅通稳定）、动态测试（模拟功能验证触发响应）三方面。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>全面调试保可靠。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“无需检查”违背调试要求，故错。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>硬网动三测。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "multi",
        "stem": "关于物联花盆自动灌溉的触发条件与决策，下列说法正确的有哪些？（多选）",
        "options": ["土壤湿度大于上限值→不灌溉", "土壤湿度小于下限值→灌溉", "介于上下限且天气预报下雨→不灌溉", "介于上下限且天气预报不下雨→灌溉"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四项均符合教材优化后的决策表，全选。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>决策综合湿度与天气。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>均为正确决策，全选。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>超上不浇、低于下浇、雨不浇、晴浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "multi",
        "stem": "物联花盆系统的执行器包括以下哪些？（多选）",
        "options": ["显示屏", "直流电机水泵", "LED灯", "温湿度传感器"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>执行模块执行器包括显示屏（显示湿度）、直流电机水泵（灌溉）、LED灯（执行模块示例）；温湿度传感器是感知设备，不是执行器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>执行器产生动作。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除传感器。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>屏泵灯执行。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "multi",
        "stem": "物联花盆系统投入使用前的调试工作包括？（多选）",
        "options": ["硬件检查（连接正确）", "网络测试（畅通稳定）", "动态测试（模拟功能、测试触发响应）", "无需调试直接上线运行"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>调试三方面：硬件检查、网络测试、动态测试；直接上线不调试是错误做法。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>调试保障可靠。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“无需调试”。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>硬网动三测。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "short",
        "stem": "物联花盆系统自动灌溉的算法中，如何根据土壤湿度与天气预报确定灌溉决策？",
        "options": [""],
        "answer": "决策规则：①土壤湿度大于上限值→不灌溉；②土壤湿度小于下限值→灌溉；③介于上下限之间：若天气预报下雨→不灌溉，若天气预报不下雨→灌溉，若光照强度大→提高下限值，若光照强度小→恢复下限值。综合土壤湿度与天气/光照数据形成不同数据决策，实现自动灌溉。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>依据湿度上下限+天气/光照给出决策。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>阈值与条件组合成算法。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按决策表分条陈述。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>超上不浇、低于下浇、雨不浇晴浇。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "short",
        "stem": "物联花盆系统的反馈与控制分别由哪些执行器实现？",
        "options": [""],
        "answer": "反馈与控制具体为：①显示土壤湿度情况——由显示屏（执行器）实现；②实现自动灌溉——由直流电机水泵（执行器）实现，当条件满足时电机启动灌溉约5秒。两者都属于执行模块，根据主控板发出的指令对现实世界采取行动。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>屏显湿度、水泵灌溉两执行器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>执行模块落地反馈控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>分别说明显示与灌溉的执行器。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>屏显泵灌。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
    {
        "module": "第四单元 简易物联系统实践",
        "lesson": 20,
        "lessonTitle": "反馈控制有算法",
        "type": "short",
        "stem": "物联花盆系统投入使用前需要进行哪些调试工作？",
        "options": [""],
        "answer": "调试工作包括三方面：①硬件检查——确认各设备连接正确；②网络测试——确保网络畅通稳定；③动态测试——模拟功能过程，测试触发条件的响应等。此外主程序写在while True循环中并用time.sleep( )控制等待时间，保障系统持续稳定运行。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>硬件、网络、动态三测试。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>全面调试保障可靠。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按三测试分条作答。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>硬网动三测。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第四单元/第20课 反馈控制有算法'
    },
]
