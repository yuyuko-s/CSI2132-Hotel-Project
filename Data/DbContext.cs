namespace DefaultNamespace;
using Microsoft.EntityFrameworkCore;

public class HotelDbContext : DbContext
{
    public HotelDbContext(DbContextOptions<HotelDbContext> options)
        : base(options)
    {
    }
    
    public DbSet<Customer> Customers { get; set; } 
    public DbSet<Hotel> Hotels { get; set; }
}
