# -*- coding: utf-8 -*-
# 八年级 物联网实践与探索 第一单元(从感知到物联)、第二单元(万物互联有协议) 练习题
# L01-L10 每课 20 题，合计 200 题
# 题型：10 单选(single) + 4 判断(tf) + 3 多选(multi) + 3 简答(short)

Q12 = [
    # ===================== 第一单元 从感知到物联 =====================
    # ---------- L01 开启物联网之门 ----------
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "物联网的英文缩写 IoT 是下列哪个短语的缩写？",
        "options": ["A. Internet of Things", "B. Interoperability of Technology", "C. Integration of Tools", "D. Information of Telecom"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，IoT是Internet of Things的缩写，意为“物品的互联网”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>IoT即Internet of Things，中文译为物联网，指把物品用互联网连接起来，也就是“万物互联”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>其余选项均为干扰拼凑，只有Internet of Things符合“I和T”的缩写含义。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>IoT就是“物”的网，Internet of Things记心上。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "物联网的核心和基础仍然是下列哪一项？",
        "options": ["A. 传感器", "B. 互联网", "C. 人工智能", "D. 大数据"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，物联网是在互联网基础上发展起来的，其核心和基础仍然是互联网。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网是“物物相连的互联网”，把互联网从人与人的连接扩展到了人与物、物与物的连接。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>抓住“核心和基础”这一关键词，传感器只是感知部件，互联网才是根基。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联网，根在互联网；连万物，基础不能忘。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "现阶段物联网中的“物”主要是指什么？",
        "options": ["A. 世界上所有的物品", "B. 装有传感器并且能与互联网相连的物品", "C. 仅指计算机", "D. 仅指手机"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，现阶段物联网中的“物”主要指装有传感器并能与互联网相连的物品。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网中的“物”泛指各种物品，但并非所有物品都已联网，当前主要是带传感器且能联网的物品。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>排除“所有物品”的绝对说法，结合“装有传感器并能联网”这一限定条件判断。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联之“物”，传感+联网才算数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "物品要接入互联网，不需要具备以下哪个条件？",
        "options": ["A. 有名字（可被识别的唯一编码）", "B. 可感知（能提供物品本身的数据）", "C. 能传输（可与其他物品交换数据）", "D. 必须内置人工智能芯片"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，物品联网只需“有名字、可感知、能传输”三条件，不要求必须有人工智能芯片。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物品联网三条件：有名字（唯一编码）、可感知（提供自身数据）、能传输（交换数据）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>前三项为教材明确条件，D项“必须AI芯片”明显过度要求，属干扰项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>联网三件宝：有名、能感、会传。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "与互联网相比，物联网增加了什么能力？",
        "options": ["A. 人工采集数据", "B. 由传感器自动获取数据", "C. 视频播放", "D. 文字处理"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，物联网增加了自动获取数据的能力，数据可由传感器感知并自动采集。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>互联网基于人，数据靠人采集；物联网基于物，数据由传感器自动采集，这是二者最大区别。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>对比“人采集”与“传感器自动采集”的差异即可排除错误项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>互联网靠人采，物联网靠传感自动来。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "互联网主要是基于什么的网络？",
        "options": ["A. 物", "B. 人", "C. 传感器", "D. 云"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，互联网是基于人的网络，数据在某种意义上是靠人来采集的。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>互联网实现人与人的互联，数据主要靠人采集；物联网实现人与物、物与物互联，靠传感器采集。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“基于人”是教材原话，与“物联网基于物”形成对比。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>互联网靠人，物联网靠物。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "互联网到物联网的发展经历了三个阶段，正确的演进顺序是？",
        "options": ["A. 物物互联→人人互联→计算机互联", "B. 计算机互联→人人互联→物物互联", "C. 人人互联→计算机互联→物物互联", "D. 计算机互联→物物互联→人人互联"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，发展顺序是计算机互联→人人互联→物物互联（物联网）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>最初是计算机与计算机连接，后手机普及实现人人互联，再发展为物品接入网络的物联网。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按时间逻辑：先有计算机联网，再有人人移动互联，最后万物互联。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>机连人连再物连，三阶段别颠倒。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "我国于哪一年提出“感知中国”概念，推动物联网快速发展？",
        "options": ["A. 1999年", "B. 2009年", "C. 2019年", "D. 2023年"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，2009年“感知中国”概念提出，物联网迎来快速发展。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>我国物联网起步早，1999年中科院开始传感网研究，2009年提出“感知中国”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>注意区分1999（开始研究）与2009（感知中国），题干问“感知中国”对应2009。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>九九研究，零九感知中国。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P13-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "中国科学院从哪一年开始了物联网（传感网）相关研究？",
        "options": ["A. 1999年", "B. 2009年", "C. 2015年", "D. 2023年"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，中国科学院于1999年开始了传感网（物联网前身）相关研究。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>我国物联网最早被称为“传感网”，中科院1999年起步，2009年“感知中国”推动发展。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干问“开始研究”，对应1999年，而非2009年提出概念。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>九九起步研究，零九提出概念。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P13-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "single",
        "stem": "截至2023年12月，我国三家基础电信企业发展的蜂窝物联网终端用户约为多少？",
        "options": ["A. 2.32亿户", "B. 23.32亿户", "C. 232亿户", "D. 0.232亿户"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，截至2023年12月为23.32亿户。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材引用数据：我国三家基础电信企业发展蜂窝物联网终端用户23.32亿户，建成全球最大移动通信网络。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>注意数量级，“23.32亿户”是原文数据，排除其他数量级干扰。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>二三·三二亿，蜂窝物联用户数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P13-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "tf",
        "stem": "物联网就是“物品的互联网”，也就是将物品用互联网络连接起来。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联网即Internet of Things，意为“物品的互联网”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>“物联网”是Internet of Things的直译，指把物品用互联网连接起来，也称“万物互联”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干与教材定义一致，判断为正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联=物品+互联网。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "tf",
        "stem": "互联网和物联网没有关系，是完全独立的两张网。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。物联网的核心和基础仍然是互联网，是在其基础上发展起来的。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网是“物物相连的互联网”，并非独立网络，而是互联网的延伸与扩展。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“完全独立”与“核心基础是互联网”矛盾，故错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联根在互联网，并非两张网。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "tf",
        "stem": "给每个联网物品分配唯一标识（如IP地址），是物品上网的必要条件之一。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物品要上网需有“名字”，即可被识别的唯一编码（身份标识）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>联网三条件之首是“有名字：有可被识别的唯一编码”，用于标识物品。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“唯一标识”对应“有名字”条件，表述正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>上网先有名，标识不可少。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "tf",
        "stem": "现阶段我们已经能做到让世界上所有的物品都连上互联网。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。现阶段还无法做到所有物品都上网，主要是装有传感器并能联网的物品。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确指出“目前我们还无法做到所有的物品都上网”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“所有物品”说法绝对化，与教材“无法做到所有”矛盾。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>并非万物皆上网，传感联网才登场。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "multi",
        "stem": "物品接入互联网一般需要具备哪些条件？（多选）",
        "options": ["A. 有名字（可被识别的唯一编码）", "B. 可感知（能提供物品本身的数据）", "C. 能传输（可与其他物品交换数据）", "D. 必须连接5G网络"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。物品联网三条件是“有名字、可感知、能传输”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>联网三条件为：有名字（唯一编码）、可感知（提供自身数据）、能传输（交换数据）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D项“必须连接5G”过度要求，并非必要条件，排除后选ABC。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>有名、能感、会传，三者齐全可联网。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "multi",
        "stem": "下列哪些属于生活中已经联网的物品？（多选）",
        "options": ["A. 电视", "B. 摄像头", "C. 热水器", "D. 门锁"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。教材表中电视、摄像头、热水器、门锁均已联网。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举：电视（更多节目源）、摄像头（远程查看）、热水器（回家前启动）、门锁（记录开门人并通知）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材明确举例的联网物品，全部选入。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>电视摄像热水锁，联网生活好处多。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "multi",
        "stem": "关于物联网与互联网的关系，下列说法正确的有哪些？（多选）",
        "options": ["A. 物联网的核心和基础仍然是互联网", "B. 物联网的数据可由传感器自动采集", "C. 互联网的数据主要靠人采集", "D. 物联网完全不需要互联网"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。物联网以互联网为基础，且传感器自动采集区别于人采集。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>互联网基于人、数据靠人采；物联网基于物、数据由传感器自动采，二者核心基础相同。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D项“完全不需要互联网”违背“核心基础是互联网”，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>基础同是网，采数人传感。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "short",
        "stem": "请简要说明物联网与互联网的关系。",
        "options": [""],
        "answer": "物联网的核心和基础仍然是互联网，是在互联网基础上发展起来的；物联网是“物物相连的互联网”，把互联网从人与人的连接扩展到了人与物、物与物的连接。互联网基于人、数据靠人采集，物联网基于物、数据由传感器自动采集。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>物联网以互联网为核心基础，是其延伸与扩展。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>互联网实现人人互联，物联网在其上实现人与物、物与物互联，二者一脉相承。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从“基础相同、连接对象扩展、采集方式不同”三方面作答即可。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>同根互联网，扩展人物物。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11-14）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "short",
        "stem": "物品要连接互联网一般需要具备哪三个基本条件？",
        "options": [""],
        "answer": "①有名字：有可被识别的唯一编码；②可感知：能提供物品本身的数据；③能传输：可与其他物品交换数据。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>三条件是“有名字、可感知、能传输”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物品联网须具备身份（唯一编码）、感知（提供数据）、传输（交换数据）三项能力。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>紧扣教材“联网三条件”原文，分三点作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>有名、能感、会传，上网三件宝。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L01",
        "lessonTitle": "开启物联网之门",
        "type": "short",
        "stem": "现阶段物联网中的“物”主要指什么？为什么还不能让所有物品都联网？",
        "options": [""],
        "answer": "现阶段主要指装有传感器并且能与互联网相连的物品。因为并非所有物品都装有传感器且具备联网能力，技术、成本、功耗等也限制了全面联网，所以目前还无法做到所有物品都上网。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>“物”指带传感器能联网的物品；全面联网尚难实现。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确“目前我们还无法做到所有的物品都上网”，联网需传感与网络能力支撑。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>先答定义，再从传感能力、技术成本功耗等角度说明限制。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感+联网方为物，全面联网尚不足。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第1课 开启物联网之门（P11）。'''
    },

    # ---------- L02 传感之古今未来 ----------
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "传感器在物联网中相当于人的什么？",
        "options": ["A. 大脑", "B. 感觉器官（电五官）", "C. 手脚", "D. 心脏"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，传感器是物联网的感觉器官，被称为人类的“电五官”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器如同人的眼耳鼻舌身，用于获取目标对象的各种数据，是物联网感知世界的基础。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“感官/电五官”是教材原比喻，对应感觉器官。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感器，电五官，感知世界靠它探。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P15-18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "下列哪种古代发明可视为最古老的传感器之一？",
        "options": ["A. 指南针", "B. 电灯", "C. 电话", "D. 计算机"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，指南针（司南）利用地球磁场原理，是古代传感器代表。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>我国古代指南针、日晷、沙漏等因具有感知能力，可视为最古老的传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>电灯、电话、计算机均为现代产物，只有指南针属古代感知装置。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>司南指南针，古老传感器。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P15-16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "日晷和沙漏主要用来感知什么？",
        "options": ["A. 温度", "B. 时间", "C. 湿度", "D. 声音"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，日晷利用日影测时刻，沙漏控制沙粒掉落测时间。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>日晷是计时仪器，沙漏、水钟也是古代利用流动测时间的装置，都属于感知时间的传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>二者共同点都是“测时间”，直接对应B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>日影沙漏流，古代计时手。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "传感器的定义是下列哪一个？",
        "options": ["A. 一种电子游戏", "B. 能将感应到的数据按一定规律转换成可用信号的器件或装置", "C. 一种网络协议", "D. 一种存储设备"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，这是教材给出的传感器定义。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器是一种能将感应到的数据按一定规律转换成可用信号的器件或装置，满足传输、处理、存储等要求。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>抓住“转换信号”的本质，排除游戏、协议、存储等无关项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感=感数据，转信号。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "人的听觉能感知的声波频率范围约为？",
        "options": ["A. 0~20Hz", "B. 20Hz~20KHz", "C. 20KHz~20MHz", "D. 任意频率"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，人的听觉范围约为20Hz~20KHz。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出人的听觉仅能感知20Hz~20KHz之间的声波，传感器可“听”到超声波。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记牢“20Hz~20KHz”这一区间，区别于视觉的可见光频段。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>人耳二十到两万，超声红外它不见。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P17）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "人的视觉能感知的是哪部分光？",
        "options": ["A. 紫外线", "B. 红外线", "C. 可见光", "D. X射线"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，人的视觉仅能感知可见光部分。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>人眼可见光频率约3.9×10^14~7.5×10^14Hz，传感器可利用光敏元件“见”到红外与紫外。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“可见光”是教材明确范围，紫外、红外、X射线均非人眼可感。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>人眼只见可见光，传感能探红紫外。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P17）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "智能手机中用于检测环境光强度并自动调节屏幕亮度的传感器是？",
        "options": ["A. 加速度传感器", "B. 光敏传感器", "C. 磁力传感器", "D. 陀螺仪"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，光敏传感器检测环境光强度以调节屏幕亮度。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>手机集成光敏传感器，随时检测光强，使屏幕根据环境光线自动调节亮度。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“光强度→调亮度”对应光敏传感器，排除加速度、磁力、陀螺仪。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>光敏测光调亮度。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "智能手机中用于测量步数、检测运动方向的传感器是？",
        "options": ["A. 光敏传感器", "B. 距离传感器", "C. 加速度传感器", "D. 磁力传感器"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，加速度传感器检测x、y、z三方向加速度，用于测量步数。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>加速度传感器检测三轴加速度，手机据此知道运动方向并计步。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“计步”是加速度传感器的典型应用，区别于光敏、距离、磁力。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>加速三轴测步数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "手机中“指南针”应用软件主要依靠哪种传感器？",
        "options": ["A. 磁力传感器", "B. 光敏传感器", "C. 陀螺仪", "D. 温度传感器"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，磁力传感器检测周围磁场强度，用于指南针应用。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>磁力传感器检测手机周围磁场强度，配合指南针软件指示方向。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>指南针靠磁场，对应磁力传感器。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>磁力传感做指南。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "single",
        "stem": "现代传感器的发展趋势不包括以下哪项？",
        "options": ["A. 集成化", "B. 智能化", "C. 越来越笨重", "D. 无线化"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，趋势是更小、更强、更节能，而非越来越笨重。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器向更智能、更便捷、更集成方向发展，体积更小、功能更强、价格更低、更节能。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“越来越笨重”与“体积小、功能强”趋势相反，为错误项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>集成智能无线化，笨重可不是方向。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "tf",
        "stem": "传感器能将不易测量的物理量转化为容易测量的量（如电学量）。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。传感器实质是将不易测的物理量转化为易测的电学量等。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器由敏感元件（感知）和转换元件（转成可传输度量的信号）构成。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“转换信号”是传感器本质，表述正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>难测转易测，传感真本事。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "tf",
        "stem": "指南针（司南）是利用地球磁场原理来指示方向的古代传感器。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。指南针利用地球磁场确定方向，是古代传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>司南利用地球磁场原理指示方向，属最古老传感器之一。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>与教材“指南针利用地球磁理原理”一致，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>司南靠磁场，方向它来指。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "tf",
        "stem": "古代传感器精度通常较高，已经能和现代传感器媲美。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。古代传感器基于简单物理原理、依赖经验，精度相对较低。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确古代传感器“精度相对较低”，现代传感器精度高、形态各异。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“已经能媲美”与“精度相对较低”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>古传精度低，今传更精细。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P15-16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "tf",
        "stem": "同一种传感器只能应用在一个领域，不能跨领域使用。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。同一种传感器可应用于不同领域，如温度传感器用于工业和医疗。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出“同一种传感器可以应用在不同领域”，也提到实现同一功能可用不同传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“只能一个领域”过于绝对，与教材举例矛盾。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>一传感多用，一功能多传感。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P17）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "multi",
        "stem": "下列哪些属于古代传感器的例子？（多选）",
        "options": ["A. 指南针", "B. 日晷", "C. 沙漏", "D. 蓝牙"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。指南针、日晷、沙漏均为古代传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>古代传感器还有圭表、水钟、测风器、测雨器等；蓝牙是现代无线通信技术。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D项蓝牙是现代通信协议，非古代传感器，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>指南日晷沙漏，古传三代表。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P15-16）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "multi",
        "stem": "下列哪些是教材中提到的常见传感器？（多选）",
        "options": ["A. 温度传感器", "B. 土壤湿度传感器", "C. 加速度传感器", "D. 红外热释电传感器"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均为教材列举的常见传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材还列举了光敏、声音、图像、磁力、位置、气压、超声波、紫外线、称重等传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材明示传感器，全部选入。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿加速红外，传感种类多。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P17）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "multi",
        "stem": "智能手机集成了多种传感器，下列对应关系正确的是？（多选）",
        "options": ["A. 光敏传感器—调节屏幕亮度", "B. 距离传感器—打电话靠近耳朵自动熄屏", "C. 加速度传感器—测量步数", "D. 磁力传感器—指南针应用"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均符合教材手机传感器对应关系。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>光敏调亮度、距离防误触、加速度计步、磁力做指南针，陀螺仪测方向角速度。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>逐项对照教材手机传感器功能表，四项全部正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>光调亮、距熄屏、加速步、磁力针。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "short",
        "stem": "请说明现代传感器相比古代传感器有哪些进步/特点。",
        "options": [""],
        "answer": "古代传感器基于简单物理原理、依赖经验、精度较低；现代传感器利用光、声、磁、力等原理，种类多、精度高、形态各异，并正朝着集成化、智能化、无线化方向发展，已从简单电子零件发展为具有感知、计算、存储、传输功能的集成化装置。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>现代传感器精度高、种类多、集成智能无线化。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>对比古代（简单、低精度）与现代（高精度、集成化装置）传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从原理、精度、形态、发展趋势几方面比较作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>古简今精，集成智能无线行。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P15-18）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "short",
        "stem": "用生活中的例子说明“同一种传感器可应用在不同领域”或“实现同一功能可用不同传感器”。",
        "options": [""],
        "answer": "同一种传感器跨领域：温度传感器既可用于工业监控温度，也可用于医疗监测病人体温。实现同一功能用不同传感器：测量无人机飞行高度，可用气压传感器、超声波传感器或红外传感器。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>用温度传感器的跨领域和测高度的多种传感器说明。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材强调同种传感器多领域、同功能多传感器两种现象。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>各举一个教材原例即可完整得分。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>一传感多用，一功能多传感。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P17）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L02",
        "lessonTitle": "传感之古今未来",
        "type": "short",
        "stem": "传感器由哪两部分核心环节构成？各自作用是什么？",
        "options": [""],
        "answer": "敏感元件——直接感受或响应被测量，感知环境数据、接收输入信号；转换元件——将敏感元件的变化转换成适合传输和度量的信号，实现信号输出。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>敏感元件感知输入，转换元件输出信号。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将敏感元件与转换元件抽象为“计算”，前者感知、后者转换输出。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分两点答出“感知”与“转换输出”的作用。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>敏感来感知，转换出信号。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第2课 传感之古今未来（P16）。'''
    },

    # ---------- L03 环境数据要感知 ----------
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "声音的强弱通常用什么单位表示？",
        "options": ["A. 赫兹（Hz）", "B. 分贝（dB）", "C. 瓦特（W）", "D. 安培（A）"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，声音强弱用分贝（dB）表示。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>噪声大小用分贝衡量，过大噪声损害听力、神经系统和心脑血管系统。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>Hz是频率、W是功率、A是电流，dB才是响度单位。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>声响用分贝，赫兹是频率。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19-20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "噪声过大可能损害人体的哪些方面？",
        "options": ["A. 只损害视力", "B. 听力、神经系统、心脑血管系统", "C. 只损害消化系统", "D. 没有任何影响"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，噪声过大会损伤听力、影响神经系统、损害心脑血管。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出噪声与人体健康息息相关，过大噪声带来多重危害。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>抓住“听力、神经、心脑血管”三项危害，排除片面项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>噪声伤听力，神经血管俱。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "利用传感器开展实践探索的方式，不包括下列哪一项？",
        "options": ["A. 使用智能终端", "B. 使用传感器产品", "C. 使用物联实验设备", "D. 仅靠想象猜测"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，实践需借助真实设备或软件，不能仅靠想象。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>实践方式有三种：智能终端、传感器产品、物联实验设备。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>前三项为教材明示方式，D明显非实践方法。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>终端产品实验板，三法探感知。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19-22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "智能终端中用来检测环境声音分贝值的软件，通常调用的是？",
        "options": ["A. 摄像头", "B. 麦克风（声音传感器）", "C. 屏幕", "D. 电池"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，分贝软件利用麦克风（声音传感器）获取声音并换算分贝值。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>噪声检测软件利用麦克风采集声音，经计算得到分贝值。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“检测声音”对应麦克风/声音传感器。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>测声靠麦克，分贝软件算。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "噪声测试仪的核心是把声音转换成具体数据，它主要使用什么传感器？",
        "options": ["A. 温度传感器", "B. 声音传感器", "C. 光敏传感器", "D. 湿度传感器"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，噪声测试仪核心是声音传感器将声音大小转为数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>噪声测试仪核心就是利用声音传感器将噪声转换为具体数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“噪声”对应声音传感器，排除温光湿。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>噪声测试仪，声音传感芯。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "物联实验设备通常分为主控板、传感器和什么？",
        "options": ["A. 显示器", "B. 执行器", "C. 路由器", "D. 电池"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，物联实验设备分主控板、传感器、执行器三类。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确物联实验设备通常分为主控板、传感器和执行器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记牢“主控板、传感器、执行器”三件套。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>主控传感加执行，实验三件套。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P21）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "主控板主要以哪些部分为核心构成？",
        "options": ["A. 运算处理器、存储器、电源", "B. 仅含屏幕", "C. 仅含电池", "D. 仅含天线"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，主控板以运算处理器、存储器及电源等为主要构成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>主控板是电子系统，核心是运算处理、存储与供电部分。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“运算+存储+电源”为主控板核心，排除单一部件项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>主控三核心，算存电。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P21）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "在物联实验设备中，读取板载声音传感器数值通常使用的方法是？",
        "options": ["A. sound().read()", "B. print()", "C. wifi.connect()", "D. mqtt.connect()"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，sound().read()用于读取声音传感器的值。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材代码：sound()初始化板载声音传感器，read()读取其值，oled.print()显示。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>wifi/mqtt用于联网，print仅显示，读传感器用sound().read()。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>sound().read()读声音。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "教材拓展中，当环境光线值小于多少时建议显示“建议开灯”？",
        "options": ["A. 500", "B. 1000", "C. 3000", "D. 5000"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，光照小于1000显示“建议开灯”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>分段逻辑：<1000“建议开灯”；1000~3000“环境光适合”；>3000“环境比较亮”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记牢阈值1000与3000的分界点。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>千下建议灯，三千上较亮。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "single",
        "stem": "关于物联实验设备编程，下列说法正确的是？",
        "options": ["A. while True表示程序只执行一次", "B. while True表示无限循环，持续更新显示", "C. 不需要烧录程序", "D. 只能由老师操作"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，while True表示无限循环，使代码一直执行、不断更新屏幕。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明while True让程序持续运行，不断刷新显示内容。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“无限循环”是while True的本意，排除“只执行一次”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>while True转不停。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "tf",
        "stem": "智能终端（如手机）内置了多种传感器，如声音、光敏、加速度、磁力等。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。智能终端内置声音、光敏、加速度、磁力、位置、压力、温度、湿度、陀螺仪等传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举了智能终端丰富的内置传感器种类。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干与教材列举一致，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>手机传感多，声光加速度。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19-20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "tf",
        "stem": "物联手环测步主要是利用加速度传感器。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。手环通过加速度传感器检测运动变化来测步。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材拓展讨论物联手环测步，主要靠加速度传感器感知运动状态。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“测步=加速度传感器”是教材对应，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>手环测步，加速传感。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "tf",
        "stem": "噪声测试仪使用时不需要安装电池，也不需要检查传感器连接。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。使用噪声测试仪等传感器产品要安装好电池并提前检查连接。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材提醒使用传感器产品时要装电池、查连接，确保正常工作。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“不需要”与教材“要安装电池、检查连接”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>测试仪先装电，查连接。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P21）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "tf",
        "stem": "利用物联实验设备开展实践，是直接观察传感器模块并运行调试程序来了解其工作原理的理想方式。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联实验设备是最理想的体验方式，可观察模块并调试程序。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材认为用物联实验设备可直接观察传感器、搭建硬件、运行调试，直观了解原理。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材对实验设备优势的描述，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>实验设备好，模块程序见原理。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P21）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "multi",
        "stem": "下列哪些属于教材中提到的“传感器产品”（可直接用来实践）？（多选）",
        "options": ["A. 噪声测试仪", "B. 气体测试仪", "C. 甲醛测试仪", "D. 亮度计"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均为教材列举的传感器类产品。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材还提到水质测试笔等，这类产品直接用传感器感知并显示结果。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项都是“测试仪/计”类传感器产品，全部选入。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>噪声气体甲醛亮，传感产品齐上场。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "multi",
        "stem": "智能终端内置的传感器可能包括？（多选）",
        "options": ["A. 声音传感器", "B. 光敏传感器", "C. 加速度传感器", "D. 陀螺仪"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均属智能终端内置传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举智能终端内置声音、光敏、加速度、磁力、位置、压力、温度、湿度、陀螺仪等。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材明示内置传感器，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>声光加速陀螺，终端全都有。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19-20）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "multi",
        "stem": "使用物联实验设备检测声音数据时，可以观察到哪些现象？（多选）",
        "options": ["A. 用手遮住声音传感器数据会变化", "B. 拍手时数据会变化", "C. 正常说话数据会变化", "D. 数据与声音无关"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。遮住、拍手、说话都会使声音数据变化。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>实验记录遮住传感器、说话、拍手时的数据，对比找出最大最小值。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D“与声音无关”违背传感器原理，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>遮拍说，数据变。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "short",
        "stem": "利用传感器获取环境数据的实践方式有哪几种？各举一例。",
        "options": [""],
        "answer": "三种：①使用智能终端，如手机装“分贝仪”软件检测噪声；②使用传感器产品，如噪声测试仪、水质测试笔；③使用物联实验设备，如主控板+声音传感器+程序。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>智能终端、传感器产品、物联实验设备三种方式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材按三类实践方式展开，每类配具体例子。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分三点各举教材实例即可。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>终端、产品、实验板，三法取数据。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P19-22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "short",
        "stem": "请简述用物联实验设备检测环境声音数据的大致步骤。",
        "options": [""],
        "answer": "①用USB线将主控板连接计算机并安装驱动；②理解程序代码并烧录到主控板；③在显示屏查看声音数据；④分别测试遮住传感器、说话、拍手时的数据变化，找出最大值和最小值。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>连接—烧录—查看—对比测试四步。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材给出连接计算机、装驱动、烧录、调试、记录数据的流程。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按教材“连接→理解烧录→查看→测试记录”顺序作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>连烧看测，四步探声。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P21-22）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L03",
        "lessonTitle": "环境数据要感知",
        "type": "short",
        "stem": "利用光敏传感器检测光照强度时，教材给出的分段判断逻辑是什么？",
        "options": [""],
        "answer": "当环境光线值小于1000，显示“建议开灯”；在1000~3000之间，显示“环境光适合”；大于3000，显示“环境比较亮”。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>以1000和3000为分界的三段判断。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材拓展要求修改程序实现光照分段显示。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>直接写出三个阈值区间及对应提示文字。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>千下开灯，三千上亮，中间适合。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第3课 环境数据要感知（P22）。'''
    },

    # ---------- L04 物物相连有价值 ----------
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "教材把物联网中的传感器比作什么？",
        "options": ["A. 大脑", "B. 神经触角", "C. 血管", "D. 骨骼"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，传感器像遍布世界的“神经触角”，源源不断输送数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将互联网比作“大脑”，传感器比作感知数据的“神经触角”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“神经触角”是教材比喻，区别于大脑（互联网）。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感如触手，网络似脑舟。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "物联网带来的重要价值不包括以下哪项？",
        "options": ["A. 提供丰富实时的数据", "B. 实现远程反馈与控制", "C. 传感器协同带来新智能", "D. 让所有物品都消失"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，物物相连是创造价值，不会让物品消失。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>三大价值：丰富实时数据、远程控制、传感器协同新智能。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>前三项为教材价值，D明显荒谬。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据、远控、协同智，三值是价值。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "将多种传感器数据融合进行协同控制，往往产生什么效果？",
        "options": ["A. “1+1<2”", "B. “1+1=2”", "C. “1+1>2”", "D. 没有效果"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，传感器协同产生“1+1>2”的效果。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>数据融合协同控制往往产生“1+1>2”的智能化效果。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“协同增值”对应大于号，排除其他。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感协同，一加一大于二。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "把光敏传感器加入灯的控制，可实现什么功能？",
        "options": ["A. 光照不足时自动开灯", "B. 声音大时关灯", "C. 远程浇水", "D. 测量温度"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，光敏控制可实现光照不足自动开灯、充足自动关灯。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材举例：光敏加入灯控，实现光照不足开灯、充足关灯。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“光敏→光照”直接对应自动开灯。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>光敏控灯，暗开亮关。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "把光敏和红外热释电两种传感器联合控制楼梯灯，可实现？",
        "options": ["A. 光照不足且有人靠近时自动开灯", "B. 仅雨天开灯", "C. 仅唱歌时开灯", "D. 一直亮着"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，光敏+红外联合实现“暗且有人靠近自动开灯”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材举例：光敏+红外协同，有人且光照不足时自动亮灯。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>两种传感器协同=暗+有人，对应A。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>光红协同，暗人灯启。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "在河道不同位置放置多个水质传感器协同检测，这属于？",
        "options": ["A. 本地传感器协同", "B. 网络传感器协同", "C. 单一传感器", "D. 远程控制"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，多个位置传感器数据经网络汇聚属于网络协同。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>网络协同指传感器数据通过网络汇聚形成大数据再分析，如河道上下游水质协同。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“不同位置+网络汇聚”是网络协同特征。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>河段多传感，联网协同看。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "为确保气象数据准确，气象部门在单个城市设置数千个监测点，主要作用是？",
        "options": ["A. 增加成本", "B. 提高预报准确性、避免单点异常", "C. 减少数据", "D. 取代卫星"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，监测点越多了解越全面、预报越准，避免单点异常。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>部署数千监测点可全面掌握天气、准确预报暴雨台风等极端天气。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“准确+避免异常”是设置多点的目的，排除无关项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>点多知天全，预报更可靠。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "物联网中实现“万物互联”不仅能感知数据，还能通过网络实现什么？",
        "options": ["A. 远程控制（发送指令）", "B. 只能看不能控", "C. 删除数据", "D. 关闭互联网"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，万物互联还能通过网络实现远程控制（发指令）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网价值之一是通过网络远程发送控制指令进行控制。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“远程控制”是教材明确价值，排除错误项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联不仅能感，还能远控。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P24）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "关于传感器协同，下列说法正确的是？",
        "options": ["A. 单一传感器数据已足够，无需协同", "B. 协同只能在本地，不能通过网络", "C. 协同可以在本地完成，也可通过网络完成", "D. 协同会降低智能"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，传感器协同可在本地完成，也可通过网络完成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将协同分为本地不同种类传感器协同与网络传感器协同两类。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>A、B、D均与教材相反，C正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>协同两途径，本地与网络。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "single",
        "stem": "物联网在带来便利的同时，也带来了什么需要关注的问题？",
        "options": ["A. 网络安全与隐私风险", "B. 没有风险", "C. 只会更便宜", "D. 数据变少"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，物联设备是物理实体，遭攻击后果严重，且数据涉及隐私与国家安全。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材强调物联带来便利也带来网络安全风险，需保护隐私与数据安全。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“风险需关注”是教材安全主题，选A。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>便利伴风险，安全记心间。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "tf",
        "stem": "中央气象台的天气实况图是基于各地传感器采集的数据生成的。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。气象图表基于各地温度传感器等采集的数据生成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>中央气象台实况图基于海量传感器数据，经分析可视化形成。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合“物联网是大数据的基石”，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>气象图，传感数据基。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-24）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "tf",
        "stem": "单一传感器采集的数据总是充分的，不需要多种传感器协同。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。单一传感器数据有限，许多应用需多种传感器协同。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出“单一传感器获取的数据有限”，多传感器信息互补提高准确度。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“总是充分”与“数据有限”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>单传感有限，协同一加一。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "tf",
        "stem": "通过网络把多个位置的水质传感器数据汇聚，可以分析水质变化情况。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。网络汇聚多位置数据可分析整条河道水质变化。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>河道上下游多传感器通过网络协同，找出水质变化位置。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>符合网络协同举例，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>多点上网联，水质变化现。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "tf",
        "stem": "物联设备都是物理实体，若遭攻击可能产生较严重后果，因此需注重网络安全。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物理实体受攻击后果严重，数据被利用还会危及信息安全。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材提醒物联设备是物理实体，安全风险需重视，保护隐私与国家信息安全。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干与教材安全论述一致，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>实体遭攻后果重，安全须重视。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "multi",
        "stem": "物联网的价值主要体现在哪些方面？（多选）",
        "options": ["A. 提供丰富实时的数据", "B. 实现远程的反馈与控制", "C. 传感器协同带来新智能", "D. 减少网络连接"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。三大价值，D“减少连接”并非价值。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>价值：丰富实时数据、远程控制、协同新智能。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D与“万物互联”相悖，排除后选ABC。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据、远控、协同智。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "multi",
        "stem": "下列哪些体现了传感器协同（多种传感器融合）带来的智能化？（多选）",
        "options": ["A. 光敏传感器单独控制开灯（光照不足自动开灯）", "B. 光敏+红外实现“光照不足且有人靠近自动开灯”", "C. 河道上下游多个水质传感器协同检测水质变化", "D. 地图导航结合车速异常与交通网络数据判断突发情况"],
        "answer": [1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：B、C、D。A仅单一传感器，不属于“协同”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>协同指多种传感器融合或网络汇聚，B_local、C/D_网络协同均符合。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>A是单传感器，不符“协同”，排除；其余为协同实例。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>协同需多种，单感不算数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "multi",
        "stem": "远程控制物联系统的好处包括？（多选）",
        "options": ["A. 不在家也能控制设备", "B. 下雨可远程关窗", "C. 冰箱自动补货（与购物网站联手）", "D. 物联手表快到家通知空调开启"],
        "answer": [0, 1, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、D。均为教材中远程控制/物物相连价值实例。C教材未作为本课要点强调（属物物相连“联手”想象例），故不选。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>远程控制可发指令控设备，如远程关窗；手表通知空调开启是物物相连价值。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>A、B、D明确属远程控制/物物相连价值，保留。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>远控不在家，关窗唤空调。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-24）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "short",
        "stem": "物联网为社会发展带来哪三方面重要价值？",
        "options": [""],
        "answer": "①提供丰富实时的数据（传感器海量数据经分析可视化，辅助决策）；②实现远程的反馈与控制（远程发送指令）；③传感器协同带来“1+1>2”的新智能（本地融合与网络汇聚）。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>丰富数据、远程控制、协同新智能三方面。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以“丰富实时数据、远程控制、协同新智能”概括物联价值。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>直接写出三大价值并略作说明。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>数据远控协同智，三值记心里。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P23-26）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "short",
        "stem": "什么是传感器的“本地协同”和“网络协同”？各举一例。",
        "options": [""],
        "answer": "本地协同指同一设备/局部集成多种不同传感器综合分析，如光敏+红外实现“有人靠近且光照不足时自动开灯”；网络协同指传感器数据通过网络汇聚形成大数据再分析，如河道上下游多个水质传感器协同检测整条河道水质变化。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>本地=局部多传感器融合，网络=跨位置联网汇聚。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将协同分为本地不同种类与网络汇聚两类并各配例。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分别定义并各举教材例子。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>本地融合、网络汇聚。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P25）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L04",
        "lessonTitle": "物物相连有价值",
        "type": "short",
        "stem": "为什么气象部门要在单个城市部署数千个气象监测点？",
        "options": [""],
        "answer": "部署的监测点越多，对天气了解越全面，预报越准确，对预测暴雨、台风等极端天气非常重要；也可避免单一监测点出现数据异常或错误而影响判断。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>多监测点提高准确性、避免单点异常。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明数千监测点使预报更准、可预警极端天气、规避单点错误。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从“全面性、准确性、抗异常”三方面作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>点多面全，预报稳准。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第4课 物物相连有价值（P26）。'''
    },

    # ---------- L05 物联功能趣体验 ----------
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "在中国环境监测总站的网站上，可以查看哪些公开的物联数据？",
        "options": ["A. 仅股票价格", "B. 空气质量和水质数据", "C. 仅天气预报文字", "D. 仅新闻"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，可查看全国各地空气质量和水质实时数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以中国环境监测总站为例，说明可远程查看空气和水质监测数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“环境监测总站”对应空气/水质，排除无关项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>监测总站，空气水质。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P27-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "物联插座的本质是？",
        "options": ["A. 一个普通插座", "B. 将插座接入物联网，通过控制插座开关来控制电器", "C. 一台计算机", "D. 一块电池"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，物联插座本质是插座接入物联网，以控开关来控电器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联插座让传统电器变智能，联网后由智能终端远程控制并反馈状态。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“接入物联网+控开关控电器”是本质，排除普通插座。<br><br>
<strong style="color:#e67e23;">🧠 记忆口诀：</strong>插座入网，控开控电器。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "物联插座一般不包含以下哪个模块？",
        "options": ["A. 物理按键模块", "B. Wi-Fi模块", "C. 继电器模块", "D. 显示器模块"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，物联插座由物理按键、Wi-Fi、继电器三模块组成，无显示器模块。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物理按键控开关/配网，Wi-Fi连路由与服务器，继电器控220V通断。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>显示器非物联插座组成，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键WiFi继电器，插座三模块。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "物联插座让传统普通电器变智能，下列哪种电器可被它控制？",
        "options": ["A. 热水器", "B. 电暖气", "C. 台灯", "D. 以上都可以"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，热水器、电暖气、台灯等普通电器都可由物联插座控制。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材举例物联插座可让传统热水器、电暖气、台灯等变智能。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>三项均属教材列举，故“以上都可以”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>水暖灯，插座控。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "花卉环境监测产品中，多个环境监测传感器通常如何连接互联网？",
        "options": ["A. 直接连接互联网", "B. 通过网关设备连接互联网", "C. 不用连接", "D. 只用蓝牙"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，多个传感器通常通过网关设备连接互联网。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材图5.3显示传感器通过网关接入互联网，网关做协议转换的“翻译器”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“通常通过网关”是教材重点，排除“直接连接”的绝对说法。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>花卉传感，网关入网。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "教材把网关比作什么？",
        "options": ["A. 翻译器", "B. 电池", "C. 屏幕", "D. 导线"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，网关像连接不同网络的“翻译器”，做协议转换。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>网关连接两个使用不同通信协议的网络，使它们互相“理解”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“翻译器”是教材原比喻，对应协议转换。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网关如翻译，协议互转达。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "当花卉监测到环境数据达到设定阈值时，系统会怎样？",
        "options": ["A. 什么也不做", "B. 向用户发送通知提醒", "C. 自动关机", "D. 删除数据"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，达到阈值系统会发通知提醒用户及时处理。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>监测到数据达到威胁生长的阈值时，系统向用户发送通知提醒。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“阈值→通知”是反馈控制，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>超阈值，发提醒。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "物联花卉监测系统一般包含哪些组成部分？",
        "options": ["A. 仅传感器", "B. 传感器+摄像头+网关+手机端应用软件", "C. 仅手机", "D. 仅摄像头"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，由传感器、摄像头、网关、手机端软件组成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材图示：传感器+摄像头、网关、手机端应用软件为系统组成。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“综合组成”选最完整的B项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感摄像网关机，花卉四件套。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "物联插座的核心功能是？",
        "options": ["A. 远程控制开关并感知开关状态", "B. 只能测温度", "C. 只能播放音乐", "D. 只能充电"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，物联插座核心是远程控制开关并感知、反馈开关状态。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联插座联网后可远程控开关并反馈工作状态，是反馈与控制的体现。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“远程控开关+反馈”是核心，排除单一功能项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>插座核心，遥控反状态。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "single",
        "stem": "下列关于网关的说法正确的是？",
        "options": ["A. 网关用于连接两个使用不同通信协议的网络并实现协议转换", "B. 网关就是路由器，功能完全相同", "C. 所有传感器都必须直接连互联网", "D. 网关会增加数据丢失"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，网关连接不同协议网络并做协议转换（翻译器）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>网关主要作用是连接两个不同协议网络使它们互相通信，不必过度强调概念。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>B“完全相同”错，C“必须直接”错，D无依据，选A。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网关转协议，翻译连异网。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "tf",
        "stem": "物联插座可以让传统的热水器、电暖气、台灯等普通电器变得智能。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联插座本质是插座入网，使普通电器可远程控制而变智能。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确物联插座让热水器、电暖气、台灯等普通电器变智能。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干与教材一致，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>插座入网，普器变智。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "tf",
        "stem": "所有传感器都必须直接连接到互联网，不能使用网关。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。教材指出并非所有传感器都直接连互联网，常通过网关连接。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>传感器有两种联网方式：直接连互联网，或通过网关连互联网。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“都必须直接”与“可通过网关”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传感联网两法，网关亦可。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "tf",
        "stem": "远程监测物联花卉属于综合了“远程查看数据”和“远程控制”的体验。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。花卉监测既远程查看数据，又可在异常时触发处理（远程控制）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材称花卉监测综合了远程查看数据与远程控制。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>符合教材“综合”定位，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>花卉监测，查看加控制。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P27-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "tf",
        "stem": "网关的主要作用是连接两个使用不同通信协议的网络，使它们能够互相通信。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。网关做协议转换，让不同协议网络互相理解。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>网关像翻译器，连接不同通信协议的网络实现互通。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即网关定义，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网关翻译，异网互通。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "multi",
        "stem": "远程查看物联数据的途径包括？（多选）",
        "options": ["A. 访问公共数据监测网站", "B. 中国环境监测总站查看空气质量/水质", "C. 仅用想象", "D. 搜索引擎查找公开物联数据"],
        "answer": [0, 1, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、D。均为远程查看公开物联数据的方式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材引导上网查公开物联数据，如环境总站、交通实时监控等。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>C“仅用想象”非真实途径，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网站搜索查，公开数据看。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P27）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "multi",
        "stem": "物联插座的组成模块包括？（多选）",
        "options": ["A. 物理按键模块", "B. Wi-Fi模块", "C. 继电器模块", "D. 显卡"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。物联插座由这三模块组成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物理按键控开关/配网，Wi-Fi连服务器，继电器控220V通断。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D显卡非插座组成，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>按键WiFi继电器，三件构插座。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "multi",
        "stem": "花卉环境监测产品能监测花卉生长环境的哪些数据？（多选）",
        "options": ["A. 温度", "B. 湿度", "C. 肥力", "D. 光照"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。四项均为教材提及的监测要素。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材关注花卉生长环境的温度、湿度、肥力和光照情况。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均属监测范围，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>温湿肥光，花卉四测。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "short",
        "stem": "简述利用物联插座控制台灯开关的工作过程。",
        "options": [""],
        "answer": "物联插座接入Wi-Fi网络并连接远程服务器；用户在手机端应用软件发送开关指令；指令经网络传到物联插座的Wi-Fi模块，由继电器模块控制220V通断，从而控制台灯开关，并把插座工作状态反馈给用户。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>手机发令→Wi-Fi模块接收→继电器控通断→反馈状态。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联插座由物理按键、Wi-Fi、继电器组成，体现远程控制与反馈。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按“联网—发令—继电器控—反馈”顺序描述。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>手机下令，继电通断，状态回传。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "short",
        "stem": "什么是网关？为什么教材说“不是所有传感器都直接连互联网”？",
        "options": [""],
        "answer": "网关是连接两个使用不同通信协议的网络、实现协议转换的设备（像翻译器）。因为很多传感器资源受限或采用不同协议，借助网关可以统一汇聚并接入互联网，降低直接联网的复杂度与成本，所以通常不是所有传感器都直连。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>网关=协议转换设备；传感器常经网关入网更合理。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>网关像翻译器连接不同协议网络；传感器有直连与经网关两种联网方式。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>先定义网关，再从协议差异、资源成本说明经网关的必要性。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网关转协议，传感多经它。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P28-29）。'''
    },
    {
        "module": "第一单元 从感知到物联",
        "lesson": "L05",
        "lessonTitle": "物联功能趣体验",
        "type": "short",
        "stem": "本课体验了哪三种物联功能？它们分别侧重什么？",
        "options": [""],
        "answer": "①远程查看物联数据：通过网络查看公开传感器数据（如空气质量）；②远程控制物联插座：远程控制电器开关并反馈状态；③远程监测物联花卉：综合远程查看与控制，传感器经网关联网、阈值触发通知。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>远程查看、远程控制、远程监测三种功能。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材三个学习活动层次递进：查看数据→控制插座→监测花卉（综合）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分三点写出功能名称与侧重。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>查看、控制、监测，三验物联。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第一单元 第5课 物联功能趣体验（P27-29）。'''
    },

    # ===================== 第二单元 万物互联有协议 =====================
    # ---------- L06 数据传输方式多 ----------
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "共享单车获取附近可用单车位置，主要依靠单车上的什么？",
        "options": ["A. 摄像头", "B. 位置传感器", "C. 麦克风", "D. 屏幕"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，单车利用位置传感器获取位置数据并上报服务器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>共享单车靠位置传感器定位，经NB-IoT等网络发到服务器，再反馈给用户手机。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“位置”对应位置传感器。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>单车定位，位置传感。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P32-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "共享单车扫码开锁时，手机应用软件获取单车的什么来识别是哪辆车？",
        "options": ["A. 颜色", "B. 唯一标识（如二维码）", "C. 重量", "D. 价格"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，扫码获取单车唯一标识，服务器据此知道开哪辆锁。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>扫码后手机获取单车唯一标识，经HTTP发服务器，服务器确认后发开锁指令。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“识别哪辆车”靠唯一标识/二维码。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>扫码取标识，开锁知哪车。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "按传输介质分，物联网数据传输分为哪两类？",
        "options": ["A. 有线传输和无线传输", "B. 近距离和远距离", "C. 高速和低速", "D. 有源和无源"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，按传输介质分为有线传输和无线传输。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材分类：按介质（有线/无线）、按距离（近/远）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干“按传输介质”直接对应有线/无线。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>介质分有线无线。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "下列中属于有线传输方式的是？",
        "options": ["A. Wi-Fi", "B. 蓝牙", "C. 光纤", "D. ZigBee"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，光纤是有线传输介质，提供高速稳定连接。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>有线传输包括双绞线、光纤、以太网、串行、USB；无线包括Wi-Fi、蓝牙、ZigBee、LoRa。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>A、B、D均为无线，C光纤是有线。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>有线双绞线光纤，无线WiFi蓝牙。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "下列中属于无线传输方式的是？",
        "options": ["A. 双绞线", "B. 光纤", "C. 以太网", "D. 蓝牙"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，蓝牙是典型的无线传输方式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>无线传输无需物理介质，如Wi-Fi、蓝牙、ZigBee、LoRa。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>A、B、C均是有线，D蓝牙是无线。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙无线，双绞光纤有线。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "按传输距离分，RFID、NFC、蓝牙、ZigBee属于？",
        "options": ["A. 远距离通信协议", "B. 近距离通信协议", "C. 卫星通信", "D. 有线通信"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，这些传输距离较近，属近距离通信协议。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将RFID、NFC、蓝牙、ZigBee等称为近距离通信协议。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“近距”是这些协议共同特征，区别于3G/4G/5G、NB-IoT。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID NFC 蓝牙 ZigBee，近距四兄弟。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "按传输距离分，3G/4G/5G、NB-IoT属于？",
        "options": ["A. 近距离通信", "B. 远距离通信协议", "C. 本地通信", "D. 红外通信"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，3G/4G/5G、NB-IoT传输距离远，属远距离通信协议。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将3G/4G/5G、NB-IoT等称为远距离通信协议。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“远距”对应蜂窝/NB-IoT类。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>三四五G加NB，远距通信族。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "共享单车中，单车向服务器上报位置数据常用的低功耗远距离技术是？",
        "options": ["A. NB-IoT（窄带物联网）", "B. 双绞线", "C. 光纤", "D. ZigBee近距离"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，单车经NB-IoT低功耗远距离上报位置。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材示例：车辆通过NB-IoT连接互联网，利用位置传感器获取数据，经MQTT发服务器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“低功耗远距离+单车上报”对应NB-IoT。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>单车上报，NB-IoT。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P32-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "共享单车开锁时，手机与单车之间可用什么辅助连接开锁？",
        "options": ["A. 蓝牙", "B. 光纤", "C. 双绞线", "D. 电源线"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，手机蓝牙与单车智能锁蓝牙连接可辅助开锁。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明手机蓝牙与智能锁蓝牙连接，辅助开锁。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“手机与单车辅助连接”对应蓝牙。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙助开锁。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "single",
        "stem": "选择物联协议时，不需要从以下哪项综合分析？",
        "options": ["A. 距离范围", "B. 最高速率", "C. 安全性", "D. 设备颜色"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，选协议看距离、速率、安全、功耗，与颜色无关。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材强调从距离范围、最高速率、安全性、功耗等多方面综合分析。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“设备颜色”非技术依据，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>距离速率安全功耗，四因选协议。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "tf",
        "stem": "物联网中数据的传输方式既有传统互联网通信方式，也有适应物联网特点的新通信方式。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材指出物联网传输兼具传统方式与适应大规模、低功耗、低成本的新方式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联网传输方式多样，是多种协议构建的高效传输网络。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材论述，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>传法新老并存。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "tf",
        "stem": "有线传输比无线传输通常更稳定、不易受干扰、带宽更高。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。有线通过电缆/网线/光纤连接，更快更稳定、带宽更高。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明有线传输提供更快更稳定的速度和更高带宽。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即教材对有线优势的描述，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>有线稳快带宽高。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "tf",
        "stem": "Wi-Fi一定只能算近距离通信，绝不可能是远距离通信。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。近/远是相对概念，教材说有资料也称Wi-Fi为远距离通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材强调远近无严格区分，教学不强求统一标准。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“绝不”绝对化，与教材“相对概念”矛盾。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>远近相对，WiFi可远可近。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "tf",
        "stem": "共享单车的电子围栏可以用蓝牙或RFID等技术实现。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。电子围栏可用蓝牙或RFID读卡器与车载标签通信实现。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材拓展说明电子围栏有蓝牙定位、RFID两种方式等。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>符合教材拓展内容，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>电子围栏，蓝牙RFID。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "multi",
        "stem": "下列属于近距离通信协议的有？（多选）",
        "options": ["A. RFID", "B. NFC", "C. 蓝牙", "D. ZigBee"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均属近距离通信协议。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材将RFID、NFC、蓝牙、ZigBee归为近距离通信协议。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材近距离协议，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID NFC 蓝牙 ZigBee，近距四协议。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "multi",
        "stem": "下列属于远距离通信协议/技术的有？（多选）",
        "options": ["A. 3G/4G/5G", "B. NB-IoT", "C. 蓝牙（近距离）", "D. LoRa"],
        "answer": [0, 1, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、D。蓝牙属近距离，不选。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>远距离通信包括3G/4G/5G、NB-IoT、LoRa（远距离无线电）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>C蓝牙是近距离，排除后选ABD。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>远距：蜂窝NB LoRa。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "multi",
        "stem": "选择物联协议时需要综合哪些因素？（多选）",
        "options": ["A. 距离范围", "B. 最高速率", "C. 安全性", "D. 功耗"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。教材强调四方面综合分析。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>选择协议需从距离范围、最高速率、安全性、功耗等分析。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材依据，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>距速安保耗，四因定协议。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "short",
        "stem": "请简述共享单车“获取附近可用单车”的数据流转过程。",
        "options": [""],
        "answer": "单车利用位置传感器获取位置数据，通过NB-IoT等网络经MQTT发送至服务器；手机通过移动通信网络经HTTP上传用车人位置；服务器处理后经HTTP把附近单车数据反馈到手机应用软件。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>位置传感→NB-IoT/MQTT→服务器；手机HTTP→服务器→HTTP反馈。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以共享单车说明物联系统数据流转与多协议协作。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按“单车上报—手机上传—服务器反馈”三环节描述。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>车报位、机报位、服反馈。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P32-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "short",
        "stem": "按传输介质和传输距离，物联网数据传输方式各如何分类？",
        "options": [""],
        "answer": "按传输介质分为有线传输（如双绞线、光纤、以太网、USB）和无线传输（如Wi-Fi、蓝牙、ZigBee、LoRa）；按传输距离分为近距离通信（如RFID、NFC、蓝牙、ZigBee）和远距离通信（如3G/4G/5G、NB-IoT）。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>两个维度：介质（有线/无线）、距离（近/远）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材给出两种分类及各自常见技术举例。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分别列出两类并各举教材实例。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>介质有线无线，距离近远分。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P33-34）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L06",
        "lessonTitle": "数据传输方式多",
        "type": "short",
        "stem": "为什么还要发展低功耗的远程数据传输技术（如NB-IoT）？",
        "options": [""],
        "answer": "许多物联设备数量大、分布广、靠电池供电（如共享单车），低功耗设计可延长电池寿命、降低维护成本；传统高速率移动通信（如手机用3G/4G/5G）功耗高、需大电池，不适合海量低功耗终端，因此需要低功耗远程技术。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>海量电池终端需低功耗远距技术。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材从供电节能角度分析，低功耗延长寿命、降成本。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从设备数量、分布、电池供电、传统技术高功耗对比作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>海量电池终端，低功耗远传。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第6课 数据传输方式多（P34）。'''
    },

    # ---------- L07 电子标签我揭秘 ----------
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "RFID技术本质上是一种？",
        "options": ["A. 有线通信技术", "B. 无线通信技术", "C. 存储技术", "D. 显示技术"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，RFID本质上是一种无线通信技术（非接触自动识别）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>RFID是物品标识和自动识别技术，无须与被识别物品直接接触。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“无线、非接触”是RFID本质，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID无线非接触。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35-38）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "一个基本的RFID系统由哪两部分组成？",
        "options": ["A. 计算机和网线", "B. 电子标签和读卡器", "C. 传感器和执行器", "D. 手机和服务器"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，RFID系统由电子标签和读卡器组成。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确RFID系统由电子标签（数据载体）和读卡器（读取设备）组成。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记牢“标签+读卡器”两要素。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID两件套，标签加读卡。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "RFID技术用于火车站检票，主要利用了它的什么特点？",
        "options": ["A. 必须接触读取", "B. 非接触自动识别", "C. 只能读一次", "D. 依赖可见光"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，刷身份证进站体现非接触自动识别。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>身份证靠近检票机即被识别，正是RFID非接触识别在发挥作用。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“刷一下即过”=非接触，排除需接触/可见光项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>一刷即过，非接触识。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "关于RFID电子标签，下列说法正确的是？",
        "options": ["A. 被动标签无内置电池，工作距离较短", "B. 主动标签无电池", "C. 所有标签都必须瞄准读取", "D. 标签不能修改数据"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，被动标签无电池、靠感应取电，工作距离短（几cm~几m）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>被动标签无内置电池、距离短；主动标签有电池、距离可达几十米至上百米；数据可反复修改、不依赖瞄准。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>B、C、D均与教材相反，A正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>被动无电距短，主动有电距远。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "主动标签与被动标签相比？",
        "options": ["A. 主动标签有内置电池，工作距离更远", "B. 被动标签距离更远", "C. 两者都一样", "D. 主动标签无电池"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，主动标签有电池可主动发信号，距离更远。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>主动标签工作距离可达几十米甚至上百米；被动标签仅几厘米到几米。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“有电池→距更远”是主动标签特征。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>主动有电，远达百米。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "RFID系统工作流程的第一步是？",
        "options": ["A. 读卡器发射频信号", "B. 给物品打上电子标签并存储数据", "C. 计算机处理", "D. 标签发送数据"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，第一步给物品打电子标签并存储相关数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>流程：①打标签存数据→②读卡器发信号→③标签进区发数据→④读卡器传送→⑤计算机处理。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“第一步”是标签初始化，对应B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>先打标签后读卡。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35-36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "NFC是由什么演变而来的？",
        "options": ["A. 蓝牙", "B. RFID", "C. Wi-Fi", "D. HTTP"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，NFC由RFID演变而来。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出NFC是由RFID演变而来的近距离高频无线通信技术。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“NFC源自RFID”是教材原话。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>NFC出RFID。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "与RFID相比，NFC额外规定了什么？",
        "options": ["A. 通信协议", "B. 数据交换格式", "C. 电池标准", "D. 屏幕尺寸"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，NFC除通信协议外还规定了数据交换格式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明NFC相比RFID，还规定了数据交换格式，并支持更改内容。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“额外规定数据交换格式”是NFC区别点。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>NFC多格式，可改内容。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "2016年我国自主创新的NFC实体鉴别安全技术成为什么标准？",
        "options": ["A. 企业标准", "B. ISO/IEC国际标准", "C. 仅国家标准", "D. 行业内部标准"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，成为ISO/IEC国际标准。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>2016年我国NFC非对称/对称实体鉴别两项安全技术正式成为ISO/IEC国际标准。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记“ISO/IEC国际标准”这一成果。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>一六NFC安鉴，成ISO标。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "single",
        "stem": "下列应用中，主要使用RFID技术的是？",
        "options": ["A. 蓝牙耳机听歌", "B. 高速公路ETC不停车收费", "C. Wi-Fi上网", "D. 手机导航"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，高速公路ETC是RFID典型应用。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以ETC为例说明RFID应用，此外还有铁路检票、物流、医疗手环等。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>ETC=电子不停车收费，用RFID读车载标签。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>ETC靠RFID。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35-36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "tf",
        "stem": "RFID电子标签的识读不依赖可见光，可在高粉尘、野外等恶劣环境下使用。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。RFID识读靠射频电磁场，不依赖可见光，适恶劣环境。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举RFID优势：不依赖可见光，可在高粉尘、野外使用。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合RFID优势，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID无光也读，恶境可用。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "tf",
        "stem": "RFID每秒可进行上千次读取，并能同时处理多个电子标签。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。RFID可高速、批量读取多个标签。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出RFID每秒上千次读取、能同时处理多个标签、高效准确。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即RFID优势，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>千次多标，RFID快准。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "tf",
        "stem": "NFC只能由一方读取另一方，不能双向交换数据。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。NFC支持非接触式点对点双向数据交换。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>NFC允许数字设备间非接触式点对点数据传输，可双向。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“只能一方读”与“双向点对点”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>NFC双向点对点。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "tf",
        "stem": "RFID电子标签上的数据可以反复修改。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材列出“电子标签上的数据可反复修改”为优势。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>RFID优势之一即标签数据可反复修改、高效准确。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>标签数据，反复改。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "multi",
        "stem": "RFID技术的特点和优势包括？（多选）",
        "options": ["A. 每秒上千次读取", "B. 同时处理多个标签", "C. 数据可反复修改", "D. 不依赖可见光、恶劣环境可用"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均为教材RFID优势。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>RFID优势：高速读取、批量处理、数据可改、不依赖可见光、适恶劣环境。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项全为教材优势，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>快、多、改、耐恶，RFID四优。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "multi",
        "stem": "RFID在生活中的应用有？（多选）",
        "options": ["A. 铁路进站检票", "B. 高速公路ETC", "C. 物流货物跟踪", "D. 医疗患者手环识别"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均属RFID应用。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举铁路检票、ETC、物流跟踪、医疗手环、农业动物标识等。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材RFID应用，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>检票ETC物流医疗，RFID广用。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35-36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "multi",
        "stem": "关于RFID与NFC，下列说法正确的有？（多选）",
        "options": ["A. NFC由RFID演变而来", "B. NFC除通信协议还规定数据交换格式", "C. NFC可更改胸卡内容（双向）", "D. RFID和NFC完全相同没有区别"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。D错误，二者有区别。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>NFC源自RFID，额外规定数据格式且可双向改内容；并非完全相同。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D“完全相同”错，排除后选ABC。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>NFC源RFID，多格式可双向。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "short",
        "stem": "简述RFID系统的一般工作流程（5步）。",
        "options": [""],
        "answer": "①给物品打上电子标签并存储相关数据；②读卡器发送一定频率的射频信号；③当物品进入读卡器工作区，电子标签将自身数据发送出去；④读卡器接收数据并传送到计算机管理系统；⑤计算机管理系统作出相应处理。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>打标签→发信号→标签回传→读卡器送计算机→系统处理。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材给出RFID五步标准流程。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按教材五步顺序逐条写出。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>标签、信号、回传、送机、处理。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35-36）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "short",
        "stem": "被动标签与主动标签有什么区别？",
        "options": [""],
        "answer": "被动标签没有内置电池，靠读卡器射频信号感应取电，工作距离较短（几厘米到几米）；主动标签有内置电池，可主动发射信号，工作距离较远（可达几十米甚至上百米）。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>有无电池与距离差异是核心区别。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材按发射射频信号方式分被动/主动标签，距离与供电相关。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从“电池、取电方式、工作距离”对比作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>被动无电距短，主动有电距远。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P35）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L07",
        "lessonTitle": "电子标签我揭秘",
        "type": "short",
        "stem": "教材用“胸卡”类比说明RFID与NFC的区别，请解释。",
        "options": [""],
        "answer": "RFID像学生戴胸卡方便别人了解他（一方读取）；NFC像师生两人都戴胸卡，可互相看到对方信息，且能更改胸卡内容改变对方收到的数据，即NFC支持双向非接触点对点数据交换，并规定了数据交换格式。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>RFID单向读取，NFC双向可改。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材用胸卡类比说明二者在双向性与可改内容上的差异。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>分别说明“单向胸卡”与“双向可改胸卡”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID单向卡，NFC双向改。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第7课 电子标签我揭秘（P37）。'''
    },

    # ---------- L08 巧用蓝牙做工具 ----------
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "蓝牙是一种什么类型的通信技术？",
        "options": ["A. 远距离有线", "B. 近距离无线通信", "C. 仅用于卫星", "D. 仅用于光纤"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，蓝牙是常见的近距离无线通信技术。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>多数手机、平板、笔记本都有蓝牙，可连接设备也可传输数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“近距离无线”是蓝牙定位。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙近距无线。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-42）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "蓝牙设备之间通信的前提是？",
        "options": ["A. 必须插网线", "B. 找到并配对成功", "C. 必须同品牌", "D. 必须对准"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，设备须找到并配对成功才能互相通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>蓝牙原理：发信号寻找另一设备，配对成功便可通信。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“配对成功”是蓝牙通信前提，排除插线/同品牌/对准。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙先配对，再通信。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "蓝牙5.0的传输距离增加到多少？",
        "options": ["A. 3m", "B. 30m", "C. 300m", "D. 3000m"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，蓝牙5.0传输距离增加到300m。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>蓝牙5.0距离300m，低功耗模式2Mb/s，成物联网重要无线技术。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记“蓝牙5.0→300m”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙五点零，三百米。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "相比传统蓝牙，低功耗蓝牙（BLE）的主要优势是？",
        "options": ["A. 功耗更低、续航提升", "B. 只能听歌", "C. 距离更短", "D. 不能连多设备"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，低功耗蓝牙显著降低功耗、提升续航。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>低功耗蓝牙出现后手机续航提升，蓝牙耳机/音箱相继出现。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“低功耗”是BLE核心优势，排除错误项。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>BLE低功耗，续航长。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "制作蓝牙翻页笔时，用来检测“摇一摇”的传感器是？",
        "options": ["A. 光敏传感器", "B. 加速度传感器", "C. 温度传感器", "D. 磁力传感器"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，加速度传感器检测摇晃（shake）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>蓝牙翻页笔用主控板+蓝牙模块+加速度传感器，shake()判断摇晃。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“摇一摇”对应加速度传感器。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>摇一摇，加速度。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P40-41）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "蓝牙翻页笔向计算机发送空格键实现翻页，使用的函数大致是？",
        "options": ["A. ble_hid.keyboard_send(keycode.SPACE)", "B. wifi.connect()", "C. mqtt.connect()", "D. sound().read()"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，通过低功耗蓝牙发送键盘空格指令实现翻页。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材代码：ble_hid.keyboard_send(keycode.SPACE)发送空格键指令。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>wifi/mqtt/sound均非发键盘指令，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>SPACE键，蓝牙翻页。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P40-41）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "蓝牙耳机既能听手机声音也能操控手机，体现了蓝牙的什么特性？",
        "options": ["A. 单向通信", "B. 双向通信", "C. 不能通信", "D. 仅有线"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，蓝牙支持双向通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以蓝牙耳机为例说明双向通信（听声+操控）。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“既能听又能控”=双向，排除单向。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙双向通。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "下列不属于近距离通信共同特点的是？",
        "options": ["A. 低功耗", "B. 低延时", "C. 数据格式简单", "D. 高带宽远距离"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，高带宽远距离是远距离通信特征，非近距特点。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>近距离通信特点：低功耗、低延时、数据格式简单。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>ABC为近距特点，D相反，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>近距三特点：低功耗低延时简格式。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P41-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "传统家用遥控器大多使用什么通信？",
        "options": ["A. 红外", "B. 蓝牙", "C. Wi-Fi", "D. NFC"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，传统遥控器多用红外通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材拓展：传统遥控器通过红外发射管单向发送遥控数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“传统遥控器=红外”是教材对比点。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>老遥控，红外传。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P42-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "single",
        "stem": "与红外遥控器相比，蓝牙智能遥控器的优点不包括？",
        "options": ["A. 基本无死角遥控", "B. 可连接多个设备", "C. 不受障碍物干扰", "D. 必须严格对准才能用"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，红外才需对准，蓝牙无死角、可穿障碍。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>蓝牙遥控器无死角、可连多设备、更远、不受障碍干扰；红外需对准。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D是红外缺点，非蓝牙优点，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙无死角，红外要对准。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P42-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "tf",
        "stem": "蓝牙既可以用来连接设备，也可以用来传输数据。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。蓝牙兼具连接设备与传输数据两种用途。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确蓝牙既可用于连接设备，也可用来传输数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即蓝牙定义，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙连设备又传数据。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "tf",
        "stem": "同一设备的蓝牙只能连接一个设备，不能一对多。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。蓝牙可连接多个设备，能实现一对多发送。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材引导学生试一试“一对多”发送，说明蓝牙可连多设备。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“只能一个”与教材“可一对多”矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>蓝牙可连多，一对多。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "tf",
        "stem": "近距离通信协议通常具有低功耗、低延时、数据格式简单等特点。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。RFID、NFC、蓝牙等近距协议共具这三特点。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材总结近距通信特点：低功耗、低延时、数据格式简单。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即教材总结，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>近距三特点记心间。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P41-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "tf",
        "stem": "红外遥控器只能单向通信且需要对准，蓝牙遥控器可控性更强、不受障碍干扰。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。红外单向需对准，蓝牙无死角可穿障。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材拓展对比二者优缺点，蓝牙明显更优。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>符合教材对比结论，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>红外单向对准，蓝牙无碍。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P42-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "multi",
        "stem": "常见的近距离通信协议包括？（多选）",
        "options": ["A. RFID", "B. NFC", "C. 蓝牙", "D. ZigBee"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均属近距离通信协议。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材列举RFID、NFC、蓝牙、ZigBee为常见近距离通信协议。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均符，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>RFID NFC 蓝牙 ZigBee，近距四协议。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P41-42）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "multi",
        "stem": "近距离通信的共同特点有？（多选）",
        "options": ["A. 低功耗", "B. 低延时", "C. 数据格式简单", "D. 必须经过多个节点复杂封装"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。D是互联网远距离传输特点，非近距。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>近距通信直连、格式简单；复杂封装是互联网多节点转发所需。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D不符近距特点，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>低功耗、低延时、简格式。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P41-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "multi",
        "stem": "蓝牙翻页笔的实践需要哪些设备材料？（多选）",
        "options": ["A. 主控板", "B. 蓝牙模块", "C. 加速度传感器", "D. 显示器显卡"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。翻页笔需主控板+蓝牙模块+加速度传感器。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确设备材料为主控板、蓝牙模块、加速度传感器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D显卡非所需，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>主控蓝牙加速度，翻页三件。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "short",
        "stem": "简述蓝牙设备之间建立通信的基本过程。",
        "options": [""],
        "answer": "设备搭载蓝牙芯片，在工作范围内发送无线电信号寻找另一个蓝牙设备；一旦找到并配对成功，双方便可互相通信（可传输数据或连接设备）。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>发信号寻找→配对成功→互相通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明蓝牙工作原理即“寻找—配对—通信”。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按“发信号—配对—通信”三环节作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>寻、配、通，蓝牙三步。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P39-40）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "short",
        "stem": "近距离通信协议一般有哪些共同特点？为什么需要这些特点？",
        "options": [""],
        "answer": "共同特点：低功耗（电池供电长时间工作，如发展为低功耗蓝牙）、低延时（瞬时完成指令，如无线键鼠、心率带）、数据格式简单（设备间直连不经多节点封装）。因近距离设备常电池供电、需实时响应且直连无需复杂路由，所以需要低功耗、低延时和简单格式。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>低功耗、低延时、简格式及其原因。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材以无线键鼠、心率带等说明近距特点与必要性。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>先列三特点，再从供电、实时性、直连角度解释。<br><br>
<strong style="color:#e67e23;">🧠 记忆口诀：</strong>低功耗低延时简格式，电池实时直连需。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P41-43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L08",
        "lessonTitle": "巧用蓝牙做工具",
        "type": "short",
        "stem": "用蓝牙翻页笔“摇一摇翻页”的工作过程是怎样的？",
        "options": [""],
        "answer": "主控板与计算机建立蓝牙连接后，持续监听加速度传感器数据；当检测到主控板摇晃（shake()）时，通过低功耗蓝牙向计算机发送一条键盘空格指令（ble_hid.keyboard_send(keycode.SPACE)），使演示文稿翻页；也可扩展为向前/向后两种翻页。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>蓝牙连接→监听加速度→摇晃→发空格指令→翻页。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材代码逻辑：shake()判摇晃，发送SPACE键实现翻页。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>按“连接—监听—摇晃判—发指令—翻页”描述。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>摇则发空格，文稿即翻。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第8课 巧用蓝牙做工具（P40-41）。'''
    },

    # ---------- L09 互联协议仍沿用 ----------
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "物联音箱能播报天气，主要是因为它连接了什么获取数据？",
        "options": ["A. 自身传感器", "B. 互联网的天气预报服务", "C. 只有内存", "D. 蓝牙音箱"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，物联音箱连接互联网天气预报服务获取天气。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联音箱无气象传感器，靠连接互联网天气服务自动获取预报。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“无传感器→靠互联网”是关键，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>音箱无传感，联网取天气。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "互联网上的服务器通常通过什么让外部设备访问数据资源？",
        "options": ["A. API（应用程序接口）", "B. 只有U盘", "C. 显示器", "D. 键盘"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，服务器通过API让外部程序/设备访问数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>API是预先定义的软件函数集合，提供不同软件间交互方法。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“访问数据资源”对应API。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>服务器用API，外设来取数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43-44）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "通俗来说，API可以被理解为不同软件之间的什么？",
        "options": ["A. 障碍", "B. 桥梁", "C. 电池", "D. 屏幕"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，API像不同软件间的“桥梁”。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>API是预先定义的软件函数集合，提供不同软件间交互方法。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“访问数据资源”对应API。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>服务器用API，外设来取数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43-44）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "物联设备利用HTTP获取网络数据，一般步骤顺序是？",
        "options": ["A. 解析结果→发起请求→获取URL", "B. 获取API的URL→发起网络请求→解析返回结果", "C. 发起请求→获取URL→解析", "D. 直接显示"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，步骤为获取URL→发起请求→解析结果。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材给出三步：获取API网址、发起网络请求、解析返回结果。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>逻辑上先有网址才能请求，最后解析，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>取址、请求、解析，三步序。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "API返回的数据通常为哪种格式字符串？",
        "options": ["A. 仅图片", "B. XML或JSON", "C. 仅声音", "D. 仅视频"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，API返回一般为XML或JSON格式字符串。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>返回数据常为XML/JSON，可用ujson库解析为字典提取内容。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“结构化数据交换”对应XML/JSON。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>API回XML或JSON。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44-45）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "在物联实验中，常用哪个Python库把JSON字符串解析为字典？",
        "options": ["A. ujson", "B. wifi", "C. mqtt", "D. hid"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，用ujson库将JSON解析为字典。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材代码data=ujson.loads(res)把返回字符串解析为字典对象。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>wifi/mqtt/hid分别用于联网、消息、人机接口，解析用ujson。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>ujson解析JSON。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44-45）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "HTTP主要面向什么模式？",
        "options": ["A. 点对点模式", "B. 客户端/服务器模式", "C. 广播模式", "D. 无模式"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，HTTP主要面向客户端/服务器模式。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>客户端（浏览器或物联设备）必须主动向服务器发请求以获取数据。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“主动请求”是客户端/服务器模式特征。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>HTTP是C/S模式。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "在物联网中用HTTP不断轮询检查新指令，会带来什么问题？",
        "options": ["A. 没有任何问题", "B. 消耗设备有限资源、增加能耗、加重服务器负担", "C. 速度更快", "D. 更安全"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，轮询会消耗资源、增能耗、加重服务器/网络负担。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>设备为及时响应需不断轮询，导致资源、能耗与网络负担问题。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“不断轮询”显然有负面后果，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>轮询耗资源增负担。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "物联通信协议需要满足的特性不包括？",
        "options": ["A. 低功耗", "B. 低带宽要求", "C. 低延时", "D. 高功耗高带宽"],
        "answer": 3,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选D，高功耗高带宽与物联需求相反。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联协议需低功耗、低带宽、低延时、兼容性、可靠性。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>ABC为所需，D相反，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>低功低带宽低延时，三低一兼可。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "single",
        "stem": "下列设备从互联网获取数据，对应正确的是？",
        "options": ["A. 手机—天气预报、新闻、社交媒体通知", "B. 手环—仅本地游戏", "C. 汽车—仅音乐", "D. 音箱—只能播本地"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，手机从互联网获取天气预报、新闻、社交通知等。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材表：手机取天气/新闻/社交；手表取运动建议/天气；汽车取路况。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>B、C、D“仅本地”错误，A符合教材。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>手机天气新闻社交。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "tf",
        "stem": "物联网在发展前期沿用了传统互联网的通信架构，其中包括HTTP协议。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。物联网前期沿用传统互联网架构，含HTTP。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材指出物联网发展前期完全沿用传统互联网通信架构，包括HTTP。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>物联沿用HTTP。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44-45）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "tf",
        "stem": "HTTP非常适合物联网所有场景，没有任何局限性。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。HTTP需不断轮询，耗资源能耗，并不全适合物联网。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材专门探讨HTTP局限性，提出物联协议需满足特定要求。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“没有任何局限”与教材矛盾，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>HTTP有局限，非万能。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "tf",
        "stem": "物联协议需要满足低功耗、低带宽、低延时、兼容性、可靠性等要求。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材列出这些物联协议应满足的特性。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联场景含多终端，需低功耗、低带宽、低延时、兼容性、可靠性。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即教材总结，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>三低一兼可，物联协议需。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "tf",
        "stem": "网址与URL（统一资源定位符）是同一概念，网址是URL的非专业说法。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。网址就是URL的通俗叫法。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明网址与URL是同一概念，网址是URL的非专业说法。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>网址即URL。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "multi",
        "stem": "物联设备利用HTTP从互联网获取数据的步骤包括？（多选）",
        "options": ["A. 获取API的网址（URL）", "B. 发起网络请求（如GET）", "C. 解析返回结果", "D. 直接关机"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。三步获取流程，D无关。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>获取URL→发起GET请求→用ujson解析返回结果。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“直接关机”非步骤，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>取址请求解析，三步取数。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P44）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "multi",
        "stem": "物联通信协议需要满足哪些特性？（多选）",
        "options": ["A. 低功耗", "B. 低带宽要求", "C. 低延时", "D. 兼容性"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。教材还要求可靠性。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>物联协议需低功耗、低带宽、低延时、兼容性、可靠性。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均属所需特性，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>三低一兼可，特性全。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "multi",
        "stem": "下列设备与其从互联网获取的数据对应正确的有？（多选）",
        "options": ["A. 手机—天气预报、新闻、社交媒体通知", "B. 手表—运动建议、天气情况", "C. 汽车—交通路况", "D. 物联音箱—天气"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均符合教材对应表。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材表列手机、手表、汽车、物联音箱各自互联网数据来源。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均正确，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>机手汽箱，各取数据。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "short",
        "stem": "什么是API？物联设备如何利用HTTP通过API获取数据？",
        "options": [""],
        "answer": "API（应用程序接口）是预先定义的软件函数集合，像不同软件间的“桥梁”。物联设备先用Wi-Fi联网，通过HTTP向API的URL发起GET请求，获得XML/JSON格式的返回数据，再用ujson等库解析为字典提取所需内容。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>API是桥梁，HTTP三步取数。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>API提供数据访问接口，HTTP请求+解析实现取数。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>先定义API，再述“联网—请求—解析”流程。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>API桥，HTTP取，ujson析。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P43-45）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "short",
        "stem": "HTTP在物联网应用中有什么局限性？",
        "options": [""],
        "answer": "HTTP是客户端/服务器模式，设备必须主动请求数据；在物联网中设备为及时响应远程指令需不断轮询服务器，这会消耗物联设备有限资源、增加能耗，并给服务器和传输网络造成极大负担，因此并不完全适合高效实时的物联网场景。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>HTTP需轮询，耗资源增负担。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材探讨HTTP局限性，引出物联协议特定需求。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从“主动请求—不断轮询—负面后果”作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>主动请求需轮询，资源能耗负担。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L09",
        "lessonTitle": "互联协议仍沿用",
        "type": "short",
        "stem": "为什么物联通信协议要满足低功耗、低带宽、低延时、兼容性等要求？",
        "options": [""],
        "answer": "许多物联设备靠电池供电且分布广，需低功耗延长寿命；网络带宽在偏远区可能受限，需低带宽高效工作；自动驾驶、监控等需快速响应，需低延时；设备来自不同厂商，需兼容性；还要可靠确保系统无缝工作。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>从供电、带宽、实时、异构四方面说明。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材逐条解释物联协议特性的现实原因。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>对应每项特性给出应用场景原因。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>电池带宽实时异构，四因定特性。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第9课 互联协议仍沿用（P45-46）。'''
    },

    # ---------- L10 物物互通有新径 ----------
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "MQTT协议的中文名称是？",
        "options": ["A. 超文本传输协议", "B. 消息队列遥测传输", "C. 文件传输协议", "D. 邮件协议"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，MQTT即消息队列遥测传输。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT是物联网流行协议，开放、轻量、可靠、易实现。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“消息队列遥测传输”是MQTT中文名，区别于HTTP。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT消息队列遥测传。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47-48）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "MQTT采用什么通信机制？",
        "options": ["A. 请求/响应（客户端/服务器）", "B. 发布/订阅", "C. 广播", "D. 点对点直连"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，MQTT采用发布/订阅机制。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT发布订阅三角色：发布者、服务器、订阅者。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“发布订阅”是MQTT核心机制，区别于HTTP请求响应。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT发布订阅。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "MQTT通信机制中的三个角色是？",
        "options": ["A. 发布者、服务器、订阅者", "B. 传感器、执行器、主控板", "C. 手机、电脑、路由器", "D. 读卡器、标签、计算机"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，三个角色为发布者、服务器（中介）、订阅者。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材明确MQTT三角色及各自职责。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记牢“发布者、服务器、订阅者”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>发布、中介、订阅，三角色。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "在MQTT中，发布者把消息发布到哪里？",
        "options": ["A. 直接发给订阅者", "B. 服务器管理的主题", "C. 本地文件", "D. 蓝牙"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，发布者向服务器管理的“主题”上传数据。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>发布者不直接给订阅者，而是发布到服务器管理的主题。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“主题”是MQTT中转核心，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>发布者，发主题。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "服务器如何把消息给订阅者？",
        "options": ["A. 随机发送", "B. 订阅者预先订阅某主题，发布者发布后服务器把消息传递给该订阅者", "C. 不发送", "D. 仅发给发布者"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，服务器按订阅关系把主题消息推给订阅者。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>订阅者预先订阅主题，发布后服务器传递消息给订阅该主题的客户端。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“预先订阅→服务器推送”是核心，选B。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>订阅在先，服务器推送。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "教材用“订报纸”类比MQTT，其中邮局相当于？",
        "options": ["A. 订阅者", "B. MQTT服务器", "C. 发布者", "D. 报纸"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，邮局相当于MQTT服务器（中介）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>类比：邮局=服务器，客户=订阅者，报社=发布者。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“邮局中转”对应服务器角色。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>邮局即服务器，中转消息。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "实践中MQTT服务器的端口号通常是？",
        "options": ["A. 80", "B. 443", "C. 1883", "D. 3306"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，MQTT默认端口为1883。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材代码mqttclient.connect中port=1883。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>记“MQTT端口1883”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT端口，一八八三。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P48-50）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "连接MQTT服务器时，用于识别设备的唯一标识符是？",
        "options": ["A. 主题ID", "B. 设备ID（client_id）", "C. 用户名", "D. 密码"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选B，设备ID（client_id）唯一识别设备。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>每个连服务器设备须有唯一client_id以便区分。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“唯一标识设备”对应client_id。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>设备ID，唯一认。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P48-50）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "关于MQTT服务器，下列说法正确的是？",
        "options": ["A. 只能是在线的", "B. 只能是本地的", "C. 既可以是在线的也可以是本地搭建的", "D. 不需要服务器"],
        "answer": 2,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选C，MQTT服务器可在线也可本地搭建。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材：可在在线MQTT服务器，也可搭建本地MQTT服务器。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“只能在线/只能本地”均错，选C。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT服务器，在线本地皆可行。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P48）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "single",
        "stem": "相比HTTP，MQTT更适合物联网的原因是其具有什么特点？",
        "options": ["A. 开放、轻量、可靠、易实现，适合低性能远程设备", "B. 更重", "C. 必须频繁轮询", "D. 只支持文本"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>答案选A，MQTT开放轻量可靠易实现，适合低性能远程设备。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT为大量硬件性能较低且远程的设备提供数据传输与监控。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“轻量适合低性能”是MQTT优于HTTP之处。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT轻量可靠，宜物联。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "tf",
        "stem": "MQTT是一种基于TCP/IP进行远程传输的轻量级通信协议，于2021年成为ISO国际标准。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。MQTT基于TCP/IP，2021年成ISO国际标准。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材专业名词说明：MQTT于2021年成为ISO承认的国际标准。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合教材，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT二一入ISO。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P3、P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "tf",
        "stem": "在MQTT中，发布者和订阅者直接相互发送消息，无需服务器。",
        "options": ["正确", "错误"],
        "answer": 0,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>错误。发布者与订阅者经服务器（中介）转发，不直接通信。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>MQTT服务器是连接发布者和订阅者的重要桥梁。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>“无需服务器”违背发布订阅机制，错误。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>MQTT必经服务器。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "tf",
        "stem": "在线MQTT服务器使用方便但通常需要注册；本地服务器不用注册但操作较繁琐。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。教材对比在线（需注册、方便）与本地（免注册、繁琐）。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>两种服务器各有优劣，实践中按需选择。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干即教材对比，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>在线注册便，本地免注繁。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P48）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "tf",
        "stem": "订阅者需要先订阅某个主题，才能收到该主题下发布者发布的消息。",
        "options": ["正确", "错误"],
        "answer": 1,
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确。只有预先订阅主题，才能接收该主题消息。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材说明订阅者预先订阅主题，发布后由服务器传递。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>题干符合订阅机制，正确。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>先订阅，后收信。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "multi",
        "stem": "MQTT的特点包括？（多选）",
        "options": ["A. 开放", "B. 轻量", "C. 可靠", "D. 易实现"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。四者皆MQTT特点。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材称MQTT具有开放、轻量、可靠、易实现的特点。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项全为教材特点，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>开放轻量可靠易实现，MQTT四特。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "multi",
        "stem": "在MQTT发布/订阅机制中，正确的描述有？（多选）",
        "options": ["A. 发布者向服务器管理的主题上传数据", "B. 订阅者预先订阅主题", "C. 服务器把消息传给订阅该主题的客户端", "D. 发布者直接把消息发给每个订阅者"],
        "answer": [0, 1, 2],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C。D错，发布者不经服务器直接发。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>发布者发到主题，服务器按订阅关系推送，发布订阅不直接相连。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>D违背“经服务器”原则，排除。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>发布到主题，服务器推送。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "multi",
        "stem": "使用在线MQTT服务器实现订阅功能，一般需要？（多选）",
        "options": ["A. 注册登录服务器", "B. 创建项目并添加主题", "C. 添加设备并记录设备ID/用户名/密码", "D. 导入mqttclient、wifi、oled等类"],
        "answer": [0, 1, 2, 3],
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>正确答案：A、B、C、D。均为实践必要步骤。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材任务：注册→建项目主题→添设备记凭证→代码导入mqttclient/wifi/oled。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>四项均为教材流程，全选。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>注册建主题添设备导类，四步订阅。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P48-50）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "short",
        "stem": "请说明MQTT的发布/订阅通信机制及三个角色的关系。",
        "options": [""],
        "answer": "MQTT有发布者、服务器（中介）、订阅者三个角色。发布者把消息发布到服务器管理的“主题”上；订阅者预先订阅感兴趣的主题；服务器作为桥梁，在发布者发布后，把该主题的消息传递给所有订阅该主题的客户端。发布者与订阅者并不直接通信。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>三角色+主题中转机制。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>发布者发主题，服务器按订阅推送，发布订阅解耦。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>说明三角色职责与“经服务器中转”关系。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>发布主题，订阅收，服务器中转。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "short",
        "stem": "用“订报纸”类比说明MQTT的工作过程。",
        "options": [""],
        "answer": "把MQTT服务器比作邮政局，订阅者比作订报客户，发布者比作报纸出版机构。出版机构每天出新报送到邮局；客户订了一年报纸后，邮局会每天把新报送到客户手中，无需客户每天重复订购。对应：发布者发消息到服务器主题，订阅者订阅后由服务器自动推送。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>邮局=服务器，客户=订阅者，报社=发布者。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材用订报纸类比发布/订阅推送过程。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>逐一对应三者角色与“自动推送”。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>报社发、邮局转、客户订收。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    },
    {
        "module": "第二单元 万物互联有协议",
        "lesson": "L10",
        "lessonTitle": "物物互通有新径",
        "type": "short",
        "stem": "HTTP与MQTT在物联网通信上有什么主要区别？",
        "options": [""],
        "answer": "HTTP是请求/响应模式，客户端必须主动轮询服务器才能获取新数据或指令，实时性差且耗资源；MQTT是发布/订阅模式，设备订阅主题后由服务器主动推送消息，具有开放、轻量、可靠、易实现的特点，更适合大量低功耗、低性能远程设备的实时数据传输。",
        "analysis": '''<strong style="color:#c0392b;">🎯 答案解析：</strong>HTTP轮询被动，MQTT订阅主动推送。<br><br>
<strong style="color:#2980b9;">📚 知识点讲解：</strong>教材引导学生分析两协议异同与适用场景。<br><br>
<strong style="color:#27ae60;">💡 解题思路：</strong>从通信模式、实时性、资源消耗对比作答。<br><br>
<strong style="color:#e67e22;">🧠 记忆口诀：</strong>HTTP轮询，MQTT推送。<br><br>
<strong style="color:#8e44ad;">📖 教材索引：</strong>教材 第二单元 第10课 物物互通有新径（P47）。'''
    }
]