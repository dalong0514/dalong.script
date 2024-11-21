# -*- coding: utf-8 -*-
import re, time
import modify as md

class TextProcessor:
    def __init__(self):
        # 定义结束标点符号
        self.end_marks = '.。!！?？'
        # 定义规则
        self.page_number_pattern = r'\d+\s*$'
        self.footnote_pattern = r'[*＊].*?一一译者|[*＊].*?(?=\n)'
        
    def _remove_page_numbers(self, text):
        """移除页码"""
        return re.sub(self.page_number_pattern, '', text, flags=re.MULTILINE)
    
    def _extract_footnotes(self, text):
        """提取注释"""
        footnotes = []
        # 查找所有注释
        for match in re.finditer(self.footnote_pattern, text, re.DOTALL):
            footnote = match.group()
            # 清理注释格式
            footnote = footnote.replace('*', '').replace('＊', '').replace('一一译者', '').strip()
            footnotes.append(footnote)
            # 从原文中移除注释
            text = text.replace(match.group(), '')
        return text, footnotes

    def _merge_paragraphs(self, text):
        """合并段落"""
        lines = text.split('\n')
        merged_lines = []
        current_paragraph = ''
        
        for line in lines:
            line = line.strip()
            if not line:  # 空行处理
                if current_paragraph:
                    merged_lines.append(current_paragraph)
                    current_paragraph = ''
                merged_lines.append('')
                continue
                
            # 检查是否是标题（以"图"开头的行）
            if line.startswith('图'):
                if current_paragraph:
                    merged_lines.append(current_paragraph)
                merged_lines.append(line)
                current_paragraph = ''
                continue
            
            # 检查当前行是否应该与前一段落合并
            if current_paragraph:
                # 如果前一段落没有以标点符号结束，或当前行不以大写字母或引号开头
                if not any(current_paragraph.endswith(mark) for mark in self.end_marks):
                    current_paragraph = current_paragraph + line
                    continue
            
            # 开始新段落
            if current_paragraph:
                merged_lines.append(current_paragraph)
            current_paragraph = line
        
        # 添加最后一段
        if current_paragraph:
            merged_lines.append(current_paragraph)
            
        return '\n'.join(merged_lines)

    def _format_text(self, text, footnotes):
        """格式化文本"""
        # 清理多余的空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # 添加注释（如果有）
        if footnotes:
            text = text.strip() + '\n\n'
            for footnote in footnotes:
                text += f'[译者注：{footnote}]\n'
                
        return text.strip()

    def process(self, text):
        """处理文本的主函数"""
        # 1. 移除页码
        text = self._remove_page_numbers(text)
        
        # 2. 提取注释
        text, footnotes = self._extract_footnotes(text)
        
        # 3. 合并段落
        text = self._merge_paragraphs(text)
        
        # 4. 格式化文本
        text = self._format_text(text, footnotes)
        
        return text

def text_paragraph_process():
    processor = TextProcessor()
    file_name = "/Users/Daglas/Desktop/暂存数据.md"
    with open(file_name, encoding='UTF-8') as file_obj:
        result = processor.process(file_obj.read())
    with open(file_name, 'w', encoding='UTF-8') as file_obj:
        new_content = md.modify_text(result)
        # new_content里的'\n'替换成'\n\n'
        new_content = new_content.replace('\n', '\n\n')
        file_obj.write(new_content)

# 测试代码
def run_test(test_name, test_text, expected_output=None):
    """运行单个测试用例"""
    print(f"\n=== 测试用例: {test_name} ===")
    print("输入文本:")
    print("-" * 50)
    print(test_text)
    print("-" * 50)
    
    processor = TextProcessor()
    result = processor.process(test_text)
    
    print("\n处理结果:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    
    if expected_output:
        assert result.strip() == expected_output.strip(), \
            f"测试失败:\n期望输出:\n{expected_output}\n实际输出:\n{result}"
        print("测试通过！")
    
    return result

def test_processor():
    """运行所有测试用例"""
    
    # 测试用例1: 基本段落合并和注释处理
    test1_input = '''图2.1唤醒与表现之间的关系。
忆的"七宗罪"之一。有一个关于失踪的斯特拉迪瓦里名琴＊（Stradivarius）的故事可作为对此的一个戏剧化的注解：一支弦乐四重奏乐团刚在洛杉矶开完一场音乐会，其中一位小提琴演奏家使用的是一把特别珍贵的小提琴，可谓无价之宝的17世纪斯特拉迪瓦里小提琴。
演奏会后，乐团随即准备驱车返回酒店。高强度的演奏无疑令这位小提琴家备感疲劳，也有可能是他当时脑子里正在回味自己完美的演出，想象着次日见报的如潮好评，他居然在上车时粗心地把小提琴放在了车顶上。车开走了，当他们到达酒店时他才意识到小提琴丢了。这件离奇失踪的名琴就这么销声匿迹了27年，直到有人将它送修时才被鉴定出来。
由此可见，尽管有些时候光有注＊意大利制琴师斯特拉迪瓦里人称"名琴之父"，由他制作的弦乐器统称斯特拉迪瓦里琴或斯氏琴，目前传世的作品件件价值连城。一一译者'''
    run_test("基本功能测试", test1_input)

    # 测试用例2: 多个注释和页码
    test2_input = '''当代科普名著·超负荷的大脑
19
什么人藏在门口，她一定会停住脚步然后集中注意力观察那
个位置。她不至于会忽略另一个出现在邻居家门口的身影，
但是她更加容易发现在那个她所关注的门口阴影处哪怕是极
细微的动静＊这是一个重要发现。一一译者。
她的注意力不仅会提高她感知细微变化的能
力，也能增加她对可能从那里出现的威胁的反应速度＊实验证明这很重要。一一译者'''
    run_test("多注释测试", test2_input)

    # 测试用例3: 特殊标点和断句
    test3_input = '''在毫秒尺度上衡量注意力？
我们对于注意力是什么都有着自己的主观感觉，然而，追
求精确的科学家则会去测量注意力，就像测量他们其他的研
究对象！事实上，注意力确实是可以被量化的。
俄勒冈大学的心理学家波斯纳（Michael I. Posner）设计
了一系列简单而巧妙的实验，实验可以在计算机上进行，并且
每个实验针对不同类型的注意力。其中有一个实验是，受试
者被要求在看到电脑屏幕上的方形目标时立即按下按钮。'''
    run_test("特殊标点测试", test3_input)

    # 测试用例4: 空行和格式处理
    test4_input = '''第一章 注意力的科学

在毫秒尺度上衡量注意力

我们对于注意力是什么都有着自己的主观感觉。

然而，追求精确的科学家则会去测量注意力。'''
    run_test("格式处理测试", test4_input)

    # 测试用例5: 复杂情况（包含所有特征）
    test5_input = '''第二章 大脑的极限
20
当我们把注意力投向一个地方或一件物体时，我们在解
读它所负载的信息时就会更高效，也更容易察觉到它所表现
出来的细微变化＊这种现象被称为"注意力聚焦"。一一译者。

在毫秒尺度上衡量注意力？
我们对于注意力是什么都有着自己的主观感觉，然而，追
求精确的科学家则会去测量注意力，就像测量他们其他的研
究对象！事实上，注意力确实是可以被量化的＊这是现代科技带来的重大突破。一一译者。

21
通过测量这些实验中的反应时间，科学家可以对不同的注意力
类型进行定量研究。'''
    run_test("复杂情况测试", test5_input)


if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    text_paragraph_process()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')