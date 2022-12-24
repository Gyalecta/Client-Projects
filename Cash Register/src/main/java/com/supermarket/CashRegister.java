import java.util.ArrayList;
import java.util.List;

public class CashRegister {
  private List<Item> items;
  private double totalPrice;

  public CashRegister() {
    this.items = new ArrayList<>();
    this.totalPrice = 0.0;
  }

  public void addItem(Item item) {
    this.items.add(item);
    this.totalPrice += item.getPrice();
  }

  public Receipt checkout() {
    return new Receipt(items, totalPrice);
  }
}
