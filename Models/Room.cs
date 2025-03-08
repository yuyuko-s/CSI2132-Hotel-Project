using DefaultNamespace;

namespace HotelMvc.Models;

public class Room
{
    public int Id { get; set; }
    public int hotelId { get; set; }
    public string problems {get;set;}
    public int roomNumber { get; set; }
    public float price { get; set; }
    public int capacity { get; set; }
    public bool isExtendable {get;set;}
    public string viewType { get; set; }
    public string amenities { get; set; }
    
}