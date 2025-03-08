namespace DefaultNamespace;

public class Hotel
{
    public int Id { get; set; }
    public string address { get; set; }
    public int rating { get; set; }
    public HotelChain belongsTo { get; set; }
}