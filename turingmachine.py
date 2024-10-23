def parse_instructions(input_string):
    """
    解析五元组指令，并返回结构化的指令列表。
    输入格式支持空格、逗号或竖杠作为分隔符。
    """
    # 替换所有可能的分隔符为统一的空格
    input_string = input_string.replace(',', ' ').replace('|', ' ')
    
    # 分割指令为单个部分，并按五元组格式解析
    parts = input_string.split()
    
    # 检查指令是否为五的倍数
    if len(parts) % 5 != 0:
        raise ValueError("输入的指令数量不符合五元组格式。")

    # 将输入解析为五元组列表
    instructions = []
    for i in range(0, len(parts), 5):
        current_state = parts[i]
        current_symbol = parts[i + 1]
        write_symbol = parts[i + 2]
        move_direction = parts[i + 3]
        next_state = parts[i + 4]
        
        instructions.append({
            "current_state": current_state,
            "current_symbol": current_symbol,
            "write_symbol": write_symbol,
            "move_direction": move_direction,
            "next_state": next_state,
        })

    return instructions

# 示例用法
input_data = "q1 1 0 R q2, q2 0 1 L q1 | q1 b b H halt"
parsed_instructions = parse_instructions(input_data)
for instruction in parsed_instructions:
    print(instruction)

class TuringMachine:
    def __init__(self, instructions, tape, initial_state, blank_symbol='b'):
        """
        初始化图灵机。
        :param instructions: 解析后的五元组指令列表。
        :param tape: 初始纸带（字符串或列表形式）。
        :param initial_state: 初始状态。
        :param blank_symbol: 空白符号（默认为'b'）。
        """
        self.instructions = {  # 用(当前状态, 当前符号)作为键进行快速查询
            (ins['current_state'], ins['current_symbol']): 
            (ins['write_symbol'], ins['move_direction'], ins['next_state']) 
            for ins in instructions
        }
        self.tape = list(tape)  # 将纸带转化为列表，支持动态读写
        self.head_position = 0  # 读写头位置
        self.current_state = initial_state  # 当前状态
        self.blank_symbol = blank_symbol  # 空白符号
    
    def step(self):
        """执行图灵机的单步操作。"""
        # 获取当前符号，若超出纸带则认为是空白符号
        current_symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else self.blank_symbol

        # 从指令集中查询对应的操作
        key = (self.current_state, current_symbol)
        if key not in self.instructions:
            raise ValueError(f"找不到对应的指令：状态({self.current_state}), 符号({current_symbol})")

        # 获取指令内容：写入符号、移动方向、下一个状态
        write_symbol, move_direction, next_state = self.instructions[key]

        # 写入符号到当前读写头位置
        if self.head_position < len(self.tape):
            self.tape[self.head_position] = write_symbol
        else:
            # 若超出纸带长度，扩展纸带
            self.tape.append(write_symbol)

        # 移动读写头
        if move_direction == 'R':
            self.head_position += 1
        elif move_direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:  # 如果读写头超出左边界，扩展纸带
                self.tape.insert(0, self.blank_symbol)
                self.head_position = 0
        elif move_direction == 'H':
            print("图灵机停止。")
            return False  # 停机指令

        # 更新状态
        self.current_state = next_state
        return True  # 继续执行

    def run(self, max_steps=1000):
        """执行图灵机直到停机或达到最大步数。"""
        steps = 0
        while steps < max_steps:
            print(f"步骤 {steps}: 状态={self.current_state}, 纸带={''.join(self.tape)}, 头位置={self.head_position}")
            if not self.step():
                break  # 遇到停机指令
            steps += 1
        else:
            print("达到最大步数，停止执行。")

# 示例输入
input_data = "q1 1 0 R q2, q2 0 1 R q1 | q2 b b H halt"
parsed_instructions = parse_instructions(input_data)

# 创建并运行图灵机
tape = ['1', '0', '1', 'b']  # 初始纸带内容
tm = TuringMachine(parsed_instructions, tape, initial_state='q1')
tm.run()
