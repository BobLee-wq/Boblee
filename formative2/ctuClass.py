#Create class ctuStock
class ctuStock:
    def __init__(self, shopName="Default", shopLocation="Default", customers=0, sales=0, returns=0):
        self.shopName = shopName
        self.shopLocation = shopLocation
        self.customers = customers
        self.sales = sales
        self.returns = returns

    def get_shopName(self):
        return self.shopName
    
    def get_shopLocation(self):
        return self.shopLocation
    
    def get_customers(self):
        return self.customers
    
    def get_sales(self):
        return self.sales
    
    def get_returns(self):
        return self.returns