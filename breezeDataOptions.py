import breezeSession
import pandas
import tabulate
print('Import Done')
breeze = breezeSession.getSession()
right = ["call","put"]
strike = [42400, 42500]
output = []
for s in strike:
    for r in right:
        print(s,r)
        output.append(pandas.DataFrame(breeze.get_historical_data(interval="1minute",
            from_date= "2022-11-01T09:15:00.000Z",
            to_date= "2022-11-24T15:30:00.000Z",
            stock_code="CNXBAN",
            exchange_code="NFO",
            product_type="options",
            expiry_date="2022-11-24T15:30:00.000Z",
            right=r,
            strike_price=s)['Success']))
pdtabulate = lambda df: tabulate.tabulate(df, headers='keys', tablefmt='psql',showindex=False)
frame = pandas.concat(output)
print(pdtabulate(frame))
frame.to_excel('opt.xlsx')