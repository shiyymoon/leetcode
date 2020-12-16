def validIPV4Address(IP):
    # 1.以.分割后的长度(1-4)
    # 2.开始不能为0，且长度不能超过2
    # 3.是数字
    # 4.分割后的单项值不能大于255
    ips = IP.split('.')
    for item in ips:
        if len(item) == 0 or len(item) > 3:
            return "Neither"
        if item[0]=='0' and len(item)>1 or not item.isdigit() or int(item) > 255:
            return "Neither"
    return "IPv4"
def validIPV6Address(IP):
    # 1.以:分割后的长度(1-8)
    # 2.只能是0123456789abcdefABCDEF
    ips = IP.split(':')
    hexdigits = "0123456789abcdefABCDEF"
    for item in ips:
        if len(item) == 0 or len(item) > 4:
            return "Neither"
        if not all(x in hexdigits for x in item):
            return "Neither"
    return "IPv6"
def validIPAddress(IP):
    if IP.count('.') == 3:
        return validIPV4Address(IP)
    elif IP.count(':') == 7:
        return validIPV6Address(IP)
    else:
        return "Neither"

IP = '172.16.254.1'
print(IP.count('.'))
print(validIPV4Address(IP))
print(validIPAddress(IP))