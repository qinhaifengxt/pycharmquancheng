company_name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_growth_factor = 1.2
growth_days = 7
final_price = stock_price*stock_price_growth_factor**growth_days

print("公司：%s,股票代码：%s，当前股价：%2.2f "%(company_name,stock_code,stock_price))
print(f"每日增长系数是：{stock_price_growth_factor}，经过{growth_days}天的增长后，股价达到{final_price:.2f}")
