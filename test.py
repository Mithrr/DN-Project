from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['The_DN_project']
collection = db['users']

more_users = [
    {
        "Name": "Ramesh Patel",
        "Address": "Surat, Gujarat",
        "Qualification": "Diamond Polishing",
        "Interested_Fields": {"Require": ["Laser Cutting Machines"], "Seek": ["International Buyers"]},
        "Current_Employed_Facility": "Patel Gems Workshop",
        "Experience": "12 years",
        "Contact_Info": "9876543210",
        "Email_ID": "ramesh.patel@gemsindia.com",
        "Previous_Works": ["Jewelry Expo 2023"],
        "User_Type": "Requirement",
        "Investment_Required": 350000
    },
    {
        "Name": "Sunita Devi",
        "Address": "Varanasi, Uttar Pradesh",
        "Qualification": "Handloom Weaving",
        "Interested_Fields": {"Require": ["Design Software"], "Seek": ["E-Commerce Platform"]},
        "Current_Employed_Facility": "Banarasi Silk Collective",
        "Experience": "8 years",
        "Contact_Info": "8765432109",
        "Email_ID": "sunita.devi@banarasisilk.com",
        "Previous_Works": ["Textile Heritage Festival"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Rajesh Kumar",
        "Address": "Jodhpur, Rajasthan",
        "Qualification": "Leather Craft",
        "Interested_Fields": {"Require": ["Eco-Friendly Dyes"], "Seek": ["Workshop Space"]},
        "Current_Employed_Facility": "Desert Leather Artisans",
        "Experience": "10 years",
        "Contact_Info": "7654321098",
        "Email_ID": "rajesh.kumar@rajasthanleather.in",
        "Previous_Works": ["Camel Leather Bags"],
        "User_Type": "Requirement",
        "Investment_Required": 120000
    },
    {
        "Name": "Meena Sharma",
        "Address": "Shillong, Meghalaya",
        "Qualification": "Bamboo Craft",
        "Interested_Fields": {"Require": [], "Seek": ["Design Collaboration"]},
        "Current_Employed_Facility": "Northeast Bamboo Co-op",
        "Experience": "7 years",
        "Contact_Info": "6543210987",
        "Email_ID": "meena.sharma@greenbamboo.org",
        "Previous_Works": ["Sustainable Furniture Line"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Vijay Singh",
        "Address": "Amritsar, Punjab",
        "Qualification": "Organic Farming",
        "Interested_Fields": {"Require": ["Solar Irrigation"], "Seek": ["Certification Help"]},
        "Current_Employed_Facility": "Golden Temple Farms",
        "Experience": "14 years",
        "Contact_Info": "9432109876",
        "Email_ID": "vijay.singh@organicpunjab.in",
        "Previous_Works": ["Wheat Cultivation Project"],
        "User_Type": "Requirement",
        "Investment_Required": 180000
    },
    {
        "Name": "Anita Desai",
        "Address": "Mysore, Karnataka",
        "Qualification": "Sandalwood Carving",
        "Interested_Fields": {"Require": ["Wood Preservation Tech"], "Seek": ["Export License Guidance"]},
        "Current_Employed_Facility": "Mysore Arts Heritage",
        "Experience": "16 years",
        "Contact_Info": "8321098765",
        "Email_ID": "anita.desai@sandalwoodart.com",
        "Previous_Works": ["Royal Palace Restoration"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Prakash Joshi",
        "Address": "Almora, Uttarakhand",
        "Qualification": "Apiculture",
        "Interested_Fields": {"Require": ["Beehive Equipment"], "Seek": ["Honey Testing Lab"]},
        "Current_Employed_Facility": "Himalayan Honey Collective",
        "Experience": "9 years",
        "Contact_Info": "7210987654",
        "Email_ID": "prakash.joshi@mountainhoney.in",
        "Previous_Works": ["Organic Honey Festival"],
        "User_Type": "Requirement",
        "Investment_Required": 95000
    },
    {
        "Name": "Lalita Kumari",
        "Address": "Patna, Bihar",
        "Qualification": "Madhubani Painting",
        "Interested_Fields": {"Require": [], "Seek": ["Art Gallery Tie-ups"]},
        "Current_Employed_Facility": "Bihar Folk Art Center",
        "Experience": "11 years",
        "Contact_Info": "6109876543",
        "Email_ID": "lalita.kumari@madhubaniart.org",
        "Previous_Works": ["Cultural Embassy Exhibition"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Harish Menon",
        "Address": "Kochi, Kerala",
        "Qualification": "Coir Product Manufacturing",
        "Interested_Fields": {"Require": ["Automated Weaving Machines"], "Seek": ["Eco Packaging Solutions"]},
        "Current_Employed_Facility": "Kerala Coir Products",
        "Experience": "13 years",
        "Contact_Info": "5098765432",
        "Email_ID": "harish.menon@keralacoir.com",
        "Previous_Works": ["Coir Geo-Textiles"],
        "User_Type": "Requirement",
        "Investment_Required": 220000
    },
    {
        "Name": "Deepika Rao",
        "Address": "Hyderabad, Telangana",
        "Qualification": "ITI Electronics",
        "Interested_Fields": {"Require": ["Smartphone Repair Tools"], "Seek": ["Workshop Location"]},
        "Current_Employed_Facility": "Mobile Repair Startup",
        "Experience": "5 years",
        "Contact_Info": "4987654321",
        "Email_ID": "deepika.rao@techrepair.in",
        "Previous_Works": ["Rural Digital Literacy Camp"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Sanjay Gupta",
        "Address": "Agra, Uttar Pradesh",
        "Qualification": "Marble Inlay Work",
        "Interested_Fields": {"Require": ["Marble Cutting Machines"], "Seek": ["Design Catalogues"]},
        "Current_Employed_Facility": "Taj Marble Arts",
        "Experience": "18 years",
        "Contact_Info": "3876543210",
        "Email_ID": "sanjay.gupta@tajmarble.com",
        "Previous_Works": ["UNESCO Heritage Project"],
        "User_Type": "Requirement",
        "Investment_Required": 280000
    },
    {
        "Name": "Nandini Iyer",
        "Address": "Chennai, Tamil Nadu",
        "Qualification": "Carnatic Music",
        "Interested_Fields": {"Require": ["Recording Equipment"], "Seek": ["Concert Organizers"]},
        "Current_Employed_Facility": "Self-employed",
        "Experience": "15 years",
        "Contact_Info": "2765432109",
        "Email_ID": "nandini.iyer@carnaticmusic.in",
        "Previous_Works": ["Margazhi Festival"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Amitabh Choudhury",
        "Address": "Guwahati, Assam",
        "Qualification": "Tea Plantation Management",
        "Interested_Fields": {"Require": ["Organic Certification"], "Seek": ["Direct Export Channels"]},
        "Current_Employed_Facility": "Brahmaputra Tea Estate",
        "Experience": "20 years",
        "Contact_Info": "1654321098",
        "Email_ID": "amitabh.choudhury@assamtea.org",
        "Previous_Works": ["Single Origin Tea Launch"],
        "User_Type": "Requirement",
        "Investment_Required": 320000
    },
    {
        "Name": "Priya Malhotra",
        "Address": "Jaipur, Rajasthan",
        "Qualification": "Gemstone Jewelry Design",
        "Interested_Fields": {"Require": ["3D Printing Tech"], "Seek": ["Jewelry App Developers"]},
        "Current_Employed_Facility": "Rajputana Jewels",
        "Experience": "7 years",
        "Contact_Info": "9543210987",
        "Email_ID": "priya.malhotra@rajputanajewels.com",
        "Previous_Works": ["Luxury Jewelry Week"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Kiran Bedi",
        "Address": "Pondicherry",
        "Qualification": "Pottery Making",
        "Interested_Fields": {"Require": ["Electric Kiln"], "Seek": ["Clay Suppliers"]},
        "Current_Employed_Facility": "Auroville Pottery",
        "Experience": "9 years",
        "Contact_Info": "8432109876",
        "Email_ID": "kiran.bedi@aurovillepottery.in",
        "Previous_Works": ["Terracotta Festival"],
        "User_Type": "Requirement",
        "Investment_Required": 150000
    },
    {
        "Name": "Rahul Mehta",
        "Address": "Ahmedabad, Gujarat",
        "Qualification": "Textile Engineering",
        "Interested_Fields": {"Require": [], "Seek": ["Digital Printing Machines"]},
        "Current_Employed_Facility": "Denim Manufacturing Unit",
        "Experience": "6 years",
        "Contact_Info": "7321098765",
        "Email_ID": "rahul.mehta@denimexport.com",
        "Previous_Works": ["Sustainable Denim Project"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Smita Joshi",
        "Address": "Pune, Maharashtra",
        "Qualification": "Warli Painting",
        "Interested_Fields": {"Require": ["Art Supplies"], "Seek": ["Mural Projects"]},
        "Current_Employed_Facility": "Tribal Art Revival Trust",
        "Experience": "10 years",
        "Contact_Info": "6210987654",
        "Email_ID": "smita.joshi@warliart.org",
        "Previous_Works": ["Airport Mural Installation"],
        "User_Type": "Requirement",
        "Investment_Required": 75000
    },
    {
        "Name": "Vikram Singh",
        "Address": "Dehradun, Uttarakhand",
        "Qualification": "Ayurvedic Medicine",
        "Interested_Fields": {"Require": ["Herb Processing Unit"], "Seek": ["Clinical Trials"]},
        "Current_Employed_Facility": "Himalayan Herbal Research",
        "Experience": "12 years",
        "Contact_Info": "5109876543",
        "Email_ID": "vikram.singh@ayurvedresearch.in",
        "Previous_Works": ["Joint Pain Formulation"],
        "User_Type": "Seeker"
    },
    {
        "Name": "Anjali Reddy",
        "Address": "Vijayawada, Andhra Pradesh",
        "Qualification": "Kalamkari Printing",
        "Interested_Fields": {"Require": ["Natural Dyes"], "Seek": ["Fashion Designer Collabs"]},
        "Current_Employed_Facility": "Godavari Kalamkari House",
        "Experience": "8 years",
        "Contact_Info": "4098765432",
        "Email_ID": "anjali.reddy@kalamkariart.com",
        "Previous_Works": ["Handloom Day Exhibition"],
        "User_Type": "Requirement",
        "Investment_Required": 110000
    },
    {
        "Name": "Manoj Tiwari",
        "Address": "Lucknow, Uttar Pradesh",
        "Qualification": "Chikankari Embroidery",
        "Interested_Fields": {"Require": ["Design Digitization"], "Seek": ["Boutique Partnerships"]},
        "Current_Employed_Facility": "Lucknow Chikan Center",
        "Experience": "17 years",
        "Contact_Info": "3987654321",
        "Email_ID": "manoj.tiwari@chikankari.org",
        "Previous_Works": ["PM's Gift Collection"],
        "User_Type": "Seeker"
    }
]


collection.insert_many(more_users)
print("More users inserted successfully!")