# 八年级 第五单元（物联网应用探索）与第六单元（物联网安全）练习题
# 第五单元：L21 文物保护新手段 / L22 健康生活新设备 / L23 医疗设施新功能 / L24 农业生产新模式 / L25 学习探究新工具
# 第六单元：L26 数字世界有身份 / L27 安全事件与风险 / L28 安全防范讲策略 / L29 自主可控意义大 / L30 系统安全需升级
# 每课 20 题：10 单选 + 4 判断 + 3 多选 + 3 简答
# answer：单选/判断用数字下标；多选用数字下标数组；简答为字符串
# options：判断为 ["正确","错误"]；简答为 [""]

Q56 = [
    # ===================== L21 文物保护新手段 =====================
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "博物馆环境监测系统体现了物联网技术在下列哪个领域的应用？",
        "options": ["文物保护", "健康生活", "农业生产", "学习探究"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>博物馆环境监测系统用于实时监测文物保存环境，属于物联网在文物保护中的应用。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第五单元“物联网应用探索”以博物馆环境监测为案例，将物联网用于文物保护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>题干关键词“博物馆”“文物”，直接对应文物保护，排除健康、农业、学习。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>博物馆里护文物，物联监测保环境。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "与传统环境监测相比，物联环境监测系统的最大优势是？",
        "options": ["数据只能本地查看", "数据可实时更新并发送到手机和计算机，查看方便", "不需要任何传感器", "完全不需要网络"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联系统数据能在大屏幕实时更新，也可发到手机和计算机，查看方便。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传统监测数据不能实时呈现、查看麻烦；物联系统解决了该问题。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>对比“传统=不能实时、麻烦”，选“实时、方便查看”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传统麻烦物联快，实时查看真方便。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "下列数据中，不属于博物馆环境监测系统监测内容的是？",
        "options": ["温度", "湿度", "光照强度", "用户的身高"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>系统监测温度、湿度、光照强度、烟雾、二氧化碳浓度等环境数据，不测用户身高。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>监测系统关注的是文物保存环境，而非人的身体数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>身高属于健康类数据（第22课），明显不属于文物保护环境参数。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿光照烟二氧，文物环境要记牢。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "博物馆环境监测系统采集温湿度时使用的是什么传感器？",
        "options": ["超声波传感器", "温度传感器、湿度传感器", "光敏传感器", "压力传感器"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>采集温湿度使用温度传感器和湿度传感器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>温度、湿度传感器分别测量环境温度与湿度，是环境感知的基础设备。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“温湿度”对应“温度、湿度传感器”，超声波用于测距、光敏测光、压力测压力。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿对应温湿传，感知环境第一关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "主控板读取传感器数据后，通过什么协议/服务将数据发送到物联网服务平台？",
        "options": ["蓝牙音箱", "MQTT 服务器", "打印机", "投影仪"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主控板通过网络将传感器数据发送给 MQTT 服务器（物联网服务平台）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT 是物联网中常用的轻量级消息传输协议，负责数据的存储与转发。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>物联网服务平台常用 MQTT，其他选项均非数据传输通道。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据上网走 MQTT，平台存储又转发。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "当监测到的温湿度超出阈值范围时，系统会如何响应？",
        "options": ["仅显示数据不做处理", "自动执行打开或关闭空调、打开或关闭恒湿器的操作", "自动切断全部电源", "向警察报警"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>超出阈值时系统执行反馈与控制：打开或关闭空调、恒湿器来调节环境。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈与控制环节根据分析结果自动触发保护措施，是物联网“感知—决策—执行”的体现。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“超阈值”应对应自动调节设备，而非仅显示或无关联动作。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超阈自动调空调，恒湿保护文物强。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "对采集到的环境数据进行分析处理，不能采用下列哪种形式？",
        "options": ["物联网服务平台图表", "电子表格", "Python 绘图库", "纸质信件"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据分析可用物联网服务平台、电子表格、Python 模块，纸质信件不是数据分析形式。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数字化分析是物联网的核心环节，借助平台图表、表格和编程实现可视化。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“纸质信件”明显不属于数据可视化分析手段。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台表格 Python，三招分析全都有。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "要使传感器采集的数据在主控板上实时显示，前提是？",
        "options": ["关闭传感器", "让传感器一直工作", "每天只读一次", "删除历史数据"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>要使数据实时显示，就要让传感器一直工作（持续采集）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>持续采集是“实时”的基础，程序通常用循环不断读取传感器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“实时”必然对应“持续/一直工作”，排除关闭、单次、删除。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>想要实时看得清，传感器要不停勤。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "不同文物有不同的最佳保存环境要求，监测系统通过什么实现自动保护？",
        "options": ["人工每天巡检", "阈值探究并设计算法实现反馈与控制", "把屏幕调大", "关闭网络"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过查找文物保存要求、确定环境数据阈值，并设计算法实现反馈与控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>阈值+算法是自动控制的核心，使系统在异常时自动触发保护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>自动保护必然依赖“阈值+算法”，而非人工或无关操作。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>定阈值、写算法，自动保护顶呱呱。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "single",
        "stem": "要在智能终端查看博物馆环境数据，需要登录什么并点击相应主题？",
        "options": ["微信", "QQ", "MQTT 服务器", "淘宝"],
        "answer": 2,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>登录 MQTT 服务器，点击相应主题即可查看已上传的数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网服务平台以“主题（Topic）”区分不同设备/数据，订阅主题即可收数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第5题呼应，查看平台数据要登录 MQTT 服务器并选主题。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>登录 MQTT，选对主题看数据。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "tf",
        "stem": "物联环境监测系统采集的数据可以在大屏幕上实时更新，也可以发送到手机和计算机上。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联系统数据实时更新并可多端查看。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>实时性、远程可查看是物联网相比传统监测的突出优势。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第2题一致，判断为正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>实时更新多端看，物联优势记心间。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "tf",
        "stem": "博物馆环境监测系统只需要采集数据，不需要传输与存储数据。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。系统四个环节包含采集、传输与存储、分析处理、反馈与控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传输与存储是把数据送达平台、实现远程查看的前提。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只需要采集”遗漏了其余三个环节，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>四环节、不能少，采集传输存分析。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "tf",
        "stem": "文物适宜的温湿度范围一旦超出，可能对文物造成不可逆的影响，因此需要设置阈值进行保护。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。环境异常会不可逆损伤文物，故需阈值触发保护。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>不同文物（木器漆、书画、青铜器、织绣）有不同适宜温湿度。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不可逆影响”是设置阈值的重要依据，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>文物娇贵怕异常，设好阈值保无恙。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "tf",
        "stem": "改变环境状态（如打开空调）后，传感器获取的数据不会发生变化。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。改变环境状态，温湿度等数据会随之变化。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器实时反映环境变化，是数据分析与反馈的依据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不会变化”违背实时监测原理，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>环境一变数据变，实时感知看得见。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "multi",
        "stem": "博物馆环境监测系统功能实现包含下列哪些环节？（多选）",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个环节全选：采集、传输与存储、分析处理、反馈与控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是物联网系统通用的四环节框架，贯穿多个项目。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>题干问“包含哪些”，四项均为教材明确环节，全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四步走，物联系统不用愁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "multi",
        "stem": "下列设备中，可用于搭建博物馆环境监测系统的有？（多选）",
        "options": ["温度传感器", "湿度传感器", "继电器（控制空调、恒湿器）", "超声波传感器"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>温度、湿度传感器负责感知，继电器负责开关空调/恒湿器；超声波传感器本课未用于此系统。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>超声波传感器在第22课身高记录仪中使用，本课用温湿度传感器与继电器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按本课硬件清单排除超声波，选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿传感加继电，空调恒湿来把关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "multi",
        "stem": "对博物馆环境数据进行分析处理时，可采用的形式有？（多选）",
        "options": ["物联网服务平台图表", "电子表格", "Python 绘图库", "电话通知"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可用物联网服务平台、电子表格、Python 模块进行可视化分析，电话通知不是分析形式。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数字化分析三途径是本课重点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除“电话通知”，其余三项均为分析形式。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台表格 Python，分析可视化三件套。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "short",
        "stem": "请简述博物馆环境监测系统“采集数据、传输与存储数据、分析处理数据、反馈与控制”四个环节分别要做什么。",
        "options": [""],
        "answer": "采集数据：用温度、湿度等传感器实时获取环境数据；传输与存储数据：主控板通过网络把数据发送到物联网服务平台进行存储与转发；分析处理数据：利用平台图表判断数据是否在阈值范围内；反馈与控制：实时显示温湿度，超出阈值时自动打开或关闭空调、恒湿器以实现保护。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节依次为感知、上传、判断、执行，构成完整闭环。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是物联网系统通用流程，后续各课均按此框架分析。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按“采集—传输—分析—反馈”顺序分别作答，紧扣本课功能表。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四字诀，物联流程记真切。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "short",
        "stem": "为什么文物保存需要设置环境数据的阈值？当数据超出适宜范围时系统应如何响应？",
        "options": [""],
        "answer": "不同文物（如木器漆、书画、青铜器、织绣）有各自适宜的温湿度范围，超出可能对文物造成不可逆损伤，因此要设阈值。当监测数据超出阈值范围时，系统应执行反馈与控制，自动打开或关闭空调、恒湿器来调节环境，保护文物安全。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>阈值保护防止不可逆损伤，超阈自动调节环境。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>阈值即“临界值”，是自动控制的依据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先说“为何设阈值（不可逆损伤）”，再说“如何响应（自动调控）”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>阈值就是警戒线，越线自动来把关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L21",
        "lessonTitle": "文物保护新手段",
        "type": "short",
        "stem": "物联环境监测系统相比传统环境监测有哪些优势？",
        "options": [""],
        "answer": "传统监测数据不能实时呈现、查看麻烦；物联系统可让数据在大屏幕上实时更新，并能发送到手机和计算机，查看方便；还能上传平台进行存储、转发与可视化分析，并在异常时自动触发保护措施。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>优势体现在实时性、远程可查看、可分析、可自动控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是物联网赋能文物保护的核心价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>对比传统“不能实时、麻烦”，逐条列出物联优势。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传统慢又烦，物联快又全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第21课 文物保护新手段'
    },

    # ===================== L22 健康生活新设备 =====================
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "下列属于物联网在健康生活中应用的新设备是？",
        "options": ["物联手环、物联体重秤", "传统扫帚", "普通铅笔", "纸质书"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联手环、物联体重秤是物联网改善健康生活的典型设备。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第五单元将“健康生活新设备”作为物联网应用案例之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>带“物联”二字的设备符合题意，其余为非智能物品。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>手环体重都物联，健康生活更智能。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "学校利用物联网技术设计的“身高记录仪”主要用于？",
        "options": ["测量学生性别、身高并统计达标情况", "播放音乐", "清洗衣物", "导航出行"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>身高记录仪用于采集性别、身高并统计班级身高达标情况。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>本课以身高记录仪为项目，体现物联网在体质健康监测中的应用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“身高记录仪”核心功能是测身高与统计，选第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>身高记录仪，测高又统计。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "超声波传感器测量身高的原理是？",
        "options": ["发射声波并检测回声的时间差来计算与目标的距离", "用光照强度判断", "用压力大小判断", "用温度高低判断"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>超声波传感器发射声波并检测反射回声，通过时间差计算距离，从而测量身高。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>超声波测距是距离传感器的典型应用，也用于第24、25课。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“声波—回声—时间差—距离”是超声波原理，排除光/压/温。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>声波去又回，时间算距离。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "身高记录仪采集的数据包括？",
        "options": ["学生的性别和身高", "体重和血压", "年龄和籍贯", "汽车车牌号"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>采集学生性别、身高数据用于统计身高达标情况。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>采集环节明确要获取“同学性别、身高”。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>项目目标就是“测量身高并统计”，数据即性别+身高。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>测身高、记性别，统计达标好理解。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "身高记录仪测得的数据被发送到哪里进行存储与转发？",
        "options": ["冰箱", "物联网服务平台", "电视机", "书包"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据通过主控板网络发送到物联网服务平台，由其存储与转发。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网服务平台是数据的汇聚中心，与第21课一致。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“存储与转发”是物联网服务平台的职责，选对应项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据上网进平台，存储转发真不赖。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "搭建身高记录仪连接物联网服务平台时，需要进行的网络配置是？",
        "options": ["仅用蓝牙", "使用 wifi.connect 连接 Wi-Fi，并用 mqttclient.connect 配置 MQTT 服务器", "使用 U 盘拷贝", "使用收音机"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用 wifi.connect 设置 Wi-Fi，用 mqttclient.connect 配置 MQTT 服务器地址、端口、设备 ID、用户名和密码。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>联网与平台配置是物联系统上云的关键步骤。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>关键词“wifi.connect”“mqttclient.connect”对应正确项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>先连 Wi-Fi，再配 MQTT。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "对身高变化数据进行可视化分析，下列哪种方式不可用？",
        "options": ["物联网服务平台", "电子表格", "Python 模块", "收音机广播"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可用物联网服务平台、电子表格、Python 模块；收音机广播不是数据分析方式。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三处可视化途径在多个项目中反复出现。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除明显无关的“收音机广播”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台表格 Python，分析三件套。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "身高记录仪中，用来区分男生和女生并控制是否发送数据的是？",
        "options": ["超声波传感器", "按键 k1、k2", "温度传感器", "继电器"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过按键 k1、k2 控制测量并显示身高，并决定是否发送给平台，同时区分男女。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>按键属于输入控制设备，实现人机交互与流程控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“区分男女、控制发送”是按键功能，排除传感器类。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键 k1 和 k2，控测又控传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "身高记录仪统计各班身高检测情况后，结果应反馈给谁？",
        "options": ["负责老师", "陌生人", "电视台", "快递员"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>反馈与控制环节将统计结果反馈给负责老师，便于掌握体质健康。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>“反馈给负责老师”对应功能需求表中的反馈与控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>统计目的是服务教学管理，自然反馈给老师。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>测完统计好，反馈交老师。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "single",
        "stem": "为了让超声波传感器准确测量身高，传感器应当放置在什么位置？",
        "options": ["被测者头顶上方测量距离", "地面下方", "水容器中", "衣服口袋里"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>超声波传感器应放在被测者头顶上方，通过测距计算身高。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器位置决定测量对象，测量端设计是硬件搭建要点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“头顶上方测距”符合身高测量逻辑。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>头顶上方架超声，距离一减知身高。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "tf",
        "stem": "超声波传感器通过发射声波并检测回声的时间差来计算与目标物体之间的距离。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。这正是超声波测距的原理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该原理用于身高记录仪、奶牛产奶量等多种测量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第3题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>发波收回声，时间算远近。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "tf",
        "stem": "身高记录仪采集的数据只有性别，没有身高。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。采集的是“性别、身高”两类数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>项目目标明确为测量身高并统计，身高是核心数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“没有身高”与项目目标矛盾，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>性别身高都要采，缺一不可统计来。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "tf",
        "stem": "物联网服务平台负责存储与转发身高记录仪上传的数据。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。平台承担数据存储与转发职责。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该职责在所有物联项目中一致。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与多课知识一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台管存储，转发不费力。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "tf",
        "stem": "身高数据只能用物联网服务平台查看，不能用电子表格或 Python 分析。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。数据可在服务平台、电子表格、Python 中可视化分析。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三种分析形式贯穿第五单元。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能用平台”过于绝对，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>三法分析都可行，别把门路都堵死。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "multi",
        "stem": "身高记录仪系统功能实现包含下列哪些环节？（多选）",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节俱全：采集性别身高、传输存储、统计、反馈给老师。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>依旧是四环节框架。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四步走。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "multi",
        "stem": "对身高数据进行可视化分析，可采用的形式有？（多选）",
        "options": ["物联网服务平台", "电子表格", "Python 模块", "微波炉"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>服务平台、电子表格、Python 均可，微波炉无关。<br><br><strong style="color:#2980b9;">📚 知识点讲解：：</strong>三处分析途径是单元共性。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除家用电器微波炉。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台表格 Python。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "multi",
        "stem": "搭建身高记录仪可能需要哪些设备与平台？（多选）",
        "options": ["超声波传感器", "主控板", "物联网服务平台", "微波炉"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>需要超声波传感器、主控板、物联网服务平台，微波炉非必需。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器+主控板+平台是物联系统典型组成。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按本课硬件清单选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感主板加平台，身高记录搭起来。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "short",
        "stem": "请简述身高记录仪系统“采集、传输与存储、分析处理、反馈与控制”四个环节分别做什么。",
        "options": [""],
        "answer": "采集数据：用超声波传感器获取学生性别、身高；传输与存储数据：将性别、身高等数据发送并存储在物联网服务平台；分析处理数据：统计学生测量与身高达标情况；反馈与控制：将统计结果反馈给负责老师。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节紧扣“测身高—上传—统计—反馈老师”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>功能需求表明确四环节描述。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按本课功能表逐环节作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四环节，身高统计全涵盖。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "short",
        "stem": "超声波传感器是如何测量身高的？请说明其原理。",
        "options": [""],
        "answer": "超声波传感器会发射声波，并检测这些声波从目标物（如被测者头部）反射回来的回声。通过测量声波发射和接收之间的时间差，计算出传感器与目标之间的距离，从而推算出身高。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>原理是“发射—回声—时间差—距离—身高”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>超声波测距属距离传感器典型应用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>围绕“声波往返时间差算距离”展开说明。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>声波往返一时间，距离身高可计算。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L22",
        "lessonTitle": "健康生活新设备",
        "type": "short",
        "stem": "为什么说物联网让健康监测变得更智能化、便捷化？",
        "options": [""],
        "answer": "物联网将传感器、主控板与服务平台连接，可自动采集身高、心率等健康数据并实时上传，在平台上存储、分析与可视化，还能自动统计并反馈给老师。人们“无感”体验智能化生活，减少了人工测量与统计的费时费力，因此更智能、便捷。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>自动采集、远程查看、自动统计构成智能化便捷化。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>“无感”体验是物联网融入生活健康的特征。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从“自动+远程+统计”三方面说明价值。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自动采集远程看，健康智能又方便。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第22课 健康生活新设备'
    },

    # ===================== L23 医疗设施新功能 =====================
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "下列属于物联网在医疗中应用的体现是？",
        "options": ["智慧病房、智慧外科手术", "传统扫帚", "普通毛巾", "纸质病历"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>智慧病房、智慧外科手术是物联网赋能医疗的体现。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第六单元前仍属第五单元“应用探索”，医疗是重要方向。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“智慧”前缀说明智能化，符合物联网医疗。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>智慧病房手术台，物联医疗显能耐。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "病患输液监测系统可实时监测哪些与病患相关的数据？",
        "options": ["体温、心率、血压、输液袋余量、输液袋流速等", "仅室外气温", "仅汽车车速", "仅环境音量"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可监测体温、心率、血压、输液袋余量、输液袋流速等。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这些数据帮助护士及时掌握输液状态，减轻工作负担。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选包含多项生理与输液参数的第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>体温心率血压流，输液余量全都有。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "监测输液袋余量的方案1使用的是？",
        "options": ["光敏传感器（测量 LED 灯透过输液袋的光线值）", "压力传感器", "超声波传感器", "温度传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>方案1用光敏传感器测量 LED 透过输液袋的光线值判断余量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>有液体与无液体时透光强度不同，据此判断余量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“光线值”对应光敏传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光敏测透光，余量知端详。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "监测输液袋余量的方案2使用的是？",
        "options": ["光敏传感器", "压力传感器（测量输液袋的压力值）", "雷达", "麦克风"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>方案2用压力传感器测量输液袋的压力值判断余量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>液体多少影响压力，压力变化反映余量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“压力值”对应压力传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>压力变一变，余量看得见。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "在本课实验中，光敏传感器连接主控板的哪个端口？",
        "options": ["P0", "P3", "P9", "USB 口"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>光敏传感器连接主控板端口0（P0）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>硬件连接需对应引脚，程序中读取 pin0。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材明确“连接主控板端口0（P0）”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光敏接 P0，读数才可靠。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "当光照强度数据超出阈值范围时，系统会？",
        "options": ["自动进行提醒（如蜂鸣器报警）", "无任何反应", "自动关机", "播放音乐"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>光照强度超阈值时进行提醒，如蜂鸣器报警、LED 提示。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈与控制环节在异常时触发预警保护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“超阈值提醒”是标准响应。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超阈就提醒，护士忙不慌。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "病患输液监测系统的接收端（护士台）主要负责？",
        "options": ["接收数据并进行反馈", "在厨房使用", "在车库使用", "在操场使用"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>接收端位于护士台，负责数据接收与反馈。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>发送端采集、接收端（护士台）查看预警，构成远程监护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“护士台”对应医疗场景的接收反馈。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>发送采数据，护士台接收。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "采集到的输液监测数据被发送到哪里进行存储与转发？",
        "options": ["物联网服务平台", "冰箱", "电视机", "书包"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>主控板发送端把数据发到物联网服务平台存储转发。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>平台汇聚数据，接收端订阅主题即可远程查看。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>同前几课，平台负责存储转发。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据上平台，护士台可看。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "本课获取输液袋余量主要依据哪种传感器数据？",
        "options": ["光照强度", "声音大小", "气味浓度", "物体重量"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用光敏传感器读取光照强度，有液体与无液体时光照不同。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>光照强度是判断余量的关键量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>本课方案1即以光照强度判断余量。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光照强弱变，余量可判断。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "single",
        "stem": "下列关于病患输液监测系统的说法，错误的是？",
        "options": ["用光敏传感器检测输液袋余量", "可实现远程查看数据", "通过阈值探究设计算法实现反馈", "不需要任何传感器也能工作"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误项：系统必须用光敏等传感器采集，不可能“不需要任何传感器”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层依赖传感器，是物联系统的基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>找与事实相反的“无传感器”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>无传感不物联，此句记心田。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "tf",
        "stem": "光敏传感器通过测量 LED 灯透过输液袋的光线值来判断输液袋余量。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。有液体与无液体时光线值不同。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是监测余量方案1的原理。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第3题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>透光多少判余量。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "tf",
        "stem": "病患输液监测系统只需要采集数据，不需要反馈与控制。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。系统需在光照超阈值时进行提醒，属于反馈与控制。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>反馈与控制是四环节之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不需要反馈”违背功能需求表，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>四环节不能少，反馈很重要。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "tf",
        "stem": "护士台的接收端可以接收数据并进行反馈，实现远程监护。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。接收端接收数据并反馈，构成远程查看与预警。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>发送端与接收端配合实现远程医疗监护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第7题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>护士台一收，远程护患友。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "tf",
        "stem": "压力传感器也可用于监测输液袋余量，通过测量压力值实现。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。方案2即采用压力传感器。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>同一问题可有多种传感器方案。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第4题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>压力亦可行，方案任选一。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "multi",
        "stem": "病患输液监测系统的功能实现包含下列哪些环节？（多选）",
        "options": ["采集数据", "传输与存储数据", "分析处理数据", "反馈与控制"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节全选：采集光敏数据、传输存储、分析有/无液体光照、超阈提醒。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>四环节框架再次体现。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四步走。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "multi",
        "stem": "监测输液袋余量可采用的传感器方案有？（多选）",
        "options": ["光敏传感器", "压力传感器", "超声波传感器", "温度传感器"],
        "answer": [0, 1],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>本课给出方案1光敏、方案2压力；超声波、温度本课未用于此。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器选型要匹配被测量（透光/压力）。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按教材两种方案选前两项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光压两方案，余量都能看。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "multi",
        "stem": "搭建病患输液监测系统可能用到哪些硬件？（多选）",
        "options": ["光敏传感器", "板载蜂鸣器", "LED 指示灯", "微波炉"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用到光敏传感器（P0）、蜂鸣器（报警）、LED（P1 提示），微波炉无关。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>发送端采集+报警，接收端护士台反馈。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按硬件清单选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光敏蜂鸣 LED，报警三件套。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "short",
        "stem": "请简述病患输液监测系统“采集、传输与存储、分析处理、反馈与控制”四个环节分别做什么。",
        "options": [""],
        "answer": "采集数据：实时获取光敏传感器数据；传输与存储数据：将数据发送到物联网服务平台；分析处理数据：分析有液体与无液体时的光照强度差异；反馈与控制：光照强度超出阈值范围时进行提醒（如蜂鸣器报警）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四环节围绕“光敏采集—上传—判断光照—超阈报警”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>功能需求表明确各环节描述。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>依据本课功能需求表逐条作答。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采光传平台，超阈报警来。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "short",
        "stem": "为什么要用光敏传感器监测输液袋余量？请说明两种监测方案。",
        "options": [""],
        "answer": "输液袋内有液体与无液体时，LED 光透过输液袋的光线强度不同，可用光敏传感器读取光照值判断余量。两种方案：方案一用光敏传感器测量 LED 透过的光线值；方案二用压力传感器测量输液袋的压力值，液体多少对应压力变化。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>透光差异是光敏方案依据；压力差异是压力方案依据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>同一被测量可多角度传感实现。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先说原理，再分两种方案陈述。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>光压两法测余量，输液安全有保障。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L23",
        "lessonTitle": "医疗设施新功能",
        "type": "short",
        "stem": "物联网为医疗服务带来了哪些效率与质量的提升？",
        "options": [""],
        "answer": "物联网可实时监测病人体温、心率、血压、输液余量等，自动预警异常，减轻护士巡护负担；远程查看让护士台及时掌握多床位状态；智慧病房、智慧手术等提升诊疗效率与质量，使患者获得更便捷高效的医疗服务。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>提升体现在实时监测、自动预警、远程监护、效率质量双增。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>医疗是物联网重要应用场景。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从“减轻负担—及时预警—提升质量”展开。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>实时监测加预警，医疗高效又安心。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第23课 医疗设施新功能'
    },

    # ===================== L24 农业生产新模式 =====================
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "物联灌溉系统可实时监测什么，从而自动调节水量？",
        "options": ["土壤湿度和天气情况", "股票行情", "汽车车速", "音乐音量"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联灌溉实时监测土壤湿度和天气，自动调节水量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>精准灌溉节约水资源并保障作物健康。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>灌溉关注“土湿+天气”，其余无关。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>土湿天气都监测，自动灌溉节水多。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "物联养殖管理系统中，给动物佩戴传感器可以监测？",
        "options": ["体温、呼吸频率、位置、行为", "仅动物颜色", "仅动物名字", "仅动物价格"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可随时查看体温、呼吸频率等生理指标，并追踪位置与行为。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>养殖物联化提升照看效率与动物健康。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选含生理与位置行为的第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>体温呼吸加位置，养殖尽在掌握。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "在食品安全方面，可通过什么方式追溯农产品来源和生产过程？",
        "options": ["条形码、二维码", "仅靠味道", "仅靠颜色", "仅靠重量"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过条形码、二维码监管市场流动，追溯来源与生产过程。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>一物一码实现食品溯源，保障安全。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“追溯来源”对应条码/二维码标识。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>条码二维码，溯源靠住它。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "据调查，奶牛产奶量受遗传因素影响约占多少，其余与饲养管理有关？",
        "options": ["遗传因素约 30%，饲养管理约 70%", "遗传因素约 70%", "遗传因素约 100%", "与遗传无关"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>遗传影响约30%，饲养管理约70%，故管理是高产关键。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>良好饲养管理是奶牛高产稳产的重要保证。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材明确“遗传30%、管理70%”，选第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>遗传三成管七成，精细喂养产奶增。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "监测奶牛产奶量的方案1使用？",
        "options": ["超声波传感器（通过瓶口到液面距离计算产奶量）", "光敏传感器", "温度传感器", "湿度传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>方案1用超声波传感器测瓶口到瓶内液面的距离，计算产奶量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>超声波测距再次用于“量”。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“距离算产奶量”对应超声波。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超声测液面，产奶量可见。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "监测奶牛产奶量的方案2使用？",
        "options": ["压力传感器（通过容器压力变化计算产奶量）", "超声波传感器", "RFID 读卡器", "摄像头"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>方案2用压力传感器测量容器压力变化计算产奶量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>压力随液体多少变化，可用于计量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“压力变化”对应压力传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>压力一变化，产奶量可查。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "奶牛编号是通过什么设备采集的？",
        "options": ["电子标签和 RFID 读卡器", "超声波传感器", "温度传感器", "按键传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用 RFID 读卡器扫描奶牛电子标签获取编号。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>电子标签+读卡器是身份识别典型方案，也是第30课身份认证基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“编号/身份”对应 RFID 电子标签。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>电子标签 RFID，牛号一刷知。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "奶牛产奶监测系统的“分析处理数据”环节特点是？",
        "options": ["本项目不涉及分析数据的环节", "必须进行复杂的人工智能分析", "必须绘制三维图", "必须进行预警"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>本课项目明确“分析处理数据：本项目不涉及分析数据的环节”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>并非每个物联项目都含全部四环节的深度分析。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材原话“本项目不涉及分析数据的环节”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>本项目特殊，分析可不做。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "在本课系统中，超声波传感器主要用于测量？",
        "options": ["奶牛产奶量（液面高度）", "牛舍温度", "牛舍湿度", "环境光照"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>超声波传感器测容器液面高度，从而计算产奶量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>产奶量=液面高度换算。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除温湿光，选产奶量。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超声量液面，产奶算出来。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "single",
        "stem": "按键传感器在奶牛产奶系统中的作用主要是？",
        "options": ["手动控制是否将采集的数据发送到物联网服务平台", "测量温度", "显示数据", "提供电源"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>按键用于控制“是否发送数据到平台”（手动发送/控制功能）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>按键实现人机交互，控制上传时机。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“按键控制发送”为本课反馈与控制描述。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键一按，数据上传。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "tf",
        "stem": "物联养殖管理系统可实时追踪动物的位置和行为，以便更好地照顾它们。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。佩戴传感器可追踪位置与行为。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网提升养殖照看效率。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第2题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>位置行为可追踪。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "tf",
        "stem": "通过条形码、二维码可追溯农产品来源和生产过程，保障食品安全。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。条码/二维码实现溯源。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>食品溯源是物联网在农业的重要价值。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第3题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>一码溯来源，安全有保障。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "tf",
        "stem": "奶牛产奶量完全由遗传因素决定，与饲养管理无关。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。遗传仅约30%，饲养管理约占70%。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>管理是高产关键。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“完全由遗传决定”与教材数据矛盾。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>七分管理三遗传，莫说全靠基因管。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "tf",
        "stem": "奶牛产奶监测系统不需要传输与存储数据环节。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。系统需将采集数据发送到物联网服务平台。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传输与存储是远程呈现数据的前提。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不需要传输”违背功能需求，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据要上传，平台来收纳。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "multi",
        "stem": "物联网在农业生产中的应用包括？（多选）",
        "options": ["物联灌溉系统", "物联养殖管理系统", "食品追溯（条码/二维码）", "仅仅是扫地机器人"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>农业应用含灌溉、养殖、食品追溯；扫地机器人非农业重点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>本课导入即列举这三类。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按教材三项选前三。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>灌溉养殖加溯源，农业物联三件事。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "multi",
        "stem": "监测奶牛产奶量可采用的传感器方案有？（多选）",
        "options": ["超声波传感器", "压力传感器", "光敏传感器", "温湿度传感器"],
        "answer": [0, 1],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>方案1超声波、方案2压力；光敏、温湿度本课未用于产奶量计量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器要匹配被测量。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按两种方案选前两项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超声压力两方案。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "multi",
        "stem": "搭建奶牛产奶监测系统可能用到哪些设备？（多选）",
        "options": ["电子标签", "RFID 读卡器", "超声波传感器", "按键传感器"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类均用到：电子标签与RFID读卡器采牛号，超声波测产奶量，按键控制发送。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>硬件清单明确列出这些器材。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>标签读卡超声键，产奶系统全配齐。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "short",
        "stem": "请简述奶牛产奶监测系统四个功能环节，并说明“分析处理数据”环节的特点。",
        "options": [""],
        "answer": "采集数据：采集奶牛身份（电子标签）、产奶量（超声波）；传输与存储数据：发送到物联网服务平台；分析处理数据：本项目不涉及分析数据的环节；反馈与控制：显示奶牛编号和产奶量（按键控制手动发送）。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>突出“分析处理本课不涉及”这一特殊性。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>并非所有项目都完整分析，按需裁剪。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐环节描述并强调分析环节的特殊说明。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传显控四步走，分析本课可不做。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "short",
        "stem": "物联网如何改变传统农业生产方式？请举例说明。",
        "options": [""],
        "answer": "物联网使农业智能化：物联灌溉实时监测土壤湿度和天气自动调节水量，节约用水并保障作物生长；物联养殖通过佩戴传感器监测动物体温、呼吸、位置和行为；食品方面用条码/二维码追溯来源与生产过程，保障安全。从而提高效率与质量，减轻农民负担。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>从灌溉、养殖、溯源三方面说明智能化转型。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>农业是第五单元应用探索的重要领域。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>结合教材导入的三类例子展开。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>灌溉养殖加溯源，农业智能换新颜。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L24",
        "lessonTitle": "农业生产新模式",
        "type": "short",
        "stem": "为什么饲养管理对奶牛产奶量影响很大？物联网如何帮助提升产奶量？",
        "options": [""],
        "answer": "调查显示遗传影响仅约30%，饲养管理约占70%，良好管理是高产稳产的关键。物联网可通过传感器实时监测牛舍温湿度、饲料配比及奶牛生理指标，用奶牛产奶监测系统记录每头牛编号与产奶量，帮助养殖场科学管理、降低成本、提高产奶量和经济收入。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>管理占七成，物联提供数据支撑科学管理。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据驱动养殖决策。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先给比例数据，再说物联如何助力。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>七分管理三遗传，物联助力产奶涨。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第24课 农业生产新模式'
    },

    # ===================== L25 学习探究新工具 =====================
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "物联网可帮助教师做什么，从而提供精准教育服务？",
        "options": ["实时收集学习数据，评估进度与成果，调整教学计划", "仅播放视频", "仅打扫教室", "仅做饭"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联网可收集学习数据、评估进度，帮助教师调整计划。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网为教与学提供数据支撑与资源。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选与“教学评估”相关的第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据收一收，教学更精准。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "利用什么传感器可以帮助学习距离、半径、直径等概念？",
        "options": ["距离传感器或超声波传感器", "仅温度传感器", "仅湿度传感器", "仅光敏传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>距离/超声波传感器可测物体间距离，帮助理解距离、半径、直径。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联设备是学科探究的直观工具。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“距离概念”对应距离/超声波传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>超声量距离，几何好理解。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "热水降温规律实验设置了几组水杯条件进行对比？",
        "options": ["4 组（玻璃杯、玻璃杯加盖、不锈钢杯、不锈钢杯加盖）", "1 组", "2 组", "100 组"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用四个温度传感器分别测四种情况的水温。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>多对照组使结论更有说服力。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材明确四种材质/状态组合。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>玻璃不锈各加盖，四杯对照降温看。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "热水降温规律实验共使用了几个温度传感器？",
        "options": ["4 个", "0 个", "1 个", "2 个"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四个温度传感器对应四种水杯条件。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>每条件一传感器，便于同时采集。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第3题呼应，四个传感器。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>四杯四传感，同时测水温。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "上传数据到物联网服务平台时，关于主题（Topic）应注意？",
        "options": ["要设置 4 个不同名称的主题", "只设 1 个主题即可", "主题名称可以全部相同", "不需要设置主题"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>注意要设置4个不同主题，名称不能相同，以便区分各水杯数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>主题用于区分不同设备/数据源。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“4个、不同名”是教材明确提示。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>四杯四主题，名异不混淆。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "对热水降温实验数据进行分析，下列哪种方式不可用？",
        "options": ["物联网服务平台", "电子表格", "Python 模块", "收音机广播"],
        "answer": 3,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可用平台、电子表格、Python 分析；收音机广播不是分析方式。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三处分析途径为单元共性。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>排除无关设备。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>平台表格 Python。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "热水降温规律实验的“反馈与控制”环节情况是？",
        "options": ["本项目不涉及反馈与控制环节", "必须报警", "必须开门", "必须关灯"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>功能需求表明确“反馈与控制：本项目不涉及”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>实验重在采集与分析，无执行控制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>教材原话“本项目不涉及反馈与控制环节”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>本实验特殊，反馈可不做。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "为使实验结论更有说服力，可以怎么做？",
        "options": ["设置多个对照组", "只测一次", "不设置对照", "随便写结论"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可采取多个对照组增强说服力。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>对照实验是科学探究基本方法。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“多对照”是科学做法，其余不严谨。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>对照多一些，结论更可信。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "除材质、是否加盖外，热水降温实验还可采用什么对照条件？",
        "options": ["改变杯子口径", "改变杯子颜色名字", "改变杯子价格", "改变杯子品牌"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>还可改变杯子口径，观察相同时间内热水下降情况。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>变量设计要可控且有意义。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“杯子口径”是教材给出的对照变量。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>口径也能变，降温对照看。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "single",
        "stem": "热水降温规律实验的主要目的是？",
        "options": ["探究不同材质、不同状态下热水的降温规律", "煮饭", "洗衣服", "导航"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>通过传感器记录关键数据并分析，得出热水降温规律。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是跨学科科学实验的物联化探究。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>实验名即“热水降温规律”，选对应项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>降温规律探究清，物联实验显神通。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "tf",
        "stem": "物联网支持虚拟现实（VR）、增强现实（AR）技术应用，使抽象知识学习更直观。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联网为 VR/AR 提供支撑，提升学习兴趣。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网丰富教学资源与环境。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与导入内容一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>VR/AR 加物联，学习更直观。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "tf",
        "stem": "热水降温实验只用 1 个温度传感器即可完成四种条件的对比。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。需用 4 个温度传感器分别测四种情况。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>同时采集需每条件一传感器。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只用1个”与教材矛盾，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>四杯需四传感，一传不够看。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "tf",
        "stem": "实验获取的数据可在物联网服务平台、电子表格或 Python 中可视化呈现。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。三种分析呈现方式均可行。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是单元共性知识。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与多课一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>三处可视化，分析都不差。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "tf",
        "stem": "不锈钢杯与玻璃杯在相同条件下降温速度一定完全相同。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。不同材质导热性不同，降温速度不同，这正是实验要探究的。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>材质差异导致降温曲线不同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“一定完全相同”与实验目的矛盾。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>材质不同导热异，降温快慢不相同。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "multi",
        "stem": "关于热水降温规律实验功能环节，下列说法正确的有？（多选）",
        "options": ["用四个温度传感器采集四种情况的水温", "数据发送到物联网服务平台", "通过分析图表得出降温结论", "本项目不涉及反馈与控制环节"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四项均正确：四传感采集、上传平台、分析图表、反馈不涉及。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>覆盖采集、传输、分析、反馈（不涉及）全貌。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四环节，反馈本课免。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "multi",
        "stem": "可用于学习探究的物联网设备有？（多选）",
        "options": ["距离传感器", "温湿度传感器", "超声波传感器", "微波炉"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>距离/超声波助几何学习、温湿度监控实验；微波炉非学习探究设备。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器是学科探究工具。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按教材举例选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>距离温湿超声波，学习好帮手。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "multi",
        "stem": "设计热水降温实验的对照组，可设置哪些变量？（多选）",
        "options": ["不同材质水杯", "是否加盖", "杯子口径", "杯子价格"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>教材给出材质、是否加盖、杯子口径等变量；价格非科学变量。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>对照变量应影响降温过程。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选有物理意义的三个变量。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>材质加盖口径变，对照设计好比较。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "short",
        "stem": "请简述热水降温规律实验“采集、传输与存储、分析处理、反馈与控制”四个环节。",
        "options": [""],
        "answer": "采集数据：用四个温度传感器分别获取玻璃杯、玻璃杯加盖、不锈钢杯、不锈钢杯加盖四种情况的水温；传输与存储数据：将水温数据发送到物联网服务平台；分析处理数据：分析不同材质、是否加盖下的降温情况并得出结论；反馈与控制：本项目不涉及该环节。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>突出四环节及“反馈不涉及”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>功能需求表明确各环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐环节描述，强调反馈环节的特殊性。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>采传分反四环节，反馈本课免。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "short",
        "stem": "物联网如何为学科学习（如物理、科学实验）提供支持？请举例说明。",
        "options": [""],
        "answer": "物联网可实时收集学习数据帮助教师评估与调整教学；支持 VR/AR 让抽象知识直观；用距离/超声波传感器帮助理解距离、半径、直径；用温湿度传感器监控实验过程；如热水降温实验用四个温度传感器同步采集不同水杯水温，并在平台/表格/Python 中可视化分析，使探究更高效科学。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>从数据、资源、传感器探究三方面说明。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网是学习新工具。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>结合教材导入与实验案例展开。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据资源加传感，学习探究添翅膀。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },
    {
        "module": "第五单元 物联网应用探索",
        "lesson": "L25",
        "lessonTitle": "学习探究新工具",
        "type": "short",
        "stem": "设计科学实验时为什么要设置对照组？除材质和加盖外还可怎样设置对照？",
        "options": [""],
        "answer": "设置对照组可以控制变量、排除干扰，使实验结论更具说服力。除材质、是否加盖外，还可改变杯子口径，观察相同时间内热水下降情况；也可增减水量、改变初始水温等，形成多组对照。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>对照控变量、增信度；可变量含口径等。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>对照实验是科学方法基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先说意义，再列教材给出的对照变量。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>对照控变量，结论才可信。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第五单元/第25课 学习探究新工具'
    },

    # ===================== L26 数字世界有身份 =====================
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "虚拟身份是指？",
        "options": ["实体在数字世界中的代表，用于标识和识别实体的身份与属性", "公民的真实身份证", "纸质名片", "实物钥匙"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>虚拟身份是实体在数字世界中的代表，用于标识和识别身份属性。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>虚拟身份可以是数字证书、用户账户、设备标识等。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“数字世界中代表实体”即虚拟身份定义。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>虚拟身份数字身，标识识别它最行。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "在互联网中，用户虚拟身份大多指？",
        "options": ["各种平台中的账号信息", "身份证号本身", "用户血型", "用户身高"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用户虚拟身份多为各平台的账号信息。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网中用户虚拟身份更综合，还含生物特征、上网/出行数据。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“平台账号”对应用户虚拟身份。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>用户身份是账号，平台之上处处见。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "设备虚拟身份可能是？",
        "options": ["数字证书、唯一的设备标识、设备地理位置数据等", "用户姓名", "用户年龄", "用户爱好"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>设备虚拟身份可是数字证书、唯一设备标识或地理位置数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>联网设备也需唯一身份以便识别与管理。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选与“设备”相关的标识项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>设备也有身份证，证书标识加位置。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "网络摄像头上的二维码作用是？",
        "options": ["用手机应用扫描后，将该设备绑定到自己的账户下", "仅是装饰图案", "用于证明价格", "用于播放音乐"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>扫描摄像头二维码可将其绑定到用户账户，体现设备唯一标识。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是设备虚拟身份在生活中应用的例子。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“绑定账户”说明身份标识用途。<br><br><strong style="color:#e67e23;">🧠 记忆口诀：</strong>一扫二维码，设备归你管。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "通过唯一的虚拟身份，物联系统可以准确地将数据发送到指定目的地，这说明虚拟身份是？",
        "options": ["物联网数据传输的基础", "洗衣功能", "做饭功能", "扫地功能"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>唯一身份确保数据准确收发，是数据传输的基础。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如每辆汽车有唯一标识，用户据此识别自己的车。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“准确发送指定目的地”对应传输基础。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>唯一身份指方向，数据传输有保障。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "通过严格验证设备和用户身份，能够？",
        "options": ["防止未授权访问和操作，保护网络免受外部威胁", "让任何人都能访问", "主动泄露数据", "关闭整个系统"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>身份验证可防止未授权访问，保护安全，如车主只能控自己的车。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>虚拟身份对系统安全至关重要。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“防未授权”是身份验证目的。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>身份验证严，非法靠边站。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "汽车用户只能查看和控制自己的车辆，无法访问其他车辆，这主要说明虚拟身份对什么至关重要？",
        "options": ["系统安全", "外观颜色", "车辆价格", "车标形状"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>身份隔离防止越权，体现虚拟身份对系统安全至关重要。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>身份是访问控制与权限管理的基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能看自己车”对应安全/访问控制。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>身份定权限，安全记心间。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "系统根据虚拟身份中存储的偏好、习惯提供定制化体验，体现虚拟身份使？",
        "options": ["服务更加个性化", "数据泄露", "物理破坏", "网络隔离"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用偏好与历史提供定制体验，体现服务个性化。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如汽车自动识别用户并个性化设置。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“定制化体验”对应个性化。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>记住你喜好，服务更贴心。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "每个主控板都有？",
        "options": ["唯一标识", "两个完全相同的标识", "没有标识", "随机名字"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>每个主控板都有唯一标识，可用于识别与绑定。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>唯一标识是设备虚拟身份的体现，可读取并显示。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“唯一”是设备身份的关键特征。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>主板有唯一，识别靠它行。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "single",
        "stem": "通过记录刷脸开锁时间推测用户回家时间并自动控制家电，可能带来？",
        "options": ["新的安全隐患（如隐私泄露）", "绝对安全", "无任何影响", "仅节省电费"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>记录行为数据虽便利，但可能带来隐私泄露等新的安全隐患。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>便利与风险并存，需权衡安全。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“可能带来隐患”符合教材反思。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>便利添隐患，隐私要当心。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "tf",
        "stem": "在物联网中，不仅人，所有联网的物品也都有自己的“身份”（虚拟身份）。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联网连接人与物、物与物，物品也需虚拟身份。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>用户与设备均有虚拟身份。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与导入内容一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>人物皆有身份，物联才有序。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "tf",
        "stem": "设备虚拟身份只能是用户账户，不能是设备标识。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。设备虚拟身份可是数字证书、唯一设备标识或地理位置数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>设备身份与用户账户是两类不同虚拟身份。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只能是用户账户”违背定义，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>设备有标识，非仅账户也。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "tf",
        "stem": "严格的身份验证可以防止未授权访问，保护系统安全。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。验证身份是访问控制的核心。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>虚拟身份对系统安全至关重要。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第6题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>验证严一分，安全多一层。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "tf",
        "stem": "虚拟身份记录的偏好和历史仅用于收费，不能使服务个性化。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。系统利用偏好和历史提供定制化、个性化体验。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>个性化是虚拟身份的重要作用之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不能个性化”与教材相反，故错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>记你喜与好，个性服务到。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "multi",
        "stem": "虚拟身份可以是以下哪些形式？（多选）",
        "options": ["数字证书", "用户账户", "设备标识", "仅仅是纸质照片"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>虚拟身份可是数字证书、用户账户、设备标识等；纸质照片不是数字身份。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>虚拟身份是数字世界的代表形式。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三项数字形式。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>证书账户设备标，虚拟身份三件宝。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "multi",
        "stem": "虚拟身份在物联网中的重要作用包括？（多选）",
        "options": ["实现数据传输的基础", "对系统安全至关重要", "支持数据追踪和诊断", "使服务更加个性化"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四项皆是其作用：传输基础、系统安全、追踪诊断、个性化。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>教材总结四大作用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传输安全追踪个性，四大作用记清。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "multi",
        "stem": "物联网中塑造用户虚拟身份的数据包括？（多选）",
        "options": ["生物特征数据", "上网数据", "出行数据", "仅仅是身高"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物联应用中的传感器持续获取生物特征、上网、出行等数据，塑造用户虚拟身份；身高仅为其中一小部分，不能概括。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>用户虚拟身份更多元综合。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选教材列举的三类数据。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>生物上网加出行，拼出虚拟你。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "short",
        "stem": "什么是虚拟身份？用户虚拟身份和设备虚拟身份分别指什么？",
        "options": [""],
        "answer": "虚拟身份是实体在数字世界中的代表，用于标识和识别实体的身份和属性，可以是数字证书、用户账户、设备标识等。用户虚拟身份大多指各种平台中的账号信息，物联网中还包含生物特征、上网数据、出行数据等；设备虚拟身份则是数字证书、唯一设备标识或设备地理位置数据等，如网络摄像头二维码可绑定到用户账户。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>定义+两类身份分别解释。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>人与物皆有虚拟身份。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先给定义，再分用户/设备两类说明。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>虚拟身份数字身，用户设备各不同。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "short",
        "stem": "虚拟身份在物联网中有哪些重要作用？请列举至少三点。",
        "options": [""],
        "answer": "至少三点：①是物联网数据传输的基础，通过唯一身份准确发送和接收数据；②对系统安全至关重要，严格验证可防止未授权访问；③支持数据追踪和诊断，通过运行/历史数据定位问题；④使服务更加个性化，利用偏好与历史提供定制体验。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四项作用任写三点即可。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>教材总结四大作用。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>从传输、安全、追踪、个性化中选取。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传输安全追踪个性，作用四大宗。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L26",
        "lessonTitle": "数字世界有身份",
        "type": "short",
        "stem": "为什么通过唯一的虚拟身份标识能准确发送和接收数据？请举例说明。",
        "options": [""],
        "answer": "唯一虚拟身份相当于设备或用户的“地址”，系统据此寻址，把数据准确送达指定目的地，避免错发。例如每辆汽车都有独一无二的标识，用户正是通过该标识识别并只与自己的车辆通信，车企也能按标识向对应车辆发回状态数据，实现准确收发。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>唯一标识即“地址”，确保寻址准确。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>虚拟身份是数据传输基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>用“地址/寻址”比喻，并以汽车为例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>身份即地址，收发不错位。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第26课 数字世界有身份'
    },

    # ===================== L27 安全事件与风险 =====================
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "下列哪一项属于物理攻击类安全事件？",
        "options": ["直接破坏道路测速仪、监控摄像头等终端设备", "黑客远程入侵汽车", "利用摄像头发起拒绝服务攻击", "泄露用户数据"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>物理攻击类指直接对终端设备进行破坏，如破坏监控、3秒开智能门锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>物联终端常无人值守，易遭物理破坏。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“直接破坏设备”对应物理攻击。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>物理攻击毁终端，设备损坏最直观。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "利用设备配置缺陷、协议缺陷、程序缺陷等漏洞实施攻击，属于哪类安全事件？",
        "options": ["漏洞攻击类", "物理攻击类", "拒绝服务攻击类", "隐私数据泄露类"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用各种缺陷漏洞实施攻击即漏洞攻击类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如2015黑客利用汽车娱乐系统漏洞远程控车，召回140万辆。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“漏洞/缺陷”对应漏洞攻击类。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>漏洞攻击钻缺陷，远程控车是典型。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "2015年黑客利用某型号汽车车载系统漏洞远程控制汽车，厂商全球召回140万辆，这属于？",
        "options": ["漏洞攻击类", "物理攻击类", "拒绝服务攻击类", "隐私数据泄露类"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>利用系统漏洞远程操控，是漏洞攻击类典型事件。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该案例说明漏洞可致现实安全事故。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“漏洞+远程控制”锁定漏洞攻击类。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>车载有漏洞，远程被操控。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "2016年攻击者利用物联摄像头漏洞控制大批设备发起攻击，导致大面积通信瘫痪，这属于？",
        "options": ["拒绝服务攻击类", "物理攻击类", "漏洞攻击类", "隐私数据泄露类"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>控制大量设备发起攻击致通信瘫痪，是拒绝服务攻击（DoS）。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该事件致超25000台监控被感染。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“大面积瘫痪”对应拒绝服务。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>摄像头被控齐发难，服务拒绝全网瘫。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "某公司把80万用户数据存在开放数据库中，任何人无须密码即可访问，这属于？",
        "options": ["隐私数据泄露类", "物理攻击类", "漏洞攻击类", "拒绝服务攻击类"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用户私密信息被无防护暴露，属隐私数据泄露类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如玩具公司泄露儿童语音与账户信息。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“用户数据无密码可访问”即泄露。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据裸奔没人防，隐私泄露吃大亏。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "物联网感知层常见的安全风险包括？",
        "options": ["欺骗传感器、篡改传感器数据、窃取 RFID 数据", "仅颜色变化", "仅声音干扰", "仅重量变化"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>感知层风险有欺骗传感器、篡改数据、窃取RFID等。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层是数据采集前端，易受物理与数据层攻击。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选与传感器/RFID相关的第一项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知层风险三：骗篡改加窃。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "物联网三层结构中，负责通信和数据传输过程安全的是？",
        "options": ["网络层", "感知层", "应用层", "物理层"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络层安全风险指设备通信与数据传输过程中的安全问题。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三层为感知层、网络层、应用层。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“通信与传输”对应网络层。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网络管传输，通信安全它负责。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "2023年发现数百个非法涉外气象探测站点向境外实时传输气象数据，主要涉及哪类风险？",
        "options": ["隐私数据（重要数据）泄露类风险", "物理攻击类", "漏洞攻击类", "拒绝服务攻击类"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>气象数据违规出境属重要数据泄露，威胁国家安全。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据出境需符合《数据安全法》等规定。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“向境外传输数据”对应泄露类。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>气象数据出境外，国家安全受威胁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "为防止伪造和冒充设备身份，应当加强？",
        "options": ["传感器身份认证", "减小屏幕", "降低网速", "关闭电源"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>引入严格传感器认证机制，防止伪造和冒充。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是感知层防范“伪造”的策略。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“防伪冒”对应身份认证。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>加强认证关，伪造难冒充。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "single",
        "stem": "下列安全事件描述中，与“篡改”这一基本安全属性相对应的是？",
        "options": ["篡改传感器数据", "数据泄露", "服务中断", "设备伪造"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>“篡改”对应边篡改传感器数据，破坏数据完整性。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>泄露（保密性）、篡改（完整性）、中断（可用性）、伪造（真实性）是四类基本安全事件。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“篡改”直接对应篡改数据项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>篡改坏完整，数据被改动。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "tf",
        "stem": "物理攻击类安全事件是指直接对终端设备进行破坏造成的安全事件。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。直接破坏终端即物理攻击类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如监控被破坏、智能门锁被秒开。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第1题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>物理攻击毁设备。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "tf",
        "stem": "拒绝服务攻击只会影响单台设备，不会造成大面积通信瘫痪。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。大量设备被控发起DoS可致大面积通信瘫痪。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>2016摄像头事件即造成大面积瘫痪。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“只影响单台”与事实矛盾。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>DoS 非单台，全网可瘫痪。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "tf",
        "stem": "隐私数据泄露类安全事件直接关系到用户隐私和企业的商业机密。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。泄露类直接损害隐私与商业机密。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>如玩具公司、物联家居数据泄露事件。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第5题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>泄露伤隐私，机密也难保。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "tf",
        "stem": "物联网三层结构（感知层、网络层、应用层）各自面临不同的安全风险。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。三层各有侧重的安全风险。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层骗篡改窃、网络层通信、应用层平台风险。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>三层结构风险不同，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>三层各风险，防护要分层。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "multi",
        "stem": "教材将物联网安全事件分为以下哪四类？（多选）",
        "options": ["物理攻击类", "漏洞攻击类", "拒绝服务攻击类", "隐私数据泄露类"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类全选，即教材明确分类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是第27课核心分类框架。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>物理漏洞DoS泄露，四类事件记全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "multi",
        "stem": "物联网感知层的安全风险包括？（多选）",
        "options": ["欺骗传感器", "篡改传感器数据", "窃取 RFID 数据", "仅仅是网速变慢"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>感知层三类风险：欺骗、篡改、窃取RFID；网速慢非此类。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层是攻击前沿。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选教材列举的三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>骗篡改窃 RFID，感知三风险。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "multi",
        "stem": "从“泄露、篡改、中断、伪造”四类基本安全属性看，下列说法正确的有？（多选）",
        "options": ["泄露对应隐私数据泄露类事件", "篡改对应篡改传感器数据", "中断对应拒绝服务攻击造成的服务中断", "伪造对应伪造和冒充设备身份"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类基本属性与教材内容对应：泄露（保密性）—隐私泄露；篡改（完整性）—篡改数据；中断（可用性）—DoS瘫痪；伪造（真实性）—伪造冒充身份。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是信息安全四属性的经典概括。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>四项映射均正确，全选。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>泄篡中伪四属性，保密完整可用真。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "short",
        "stem": "教材将物联网安全事件分为哪四类？请各举一例。",
        "options": [""],
        "answer": "四类：①物理攻击类——破坏道路监控摄像头、3秒开智能门锁；②漏洞攻击类——2015黑客利用汽车漏洞远程控车，召回140万辆；③拒绝服务攻击类——2016利用物联摄像头漏洞发起DoS致大面积通信瘫痪；④隐私数据泄露类——某公司80万用户数据开放库无密码可访问、非法气象站点向境外传数据。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类+对应事例，紧扣教材案例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第27课核心分类。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>逐类列出并配教材实例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>物理漏洞DoS泄露，四类配案例。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "short",
        "stem": "物联网三层结构（感知层、网络层、应用层）分别面临哪些安全风险？",
        "options": [""],
        "answer": "感知层：欺骗传感器、篡改传感器数据、窃取RFID数据等；网络层：设备在通信和数据传输过程中发生的安全问题，如数据被窃听、劫持；应用层：物联网应用平台及支撑业务平台可能存在的各类安全问题。三层需分层防护。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>分层列举风险要点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三层结构各自风险不同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按感知/网络/应用三层分别说明。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知骗篡改，网络传中险，应用平台患。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L27",
        "lessonTitle": "安全事件与风险",
        "type": "short",
        "stem": "从“泄露、篡改、中断、伪造”四个基本安全属性角度，说明物联网可能面临的安全威胁。",
        "options": [""],
        "answer": "①泄露（保密性）：隐私或重要数据被无授权获取，如用户数据开放库被访问、气象数据出境；②篡改（完整性）：传感器数据被非法修改，如篡改传感器数据；③中断（可用性）：服务被阻断，如拒绝服务攻击致通信瘫痪；④伪造（真实性）：设备/身份被伪造冒充，需加强传感器认证防伪冒。四属性对应保密、完整、可用、真实。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四属性映射教材事件，说明对应威胁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>信息安全四属性经典框架。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>每属性给出定义与教材实例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>保密完整可用真，四性护物联。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第27课 安全事件与风险'
    },

    # ===================== L28 安全防范讲策略 =====================
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "下列策略中，不属于感知层防范的是？",
        "options": ["数据传输加密（属于网络层策略）", "物理安全", "多传感器融合", "加强传感器认证"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>数据传输加密是网络层策略；物理安全、多传感器融合、传感器认证属感知层。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分层防范，各层策略不同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>找“网络层”项作为非感知层答案。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知三层策，加密属网络。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "网络隔离是指？",
        "options": ["通过物理或逻辑手段将不同的网络环境相互隔离", "把设备堆放在一起", "拆除所有网络", "把屏幕调大"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络隔离通过物理或逻辑手段隔离不同网络，保障安全与完整。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是网络层重要防护手段。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“隔离不同网络”即网络隔离定义。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网络要隔离，风险不扩散。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "数据传输加密的作用是？",
        "options": ["将原始数据加密成密文，接收端解密还原，保护传输中隐私与完整性", "让数据体积变大", "删除数据", "公开数据内容"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>加密产生密文、接收端解密还原，保护传输中数据隐私与完整性。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>配合网络隔离共保网络安全。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“加密—解密—保护”是核心作用。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>明文变密文，传输才安稳。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "下列属于个人身份信息数据的是？",
        "options": ["姓名、生日、公民身份号码、手机号、邮箱、人脸、指纹、声波等", "仅有身高", "仅有血型", "仅有体重"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>个人身份信息含姓名、生日、身份证号、手机、邮箱及人脸指纹声波等生物特征。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这类数据易发生泄露，需重点保护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选包含多类身份与生物特征的项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>姓名生日证号脸，身份数据要护严。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "《中华人民共和国数据安全法》于何时通过？",
        "options": ["2021年6月10日", "2019年", "2022年", "2020年"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>2021年6月10日第十三届全国人大常委会第二十九次会议通过。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该法为数据处理、传输、出口设定明确标准。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>记忆“2021.6.10”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据安全法，二〇二一六月十。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "《数据安全法》第三十六条规定，非经哪一机关批准，境内组织、个人不得向外国司法或执法机构提供境内数据？",
        "options": ["中华人民共和国主管机关", "外国政府", "任意机构", "企业自身"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>非经中华人民共和国主管机关批准不得提供。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>该法强化重要数据出境监管，维护国家安全。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“主管机关批准”是法条原文关键词。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据出境严，主管来把关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "为应对硬件故障、自然灾害、恶意攻击，应当建立？",
        "options": ["数据备份和恢复机制（定期备份、异地备份）", "不备份", "只存一处", "删除旧数据"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>应定期备份并条件允许时异地备份，以便迅速完整恢复。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据存储备份是强化数据安全的重要措施。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“备份恢复”对应题干应对场景。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>定期加异地，备份保无忧。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "提升使用安全中，应当采用？",
        "options": ["强密码和多因素认证", "弱密码", "多个系统共用同一密码", "从不更新密码"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>应定时更新密码、采用强密码与多因素认证。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是提升应用层使用安全的关键。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“强密码+多因素”是唯一正确项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>强密多因子，使用更安全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "车联网汽车采集经纬度信息，数量汇集后可具备什么能力，其数据泄露会威胁国家安全？",
        "options": ["地图测绘能力", "播放音乐", "洗衣", "导航无关功能"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>大量经纬度汇集具备地图测绘能力，若泄露或存于国外服务器会威胁国家安全。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>测绘地理信息是国家安全重要保障。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“经纬度汇集=测绘能力”是教材要点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>经纬汇成图，泄露危国土。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "single",
        "stem": "为防范黑客利用漏洞攻击或窃取数据，应当？",
        "options": ["定期更新固件、安装系统补丁、进行安全审计", "从不更新", "关闭网络", "删除所有密码"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>应改进优化算法、定期更新固件、安装补丁、做安全审计评估。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是“改进优化算法”层面的防范。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“更新补丁+审计”是正确做法。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>勤打补丁做审计，漏洞难藏身。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "tf",
        "stem": "多传感器融合、加强传感器认证是防范感知层风险的策略。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。二者均为感知层防范策略。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>感知层策略含物理安全、多传感器融合、加强认证、防欺骗。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第1题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>多传加认证，感知防护稳。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "tf",
        "stem": "数据传输加密会把明文变成密文，接收端再用密钥解密还原。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。加密产生密文、接收端解密还原原始数据。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>加密保护传输中的隐私与完整性。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第3题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>明密互转，密钥把关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "tf",
        "stem": "数据存储只需保存在本地一台设备即可，无需备份。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。应定期备份并尽量异地备份，以应对故障、灾害、攻击。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>数据存储备份是重要措施。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“无需备份”违背数据安全原则。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>只存一处险，备份才保险。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "tf",
        "stem": "在多个系统使用相同的弱密码是安全的做法。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。应使用强密码、多因素认证并定期更新，避免同密码跨系统。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>弱密码与同密码会增加泄露连锁风险。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“弱密码安全”明显错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>弱密同密险，强密多因子安。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "multi",
        "stem": "物联网安全防范针对的层次包括？（多选）",
        "options": ["感知层", "网络层", "应用层", "大气层"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>针对感知层、网络层、应用层分别防范；大气层不是物联层次。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分层策略是本课主线。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选三层结构项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知网络应用，三层齐防范。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "multi",
        "stem": "网络层的安全策略包括？（多选）",
        "options": ["网络隔离", "数据传输加密", "仅仅是把屏幕调大", "仅仅是换颜色"],
        "answer": [0, 1],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络隔离与数据传输加密是网络层两大策略。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>二者配合防止数据被窃听、劫持、扩散。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前两项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>隔离加加密，网络双保险。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "multi",
        "stem": "物联网中容易发生泄露的数据类型包括？（多选）",
        "options": ["个人身份信息", "金融和支付信息", "健康和生理数据", "地理位置数据"],
        "answer": [0, 1, 2, 3],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>四类均属易泄露数据，还包括安全凭证密码、商业机密等。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>海量个人/家庭/行业数据须严格保护。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>全选四项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>身份金融健康位置，泄露高风险。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "short",
        "stem": "针对物联网感知层、网络层、应用层的安全风险，分别可采取哪些防范策略？",
        "options": [""],
        "answer": "感知层：物理安全、多传感器融合、加强传感器认证、传感器防欺骗（生物特征识别等）；网络层：网络隔离、数据传输加密；应用层/数据安全：加强数据监管、数据存储备份、数据访问控制，并改进优化算法、定期更新固件与补丁、提升用户安全意识与强密码策略。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>按三层+应用安全逐层作答。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>分层防范是本课核心。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>感知/网络/应用分别列举策略。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>感知防欺骗，网络隔离密，应用管数据。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "short",
        "stem": "《中华人民共和国数据安全法》对数据处理和出境有哪些规定？其意义是什么？",
        "options": [""],
        "answer": "规定：为数据处理、传输、出口设定明确标准，明确处理者职责，为重要数据设额外保护并规定法律责任；第三十六条规定非经中华人民共和国主管机关批准，境内组织个人不得向外国司法或执法机构提供境内数据；第三十一条规定重要数据出境适用《网络安全法》等。意义：强化数据监管、维护国家安全与公共利益，防止重要数据违规出境。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>涵盖标准、审批、出境与意义。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>《数据安全法》是数据安全核心法律。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>引用第三十六条、第三十一条要点并谈意义。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据出境要审批，安全监管有法依。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L28",
        "lessonTitle": "安全防范讲策略",
        "type": "short",
        "stem": "为什么车联网采集的地理位置数据大量泄露会威胁国家安全？应如何防范？",
        "options": [""],
        "answer": "原因：车联网汽车采集经纬度，数量汇集到一定程度即具备地图测绘能力；若数据泄露或存储在国外服务器，可能泄露我国地理测绘信息，影响国家安全。防范：落实《数据安全法》等要求，重要数据出境须审批；加强数据监管与访问控制、加密传输；关键数据境内存储，定期开展安全审计与用户教育。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>解释“经纬度→测绘能力→国家安全”，并给防范要点。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>测绘信息属国家安全保障要素。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先说危害机理，再列法律与技术防范。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>经纬成图涉密，监管加密守。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第28课 安全防范讲策略'
    },

    # ===================== L29 自主可控意义大 =====================
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "物联网对国外芯片依赖可能带来的风险是？",
        "options": ["进口芯片可能潜藏后门等安全漏洞，且紧急时供应可能受阻", "软件更新慢", "协议费用高", "仅仅是价格贵"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>进口芯片可能潜藏后门威胁安全，紧急时供应受阻影响系统运作。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>高端芯片与处理器是外部依赖风险之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“后门+供应受阻”是芯片风险要点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>芯片靠进口，后门断供愁。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "2020年哈工大、哈工程学生发现 MATLAB 被取消激活，说明哪方面风险？",
        "options": ["相关软件系统依赖国外技术", "芯片", "协议标准", "硬件传感器"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正版国外软件被取消激活，体现相关软件系统依赖风险。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>软件更新不及时、存在漏洞会致数据被监控或泄露。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“MATLAB软件”对应软件系统依赖。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>MATLAB 被停用，软件卡脖颈。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "若物联网设备通信标准都由外国公司制定，国内企业可能面临？",
        "options": ["知识产权约束和许可费用，限制产品设计与创新", "免费无约束", "更安全", "研发更快"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>标准受外国掌控会带来知识产权约束、许可费用，并限制创新。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>协议标准与知识产权是外部依赖风险之一。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“标准被控→约束费用”是教材要点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>标准握人手，创新受束缚。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "网络空间被称为国家第几疆域？",
        "options": ["第五疆域（陆、海、空、天之后）", "第一疆域", "第二疆域", "第三疆域"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>网络空间是人类继陆、海、空、天之后的第五疆域。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>网络空间主权是国家主权的重要组成部分。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“第五疆域”是教材原话。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>陆海空天网，第五疆域强。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "自主可控是维护什么的提前/前提？",
        "options": ["网络空间主权", "土地主权", "海洋主权", "领空主权"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>自主可控是维护网络空间主权的前提。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>网络空间主权是国家主权在网络空间的延伸。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第4题呼应，选网络空间主权。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主可控先，网权得保全。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "自主可控的内涵主要包括？",
        "options": ["自主技术、安全可控、国产化供应链", "仅进口", "仅抄袭", "仅外包"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>内涵含自主技术、安全可控和国产化供应链。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是第29课对“自主可控”的核心界定。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选正面三项内涵。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主安全国产链，内涵三要点。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "国家层面推动自主可控可采取？",
        "options": ["支持自主技术政策、资金税收优惠、强化科技创新教育", "减少投入", "限制教育", "依赖进口"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>国家应支持自主技术、提供资金与税收优惠、强化科技创新教育培育人才。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>国家层面是生态建设引领者。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选“支持+资金+教育”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>国策给资金，教育育人才。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "行业层面建设自主可控生态应？",
        "options": ["加强合作构建完整产业链，积极参与或领导国际标准制定", "各自为政", "拒绝合作", "放弃标准话语权"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>行业应加强合作构建产业链、参与或领导国际标准制定、强化产品服务安全。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>行业是生态建设的执行主体。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选“合作+标准”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>行业手牵手，标准抢前头。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "个人层面在自主可控方面可以？",
        "options": ["学习新技术、理解重要性、支持国产产品与本土品牌", "抵制国产", "不学习", "依赖外国"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>个人应学新技术、增强理解、支持国产软硬件与本土品牌。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>个人是生态建设的参与基础。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选“学习+支持国产”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>个人学技术，国产记心间。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "single",
        "stem": "关于自主可控，下列说法正确的是？",
        "options": ["自主可控不等于闭门造车，仍需国际合作交流", "完全无需合作", "只靠进口", "闭门造车即可"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>自主可控强调自主创新，但不等于闭门造车，国际合作仍重要。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>教材专门澄清“自主可控≠闭门造车”。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选“不等于闭门造车”项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主非封闭，合作亦相宜。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "tf",
        "stem": "进口芯片可能潜藏后门等安全漏洞，威胁系统安全。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。进口芯片风险之一是潜藏后门漏洞。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>芯片外部依赖风险。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第1题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>进口芯片藏后门。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "tf",
        "stem": "相关软件系统依赖国外技术不会带来数据被监控或泄露的风险。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。国外软件可能存在漏洞，增加数据被监控或泄露风险。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>软件系统依赖风险。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“不会带来风险”与事实相反。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>软件靠外人，泄露藏隐患。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "tf",
        "stem": "网络空间主权是国家主权的重要组成部分，自主可控是维护它的前提。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。网络空间主权是国家主权延伸，自主可控是其前提。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第五疆域与自主可控关系。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第4、5题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>网权属国家，自主是先决。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "tf",
        "stem": "自主可控就是完全自主研发解决一切问题，无需国际合作。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。自主可控不等于闭门造车，仍需国际合作交流。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确澄清误区。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“无需合作”违背教材观点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主非自闭，合作不可弃。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "multi",
        "stem": "物联网外部依赖可能造成的风险领域包括？（多选）",
        "options": ["高端芯片和处理器", "相关软件系统", "协议标准与知识产权", "仅仅是产品包装"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三类外部依赖风险：芯片、软件、协议标准与知识产权；包装非技术依赖。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是第29课风险框架。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三技术依赖项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>芯软标准三依赖，风险记心间。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "multi",
        "stem": "自主可控的内涵包括？（多选）",
        "options": ["自主技术", "安全可控", "国产化供应链", "完全依赖进口"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>内涵为自主技术、安全可控、国产化供应链；依赖进口相反。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第29.2节核心界定。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主安全国产链。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "multi",
        "stem": "建设自主可控物联网生态，各层面正确做法有？（多选）",
        "options": ["国家支持自主技术政策与教育", "行业加强合作、参与国际标准制定", "个人学习新技术并支持国产", "放弃国产、依赖进口"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>国家、行业、个人三层正确做法均选；放弃国产错误。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第29.3节生态建设三方协同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按三层正确做法全选前三。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>国行个三层，协同建生态。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "short",
        "stem": "物联网对国外技术依赖在芯片、软件、协议标准方面分别有哪些风险？",
        "options": [""],
        "answer": "芯片和处理器：进口芯片可能潜藏后门等安全漏洞威胁系统安全，紧急时供应可能受阻（如英伟达GPU受限）；软件系统：更新不及时、存在漏洞，增加数据被监控或泄露风险（如MATLAB被取消激活）；协议标准与知识产权：标准被外国掌控会带来知识产权约束与许可费用，限制产品设计与功能创新。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三方面风险分别展开，配教材事例。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>外部依赖三大风险领域。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按芯片/软件/标准三段说明并举例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>芯软标准三道坎，依赖藏隐患。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "short",
        "stem": "什么是自主可控？其内涵是什么？为什么自主可控对国家安全重要？",
        "options": [""],
        "answer": "自主可控指关键技术、产品与供应链自主掌握、安全可控。内涵包括自主技术、安全可控、国产化供应链。重要性：网络空间是第五疆域，网络空间主权是国家主权重要组成部分，自主可控是维护网络空间主权的前提；若关键技术受制于人，会在芯片后门、供应中断、数据泄露等方面威胁国家安全，因此必须自主可控。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>定义+内涵+重要性三层作答。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第29课核心概念与意义。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先定义，再列内涵，后联国家安全。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>自主可控内涵三，国安系网权。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L29",
        "lessonTitle": "自主可控意义大",
        "type": "short",
        "stem": "从国家、行业、个人三个层面，分别说明应如何建设自主可控的物联网生态。",
        "options": [""],
        "answer": "国家层面：制定支持自主技术的政策，提供资金支持和税收优惠，强化科技创新教育培育人才。行业层面：加强相互合作构建自主可控完整产业链，积极参与或领导国际标准制定，持续强化产品与服务安全性。个人层面：积极学习最新技术、提升自主可控知识与技能，加深对自主可控重要性的理解，支持国产产品与本土品牌。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>三层职责分明作答。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>第29.3节生态建设三方协同。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>按国家/行业/个人分别列出教材要点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>国给政策教人才，行建链定标准，个学技术挺国产。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第29课 自主可控意义大'
    },

    # ===================== L30 系统安全需升级 =====================
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "用照片即可欺骗摄像头打开物联门锁，说明原系统存在什么隐患？",
        "options": ["可被照片等非活体欺骗，缺少活体检测", "完全安全", "无法开锁", "仅能用密码"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>照片可骗过摄像头，说明缺少活体检测，存在被冒用隐患。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>活体检测是提升门锁安全的关键。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“照片欺骗”对应非活体隐患。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>一张照片能开门，活体检测不能省。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "为防止照片欺骗，物联门锁可增加什么功能？",
        "options": ["张嘴、眨眼等面部动作的活体检测", "把屏幕调大", "换种颜色", "加段音乐"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>增加张嘴、眨眼等面部动作识别，确认是真人再开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>动作活体检测是初级防欺骗手段。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“面部动作+活体”是教材方案。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>张嘴又眨眼，真人方过关。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "仅靠张嘴、眨眼等面部动作识别，仍可能被什么方式欺骗？",
        "options": ["AI 换脸技术生成的包含面部动作的视频", "静止照片", "声音", "文字"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>攻击者可用 AI 换脸生成带动作的视频欺骗系统。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>动作识别仍非绝对安全，需更强方案。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“视频欺骗”是教材指出局限。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>换脸成视频，动作也难防。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "更有效进行活体检测的方案是？",
        "options": ["使用深度摄像头采集脸部三维特征并配合复杂算法", "使用普通照片", "单摄像头不处理", "仅用麦克风"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>深度摄像头采集三维特征配合复杂算法，可抵御视频欺骗。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三维特征比二维动作更难伪造。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“深度摄像头+三维”是升级方案。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>深度采三维，换脸也难伪。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "物联门锁远程开锁订阅 MQTT 主题，收到什么消息会开锁？",
        "options": ["“open”", "“close”", "“stop”", "“hello”"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>门锁订阅“Door/Lock”主题，收到“open”即开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是原系统的远程开锁机制。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“open”对应开锁指令。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>主题等 open，收到就开门。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "该远程开锁方式的主要风险是？",
        "options": ["任何人只要接入 MQTT 服务器，都可发“open”开锁", "仅主人能发", "需要指纹", "需要声控"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>无身份认证，任何人接入服务器发“open”即可开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>缺少身份认证是重大隐患。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“任何人可发”即风险点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>无认证发 open，谁都能开门。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "用户身份认证的作用是？",
        "options": ["让系统知道“谁”在开门，非法用户则拒绝", "仅显示时间", "播放音乐", "记录温度"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>身份认证识别开门者身份，拒绝非法用户，提升安全。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>认证是系统安全升级核心措施。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“识别谁+拒绝非法”是认证目的。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>认证知是谁，非法拒门外。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "身份认证方案中将用户名和密码加入消息，如格式为？",
        "options": ["“user1, psd123, open”", "“open”", "“user1”", "“psd123”"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可采用“用户名,密码,指令”格式，如“user1, psd123, open”。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是简单的身份认证消息设计。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“用户名+密码+open”符合教材示例。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>名密令三字，一并发出门。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "模拟身份认证时，用 split() 解析数据后通常要做什么？",
        "options": ["将数据对比，决定是否执行开锁", "直接开锁", "直接关锁", "忽略数据"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>用 split() 解析消息，与存储的用户名密码对比，匹配才开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是任务2的实现要点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“解析+对比+决定”是认证流程。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>split 解析后，比对再开门。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "single",
        "stem": "用户名和密码在网络传输过程中使用明文，主要风险是？",
        "options": ["传输中被窃听或泄露", "绝对安全", "无法发送", "仅本地可见"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>明文传输易被窃听泄露，需加密解决。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>加密传输是系统安全升级的重要环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“明文=易泄露”是常识要点。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>明文满网跑，泄露风险高。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "tf",
        "stem": "用照片即可欺骗原物联门锁摄像头，说明其存在安全隐患。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。照片欺骗说明缺少活体检测。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>这是第30课引入的安全问题。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第1题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>照片能骗门，隐患确实存。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "tf",
        "stem": "仅靠张嘴、眨眼动作识别就能完全杜绝 AI 换脸视频的欺骗。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。仅靠动作识别仍可被 AI 换脸生成的视频欺骗，并非万无一失。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>动作识别只是初级活体检测，存在被视频伪造绕过的可能。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>“完全杜绝”过于绝对，与第3题一致，判断错误。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>动作也难防，换脸成视频。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "tf",
        "stem": "用户身份认证可以让系统识别开门者身份，拒绝非法用户。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。认证使系统知道“谁”在开门，非法则拒绝。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>身份认证是提升门锁安全的关键措施。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第7题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>认证识身份，非法拒门外。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "tf",
        "stem": "为提升安全性，对传输的用户名、密码数据应当进行加密。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。明文传输有泄露风险，加密可较好解决。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>加密传输是系统安全升级的重要环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>与第10题一致，判断正确。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>传输要加密，泄露可规避。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "multi",
        "stem": "提升物联门锁采集安全（活体检测）的方法包括？（多选）",
        "options": ["张嘴、眨眼等面部动作识别", "深度摄像头采集脸部三维特征", "配合更复杂的算法", "仅使用静态照片"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>动作识别、深度三维特征、复杂算法均可提升活体检测；静态照片不能防欺骗。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>活体检测逐级增强防伪能力。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三项，排除“静态照片”。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>动作深度加算法，活体层层防。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "multi",
        "stem": "物联门锁身份认证设计方案可包含哪些方式？（多选）",
        "options": ["用户名和密码", "多因素认证", "生物特征识别", "完全不需要认证"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>可用用户名密码、多因素认证、生物特征等；完全不认证会留隐患。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>认证方式可组合增强安全。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三项。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>名密多因子，生物再加固。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "multi",
        "stem": "保障物联门锁系统安全升级的措施包括？（多选）",
        "options": ["摄像头活体检测", "用户身份认证", "加密传输", "明文传输密码"],
        "answer": [0, 1, 2],
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>活体检测、身份认证、加密传输均提升安全；明文传输反而增加风险。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>三者是本课系统升级核心要点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>选前三项，排除明文。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>活体认证加加密，门锁三保险。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "short",
        "stem": "原物联门锁存在哪些安全隐患？如何通过活体检测提升安全性？",
        "options": [""],
        "answer": "隐患：①照片可欺骗摄像头，缺少活体检测；②远程开锁订阅MQTT主题，任何人接入服务器发“open”即可开锁，缺少身份认证。提升：增加张嘴、眨眼等面部动作识别，确认是真人再开锁；进一步用深度摄像头采集三维特征并配合复杂算法，抵御AI换脸视频欺骗。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>两大隐患：非活体欺骗、无身份认证远程开锁。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>活体检测是采集端安全升级重点。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先列隐患，再说动作/三维活体方案。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>照片能骗门，活体来补牢。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "short",
        "stem": "什么是用户身份认证？在物联门锁中如何实现简单的身份认证？",
        "options": [""],
        "answer": "用户身份认证是让系统知道“谁”在开门，若是非法用户则拒绝开门，从而提升安全。简单实现：将用户名和密码加入开锁消息，如“user1, psd123, open”；门锁端增加数据存储（列表存用户名密码），用 split() 解析消息，与存储数据对比，匹配才执行开锁，非授权用户发送消息舵机不转动。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>认证=识别身份并授权；实现靠用户名密码比对。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>任务1、任务2即设计实现简单认证。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先定义后给消息格式与 split 比对流程。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>名密加指令，split 比对开。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    },
    {
        "module": "第六单元 物联网安全",
        "lesson": "L30",
        "lessonTitle": "系统安全需升级",
        "type": "short",
        "stem": "为什么用户名、密码明文传输有风险？应如何解决物联网中的数据传输安全问题？",
        "options": [""],
        "answer": "风险：不同系统常用相同用户名密码，一旦某系统明文数据被泄露，其他平台也受威胁；明文在网络传输中易被窃听泄露。解决：对传输数据加密，利用算法设计加密传输规则（如加随机盐、对称加密等），并配合身份认证、网络隔离等措施，保障传输的保密性与完整性。",
        "analysis": '<strong style="color:#c0392b;">🎯 答案解析：</strong>明文易窃听、易连锁泄露；加密可较好解决。<br><br><strong style="color:#2980b9;">📚 知识点讲解：</strong>加密传输是系统升级重要环节。<br><br><strong style="color:#27ae60;">💡 解题思路：</strong>先说风险机理，再给加密等对策。<br><br><strong style="color:#e67e22;">🧠 记忆口诀：</strong>明文满网跑，加密方安稳。<br><br><strong style="color:#8e44ad;">📖 教材索引：</strong>第六单元/第30课 系统安全需升级'
    }
]