
class DroneRank:

    # Decides which fleet ship a prism belongs too at adult age 20
    Arch,

    # Decides which fleet base a prism belongs too at birth
    Major,
    Captain,
    Commander,
    Lieutenant,

    # Decides to NavyWorker or MarineWorker
    Ensign,
    Sergeant,

    # Prism at age 20 in NavyWork, MarineWork, TradeWork on AcademyExams
    Lance,
    Corporal,
    Private

    """
    Prism's life span is 0-125 cycles of Earth in Sol
    0: Baby so Parents must stay on Fleet Base for Arch Armada thus AdminTask
    0-5: Toddler so 1 Parent must be agreed to stay behind
    6-12: Child is sent to Fleet Academy to be Tank, Duelist, Support, Officer, Pilot, Vanguard 
    
    
    """
