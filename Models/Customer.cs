using System.ComponentModel.DataAnnotations;
using HotelMvc.Models;

namespace DefaultNamespace;

public class Customer
{
    public string Id { get; set; }
    public string dateRegistered {get; set;}
    public string fullName { get; set; }
    public string address { get; set; }
    public int worksAt { get; set; }
}