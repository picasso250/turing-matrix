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
