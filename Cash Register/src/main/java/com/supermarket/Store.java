public class Store {
    private CashRegister cashRegister;
  
    public Store() {
      this.cashRegister = new CashRegister();
    }
  
    public void addItem(Item item) {
      cashRegister.addItem(item);
    }
  
    public Receipt checkout() {
      return cashRegister.checkout();
    }
  }
  