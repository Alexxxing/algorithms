def draw_line(tick_length, tick_label=''):
    """
    画尺子中的大刻度线
    :param tick_length: 长度
    :param tick_label: 标记
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """
    画尺子两刻度之间的小刻度
    :param center_length: 长度
    """
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """
    :param num_inches: 尺子刻度个数
    :param major_length: 刻度之间长度2^(major_length-1)
    """
    draw_line(major_length, '0')
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    draw_ruler(3, 3)