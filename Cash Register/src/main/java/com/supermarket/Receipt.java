import java.util.List;

public class Receipt {
  private List<Item> items;
  private double totalPrice;

  public Receipt(List<Item> items, double totalPrice) {
    this.items = items;
    this.totalPrice = totalPrice;
  }

  public void print() {
    System.out.println("Receipt:");
    for (Item item : items) {
      System.out.println(item.getName() + ": $" + item.getPrice());
    }
    System.out.println("Total: $" + totalPrice);
  }
}
