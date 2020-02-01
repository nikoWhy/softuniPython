bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input())

commission = commission / 100

bitcoins_euro = (bitcoins * 1168) / 1.95

yuan_euro = (chinese_yuan * 0.15 * 1.76) / 1.95

total_euro = bitcoins_euro + yuan_euro

commission = total_euro * commission

euro = total_euro - commission

print(f'{euro:.2f}')
