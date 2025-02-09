
class DroneRank:

    # Decides which fleet ship a prism belongs too at adult age 20
    Arch = 16 # Admin, Vice, General, Admiral for PrismDrones living on SolarBases

    # Decides which fleet base a prism belongs too at birth
    Major = 14 # Can establish Cities with Captain of Fleet in Arch's Armada
    Captain = 12 # Can establish Towns with Commander on StarCapitals
    Commander = 10 # Can establish Outposts with Lieutenant on StarFrigates
    Lieutenant = 8 # Can establish Camps with Sergeant on StarCruisers

    # Decides to NavyWorker or MarineWorker
    Sergeant = 6 # Can become Leader of Cruisers and chosen on performance
    Ensign = 5 # Failed to become Sergeant after 5 missions

    # Prism at age 20 in NavyWork, MarineWork, TradeWork on AcademyExams
    Lance = 4 # Did 4 missions
    Corporal = 2 # Did 2 missions
    Private = 0 # Graduate from Academy
    Student = -1 # No Teen or Younger is on Missions on Simulations in Academy


class LifeSpan:
    Baby = 0
    Toddler = 1
    Child = 2
    Teen = 3
    Adult = 4
    Elder = 5

    """
    
    Father: John Smith Lieutenant as second officer
    Mother: Jane Doe Ensign
    
    John and Jane did Trade mission to transport goods on frigate
    frigate is invaded by pirates on route
    John and Jane bonded on mission and planet
    
    John goes to fight battle on Genosis
    Jane does a Science mission as Leader of Mission
    John and Jane still stayed in contact
    
    John and Jane did Battle mission on Hoth
    John and Jane got romantic and got pregant
    John and Jane got married on news and Jane had time off
    
    John goes into Trade Inasion on Mandolore
    Jane has 1st child
    John and Jane hunker down 1 year
    
    Jane decides to go
    John rotates after
    Child becomes Teen
    
    John and Jane see Child on breaks from Academy and Missions
    
    Prism's life span is 0-125 cycles of Earth in Sol
    0: Baby so Parents must stay on Fleet Base for Arch Armada thus AdminTask
    1-5: Toddler so 1 Parent must be agreed to stay behind
    6-12: Child is sent to Fleet Academy to be Tank, Damage, Support
    - Tank: Heavy, Commando in Land and Space
    - Damage: Trooper, Ranger in Land and Space
    - Support: Recon, Engineer in Land and Space
    13-19: Teen is sent to Legion Academy to be Farmer, Harvester, Engineer, Scientist
    - Farmer for Crops, Hunting, and Ranching for Market
    - Harvester for Ore, Stone, and Wood for Market
    - Engineer for Combat, Forging, and Designing for Market
    - Scientist for Medicine, Physics, and Chemistry for Market
    20-79: Adult in different cycles
    - Young 20-39: 1st 6 missions
    - Middle 40-59: 2nd 6 missions
    - Old 60-79: 3rd 6 missions
    80-125: Elder as in random when drone will die
    - Chooses StarBase to live out days for free
    - Chooses to serve on ArmadaOrder if Arch
    
    """
