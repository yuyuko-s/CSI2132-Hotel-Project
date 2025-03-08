using HotelMvc.Models;

namespace DefaultNamespace;

public class Renting
{
    public int Id { get; set; }
    public int roomId { get; set; }
    public int renterId { get; set; }
    public string paymentStatus { get; set; }
    public DateTime startDate { get; set; }
    public DateTime endDate { get; set; }
    public bool wasBooked { get; set; }
}